from __future__ import annotations

AI_SUBSKILLS: list[dict] = [
    {"id": "models-general-assistants", "category_id": "ai-models", "category_label": "AI MODELS", "label": "General AI Assistants", "label_cn": "通用 AI 助手", "sort_order": 10},
    {"id": "models-reasoning-long-context", "category_id": "ai-models", "category_label": "AI MODELS", "label": "Reasoning & Long Context", "label_cn": "推理与长上下文", "sort_order": 20},
    {"id": "models-chinese-ecosystem", "category_id": "ai-models", "category_label": "AI MODELS", "label": "Chinese Model Ecosystem", "label_cn": "中文模型生态", "sort_order": 30},
    {"id": "models-local-open-source", "category_id": "ai-models", "category_label": "AI MODELS", "label": "Local & Open Models", "label_cn": "本地与开源模型", "sort_order": 40},
    {"id": "coding-app-prototype", "category_id": "ai-coding", "category_label": "AI CODING", "label": "App & Prototype Build", "label_cn": "应用与原型构建", "sort_order": 10},
    {"id": "coding-code-edit-review", "category_id": "ai-coding", "category_label": "AI CODING", "label": "Code Edit & Review", "label_cn": "代码生成与审查", "sort_order": 20},
    {"id": "coding-devops-testing", "category_id": "ai-coding", "category_label": "AI CODING", "label": "DevOps, QA & Security", "label_cn": "部署测试与安全", "sort_order": 30},
    {"id": "coding-data-backend", "category_id": "ai-coding", "category_label": "AI CODING", "label": "Backend, API & Data Infra", "label_cn": "后端 API 与数据工程", "sort_order": 40},
    {"id": "visual-image-generation", "category_id": "ai-visual", "category_label": "AI VISUAL", "label": "Image Generation & Editing", "label_cn": "图像生成与修图", "sort_order": 10},
    {"id": "visual-brand-design", "category_id": "ai-visual", "category_label": "AI VISUAL", "label": "Brand & Graphic Design", "label_cn": "品牌与平面设计", "sort_order": 20},
    {"id": "visual-ui-prototype", "category_id": "ai-visual", "category_label": "AI VISUAL", "label": "UI, UX & Product Mockups", "label_cn": "UI/UX 与产品稿", "sort_order": 30},
    {"id": "visual-3d-assets", "category_id": "ai-visual", "category_label": "AI VISUAL", "label": "3D & Asset Pipeline", "label_cn": "3D 与资产管线", "sort_order": 40},
    {"id": "media-video-editing", "category_id": "ai-media", "category_label": "AI MEDIA", "label": "Video Generation & Editing", "label_cn": "视频生成与剪辑", "sort_order": 10},
    {"id": "media-audio-voice-music", "category_id": "ai-media", "category_label": "AI MEDIA", "label": "Audio, Voice & Music", "label_cn": "音频语音与音乐", "sort_order": 20},
    {"id": "media-avatar-livestream", "category_id": "ai-media", "category_label": "AI MEDIA", "label": "Avatar & Livestream", "label_cn": "数字人与直播", "sort_order": 30},
    {"id": "media-social-publishing", "category_id": "ai-media", "category_label": "AI MEDIA", "label": "Social Content Publishing", "label_cn": "社媒内容发布", "sort_order": 40},
    {"id": "office-ppt-decks", "category_id": "ai-office", "category_label": "AI OFFICE", "label": "PPT, Decks & Proposals", "label_cn": "PPT 提案与汇报", "sort_order": 10},
    {"id": "office-doc-writing", "category_id": "ai-office", "category_label": "AI OFFICE", "label": "Docs, Writing & Translation", "label_cn": "文档写作与翻译", "sort_order": 20},
    {"id": "office-sheets-data", "category_id": "ai-office", "category_label": "AI OFFICE", "label": "Sheets & Office Data", "label_cn": "表格与办公数据", "sort_order": 30},
    {"id": "office-meetings-knowledge", "category_id": "ai-office", "category_label": "AI OFFICE", "label": "Meetings, Notes & Knowledge", "label_cn": "会议笔记与知识库", "sort_order": 40},
    {"id": "research-web-search", "category_id": "ai-research", "category_label": "AI RESEARCH", "label": "Web Search & Source QA", "label_cn": "搜索与来源核查", "sort_order": 10},
    {"id": "research-academic-literature", "category_id": "ai-research", "category_label": "AI RESEARCH", "label": "Academic & Literature Review", "label_cn": "论文文献与综述", "sort_order": 20},
    {"id": "research-market-competitive", "category_id": "ai-research", "category_label": "AI RESEARCH", "label": "Market & Competitive Intel", "label_cn": "市场竞品与情报", "sort_order": 30},
    {"id": "research-data-reports", "category_id": "ai-research", "category_label": "AI RESEARCH", "label": "Data Analysis & Reports", "label_cn": "数据分析与报告", "sort_order": 40},
    {"id": "agent-workflow-automation", "category_id": "ai-agent", "category_label": "AI AGENT", "label": "Workflow Automation", "label_cn": "工作流自动化", "sort_order": 10},
    {"id": "agent-browser-task", "category_id": "ai-agent", "category_label": "AI AGENT", "label": "Browser & Task Agents", "label_cn": "浏览器与任务 Agent", "sort_order": 20},
    {"id": "agent-bots-rag", "category_id": "ai-agent", "category_label": "AI AGENT", "label": "Bots, RAG & Knowledge Agents", "label_cn": "Bot、RAG 与知识 Agent", "sort_order": 30},
    {"id": "agent-api-mcp-integrations", "category_id": "ai-agent", "category_label": "AI AGENT", "label": "API, MCP & Tool Integrations", "label_cn": "API、MCP 与工具连接", "sort_order": 40},
    {"id": "business-marketing-growth", "category_id": "ai-business", "category_label": "AI BUSINESS", "label": "Marketing, SEO & Growth", "label_cn": "营销 SEO 与增长", "sort_order": 10},
    {"id": "business-sales-crm", "category_id": "ai-business", "category_label": "AI BUSINESS", "label": "Sales, CRM & Outreach", "label_cn": "销售 CRM 与外联", "sort_order": 20},
    {"id": "business-support-community", "category_id": "ai-business", "category_label": "AI BUSINESS", "label": "Support, Community & Moderation", "label_cn": "客服社群与审核", "sort_order": 30},
    {"id": "business-ops-finance-legal", "category_id": "ai-business", "category_label": "AI BUSINESS", "label": "Ops, Finance, Legal & HR", "label_cn": "运营财务法务 HR", "sort_order": 40},
    {"id": "business-ecommerce-product", "category_id": "ai-business", "category_label": "AI BUSINESS", "label": "E-commerce & Product Ops", "label_cn": "电商与产品运营", "sort_order": 50},
]

