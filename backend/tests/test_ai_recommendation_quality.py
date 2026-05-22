from __future__ import annotations

from collections import Counter
from itertools import product

from fastapi.testclient import TestClient

from app.main import app


QUALITY_CASES = (
    (
        "presentation_deck",
        ("ppt", "presentation", "deck", "slides", "gamma", "canva", "演示", "幻灯", "汇报", "提案"),
        (
            "我想做一个给客户看的 PPT，我有资料，今天要，正式一点",
            "我需要把旧 PPT 美化成给老板看的团队汇报",
            "我要做论文答辩演示文档，需要逻辑严谨",
        ),
    ),
    (
        "coding_build",
        ("cursor", "claude code", "github", "react", "api", "code", "代码", "编程", "部署"),
        (
            "我想做一个前端网站，有 GitHub repo，最后要部署上线",
            "我想给现有项目加一个后端 API，有本地代码",
            "我想修一个网站 bug，并且让 AI 帮我检查代码",
        ),
    ),
    (
        "research_report",
        ("research", "perplexity", "notebooklm", "elicit", "paper", "报告", "研究", "文献", "调研"),
        (
            "我想做新能源汽车行业研究，最后要完整报告",
            "我想做公司研究和竞品分析，最后要一页 brief",
            "我需要做论文文献综述，并整理成中英双语报告",
        ),
    ),
    (
        "visual_design",
        ("canva", "midjourney", "recraft", "photoshop", "figma", "visual", "设计", "海报", "logo"),
        (
            "我想做一个品牌海报和 logo 视觉设计，要适合社媒投放",
            "我想做电商产品图，有参考图，需要可商用素材",
            "我想做 App UI 视觉，有 Figma 设计稿",
        ),
    ),
    (
        "video_audio",
        ("video", "runway", "veo", "kling", "suno", "elevenlabs", "capcut", "视频", "配音", "剪辑"),
        (
            "我想做一个短视频和配音，用来发小红书",
            "我想把长视频切成 YouTube Shorts 和 TikTok 短视频",
            "我想做产品广告视频，需要脚本、配音和剪辑",
        ),
    ),
    (
        "automation_agent",
        ("automation", "agent", "bot", "rag", "n8n", "zapier", "coze", "dify", "自动化", "机器人", "知识库", "工单"),
        (
            "我想做一个自动化客服机器人，连接知识库和工单系统",
            "我想用 n8n 把报表数据定时推送到 Slack",
            "我想做一个企业知识库问答 RAG bot，连接 Notion",
        ),
    ),
    (
        "business_growth",
        ("sales", "crm", "marketing", "hubspot", "apollo", "clay", "zendesk", "营销", "销售", "客服", "线索"),
        (
            "我想做营销邮件和 CRM 销售线索跟进流程",
            "我想优化 Shopify 电商运营，并做广告投放复盘",
            "我想做客服支持系统，自动整理客户问题",
        ),
    ),
    (
        "data_analysis",
        ("excel", "spreadsheet", "sheet", "dashboard", "chart", "power bi", "hex", "snowflake", "数据", "表格", "图表", "仪表盘"),
        (
            "我想分析 Excel 数据表并做一个 dashboard 图表",
            "我想把 BigQuery 数据做成管理层 BI 仪表盘",
            "我想清洗 CSV 数据，生成业务分析报告",
        ),
    ),
)


def _post_advice(client: TestClient, query: str, top_k: int = 3) -> dict:
    response = client.post("/api/v1/ai-skills/advice", json={"query": query, "top_k": top_k})
    assert response.status_code == 200
    return response.json()


def _plan_text(payload: dict) -> str:
    return " ".join(
        " ".join(
            [
                plan["recommendation"]["title"],
                plan["recommendation"].get("summary", ""),
                " ".join(plan["recommendation"].get("tools", [])),
                " ".join(plan["recommendation"].get("tags", [])),
                plan.get("best_for", ""),
            ]
        )
        for plan in payload["plans"]
    ).lower()


def _top3(payload: dict) -> tuple[str, ...]:
    return tuple(plan["recommendation"]["source_id"] for plan in payload["plans"][:3])


