from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class IntentDefinition:
    id: str
    label: str
    use_case: str
    triggers: tuple[str, ...]
    expansion_terms: tuple[str, ...]


INTENTS: tuple[IntentDefinition, ...] = (
    IntentDefinition(
        id="presentation_deck",
        label="Presentation, PPT, deck, proposal, and speaking document",
        use_case="Use when the user wants to make a PPT, slide deck, presentation document, proposal deck, speech deck, or work report.",
        triggers=("ppt", "presentation", "slides", "slide", "deck", "gamma", "beautiful.ai", "演示", "演示文档", "演示稿", "幻灯", "幻灯片", "汇报", "提案", "路演", "答辩"),
        expansion_terms=("ppt", "presentation", "slides", "deck", "proposal", "pitch", "gamma", "beautiful.ai", "演示文档", "演示稿", "幻灯片", "汇报", "提案"),
    ),
    IntentDefinition(
        id="research_report",
        label="Research, information gathering, report writing, and evidence synthesis",
        use_case="Use when the user wants market research, academic research, source synthesis, deep research, or a structured report.",
        triggers=("research", "report", "paper", "literature", "perplexity", "notebooklm", "elicit", "consensus", "研究", "调研", "报告", "研报", "论文", "文献", "资料", "综述"),
        expansion_terms=("research", "deep research", "report", "paper", "literature review", "sources", "perplexity", "notebooklm", "研究", "调研", "报告", "研报", "论文", "文献"),
    ),
    IntentDefinition(
        id="coding_build",
        label="Coding, product prototype, app build, debugging, and deployment",
        use_case="Use when the user wants to build software, write code, debug, prototype an app, or ship a web product.",
        triggers=("code", "coding", "cursor", "claude code", "github", "deploy", "saas", "react", "api", "代码", "编程", "开发", "网站", "网页", "应用", "后端", "前端", "部署", "调试"),
        expansion_terms=("code", "coding", "cursor", "claude code", "github", "react", "api", "debug", "deploy", "saas", "代码", "编程", "开发", "前端", "后端", "部署"),
    ),
    IntentDefinition(
        id="visual_design",
        label="Visual design, image generation, brand assets, and layout",
        use_case="Use when the user wants images, brand visuals, product graphics, UI visuals, posters, or design assets.",
        triggers=("image", "visual", "design", "brand", "poster", "midjourney", "recraft", "photoshop", "图片", "图像", "设计", "视觉", "海报", "品牌", "logo", "配图"),
        expansion_terms=("image", "visual", "design", "brand", "poster", "midjourney", "recraft", "photoshop", "canva", "图片", "图像", "视觉", "设计", "品牌", "海报"),
    ),
    IntentDefinition(
        id="video_audio",
        label="Video, audio, music, voice, avatar, and editing production",
        use_case="Use when the user wants videos, short clips, music, voiceover, avatar video, MV, or editing workflows.",
        triggers=("video", "audio", "music", "voice", "runway", "veo", "kling", "suno", "elevenlabs", "视频", "音频", "音乐", "配音", "声音", "剪辑", "短视频", "mv"),
        expansion_terms=("video", "audio", "music", "voice", "runway", "veo", "kling", "suno", "elevenlabs", "视频", "音频", "音乐", "配音", "剪辑", "短视频"),
    ),
    IntentDefinition(
        id="automation_agent",
        label="Automation, agent, bot, RAG, workflow orchestration, and tool connection",
        use_case="Use when the user wants automated workflows, bots, RAG systems, agents, integrations, or recurring operations.",
        triggers=("automation", "agent", "workflow", "bot", "rag", "n8n", "make", "zapier", "mcp", "自动化", "智能体", "机器人", "工作流", "流程", "知识库", "集成", "连接"),
        expansion_terms=("automation", "agent", "workflow", "bot", "rag", "n8n", "make", "zapier", "mcp", "自动化", "智能体", "工作流", "知识库", "集成"),
    ),
    IntentDefinition(
        id="business_growth",
        label="Business, marketing, sales, CRM, support, and growth operations",
        use_case="Use when the user wants marketing, sales outreach, CRM operations, customer support, ecommerce, or growth campaigns.",
        triggers=("marketing", "sales", "crm", "support", "customer", "seo", "campaign", "hubspot", "zendesk", "intercom", "营销", "销售", "客服", "客户", "增长", "电商", "邮件", "投放", "线索"),
        expansion_terms=("marketing", "sales", "crm", "support", "customer", "seo", "campaign", "hubspot", "zendesk", "营销", "销售", "客服", "增长", "电商", "线索"),
    ),
    IntentDefinition(
        id="data_analysis",
        label="Data analysis, spreadsheet, dashboard, finance, and visualization",
        use_case="Use when the user wants spreadsheet analysis, dashboards, charts, financial analysis, data storytelling, or metrics.",
        triggers=("data", "spreadsheet", "excel", "sheet", "dashboard", "chart", "finance", "snowflake", "hex", "数据", "表格", "仪表盘", "图表", "财务", "分析", "可视化"),
        expansion_terms=("data", "spreadsheet", "excel", "dashboard", "chart", "finance", "snowflake", "hex", "数据", "表格", "仪表盘", "图表", "财务", "可视化"),
    ),
)


def detect_intents(text: str, limit: int = 3) -> list[tuple[str, float]]:
    lowered = text.lower()
    compact = re.sub(r"\s+", "", lowered)
    scores: list[tuple[str, float]] = []
    for intent in INTENTS:
        score = 0.0
        for trigger in intent.triggers:
            trigger_l = trigger.lower()
            if trigger_l in lowered or trigger_l.replace(" ", "") in compact:
                score += 2.0 if len(trigger_l) >= 4 else 1.0
        if score:
            scores.append((intent.id, score))
    scores.sort(key=lambda item: item[1], reverse=True)
    return scores[:limit]


def intent_ids(text: str, limit: int = 3) -> list[str]:
    return [intent_id for intent_id, _score in detect_intents(text, limit=limit)]


def expand_text_with_intents(text: str) -> str:
    ids = set(intent_ids(text, limit=4))
    additions: list[str] = []
    for intent in INTENTS:
        if intent.id in ids:
            additions.extend([intent.label, intent.use_case, " ".join(intent.expansion_terms)])
    return "\n".join([text, *additions])


def intent_profile(title: str, parts: list[str]) -> dict:
    text = "\n".join([title, *parts])
    ids = intent_ids(text, limit=4)
    definitions = [intent for intent in INTENTS if intent.id in ids]
    return {
        "intents": ids,
        "use_cases": [intent.use_case for intent in definitions],
        "semantic_labels": [intent.label for intent in definitions],
        "expanded_terms": sorted({term for intent in definitions for term in intent.expansion_terms}),
    }