SUBSKILLS_BY_ID = {item["id"]: item for item in AI_SUBSKILLS}

DEFAULT_BY_CATEGORY = {
    "ai-models": "models-general-assistants",
    "ai-coding": "coding-code-edit-review",
    "ai-visual": "visual-image-generation",
    "ai-media": "media-video-editing",
    "ai-office": "office-doc-writing",
    "ai-research": "research-web-search",
    "ai-agent": "agent-workflow-automation",
    "ai-business": "business-ops-finance-legal",
}

RULES_BY_CATEGORY = {
    "ai-models": [
        ("models-local-open-source", ("local", "open source", "ollama", "lm studio", "open webui", "本地", "开源", "私有", "qwen 开源", "glm 开源", "deepseek 开源")),
        ("models-chinese-ecosystem", ("豆包", "kimi", "元宝", "通义", "文小言", "秘塔", "纳米", "天工", "星火", "百度文库", "智谱", "中文")),
        ("models-reasoning-long-context", ("reasoning", "long context", "长上下文", "复杂推理", "长文档", "claude", "gemini")),
    ],
    "ai-coding": [
        ("coding-app-prototype", ("prototype", "app", "bolt", "lovable", "v0", "replit", "应用", "原型", "全栈")),
        ("coding-devops-testing", ("devops", "deploy", "test", "qa", "security", "ci", "github actions", "测试", "部署", "安全", "审计")),
        ("coding-data-backend", ("backend", "api", "database", "sql", "supabase", "firebase", "server", "后端", "数据工程", "接口")),
    ],
    "ai-visual": [
        ("visual-3d-assets", ("3d", "blender", "comfyui", "asset", "三维", "资产")),
        ("visual-ui-prototype", ("ui", "ux", "figma", "mockup", "wireframe", "界面", "产品稿")),
        ("visual-brand-design", ("brand", "logo", "canva", "graphic", "poster", "品牌", "海报", "平面")),
    ],
    "ai-media": [
        ("media-audio-voice-music", ("audio", "voice", "music", "suno", "udio", "elevenlabs", "音频", "语音", "音乐", "配音")),
        ("media-avatar-livestream", ("avatar", "livestream", "digital human", "heygen", "直播", "数字人")),
        ("media-social-publishing", ("social", "publish", "xhs", "tiktok", "youtube", "instagram", "社媒", "发布", "小红书", "短视频")),
    ],
    "ai-office": [
        ("office-ppt-decks", ("ppt", "slides", "deck", "gamma", "presentation", "提案", "汇报", "幻灯")),
        ("office-sheets-data", ("sheet", "excel", "spreadsheet", "table", "表格", "数据表")),
        ("office-meetings-knowledge", ("meeting", "notes", "knowledge", "notion", "obsidian", "granola", "会议", "纪要", "知识库")),
    ],
    "ai-research": [
        ("research-academic-literature", ("paper", "academic", "literature", "zotero", "elicit", "论文", "文献", "综述")),
        ("research-market-competitive", ("market", "competitive", "competitor", "industry", "竞品", "市场", "行业", "情报")),
        ("research-data-reports", ("data analysis", "dashboard", "report", "chart", "数据分析", "报告", "图表")),
    ],
    "ai-agent": [
        ("agent-browser-task", ("browser", "operator", "web task", "浏览器", "网页操作")),
        ("agent-bots-rag", ("bot", "rag", "knowledge agent", "chatbot", "问答", "知识 agent", "客服机器人")),
        ("agent-api-mcp-integrations", ("api", "mcp", "webhook", "connector", "integration", "接口", "工具连接")),
    ],
    "ai-business": [
        ("business-marketing-growth", ("marketing", "seo", "growth", "campaign", "copy", "营销", "增长", "投放")),
        ("business-sales-crm", ("sales", "crm", "outreach", "lead", "hubspot", "销售", "线索", "外联")),
        ("business-support-community", ("support", "community", "moderation", "zendesk", "客服", "社群", "审核")),
        ("business-ecommerce-product", ("e-commerce", "ecommerce", "shop", "product ops", "sku", "电商", "商品", "产品运营")),
    ],
}


def classify_subskill(data: dict) -> tuple[str, str]:
    category_id = data.get("category_id", "")
    existing = data.get("sub_skill_id") or ""
    if existing in SUBSKILLS_BY_ID:
        sub = SUBSKILLS_BY_ID[existing]
        return sub["id"], sub["label"]

    haystack = " ".join(
        str(data.get(key, ""))
        for key in ("id", "name", "title", "tool", "stage", "summary", "description", "source_section")
    )
    for key in ("tags", "tools", "steps", "outputs", "examples"):
        value = data.get(key) or []
        if isinstance(value, list):
            haystack += " " + " ".join(str(item) for item in value)
    haystack = haystack.lower()

    for sub_id, keywords in RULES_BY_CATEGORY.get(category_id, []):
        if any(keyword.lower() in haystack for keyword in keywords):
            sub = SUBSKILLS_BY_ID[sub_id]
            return sub["id"], sub["label"]

    sub = SUBSKILLS_BY_ID[DEFAULT_BY_CATEGORY.get(category_id, "models-general-assistants")]
    return sub["id"], sub["label"]
