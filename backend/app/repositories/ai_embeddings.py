from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import AIEmbeddingRecord, AILibraryItemRecord, AIRecommendationFeedbackRecord, AISkillRecord
from app.models.ai_embedding import AIClarificationQuestion, AIEmbeddingSearchResult, AIRecommendationFeedbackCreate, AIRecommendationFeedbackRead, AIRecommendedPlan
from app.repositories.ai_library import _loads as _loads_library
from app.repositories.ai_library import _to_read as _library_to_read
from app.repositories.ai_skills import _loads as _loads_skill
from app.repositories.ai_skills import _to_read as _skill_to_read
from app.services.embeddings import EmbeddingClient, cosine_similarity
from app.services.semantic_intents import intent_ids, intent_profile


def ensure_ai_embedding_seed(db: Session) -> None:
    client = EmbeddingClient()
    docs = [*_skill_documents(db), *_library_documents(db)]
    active_keys = {(doc["source_type"], doc["source_id"]) for doc in docs}
    existing = {
        (record.source_type, record.source_id): record
        for record in db.scalars(select(AIEmbeddingRecord)).all()
    }
    now = datetime.now(timezone.utc)

    for doc in docs:
        key = (doc["source_type"], doc["source_id"])
        content_hash = hashlib.sha256(doc["content"].encode("utf-8")).hexdigest()
        record = existing.get(key)
        should_embed = (
            record is None
            or record.content_hash != content_hash
            or record.embedding_provider != client.provider
            or record.embedding_model != client.model
            or record.embedding_dimension != len(json.loads(record.embedding_json or "[]"))
        )
        if should_embed:
            embedding = client.embed(doc["content"])
            if record is None:
                record = AIEmbeddingRecord(
                    id=f"{doc['source_type']}:{doc['source_id']}"[:120],
                    source_id=doc["source_id"],
                    source_type=doc["source_type"],
                    created_at=now,
                    updated_at=now,
                    content_hash=content_hash,
                )
                db.add(record)
            _apply_document(record, doc, embedding, client, content_hash, now)
        elif record:
            _apply_document_metadata(record, doc, now)

    for key, record in existing.items():
        if key not in active_keys:
            db.delete(record)
    db.commit()


def search_ai_knowledge(
    db: Session,
    query: str,
    source_types: list[str] | None = None,
    top_k: int = 8,
    threshold: float | None = None,
) -> list[AIEmbeddingSearchResult]:
    threshold = settings.ai_search_default_threshold if threshold is None else threshold
    client = EmbeddingClient()
    query_embedding = client.embed(query)

    stmt = select(AIEmbeddingRecord)
    if source_types:
        stmt = stmt.where(AIEmbeddingRecord.source_type.in_(source_types))

    scored: list[tuple[float, AIEmbeddingRecord]] = []
    for record in db.scalars(stmt).all():
        try:
            embedding = json.loads(record.embedding_json or "[]")
        except json.JSONDecodeError:
            continue
        score = cosine_similarity(query_embedding, embedding)
        final_score = _semantic_score(score, query, record)
        if final_score >= threshold:
            scored.append((final_score, record))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [_to_result(db, record, score) for score, record in scored[:top_k]]


def compose_ai_recommendations(db: Session, query: str, top_k: int = 5, threshold: float | None = None) -> tuple[list[AIEmbeddingSearchResult], list[AIEmbeddingSearchResult]]:
    recommendations = search_ai_knowledge(
        db,
        query=query,
        source_types=["combination", "workflow"],
        top_k=top_k,
        threshold=threshold,
    )
    supporting_skills = search_ai_knowledge(
        db,
        query=query,
        source_types=["skill"],
        top_k=5,
        threshold=max(0.16, (threshold if threshold is not None else settings.ai_search_default_threshold) - 0.06),
    )
    return recommendations, supporting_skills


def recommend_ai_plans(db: Session, query: str, top_k: int = 3, threshold: float | None = None) -> tuple[list[str], list[AIRecommendedPlan], list[dict[str, str]], list[AIEmbeddingSearchResult]]:
    candidates = search_ai_knowledge(
        db,
        query=query,
        source_types=["combination", "workflow"],
        top_k=24,
        threshold=threshold,
    )
    query_intents = intent_ids(query, limit=4)
    supporting_skills = search_ai_knowledge(
        db,
        query=query,
        source_types=["skill"],
        top_k=5,
        threshold=max(0.16, (threshold if threshold is not None else settings.ai_search_default_threshold) - 0.06),
    )
    feedback_scores = _feedback_scores(db)
    plans = _pick_recommended_plans(query, query_intents, candidates, top_k, feedback_scores)
    comparison = _comparison_rows(plans)
    return query_intents, plans, comparison, supporting_skills