def test_ai_advice_quality_covers_all_major_intents() -> None:
    with TestClient(app) as client:
        for expected_intent, expected_terms, queries in QUALITY_CASES:
            for query in queries:
                payload = _post_advice(client, query)
                assert payload["needs_clarification"] is False, query
                assert expected_intent in payload["intent_ids"], query
                assert len(payload["plans"]) == 3, query
                text = _plan_text(payload)
                assert any(term in text for term in expected_terms), query
                assert len(set(_top3(payload))) == 3, query


def test_ai_advice_vague_queries_ask_option_questions_for_every_major_intent() -> None:
    vague_queries = {
        "presentation_deck": "我想做 PPT",
        "coding_build": "我想写代码",
        "research_report": "我想做研究",
        "visual_design": "我想做设计",
        "video_audio": "我想做视频",
        "automation_agent": "我想做自动化",
        "business_growth": "我想做营销",
        "data_analysis": "我想分析数据",
    }

    with TestClient(app) as client:
        for expected_intent, query in vague_queries.items():
            payload = _post_advice(client, query)
            assert expected_intent in payload["intent_ids"], query
            assert payload["needs_clarification"] is True, query
            assert payload["clarification_questions"], query
            assert all(question["options"] for question in payload["clarification_questions"]), query


def test_ppt_option_matrix_changes_rankings_without_missing_plans() -> None:
    audiences = ["给客户看", "给老师/课堂汇报", "给老板/团队看", "给投资人路演", "论文答辩"]
    materials = ["已有文档/资料", "只有主题，从零开始", "有数据表", "有链接/网页资料", "有旧 PPT 需要美化"]
    priorities = ["越快越好", "要好看", "要正式专业", "要逻辑严谨", "要适合商业提案"]

    rankings: list[tuple[str, ...]] = []
    with TestClient(app) as client:
        for audience, material, priority in product(audiences, materials, priorities):
            payload = _post_advice(client, f"我想做 PPT；{audience}；{material}；{priority}")
            assert payload["needs_clarification"] is False
            assert len(payload["plans"]) == 3
            rankings.append(_top3(payload))

    assert len(set(rankings)) >= 100
    assert Counter(rankings).most_common(1)[0][1] <= 4


def test_coding_and_research_option_matrices_change_rankings() -> None:
    matrices = (
        (
            "我想写代码",
            ["做前端网页", "做后端 API", "做完整 App 原型", "修 bug", "部署上线"],
            ["有 GitHub repo", "有本地代码", "有 Figma/设计稿", "只有想法，从零开始"],
            10,
        ),
        (
            "我想做研究报告",
            ["行业研究", "公司研究", "竞品分析", "论文/文献综述", "市场调研"],
            ["完整报告", "汇报 PPT", "Excel/表格", "一页 brief", "中英双语版本"],
            12,
        ),
    )

    with TestClient(app) as client:
        for prefix, first_axis, second_axis, min_unique in matrices:
            rankings = []
            for first, second in product(first_axis, second_axis):
                payload = _post_advice(client, f"{prefix}；{first}；{second}")
                assert payload["needs_clarification"] is False, (prefix, first, second)
                assert len(payload["plans"]) == 3, (prefix, first, second)
                rankings.append(_top3(payload))
            assert len(set(rankings)) >= min_unique, prefix


def test_non_ppt_major_intent_use_cases_produce_distinct_rankings() -> None:
    use_case_queries = (
        ("visual", ["我想做品牌海报；有参考图/素材", "我想做 Logo / 品牌识别；需要多版风格", "我想做产品图 / 电商图；需要可商用素材"]),
        ("video", ["我想做短视频剪辑；小红书 / 抖音", "我想做配音 / 多语音频；YouTube / Shorts", "我想做产品广告视频；广告投放"]),
        ("automation", ["我想做客服机器人 / 工单；Zendesk / Intercom", "我想做知识库问答 / RAG；Notion / Airtable", "我想做报表 / 数据推送；飞书 / 钉钉 / Slack"]),
        ("business", ["我想做营销活动 / 广告；社媒 / 广告", "我想做销售线索 / CRM；CRM / HubSpot", "我想做客服支持；客服系统"]),
        ("data", ["我想做 Excel / CSV；清洗 / 整理数据", "我想做数据库 / BigQuery；Dashboard / 仪表盘", "我想做 Snowflake / BI；图表 / 可视化"]),
    )

    with TestClient(app) as client:
        for label, queries in use_case_queries:
            rankings = [_top3(_post_advice(client, query)) for query in queries]
            assert len(set(rankings)) >= 2, label