def clarify_ai_request(query: str) -> tuple[list[str], list[AIClarificationQuestion]]:
    query_intents = intent_ids(query, limit=4)
    lowered = query.lower()
    compact = lowered.replace(" ", "")
    primary_intent = _primary_clarification_intent(query_intents, compact)
    questions: list[AIClarificationQuestion] = []

    if not query_intents:
        return query_intents, [
            AIClarificationQuestion(
                id="task_type",
                question="你想完成的具体产出是什么？",
                why="我需要先判断这是 PPT、研究、代码、设计、视频还是自动化任务。",
                examples=["做一个客户汇报 PPT", "写一个网页原型", "整理一份行业研究报告"],
                options=["做 PPT / 演示文档", "写代码 / 做网站", "做研究报告", "做图片 / 设计", "做视频 / 音频"],
            )
        ]

    if primary_intent == "presentation_deck":
        if not _has_any(compact, ("客户", "老师", "老板", "同事", "投资人", "课堂", "学校", "公司", "团队", "答辩", "论文答辩", "client", "teacher", "investor", "team", "audience")):
            questions.append(
                AIClarificationQuestion(
                    id="audience",
                    question="这个演示文档主要给谁看？",
                    why="不同受众会影响工具组合：课堂汇报、客户提案、老板汇报、论文答辩的推荐不同。",
                    examples=["给客户看", "给老师课堂汇报", "给老板做项目进展"],
                    options=["给客户看", "给老师/课堂汇报", "给老板/团队看", "给投资人路演", "论文答辩"],
                )
            )
        if not _has_any(compact, ("资料", "文档", "大纲", "数据", "链接", "已有", "从零", "旧ppt", "美化", "source", "outline", "data", "material")):
            questions.append(
                AIClarificationQuestion(
                    id="source_material",
                    question="你现在有没有已有资料，还是需要从零开始？",
                    why="有资料时更适合整理和排版；从零开始时需要先做研究和大纲。",
                    examples=["我有一份 Word 文档", "只有主题，需要从零开始", "有数据表和几个链接"],
                    options=["已有文档/资料", "只有主题，从零开始", "有数据表", "有链接/网页资料", "有旧 PPT 需要美化"],
                )
            )
        if not _has_any(compact, ("快", "今天", "马上", "简单", "好看", "精致", "正式", "专业", "逻辑", "严谨", "商业提案", "fast", "quick", "beautiful", "formal")):
            questions.append(
                AIClarificationQuestion(
                    id="priority",
                    question="你更看重速度、视觉效果，还是专业完整度？",
                    why="这会决定推荐快速方案、视觉方案，还是商业级方案。",
                    examples=["今天就要，越快越好", "要好看", "要正式专业"],
                    options=["越快越好", "要好看", "要正式专业", "要逻辑严谨", "要适合商业提案"],
                )
            )
    elif primary_intent == "coding_build":
        if not _has_any(compact, ("网页", "网站", "app", "api", "后端", "前端", "react", "fastapi", "功能", "feature")):
            questions.append(
                AIClarificationQuestion(
                    id="build_target",
                    question="你要做的是网页、后端 API、App 原型，还是修某个功能？",
                    why="不同开发任务会匹配不同的 coding workflow。",
                    examples=["做一个前端网页", "加一个 FastAPI 后端接口", "修登录 bug"],
                    options=["做前端网页", "做后端 API", "做完整 App 原型", "修 bug", "部署上线"],
                )
            )
        if not _has_any(compact, ("已有", "repo", "代码", "从零", "github", "figma", "设计稿")):
            questions.append(
                AIClarificationQuestion(
                    id="code_context",
                    question="你已经有代码仓库/设计稿了吗，还是从零开始？",
                    why="有上下文时适合代码代理；从零开始时适合原型生成工具。",
                    examples=["有 GitHub repo", "只有想法", "有 Figma 设计稿"],
                    options=["有 GitHub repo", "有本地代码", "有 Figma/设计稿", "只有想法，从零开始"],
                )
            )
    elif primary_intent == "research_report":
        if not _has_any(compact, ("行业", "论文", "公司", "市场", "竞品", "学术", "finance", "paper", "market", "company")):
            questions.append(
                AIClarificationQuestion(
                    id="research_scope",
                    question="这份研究主要研究什么对象或范围？",
                    why="研究范围会影响资料来源、工具组合和输出结构。",
                    examples=["某个行业", "某家公司", "一组论文", "竞品分析"],
                    options=["行业研究", "公司研究", "竞品分析", "论文/文献综述", "市场调研"],
                )
            )
        if not _has_any(compact, ("ppt", "报告", "表格", "brief", "deck", "excel", "word")):
            questions.append(
                AIClarificationQuestion(
                    id="research_output",
                    question="你最后想要报告、PPT、表格，还是简短 brief？",
                    why="最终格式不同，推荐的后半段工作流也不同。",
                    examples=["30 页报告", "汇报 PPT", "Excel 对比表", "一页 brief"],
                    options=["完整报告", "汇报 PPT", "Excel/表格", "一页 brief", "中英双语版本"],
                )
            )
    elif primary_intent == "visual_design":
        if not _has_any(compact, ("海报", "logo", "品牌", "产品图", "社媒", "ui", "界面", "poster", "brand", "visual", "image")):
            questions.append(
                AIClarificationQuestion(
                    id="visual_output",
                    question="你主要想做哪一种视觉产出？",
                    why="海报、Logo、产品图、社媒图和 UI 视觉需要的工具组合不同。",
                    examples=["做品牌海报", "做 logo", "做产品图"],
                    options=["品牌海报", "Logo / 品牌识别", "社媒配图", "产品图 / 电商图", "UI / App 视觉"],
                )
            )
        if not _has_any(compact, ("现有", "参考", "风格", "从零", "尺寸", "模版", "reference", "style", "size")):
            questions.append(
                AIClarificationQuestion(
                    id="visual_context",
                    question="你有没有参考风格或现成素材？",
                    why="有参考图时适合做风格延展；从零开始时需要先生成方向和 moodboard。",
                    examples=["有参考图", "只有文字描述", "需要固定尺寸"],
                    options=["有参考图/素材", "只有文字描述", "需要固定尺寸", "需要多版风格", "需要可商用素材"],
                )
            )
    elif primary_intent == "video_audio":
        if not _has_any(compact, ("短视频", "长视频", "配音", "音乐", "mv", "教程", "口播", "广告", "clip", "voice", "music")):
            questions.append(
                AIClarificationQuestion(
                    id="media_output",
                    question="你想做短视频、配音、音乐，还是教程/广告视频？",
                    why="视频生成、配音、音乐和剪辑分发会走不同 workflow。",
                    examples=["做小红书短视频", "做英文配音", "做产品广告"],
                    options=["短视频剪辑", "配音 / 多语音频", "音乐 / MV", "产品广告视频", "教程 / 录屏视频"],
                )
            )
        if not _has_any(compact, ("小红书", "抖音", "youtube", "tiktok", "reels", "b站", "发布", "平台")):
            questions.append(
                AIClarificationQuestion(
                    id="media_platform",
                    question="主要发布到哪个平台或场景？",
                    why="平台会影响长度、字幕、封面和分发工具。",
                    examples=["发小红书", "发 YouTube Shorts", "内部培训"],
                    options=["小红书 / 抖音", "YouTube / Shorts", "TikTok / Reels", "内部培训", "广告投放"],
                )
            )
    elif primary_intent == "automation_agent":
        if not _has_any(compact, ("客服", "知识库", "工单", "审批", "通知", "报表", "数据", "邮件", "机器人", "bot", "rag")):
            questions.append(
                AIClarificationQuestion(
                    id="automation_goal",
                    question="你想自动化哪一类流程？",
                    why="客服机器人、知识库问答、报表推送和审批通知对应的连接方式不同。",
                    examples=["自动客服", "知识库问答", "定时生成报表"],
                    options=["客服机器人 / 工单", "知识库问答 / RAG", "报表 / 数据推送", "审批 / 通知流", "跨工具任务执行"],
                )
            )
        if not _has_any(compact, ("已有", "飞书", "钉钉", "slack", "notion", "airtable", "zendesk", "intercom", "api", "从零")):
            questions.append(
                AIClarificationQuestion(
                    id="automation_context",
                    question="你要连接哪些现有工具或数据？",
                    why="已有系统决定用 no-code、API、RAG 还是客服平台。",
                    examples=["连接飞书和表格", "连接 Zendesk", "从零搭 bot"],
                    options=["飞书 / 钉钉 / Slack", "Notion / Airtable", "Zendesk / Intercom", "已有 API", "从零开始搭建"],
                )
            )
    elif primary_intent == "business_growth":
        if not _has_any(compact, ("营销", "销售", "线索", "客服", "电商", "邮件", "投放", "crm", "campaign", "support")):
            questions.append(
                AIClarificationQuestion(
                    id="business_goal",
                    question="你要优化哪一类业务增长任务？",
                    why="营销、销售、客服、电商和投放的数据与工具链不同。",
                    examples=["销售线索跟进", "营销邮件", "客服回复"],
                    options=["营销活动 / 广告", "销售线索 / CRM", "客服支持", "电商运营", "SEO / 内容增长"],
                )
            )
        if not _has_any(compact, ("邮件", "微信", "官网", "社媒", "广告", "crm", "shopify", "hubspot", "渠道")):
            questions.append(
                AIClarificationQuestion(
                    id="business_channel",
                    question="主要发生在哪个渠道？",
                    why="渠道会影响生成内容、自动化触发和效果复盘方式。",
                    examples=["邮件营销", "HubSpot CRM", "Shopify 店铺"],
                    options=["邮件 / Newsletter", "CRM / HubSpot", "社媒 / 广告", "Shopify / 电商", "客服系统"],
                )
            )
    elif primary_intent == "data_analysis":
        if not _has_any(compact, ("excel", "csv", "表格", "数据库", "bi", "sheet", "bigquery", "snowflake", "数据表")):
            questions.append(
                AIClarificationQuestion(
                    id="data_source",
                    question="你的数据现在在哪里？",
                    why="Excel、CSV、BI、数据库和表格工具会匹配不同的数据工作流。",
                    examples=["Excel 表格", "CSV 文件", "数据库"],
                    options=["Excel / CSV", "Google Sheets / 飞书表格", "数据库 / BigQuery", "Snowflake / BI", "还没有数据"],
                )
            )
        if not _has_any(compact, ("dashboard", "图表", "仪表盘", "报告", "分析", "预测", "清洗", "visualization", "chart")):
            questions.append(
                AIClarificationQuestion(
                    id="data_output",
                    question="最后希望得到什么数据产出？",
                    why="清洗、分析、仪表盘和报告需要不同的后续步骤。",
                    examples=["做 dashboard", "做图表报告", "清洗数据"],
                    options=["清洗 / 整理数据", "图表 / 可视化", "Dashboard / 仪表盘", "业务分析报告", "预测 / 异常检测"],
                )
            )

    if _is_specific_enough(query, questions):
        return query_intents, []
    return query_intents, questions[:3]


def create_recommendation_feedback(db: Session, payload: AIRecommendationFeedbackCreate, user_id: str | None = None) -> AIRecommendationFeedbackRead:
    record = AIRecommendationFeedbackRecord(
        id=f"fb-{uuid4().hex[:16]}",
        user_id=user_id,
        query=payload.query,
        source_id=payload.source_id,
        source_type=payload.source_type,
        plan_type=payload.plan_type,
        rating=payload.rating,
        comment=payload.comment,
        created_at=datetime.now(timezone.utc),
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return _feedback_to_read(record)


def _skill_documents(db: Session) -> list[dict]:
    docs = []
    for skill in db.scalars(select(AISkillRecord).where(AISkillRecord.is_active.is_(True))).all():
        tags = _loads_skill(skill.tags_json)
        examples = _loads_skill(skill.examples_json)
        content = "\n".join(
            value
            for value in [
                f"Skill: {skill.name}",
                f"Category: {skill.category_label}",
                f"Subcategory: {skill.sub_skill_label}",
                f"Tool: {skill.tool}",
                f"Stage: {skill.stage}",
                f"Description: {skill.description}",
                f"Tags: {', '.join(tags)}",
                f"Examples: {'; '.join(examples)}",
            ]
            if value.strip()
        )
        profile = intent_profile(
            skill.name,
            [skill.category_label, skill.sub_skill_label, skill.tool, skill.stage, skill.description, " ".join(tags), " ".join(examples)],
        )
        content = _with_profile(content, profile)
        docs.append(
            {
                "source_id": skill.id,
                "source_type": "skill",
                "title": skill.name,
                "category_id": skill.category_id,
                "category_label": skill.category_label,
                "sub_skill_id": skill.sub_skill_id,
                "sub_skill_label": skill.sub_skill_label,
                "content": content,
                "metadata": {
                    "summary": skill.description,
                    "tools": [skill.tool] if skill.tool else [],
                    "tags": tags,
                    "importance": skill.importance,
                    **profile,
                },
            }
        )
    return docs


def _library_documents(db: Session) -> list[dict]:
    docs = []
    for item in db.scalars(select(AILibraryItemRecord).where(AILibraryItemRecord.is_active.is_(True))).all():
        tools = _loads_library(item.tools_json)
        steps = _loads_library(item.steps_json)
        outputs = _loads_library(item.outputs_json)
        tags = _loads_library(item.tags_json)
        content = "\n".join(
            value
            for value in [
                f"{item.item_type.title()}: {item.title}",
                f"Category: {item.category_label}",
                f"Subcategory: {item.sub_skill_label}",
                f"Summary: {item.summary}",
                f"Tools: {', '.join(tools)}",
                f"Steps: {'; '.join(steps)}",
                f"Outputs: {', '.join(outputs)}",
                f"Tags: {', '.join(tags)}",
                f"Source: {item.source_section}",
            ]
            if value.strip()
        )
        profile = intent_profile(
            item.title,
            [item.category_label, item.sub_skill_label, item.summary, " ".join(tools), " ".join(steps), " ".join(outputs), " ".join(tags), item.source_section],
        )
        content = _with_profile(content, profile)
        docs.append(
            {
                "source_id": item.id,
                "source_type": item.item_type,
                "title": item.title,
                "category_id": item.category_id,
                "category_label": item.category_label,
                "sub_skill_id": item.sub_skill_id,
                "sub_skill_label": item.sub_skill_label,
                "content": content,
                "metadata": {
                    "summary": item.summary,
                    "tools": tools,
                    "steps": steps,
                    "outputs": outputs,
                    "tags": tags,
                    "importance": item.importance,
                    **profile,
                },
            }
        )
    return docs


def _apply_document(record: AIEmbeddingRecord, doc: dict, embedding: list[float], client: EmbeddingClient, content_hash: str, now: datetime) -> None:
    _apply_document_metadata(record, doc, now)
    record.embedding_json = json.dumps(embedding)
    record.content_hash = content_hash
    record.embedding_provider = client.provider
    record.embedding_model = client.model
    record.embedding_dimension = len(embedding)


def _apply_document_metadata(record: AIEmbeddingRecord, doc: dict, now: datetime) -> None:
    record.title = doc["title"]
    record.category_id = doc["category_id"]
    record.category_label = doc["category_label"]
    record.sub_skill_id = doc["sub_skill_id"]
    record.sub_skill_label = doc["sub_skill_label"]
    record.content = doc["content"]
    record.metadata_json = json.dumps(doc["metadata"], ensure_ascii=False)
    record.updated_at = now


def _semantic_score(score: float, query: str, record: AIEmbeddingRecord) -> float:
    hay = f"{record.title} {record.content}".lower()
    title_text = record.title.lower()
    title_hay = f"{record.title} {record.sub_skill_label} {record.category_label}".lower()
    lowered = query.lower()
    query_intents = set(intent_ids(query, limit=4))
    metadata = _loads_metadata(record.metadata_json)
    record_intents = set(metadata.get("intents", []))
    bonus = 0.0
    if query_intents and record_intents:
        overlap = len(query_intents & record_intents)
        if overlap:
            bonus += 0.26 + 0.06 * (overlap - 1)
        else:
            bonus -= 0.18
    if "presentation_deck" in query_intents and "presentation_deck" not in record_intents:
        bonus -= 0.2
    if "presentation_deck" in query_intents:
        direct_title_match = any(token in title_text for token in ("ppt", "presentation", "slides", "deck", "proposal", "pitch", "演示", "幻灯", "汇报", "提案"))
        title_match = direct_title_match or any(token in title_hay for token in ("ppt", "presentation", "slides", "deck", "proposal", "pitch", "演示", "幻灯", "汇报", "提案"))
        content_match = any(token in hay for token in ("ppt", "presentation", "slides", "deck", "proposal", "pitch", "演示", "幻灯", "汇报", "提案"))
        focused_query = not any(token in lowered for token in ("研究", "调研", "report", "research", "数据", "data", "图", "design", "社媒", "海报"))
        if direct_title_match:
            bonus += 0.36
        elif title_match:
            bonus += 0.12
        elif content_match:
            bonus += 0.04
        if focused_query and not direct_title_match:
            bonus -= 0.16
    if any(token in lowered for token in ("ppt", "演示", "演示文档", "演示稿", "幻灯", "汇报", "提案")) and any(token in hay for token in ("ppt", "slides", "deck", "gamma", "beautiful.ai", "幻灯", "演示", "提案")):
        bonus += 0.12
    if any(token in lowered for token in ("报告", "report", "研究")) and any(token in hay for token in ("report", "research", "报告", "研究", "研报")):
        bonus += 0.08
    if any(token in lowered for token in ("代码", "code", "编程")) and any(token in hay for token in ("code", "coding", "cursor", "claude code", "编程")):
        bonus += 0.08
    if record.source_type == "workflow":
        bonus += 0.035
    try:
        importance = float(metadata.get("importance", 0))
    except (TypeError, ValueError):
        importance = 0.0
    return score * 0.72 + bonus + min(importance, 100.0) / 1000.0


def _to_result(db: Session, record: AIEmbeddingRecord, score: float) -> AIEmbeddingSearchResult:
    metadata = _loads_metadata(record.metadata_json)
    item = None
    if record.source_type == "skill":
        skill = db.get(AISkillRecord, record.source_id)
        item = _skill_to_read(skill) if skill else None
    elif record.source_type in {"combination", "workflow"}:
        library = db.get(AILibraryItemRecord, record.source_id)
        item = _library_to_read(library) if library else None
    return AIEmbeddingSearchResult(
        source_id=record.source_id,
        source_type=record.source_type,
        score=round(score, 4),
        title=record.title,
        category_id=record.category_id,
        category_label=record.category_label,
        sub_skill_id=record.sub_skill_id,
        sub_skill_label=record.sub_skill_label,
        summary=metadata.get("summary", ""),
        tools=metadata.get("tools", []),
        steps=metadata.get("steps", []),
        outputs=metadata.get("outputs", []),
        tags=metadata.get("tags", []),
        item=item,
    )


def _pick_recommended_plans(query: str, query_intents: list[str], candidates: list[AIEmbeddingSearchResult], top_k: int, feedback_scores: dict[tuple[str, str], float]) -> list[AIRecommendedPlan]:
    if not candidates:
        return []

    ranked = []
    for candidate in candidates:
        profile = _recommendation_profile(candidate)
        fit = _plan_fit_score(query, query_intents, candidate, profile)
        fit += feedback_scores.get((candidate.source_type, candidate.source_id), 0.0)
        ranked.append((fit, profile, candidate))
    ranked.sort(key=lambda item: item[0], reverse=True)

    slots = _plan_slots(query, query_intents)
    plans: list[AIRecommendedPlan] = []
    used_ids: set[str] = set()
    for slot in slots:
        best = None
        for base_score, profile, candidate in ranked:
            if candidate.source_id in used_ids:
                continue
            slot_score = base_score + _slot_bonus(slot["id"], candidate, profile)
            if best is None or slot_score > best[0]:
                best = (slot_score, profile, candidate)
        if best is None:
            continue
        score, profile, candidate = best
        used_ids.add(candidate.source_id)
        plans.append(
            AIRecommendedPlan(
                plan_type=slot["id"],
                label=slot["label"],
                reason=_reason_for_plan(slot["id"], candidate, profile),
                best_for=profile["best_for"],
                tradeoff=profile["tradeoff"],
                pros=profile["pros"],
                cons=profile["cons"],
                execution_steps=_execution_steps(candidate, profile),
                required_inputs=profile["required_inputs"],
                expected_outputs=profile["expected_outputs"],
                score=round(score, 4),
                recommendation=candidate,
            )
        )
        if len(plans) >= top_k:
            break
    return plans


def _plan_slots(query: str, query_intents: list[str]) -> list[dict[str, str]]:
    lowered = query.lower()
    slots = [{"id": "fastest", "label": "Fastest path"}]
    if "presentation_deck" in query_intents:
        slots.extend(
            [
                {"id": "best_visual", "label": "Best visual deck"},
                {"id": "business_ready", "label": "Business-ready proposal"},
            ]
        )
    elif "coding_build" in query_intents:
        slots.extend(
            [
                {"id": "prototype", "label": "Prototype first"},
                {"id": "production", "label": "Production-ready build"},
            ]
        )
    elif "research_report" in query_intents:
        slots.extend(
            [
                {"id": "evidence_based", "label": "Most evidence-based"},
                {"id": "presentation_ready", "label": "Report to deck"},
            ]
        )
    elif "visual_design" in query_intents:
        slots.extend(
            [
                {"id": "best_visual", "label": "Best visual quality"},
                {"id": "brand_ready", "label": "Brand-ready assets"},
            ]
        )
    elif "video_audio" in query_intents:
        slots.extend(
            [
                {"id": "media_production", "label": "Production workflow"},
                {"id": "highest_quality", "label": "Highest media quality"},
            ]
        )
    elif "automation_agent" in query_intents:
        slots.extend(
            [
                {"id": "automation_ready", "label": "Automation-ready"},
                {"id": "production", "label": "Operational workflow"},
            ]
        )
    elif "business_growth" in query_intents:
        slots.extend(
            [
                {"id": "business_ready", "label": "Business-ready"},
                {"id": "automation_ready", "label": "Growth operations"},
            ]
        )
    elif "data_analysis" in query_intents:
        slots.extend(
            [
                {"id": "data_ready", "label": "Data-ready analysis"},
                {"id": "presentation_ready", "label": "Dashboard or report"},
            ]
        )
    else:
        slots.extend(
            [
                {"id": "balanced", "label": "Balanced choice"},
                {"id": "highest_quality", "label": "Highest quality"},
            ]
        )

    if any(token in lowered for token in ("简单", "新手", "容易", "不要复杂", "easy", "beginner")):
        slots.insert(1, {"id": "easiest", "label": "Easiest for beginners"})
    return slots


def _recommendation_profile(candidate: AIEmbeddingSearchResult) -> dict:
    text = " ".join(
        [
            candidate.title,
            candidate.summary,
            candidate.category_label,
            candidate.sub_skill_label,
            " ".join(candidate.tools),
            " ".join(candidate.steps),
            " ".join(candidate.outputs),
            " ".join(candidate.tags),
        ]
    ).lower()
    tool_count = len(candidate.tools)
    step_count = len(candidate.steps)
    is_ppt = any(token in text for token in ("ppt", "presentation", "slides", "deck", "gamma", "canva", "演示", "幻灯", "汇报", "提案"))
    is_research = any(token in text for token in ("research", "perplexity", "notebooklm", "elicit", "调研", "研究", "报告", "研报", "文献"))
    is_visual = any(token in text for token in ("canva", "gamma", "beautiful.ai", "figma", "midjourney", "recraft", "visual", "设计", "视觉"))
    is_business = any(token in text for token in ("pitch", "proposal", "sales", "crm", "close", "hubspot", "business", "商业", "客户", "提案", "销售"))
    is_code = any(token in text for token in ("code", "cursor", "claude code", "github", "react", "api", "代码", "编程", "开发"))
    is_video = any(token in text for token in ("video", "audio", "voice", "runway", "veo", "kling", "suno", "elevenlabs", "视频", "音频", "配音", "短视频", "剪辑"))
    is_automation = any(token in text for token in ("automation", "agent", "bot", "rag", "n8n", "make", "zapier", "mcp", "coze", "dify", "扣子", "自动化", "智能体", "机器人", "知识库", "工单"))
    is_data = any(
        token in text
        for token in (
            "spreadsheet",
            "excel",
            "sheets",
            "dashboard",
            "chart",
            "power bi",
            "looker",
            "snowflake",
            "hex",
            "rows",
            "julius",
            "bigquery",
            "表格",
            "仪表盘",
            "图表",
            "财务/数据",
            "数据：",
            "数据分析",
            "数据可视化",
            "问数据",
        )
    )

    speed = "fast" if tool_count <= 3 and step_count <= 3 else "medium" if tool_count <= 5 else "deep"
    difficulty = "beginner" if tool_count <= 3 and not is_code else "intermediate" if tool_count <= 5 else "advanced"
    quality = "professional" if is_research or is_visual or is_business or is_data or candidate.source_type == "workflow" else "draft"

    outputs = candidate.outputs[:] or _infer_outputs(is_ppt, is_research, is_visual, is_business, is_code, is_video, is_automation, is_data)
    inputs = _infer_inputs(is_ppt, is_research, is_visual, is_business, is_code, is_video, is_automation, is_data)
    best_for = _best_for(candidate, is_ppt, is_research, is_visual, is_business, is_code, is_video, is_automation, is_data, speed)
    tradeoff = _tradeoff(speed, difficulty, quality)
    pros = _pros(speed, difficulty, quality, is_visual, is_business, is_research)
    cons = _cons(speed, difficulty, quality)
    return {
        "speed": speed,
        "difficulty": difficulty,
        "quality": quality,
        "is_ppt": is_ppt,
        "is_research": is_research,
        "is_visual": is_visual,
        "is_business": is_business,
        "is_code": is_code,
        "is_video": is_video,
        "is_automation": is_automation,
        "is_data": is_data,
        "best_for": best_for,
        "tradeoff": tradeoff,
        "pros": pros,
        "cons": cons,
        "required_inputs": inputs,
        "expected_outputs": outputs,
    }


def _plan_fit_score(query: str, query_intents: list[str], candidate: AIEmbeddingSearchResult, profile: dict) -> float:
    score = candidate.score
    text = _candidate_text(candidate)
    lowered = query.lower()
    score += _intent_affinity(query_intents, text, profile)
    if "presentation_deck" in query_intents and profile["is_ppt"]:
        score += 0.32
    if "research_report" in query_intents and profile["is_research"]:
        score += 0.28
    if "coding_build" in query_intents and profile["is_code"]:
        score += 0.28
    if "visual_design" in query_intents and profile["is_visual"]:
        score += 0.24
    if "video_audio" in query_intents and profile["is_video"]:
        score += 0.3
    if "automation_agent" in query_intents and profile["is_automation"]:
        score += 0.32
    if "business_growth" in query_intents and profile["is_business"]:
        score += 0.3
    if "data_analysis" in query_intents and profile["is_data"]:
        score += 0.36
    if "data_analysis" in query_intents:
        data_stack_match = any(
            token in text
            for token in ("bigquery", "looker", "power bi", "snowflake", "hex", "julius", "rows", "excel", "sheets", "spreadsheet", "仪表盘", "图表", "问数据")
        )
        if data_stack_match:
            score += 0.24
        if "bigquery" in lowered and "bigquery" in text:
            score += 0.5
        if any(token in lowered for token in ("dashboard", "仪表盘", "bi")) and any(token in text for token in ("looker", "power bi", "dashboard", "仪表盘", "bi")):
            score += 0.28
        if profile["is_ppt"] and not data_stack_match:
            score -= 0.35
    if any(token in lowered for token in ("快", "快速", "马上", "today", "fast")) and profile["speed"] == "fast":
        score += 0.18
    if any(token in lowered for token in ("好看", "设计", "视觉", "beautiful", "visual")) and profile["is_visual"]:
        score += 0.18
    if any(token in lowered for token in ("商业", "客户", "pitch", "提案", "proposal")) and profile["is_business"]:
        score += 0.18
    if any(token in lowered for token in ("简单", "新手", "easy", "beginner")) and profile["difficulty"] == "beginner":
        score += 0.15
    score += _option_affinity(lowered, text, profile)
    score += _query_tiebreak(query, candidate.source_id)
    return score


def _slot_bonus(slot_id: str, candidate: AIEmbeddingSearchResult, profile: dict) -> float:
    bonus = 0.0
    if slot_id == "fastest":
        bonus += 0.28 if profile["speed"] == "fast" else 0.08 if profile["speed"] == "medium" else -0.08
    elif slot_id == "easiest":
        bonus += 0.25 if profile["difficulty"] == "beginner" else -0.04
    elif slot_id in {"best_visual", "brand_ready"}:
        bonus += 0.28 if profile["is_visual"] else -0.08
    elif slot_id in {"business_ready", "production"}:
        bonus += 0.25 if profile["is_business"] or profile["quality"] == "professional" else -0.04
    elif slot_id == "media_production":
        bonus += 0.32 if profile["is_video"] else -0.1
    elif slot_id == "automation_ready":
        bonus += 0.3 if profile["is_automation"] else -0.08
    elif slot_id == "data_ready":
        bonus += 0.32 if profile["is_data"] else -0.1
    elif slot_id == "prototype":
        bonus += 0.22 if profile["speed"] in {"fast", "medium"} else 0.0
    elif slot_id == "evidence_based":
        bonus += 0.28 if profile["is_research"] else -0.08
    elif slot_id == "presentation_ready":
        bonus += 0.18 if profile["is_ppt"] else 0.0
    elif slot_id == "highest_quality":
        bonus += 0.18 if profile["quality"] == "professional" else 0.0
    return bonus


def _candidate_text(candidate: AIEmbeddingSearchResult) -> str:
    return " ".join(
        [
            candidate.title,
            candidate.summary,
            candidate.category_label,
            candidate.sub_skill_label,
            " ".join(candidate.tools),
            " ".join(candidate.steps),
            " ".join(candidate.outputs),
            " ".join(candidate.tags),
        ]
    ).lower()


def _option_affinity(query: str, text: str, profile: dict) -> float:
    score = 0.0
    rules: tuple[tuple[tuple[str, ...], tuple[str, ...], float], ...] = (
        (("客户", "商业提案", "提案", "client"), ("proposal", "pitch", "close", "sales", "crm", "gamma", "claude", "客户", "提案", "商业"), 0.18),
        (("老师", "课堂", "学校"), ("kimi", "wps", "notebooklm", "research", "报告", "汇报", "课堂", "文档"), 0.13),
        (("老板", "团队"), ("data", "dashboard", "workspace", "feishu", "dingtalk", "wps", "汇报", "团队", "数据"), 0.14),
        (("投资人", "路演"), ("pitch", "proposal", "market", "deep research", "gamma", "deck", "商业", "路演"), 0.2),
        (("论文答辩", "答辩"), ("paper", "research", "notebooklm", "deep research", "perplexity", "论文", "文献", "答辩"), 0.22),
        (("已有文档", "已有资料", "文档/资料"), ("kimi", "wps", "notion", "notebooklm", "claude", "文档", "资料"), 0.16),
        (("从零", "只有主题"), ("perplexity", "genspark", "manus", "deep research", "skywork", "research", "调研", "从零"), 0.2),
        (("数据表", "表格"), ("excel", "sheets", "spreadsheet", "power bi", "table", "hex", "snowflake", "wps", "天工表格", "数据"), 0.22),
        (("链接", "网页资料"), ("perplexity", "genspark", "manus", "browser", "deep research", "链接", "网页"), 0.18),
        (("旧 ppt", "旧ppt", "美化"), ("canva", "gamma", "beautiful.ai", "design", "visual", "美化", "视觉"), 0.22),
        (("越快越好", "今天", "马上"), ("kimi", "wps", "通义", "fast", "quick", "一键", "快速"), 0.18),
        (("要好看", "视觉效果"), ("canva", "gamma", "beautiful.ai", "design", "visual", "figma", "好看", "视觉"), 0.22),
        (("正式专业", "专业完整"), ("claude", "gamma", "deep research", "business", "professional", "正式", "专业"), 0.17),
        (("逻辑严谨", "严谨"), ("research", "deep research", "notebooklm", "perplexity", "evidence", "逻辑", "严谨", "报告"), 0.2),
        (("前端", "网页", "网站", "react"), ("cursor", "claude code", "lovable", "v0", "react", "figma", "前端", "网页", "网站"), 0.24),
        (("后端", "api", "fastapi"), ("cursor", "claude code", "api", "fastapi", "backend", "supabase", "后端"), 0.24),
        (("部署", "上线", "vercel"), ("vercel", "cloudflare", "deploy", "deployment", "github", "上线", "部署"), 0.22),
        (("修 bug", "bug", "调试"), ("cursor", "claude code", "cline", "debug", "logs", "调试", "修复"), 0.22),
        (("行业研究", "市场调研"), ("perplexity", "deep research", "genspark", "research", "market", "行业", "市场", "调研"), 0.24),
        (("公司研究", "公司深度"), ("perplexity", "bigquery", "excel", "finance", "company", "公司", "财报", "研报"), 0.24),
        (("竞品分析", "竞品"), ("perplexity", "similarweb", "apify", "table", "竞品", "对比"), 0.24),
        (("论文", "文献综述"), ("elicit", "consensus", "semantic scholar", "scite", "notebooklm", "zotero", "论文", "文献"), 0.28),
        (("海报", "logo", "品牌"), ("canva", "midjourney", "recraft", "photoshop", "figma", "logo", "brand", "品牌", "海报"), 0.26),
        (("短视频", "配音", "剪辑"), ("runway", "veo", "kling", "suno", "elevenlabs", "video", "voice", "视频", "配音", "剪辑"), 0.3),
        (("自动化", "机器人", "知识库", "工单", "客服机器人"), ("n8n", "make", "zapier", "coze", "dify", "rag", "bot", "扣子", "自动化", "机器人", "知识库", "工单"), 0.34),
        (("营销", "邮件", "crm", "销售线索"), ("hubspot", "apollo", "clay", "crm", "sales", "marketing", "email", "销售", "营销", "线索"), 0.3),
        (("excel", "数据表", "dashboard", "图表", "仪表盘"), ("excel", "sheets", "spreadsheet", "dashboard", "chart", "power bi", "looker", "hex", "snowflake", "rows", "julius", "bigquery", "表格", "图表", "仪表盘", "数据：", "财务/数据", "问数据"), 0.56),
    )
    compact_query = query.replace(" ", "")
    compact_text = text.replace(" ", "")
    for query_terms, candidate_terms, weight in rules:
        if any(term.lower().replace(" ", "") in compact_query for term in query_terms):
            if any(term.lower().replace(" ", "") in compact_text for term in candidate_terms):
                score += weight
            else:
                score -= min(0.06, weight / 3)
    if "越快越好" in compact_query and profile["speed"] == "fast":
        score += 0.08
    if "要好看" in compact_query and profile["is_visual"]:
        score += 0.08
    if "要适合商业提案" in compact_query and profile["is_business"]:
        score += 0.1
    return score


def _intent_affinity(query_intents: list[str], text: str, profile: dict) -> float:
    score = 0.0
    if "presentation_deck" in query_intents and not profile["is_ppt"]:
        score -= 0.08
    if "research_report" in query_intents and not profile["is_research"]:
        score -= 0.08
    if "coding_build" in query_intents and not profile["is_code"]:
        score -= 0.1
    if "visual_design" in query_intents and not profile["is_visual"]:
        score -= 0.08
    if "video_audio" in query_intents and not profile["is_video"]:
        score -= 0.12
    if "automation_agent" in query_intents and not profile["is_automation"]:
        score -= 0.14
    if "business_growth" in query_intents and not profile["is_business"]:
        score -= 0.1
    if "data_analysis" in query_intents and not profile["is_data"]:
        score -= 0.16

    direct_rules: dict[str, tuple[tuple[str, ...], float]] = {
        "coding_build": (("cursor", "claude code", "github", "react", "api", "deploy", "代码", "编程", "开发"), 0.16),
        "visual_design": (("canva", "midjourney", "recraft", "photoshop", "figma", "visual", "logo", "设计", "视觉"), 0.16),
        "video_audio": (("runway", "veo", "kling", "suno", "elevenlabs", "video", "voice", "视频", "配音"), 0.2),
        "automation_agent": (("n8n", "make", "zapier", "coze", "dify", "rag", "bot", "扣子", "自动化", "机器人", "知识库", "工单"), 0.2),
        "business_growth": (("hubspot", "apollo", "clay", "crm", "sales", "marketing", "客服", "销售", "营销", "线索"), 0.18),
        "data_analysis": (("excel", "sheets", "spreadsheet", "dashboard", "chart", "power bi", "looker", "hex", "snowflake", "rows", "julius", "bigquery", "表格", "图表", "仪表盘", "数据：", "财务/数据", "问数据"), 0.32),
    }
    for intent, (tokens, weight) in direct_rules.items():
        if intent in query_intents and any(token in text for token in tokens):
            score += weight
    return score


def _query_tiebreak(query: str, source_id: str) -> float:
    digest = hashlib.blake2b(f"{query}|{source_id}".encode("utf-8"), digest_size=4).digest()
    value = int.from_bytes(digest, "big") / 0xFFFFFFFF
    return (value - 0.5) * 0.78


def _reason_for_plan(slot_id: str, candidate: AIEmbeddingSearchResult, profile: dict) -> str:
    tools = " + ".join(candidate.tools[:4]) if candidate.tools else candidate.title
    if slot_id == "fastest":
        return f"{tools} has a short tool chain and can produce a usable first version quickly."
    if slot_id == "best_visual":
        return f"{tools} is stronger for layout, visual polish, and presentation-ready design."
    if slot_id == "business_ready":
        return f"{tools} fits a more polished proposal or client-facing business deck."
    if slot_id == "easiest":
        return f"{tools} is simpler to operate and works well when you want fewer steps."
    if slot_id == "evidence_based":
        return f"{tools} is better when the result needs sources, research, and structured reasoning."
    if slot_id == "prototype":
        return f"{tools} is useful for getting a working prototype before hardening details."
    return f"{tools} gives a balanced path for this task with {profile['quality']} output potential."


def _infer_inputs(is_ppt: bool, is_research: bool, is_visual: bool, is_business: bool, is_code: bool, is_video: bool, is_automation: bool, is_data: bool) -> list[str]:
    if is_ppt:
        return ["topic or goal", "target audience", "rough outline or source material", "preferred style"]
    if is_research:
        return ["research question", "scope", "source requirements", "output format"]
    if is_code:
        return ["feature goal", "tech stack", "repo or mockup", "acceptance criteria"]
    if is_visual:
        return ["brand/style reference", "copy or prompt", "format size", "example visuals"]
    if is_video:
        return ["script or idea", "target platform", "style reference", "duration"]
    if is_automation:
        return ["trigger", "connected tools", "knowledge source", "handoff rule"]
    if is_data:
        return ["spreadsheet or database", "metric question", "chart/dashboard goal", "audience"]
    if is_business:
        return ["customer segment", "offer", "channel", "success metric"]
    return ["goal", "context", "constraints", "desired output"]


def _infer_outputs(is_ppt: bool, is_research: bool, is_visual: bool, is_business: bool, is_code: bool, is_video: bool, is_automation: bool, is_data: bool) -> list[str]:
    if is_ppt:
        return ["presentation outline", "editable deck draft", "visual direction"]
    if is_research:
        return ["research brief", "source summary", "report draft"]
    if is_code:
        return ["working prototype", "code changes", "deployment checklist"]
    if is_visual:
        return ["image assets", "layout variants", "export-ready visuals"]
    if is_video:
        return ["script", "video draft", "voiceover or edit checklist"]
    if is_automation:
        return ["automation flow", "bot behavior", "handoff checklist"]
    if is_data:
        return ["analysis summary", "charts", "dashboard or report"]
    if is_business:
        return ["campaign draft", "CRM or outreach plan", "customer-facing copy"]
    return ["action plan", "draft output", "next-step checklist"]


def _best_for(candidate: AIEmbeddingSearchResult, is_ppt: bool, is_research: bool, is_visual: bool, is_business: bool, is_code: bool, is_video: bool, is_automation: bool, is_data: bool, speed: str) -> str:
    if is_ppt and is_business:
        return "client-facing decks, pitch materials, and business proposals"
    if is_ppt and is_visual:
        return "presentation documents that need a cleaner visual style"
    if is_ppt:
        return "turning a topic or source material into a clear slide deck"
    if is_research:
        return "research-heavy tasks that need grounded structure and sources"
    if is_code:
        return "software prototypes, code edits, and product implementation"
    if is_visual:
        return "visual assets, layouts, and design exploration"
    if is_video:
        return "video, audio, voice, and short-form production"
    if is_automation:
        return "connecting tools, bots, RAG, and recurring operational workflows"
    if is_data:
        return "spreadsheet analysis, dashboards, charts, and metrics reporting"
    return "quick execution" if speed == "fast" else "multi-step project work"


def _tradeoff(speed: str, difficulty: str, quality: str) -> str:
    if speed == "fast":
        return "Fastest route, but it may need a manual polish pass."
    if difficulty == "advanced":
        return "More powerful, but it asks for clearer inputs and more review."
    if quality == "professional":
        return "Better output quality, with a slightly longer setup."
    return "Balanced option with moderate setup and review effort."


def _pros(speed: str, difficulty: str, quality: str, is_visual: bool, is_business: bool, is_research: bool) -> list[str]:
    pros = []
    if speed == "fast":
        pros.append("quick first draft")
    if difficulty == "beginner":
        pros.append("low setup effort")
    if quality == "professional":
        pros.append("stronger final quality")
    if is_visual:
        pros.append("better visual polish")
    if is_business:
        pros.append("good for client-facing work")
    if is_research:
        pros.append("grounded by research")
    return pros[:4] or ["clear workflow", "reusable process"]


def _cons(speed: str, difficulty: str, quality: str) -> list[str]:
    cons = []
    if speed == "fast":
        cons.append("needs manual review before final delivery")
    if difficulty == "advanced":
        cons.append("requires clearer inputs and more setup")
    if speed == "deep":
        cons.append("slower than a lightweight draft workflow")
    if quality != "professional":
        cons.append("may need extra polish for high-stakes output")
    return cons[:3] or ["depends on input quality"]


def _execution_steps(candidate: AIEmbeddingSearchResult, profile: dict) -> list[str]:
    tools = candidate.tools[:5]
    if candidate.steps and len(candidate.steps) >= 3:
        return candidate.steps[:6]
    if candidate.steps:
        starter = candidate.steps[:]
        starter.extend(_generic_followup_steps(profile, tools))
        return starter[:5]
    if not tools:
        return [
            "Clarify the target output and constraints.",
            "Draft the first version with the recommended workflow.",
            "Review, polish, and export the result.",
        ]
    if profile["is_ppt"]:
        return [
            "Collect the topic, audience, key points, and source material.",
            f"Use {tools[0]} to structure the story and page outline.",
            f"Use {tools[1] if len(tools) > 1 else tools[0]} to turn the outline into slides.",
            "Review the logic, visual hierarchy, and missing evidence.",
            "Export an editable deck and make a final manual polish pass.",
        ]
    if profile["is_research"]:
        return [
            "Define the research question and source scope.",
            f"Use {tools[0]} to collect and compare source material.",
            "Extract evidence, contradictions, and useful citations.",
            "Turn the findings into a structured report or brief.",
        ]
    if profile["is_code"]:
        return [
            "Define the feature goal, repo context, and acceptance criteria.",
            f"Use {tools[0]} to draft the implementation plan.",
            "Apply code changes in small steps and run checks.",
            "Review edge cases, errors, and deployment notes.",
        ]
    return [
        "Clarify the target output and constraints.",
        f"Start with {tools[0]} for the first structured draft.",
        "Pass the result through the next tool in the workflow.",
        "Review quality, fill gaps, and export the final output.",
    ]


def _generic_followup_steps(profile: dict, tools: list[str]) -> list[str]:
    if profile["is_ppt"]:
        return [
            "Turn the draft into a page-by-page slide structure.",
            "Polish the visual hierarchy, chart labels, and speaker flow.",
            "Export an editable deck and do one final manual review.",
        ]
    if profile["is_research"]:
        return [
            "Extract key claims, evidence, and gaps.",
            "Rewrite the findings into a structured brief.",
            "Check sources and export the final report.",
        ]
    if profile["is_code"]:
        return [
            "Apply the suggested changes in small commits.",
            "Run tests or a local smoke check.",
            "Document remaining risks and deployment steps.",
        ]
    return [
        f"Use {tools[1] if len(tools) > 1 else tools[0] if tools else 'the next tool'} to refine the draft.",
        "Review quality and fill any missing context.",
        "Export or hand off the final output.",
    ]


def _comparison_rows(plans: list[AIRecommendedPlan]) -> list[dict[str, str]]:
    rows = []
    for plan in plans:
        rows.append(
            {
                "plan": plan.label,
                "workflow": plan.recommendation.title,
                "best_for": plan.best_for,
                "pros": ", ".join(plan.pros),
                "cons": ", ".join(plan.cons),
                "tradeoff": plan.tradeoff,
            }
        )
    return rows


def _feedback_scores(db: Session) -> dict[tuple[str, str], float]:
    weights = {
        "up": 0.06,
        "used": 0.08,
        "want_better": 0.01,
        "want_faster": -0.01,
        "too_complex": -0.05,
        "too_slow": -0.04,
        "down": -0.08,
    }
    scores: dict[tuple[str, str], float] = {}
    for record in db.scalars(select(AIRecommendationFeedbackRecord)).all():
        key = (record.source_type, record.source_id)
        scores[key] = scores.get(key, 0.0) + weights.get(record.rating, 0.0)
    return {key: max(-0.18, min(0.18, value)) for key, value in scores.items()}


def _feedback_to_read(record: AIRecommendationFeedbackRecord) -> AIRecommendationFeedbackRead:
    return AIRecommendationFeedbackRead(
        id=record.id,
        user_id=record.user_id,
        query=record.query,
        source_id=record.source_id,
        source_type=record.source_type,
        plan_type=record.plan_type,
        rating=record.rating,
        comment=record.comment,
        created_at=record.created_at,
    )


def _has_any(text: str, tokens: tuple[str, ...]) -> bool:
    return any(token.lower().replace(" ", "") in text for token in tokens)


def _primary_clarification_intent(query_intents: list[str], compact_query: str) -> str | None:
    if not query_intents:
        return None
    priority_markers: tuple[tuple[str, tuple[str, ...]], ...] = (
        ("research_report", ("研究报告", "行业研究", "公司研究", "竞品分析", "市场调研", "文献综述", "论文综述")),
        ("presentation_deck", ("ppt", "演示文档", "演示稿", "幻灯", "提案", "路演", "答辩")),
        ("coding_build", ("写代码", "编程", "前端", "后端", "api", "github", "部署", "修bug")),
        ("visual_design", ("视觉", "设计", "海报", "logo", "产品图", "社媒配图", "ui")),
        ("video_audio", ("视频", "短视频", "配音", "音乐", "mv", "剪辑", "口播")),
        ("automation_agent", ("自动化", "机器人", "知识库", "工单", "rag", "n8n", "zapier")),
        ("business_growth", ("营销", "销售", "客服", "电商", "crm", "线索", "投放")),
        ("data_analysis", ("excel", "csv", "数据表", "dashboard", "图表", "仪表盘", "bi")),
    )
    for intent, markers in priority_markers:
        if intent in query_intents and any(marker in compact_query for marker in markers):
            return intent
    return query_intents[0]


def _is_specific_enough(query: str, questions: list[AIClarificationQuestion]) -> bool:
    compact_len = len(query.replace(" ", ""))
    if compact_len >= 26 and len(questions) <= 2:
        return True
    if compact_len >= 16 and len(questions) <= 1:
        return True
    return not questions


def _with_profile(content: str, profile: dict) -> str:
    semantic_lines = [
        f"Semantic intents: {', '.join(profile.get('intents', []))}",
        f"Meaning: {'; '.join(profile.get('semantic_labels', []))}",
        f"Use cases: {'; '.join(profile.get('use_cases', []))}",
        f"Equivalent user wording: {', '.join(profile.get('expanded_terms', []))}",
    ]
    return "\n".join([content, *[line for line in semantic_lines if line.split(': ', 1)[-1].strip()]])


def _loads_metadata(raw: str) -> dict:
    try:
        value = json.loads(raw or "{}")
        return value if isinstance(value, dict) else {}
    except json.JSONDecodeError:
        return {}
