from __future__ import annotations

import re

# Generated from /Users/jasminezhang1357/Desktop/AI工作流100条.pdf.
# The PDF is treated as a seed source for AI Skill Database items.
# Each source row produces one combination item and one workflow item;
# missing tools from those combinations are added as contextual skills.

AIW100_SOURCE = "AI工作流100条.pdf"

AIW100_WORKFLOWS = [
    {
        "num": "001",
        "title": "YouTube 长视频→多平台短视频矩阵",
        "id_slug": "youtube-long-video-multi-platform-short-video-matrix",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "yt-dlp",
            "Whisper",
            "AssemblyAI",
            "ChatGPT",
            "Opus Clip",
            "Submagic",
            "ElevenLabs",
            "HeyGen",
            "Buffer"
        ],
        "steps": [
            "yt-dlp 下载源视频",
            "Whisper/AssemblyAI 转写",
            "GPT-4 提炼 10 个高光点",
            "Opus Clip 自动切片+ClipScore 排序",
            "Submagic 加爆款字幕特效",
            "ElevenLabs 多语种配音",
            "HeyGen 对口型",
            "Buffer 一键分发 TikTok/Reels/Shorts，单条长视频裂变出 50+ 条短内容。"
        ],
        "outputs": [
            "YouTube 长视频→多平台短视频矩阵"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：YouTube 长视频→多平台短视频矩阵。工具链：yt-dlp + Whisper + AssemblyAI + ChatGPT + Opus Clip + Submagic + ElevenLabs + HeyGen。",
        "tags": [
            "media",
            "youtube"
        ],
        "importance": 95,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "002",
        "title": "PRD→上线 SaaS 全栈一日流",
        "id_slug": "prd-launch-saas-full-stack",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "ChatGPT",
            "v0",
            "Claude",
            "Stripe",
            "Vercel",
            "PostHog"
        ],
        "steps": [
            "ChatGPT o1 写 PRD+用户故事",
            "v0.dev 生成 React+Tailwind UI",
            "截图导入 Cursor Composer 接 Supabase 后端",
            "Claude Sonnet 写测试",
            "Stripe MCP 接支付",
            "Vercel 部署",
            "PostHog 埋点",
            "当天可上线收费 MVP，独立开发者周末项目标配。"
        ],
        "outputs": [
            "PRD→上线 SaaS 全栈一日流"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：PRD→上线 SaaS 全栈一日流。工具链：ChatGPT + v0 + Claude + Stripe + Vercel + PostHog。",
        "tags": [
            "coding",
            "saas"
        ],
        "importance": 95,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "003",
        "title": "企业内部知识库智能问答",
        "id_slug": "knowledge-base-qa",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Notion",
            "Confluence",
            "Unstructured",
            "LlamaIndex",
            "Qdrant",
            "Dify",
            "Claude",
            "Slack",
            "Langfuse"
        ],
        "steps": [
            "Notion/Confluence 文档导出",
            "Unstructured 解析",
            "LlamaIndex 切块嵌入",
            "Qdrant 向量库",
            "Dify 编排 RAG 工作流",
            "Claude 3.5 Haiku 做检索答复",
            "Slack Bot 出口",
            "Langfuse 监控；员工问报销流程秒回带原文链接。"
        ],
        "outputs": [
            "企业内部知识库智能问答"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：企业内部知识库智能问答。工具链：Notion + Confluence + Unstructured + LlamaIndex + Qdrant + Dify + Claude + Slack。",
        "tags": [
            "office",
            "rag"
        ],
        "importance": 95,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "004",
        "title": "销售外联个性化批量化",
        "id_slug": "sales-outreach-quant",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Apollo",
            "Clay",
            "ChatGPT",
            "Lavender",
            "Smartlead",
            "HubSpot",
            "Gong"
        ],
        "steps": [
            "Apollo 拉 ICP 名单",
            "Clay 用 LinkedIn+网站+招聘动态做 enrichment",
            "GPT-4o 按公司新闻写个性化首句",
            "Lavender 实时打分优化",
            "Smartlead 多账号轮发",
            "HubSpot 自动入 CRM",
            "Gong 录跟进电话",
            "整体回复率从 1% 拉到 8%。"
        ],
        "outputs": [
            "销售外联个性化批量化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：销售外联个性化批量化。工具链：Apollo + Clay + ChatGPT + Lavender + Smartlead + HubSpot + Gong。",
        "tags": [
            "business",
            "crm"
        ],
        "importance": 95,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "005",
        "title": "跨境电商商品页全自动化",
        "id_slug": "product-page",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "1688",
            "Magnific",
            "Photoshop AI",
            "FLUX",
            "Ideogram",
            "ChatGPT",
            "DeepL",
            "Shopify"
        ],
        "steps": [
            "1688 抓图",
            "Magnific 放大",
            "Photoshop Generative Fill 去水印",
            "Flux+品牌 LoRA 重绘场景",
            "Ideogram 生成多语 slogan 海报",
            "ChatGPT 写 SEO 标题描述",
            "DeepL 翻译 7 国语",
            "Shopify 批量上架，10 分钟一个 SKU。"
        ],
        "outputs": [
            "跨境电商商品页全自动化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：跨境电商商品页全自动化。工具链：1688 + Magnific + Photoshop AI + FLUX + Ideogram + ChatGPT + DeepL + Shopify。",
        "tags": [
            "media",
            "seo"
        ],
        "importance": 94,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "006",
        "title": "行业深度研究报告",
        "id_slug": "industry-deep-research-report",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Perplexity Deep Research",
            "Genspark",
            "Stanford Storm",
            "NotebookLM",
            "Claude",
            "Gamma",
            "ElevenLabs"
        ],
        "steps": [
            "Perplexity Deep Research 跑初轮",
            "Genspark 补多源",
            "Stanford Storm 生成综述大纲",
            "NotebookLM 上传 30 篇 PDF 抽要点",
            "Claude Projects 整合写正稿",
            "Gamma 出 PPT 版",
            "ElevenLabs 录播客版，研究员一周量压缩到一天。"
        ],
        "outputs": [
            "行业深度研究报告"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：行业深度研究报告。工具链：Perplexity Deep Research + Genspark + Stanford Storm + NotebookLM + Claude + Gamma + ElevenLabs。",
        "tags": [
            "media",
            "research"
        ],
        "importance": 94,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "007",
        "title": "YouTube 频道选题到成片流水线",
        "id_slug": "youtube-channel-topic-production",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "VidIQ",
            "TubeBuddy",
            "ChatGPT",
            "Midjourney",
            "Runway",
            "Descript",
            "Submagic"
        ],
        "steps": [
            "VidIQ/TubeBuddy 找蓝海关键词",
            "ChatGPT 写脚本+缩略图 prompt",
            "Midjourney v7+sref 出缩略图",
            "Runway Gen-3 做开场转场",
            "Descript 录制+去停顿",
            "Submagic 加字幕",
            "TubeBuddy 优化标题，单人频道日更不掉线。"
        ],
        "outputs": [
            "YouTube 频道选题到成片流水线"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：YouTube 频道选题到成片流水线。工具链：VidIQ + TubeBuddy + ChatGPT + Midjourney + Runway + Descript + Submagic。",
        "tags": [
            "media",
            "youtube"
        ],
        "importance": 94,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "008",
        "title": "AI 数字人带货直播",
        "id_slug": "ai-avatar-selling-livestream",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "ElevenLabs",
            "HeyGen Interactive Avatar",
            "飞瓜",
            "OBS"
        ],
        "steps": [
            "ChatGPT 写直播脚本",
            "ElevenLabs 克隆主播声",
            "HeyGen Interactive Avatar 做实时数字人",
            "飞瓜监听弹幕",
            "GPT 实时生成回复",
            "OBS 推流抖音；24 小时无人直播。"
        ],
        "outputs": [
            "AI 数字人带货直播"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 数字人带货直播。工具链：ChatGPT + ElevenLabs + HeyGen Interactive Avatar + 飞瓜 + OBS。",
        "tags": [
            "media"
        ],
        "importance": 94,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "009",
        "title": "个人品牌 LinkedIn 增长引擎",
        "id_slug": "personal-brand-linkedin-growth",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Taplio",
            "Claude",
            "ChatGPT",
            "Canva",
            "Buffer",
            "Phantombuster"
        ],
        "steps": [
            "Taplio 监听竞品 viral 帖",
            "Claude 仿写个人语调",
            "ChatGPT 配 carousel 文案",
            "Canva Magic 出 10 页轮播",
            "Buffer 排程",
            "Phantombuster 自动评论同行帖；3 个月涨 1 万粉。"
        ],
        "outputs": [
            "个人品牌 LinkedIn 增长引擎"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：个人品牌 LinkedIn 增长引擎。工具链：Taplio + Claude + ChatGPT + Canva + Buffer + Phantombuster。",
        "tags": [
            "visual"
        ],
        "importance": 94,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "010",
        "title": "Cold Email→Demo 预约自动化",
        "id_slug": "cold-email-demo",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Apollo",
            "Instantly",
            "Lemlist",
            "Lavender",
            "Calendly",
            "Fireflies",
            "ChatGPT",
            "Pipedrive"
        ],
        "steps": [
            "Apollo 找邮箱",
            "Instantly 暖号",
            "Lemlist 多轮序列",
            "Lavender 改写",
            "Calendly 自动约会",
            "Fireflies 录 demo",
            "ChatGPT 写跟进邮件",
            "Pipedrive 推进阶段，BDR 单人月产 80 个 demo。"
        ],
        "outputs": [
            "Cold Email→Demo 预约自动化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：Cold Email→Demo 预约自动化。工具链：Apollo + Instantly + Lemlist + Lavender + Calendly + Fireflies + ChatGPT + Pipedrive。",
        "tags": [
            "agent"
        ],
        "importance": 93,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "011",
        "title": "用户研究访谈全闭环",
        "id_slug": "user-research-interview",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Calendly",
            "Otter",
            "Dovetail",
            "ChatGPT",
            "Claude",
            "Notion AI",
            "Figma"
        ],
        "steps": [
            "Calendly 约谈",
            "Otter 录音",
            "Dovetail 上传转录",
            "GPT-4 自动打标签做亲和图",
            "Claude 生成洞察",
            "Notion AI 写成研究报告",
            "Figma 联动出原型，PM 周期从 4 周压到 1 周。"
        ],
        "outputs": [
            "用户研究访谈全闭环"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：用户研究访谈全闭环。工具链：Calendly + Otter + Dovetail + ChatGPT + Claude + Notion AI + Figma。",
        "tags": [
            "research"
        ],
        "importance": 93,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "012",
        "title": "软件 Bug 定位到修复",
        "id_slug": "software-bug-debug-fix",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Sentry",
            "Linear",
            "Claude Code",
            "复现",
            "二分",
            "gh pr create",
            "Greptile",
            "合并"
        ],
        "steps": [
            "Sentry 抓异常",
            "Linear 自动建 ticket",
            "Claude Code 拉 ticket 读代码库",
            "复现+二分定位",
            "改完跑 Vitest",
            "gh pr create",
            "Greptile 自动 review",
            "合并部署，老项目维护近全自动。"
        ],
        "outputs": [
            "软件 Bug 定位到修复"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：软件 Bug 定位到修复。工具链：Sentry + Linear + Claude Code + 复现 + 二分 + gh pr create + Greptile + 合并。",
        "tags": [
            "coding"
        ],
        "importance": 93,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "013",
        "title": "产品文档双语同步",
        "id_slug": "product-docs-bilingual",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Mintlify",
            "ChatGPT",
            "Claude",
            "Crowdin",
            "Algolia DocSearch",
            "Discord"
        ],
        "steps": [
            "Mintlify 写英文 docs",
            "GPT-4o 翻译中文",
            "Claude 校对术语一致性",
            "Crowdin 管多语版本",
            "Algolia DocSearch 接搜索",
            "Discord Bot 答用户问，开源项目国际化标配。"
        ],
        "outputs": [
            "产品文档双语同步"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：产品文档双语同步。工具链：Mintlify + ChatGPT + Claude + Crowdin + Algolia DocSearch + Discord。",
        "tags": [
            "office"
        ],
        "importance": 93,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "014",
        "title": "AI 播客制作流水线",
        "id_slug": "ai-podcast",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Perplexity",
            "Riverside.fm",
            "Descript",
            "Auphonic",
            "Castmagic",
            "Spotify",
            "Apple"
        ],
        "steps": [
            "ChatGPT o1 头脑风暴选题",
            "Perplexity 找嘉宾资料",
            "Riverside.fm 多机位录",
            "Descript 文字剪辑",
            "Auphonic 自动调音",
            "Castmagic 生成 show notes+timestamps",
            "Spotify+Apple 一键分发，单期成本砍半。"
        ],
        "outputs": [
            "AI 播客制作流水线"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 播客制作流水线。工具链：ChatGPT + Perplexity + Riverside.fm + Descript + Auphonic + Castmagic + Spotify + Apple。",
        "tags": [
            "media"
        ],
        "importance": 93,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "015",
        "title": "跨境出海视频本地化",
        "id_slug": "localization",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Whisper",
            "DeepL",
            "ElevenLabs",
            "HeyGen",
            "CapCut",
            "YouTube"
        ],
        "steps": [
            "原版视频",
            "Whisper 转录",
            "DeepL 翻 10 语",
            "ElevenLabs Dubbing 克隆原声多语版",
            "HeyGen 改口型",
            "CapCut 加本地字幕风格",
            "YouTube 多语轨上传，海外 view 翻 5 倍。"
        ],
        "outputs": [
            "跨境出海视频本地化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：跨境出海视频本地化。工具链：Whisper + DeepL + ElevenLabs + HeyGen + CapCut + YouTube。",
        "tags": [
            "media",
            "youtube"
        ],
        "importance": 92,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "016",
        "title": "AI 课程设计与售卖",
        "id_slug": "ai-course-design",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Claude",
            "HeyGen",
            "Synthesia",
            "Heptabase",
            "Teachable",
            "Beehiiv",
            "独立讲师月入过万"
        ],
        "steps": [
            "ChatGPT 拆课程大纲",
            "Claude 写每节脚本",
            "HeyGen 录数字人讲解",
            "Synthesia 做配套培训视频",
            "Heptabase 建知识图谱",
            "Teachable 上架",
            "Beehiiv 邮件营销，独立讲师月入过万。"
        ],
        "outputs": [
            "AI 课程设计与售卖"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 课程设计与售卖。工具链：ChatGPT + Claude + HeyGen + Synthesia + Heptabase + Teachable + Beehiiv + 独立讲师月入过万。",
        "tags": [
            "media"
        ],
        "importance": 92,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "017",
        "title": "竞品监控自动情报",
        "id_slug": "competitor",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Visualping",
            "Diffbot",
            "BuiltWith",
            "Apollo",
            "Clay",
            "Claude",
            "Slack"
        ],
        "steps": [
            "Visualping 监控竞品落地页变化",
            "Diffbot 抓 SEC/招聘",
            "BuiltWith 看技术栈",
            "Apollo 跟踪人员变动",
            "Clay 聚合",
            "Claude 周报告生成",
            "Slack 推送，市场团队信息差归零。"
        ],
        "outputs": [
            "竞品监控自动情报"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：竞品监控自动情报。工具链：Visualping + Diffbot + BuiltWith + Apollo + Clay + Claude + Slack。",
        "tags": [
            "office"
        ],
        "importance": 92,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "018",
        "title": "AI 代码审查机器人",
        "id_slug": "ai-code-review",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "GitHub Actions",
            "Claude Code"
        ],
        "steps": [
            "GitHub Action 触发",
            "Claude Code 读 diff",
            "跑 ESLint/Semgrep",
            "调用 Greptile 跨仓库找类似 bug",
            "自动评论 inline",
            "必要时 @ 工程师",
            "合并后 Datadog 监控异常，团队 review 时间砍 70%。"
        ],
        "outputs": [
            "AI 代码审查机器人"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 代码审查机器人。工具链：GitHub Actions + Claude Code。",
        "tags": [
            "coding",
            "data"
        ],
        "importance": 92,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "019",
        "title": "个人财务智能管家",
        "id_slug": "finance",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Cursor",
            "Metabase",
            "Notion"
        ],
        "steps": [
            "招商/支付宝账单 PDF",
            "ChatGPT 解析",
            "Cursor 写脚本入 PostgreSQL",
            "Metabase 建仪表盘",
            "GPT 月度分析消费习惯",
            "Notion 推送理财建议，理财小白 30 分钟搭建。"
        ],
        "outputs": [
            "个人财务智能管家"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：个人财务智能管家。工具链：ChatGPT + Cursor + Metabase + Notion。",
        "tags": [
            "business"
        ],
        "importance": 92,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "020",
        "title": "学术论文写作助手",
        "id_slug": "paper-assistant",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Scite",
            "Consensus",
            "Zotero",
            "SciSpace",
            "NotebookLM",
            "Claude",
            "Grammarly",
            "QuillBot",
            "Overleaf",
            "Turnitin"
        ],
        "steps": [
            "Scite/Consensus 找文献",
            "Zotero 管引用",
            "SciSpace 阅读总结",
            "NotebookLM 跨文献问答",
            "Claude 写初稿",
            "Grammarly+QuillBot 润色",
            "Overleaf 排版",
            "Turnitin 查重，硕博效率翻倍。"
        ],
        "outputs": [
            "学术论文写作助手"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：学术论文写作助手。工具链：Scite + Consensus + Zotero + SciSpace + NotebookLM + Claude + Grammarly + QuillBot。",
        "tags": [
            "research"
        ],
        "importance": 91,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "021",
        "title": "数据分析自然语言查询",
        "id_slug": "data-analysis-natural-language-query",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Snowflake",
            "dbt",
            "Cube.dev",
            "Cursor",
            "MCP",
            "自然语言",
            "Hex",
            "Mode",
            "Slack",
            "业务团队不"
        ],
        "steps": [
            "Snowflake 数仓",
            "dbt 建语义层",
            "Cube.dev 暴露 API",
            "Cursor+MCP 接",
            "自然语言提问自动写 SQL",
            "Hex/Mode 出图",
            "Slack 定时推送，业务团队不用催数据组。"
        ],
        "outputs": [
            "数据分析自然语言查询"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：数据分析自然语言查询。工具链：Snowflake + dbt + Cube.dev + Cursor + MCP + 自然语言 + Hex + Mode。",
        "tags": [
            "agent"
        ],
        "importance": 91,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "022",
        "title": "UI 设计→可点击原型",
        "id_slug": "ui-design-prototype",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Mobbin",
            "Galileo AI",
            "Figma",
            "Magician",
            "Anima",
            "v0",
            "Cursor",
            "Vercel"
        ],
        "steps": [
            "Mobbin 找参考",
            "Galileo AI 一句话出布局",
            "Figma 微调",
            "Magician 插件补图标",
            "Anima 转代码",
            "v0 生成 React",
            "Cursor 接 API",
            "Vercel 预览，设计交付速度 3 倍。"
        ],
        "outputs": [
            "UI 设计→可点击原型"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：UI 设计→可点击原型。工具链：Mobbin + Galileo AI + Figma + Magician + Anima + v0 + Cursor + Vercel。",
        "tags": [
            "coding"
        ],
        "importance": 91,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "023",
        "title": "AI 简历优化求职流",
        "id_slug": "ai-resume-job-search",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Teal HQ",
            "Resume Worded",
            "ChatGPT",
            "Earkick",
            "Yoodli",
            "LinkedIn Recruiter"
        ],
        "steps": [
            "Teal HQ 解析 JD",
            "Resume Worded 评分简历",
            "ChatGPT 按 STAR 改写",
            "Earkick 模拟面试",
            "Yoodli 练表达",
            "LinkedIn Recruiter Lite 反向触达 HR，月均 5 个 onsite。"
        ],
        "outputs": [
            "AI 简历优化求职流"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 简历优化求职流。工具链：Teal HQ + Resume Worded + ChatGPT + Earkick + Yoodli + LinkedIn Recruiter。",
        "tags": [
            "office"
        ],
        "importance": 91,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "024",
        "title": "内容 SEO 全栈打法",
        "id_slug": "content-seo-full-stack",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Ahrefs",
            "Surfer SEO",
            "Claude",
            "Frase",
            "Midjourney",
            "Wordable",
            "Schema",
            "Google Search Console"
        ],
        "steps": [
            "Ahrefs 找关键词",
            "Surfer SEO 出 brief",
            "Claude 写长文",
            "Frase 优化 NLP 词频",
            "Midjourney 配封面",
            "Wordable 推 WordPress",
            "Schema 自动结构化",
            "Google Search Console 监控，3 月 0",
            "10 万 UV。"
        ],
        "outputs": [
            "内容 SEO 全栈打法"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：内容 SEO 全栈打法。工具链：Ahrefs + Surfer SEO + Claude + Frase + Midjourney + Wordable + Schema + Google Search Console。",
        "tags": [
            "research",
            "seo"
        ],
        "importance": 91,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "025",
        "title": "AI 招聘到入职闭环",
        "id_slug": "ai-recruiting-onboarding",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "JobScan",
            "LinkedIn Recruiter",
            "Hireflix",
            "ChatGPT",
            "Greenhouse",
            "DocuSign",
            "BambooHR",
            "Notion"
        ],
        "steps": [
            "JobScan 写 JD",
            "LinkedIn Recruiter 搜",
            "Hireflix 异步面试",
            "ChatGPT 评分录像",
            "Greenhouse ATS",
            "DocuSign offer",
            "BambooHR onboard",
            "Notion 入职手册自动生成。"
        ],
        "outputs": [
            "AI 招聘到入职闭环"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 招聘到入职闭环。工具链：JobScan + LinkedIn Recruiter + Hireflix + ChatGPT + Greenhouse + DocuSign + BambooHR + Notion。",
        "tags": [
            "business"
        ],
        "importance": 90,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "026",
        "title": "法务合同 AI 审查",
        "id_slug": "legal-contract-ai",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DocuSign",
            "PandaDoc",
            "Spellbook",
            "Harvey",
            "Robin",
            "Claude",
            "Ironclad",
            "Notion"
        ],
        "steps": [
            "DocuSign/PandaDoc 收稿",
            "Spellbook 比对模板",
            "Harvey/Robin 标条款风险",
            "Claude 改红线",
            "Ironclad 走审批",
            "DocuSign 签",
            "Notion 归档可检索，律师省 70% 时间。"
        ],
        "outputs": [
            "法务合同 AI 审查"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：法务合同 AI 审查。工具链：DocuSign + PandaDoc + Spellbook + Harvey + Robin + Claude + Ironclad + Notion。",
        "tags": [
            "business"
        ],
        "importance": 90,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "027",
        "title": "客户支持 Tier1 自动化",
        "id_slug": "support-tier1",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Intercom",
            "Pylon",
            "Loom"
        ],
        "steps": [
            "Intercom Fin AI 接前线",
            "接 Zendesk 历史工单 RAG",
            "解决不了升 Tier2",
            "Pylon 给工程师上下文",
            "Loom 录解释视频",
            "自动 KB 沉淀，CSAT 不降反升。"
        ],
        "outputs": [
            "客户支持 Tier1 自动化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：客户支持 Tier1 自动化。工具链：Intercom + Pylon + Loom。",
        "tags": [
            "media",
            "rag"
        ],
        "importance": 90,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "028",
        "title": "营销活动从创意到投放",
        "id_slug": "marketing",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Midjourney",
            "Runway",
            "ElevenLabs",
            "Meta Advantage",
            "Triple Whale",
            "Northbeam"
        ],
        "steps": [
            "ChatGPT brainstorm slogan",
            "Midjourney 出 KV",
            "Runway 出动态广告",
            "ElevenLabs 配音",
            "Meta Advantage+ 自动投放",
            "Triple Whale 归因",
            "Northbeam 优化预算，DTC 品牌 ROAS 翻倍。"
        ],
        "outputs": [
            "营销活动从创意到投放"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：营销活动从创意到投放。工具链：ChatGPT + Midjourney + Runway + ElevenLabs + Meta Advantage + Triple Whale + Northbeam。",
        "tags": [
            "media"
        ],
        "importance": 90,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "029",
        "title": "电子书写作出版一条龙",
        "id_slug": "ebook",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ChatGPT",
            "Claude",
            "Sudowrite",
            "Grammarly",
            "Atticus",
            "Midjourney",
            "KDP",
            "Gumroad",
            "Beehiiv",
            "自媒体被动收入"
        ],
        "steps": [
            "ChatGPT 大纲",
            "Claude 200K 写章节",
            "Sudowrite 风格润色",
            "Grammarly 校对",
            "Atticus 排版",
            "Midjourney 出封面",
            "KDP/Gumroad 上架",
            "Beehiiv 邮件预热，自媒体被动收入。"
        ],
        "outputs": [
            "电子书写作出版一条龙"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：电子书写作出版一条龙。工具链：ChatGPT + Claude + Sudowrite + Grammarly + Atticus + Midjourney + KDP + Gumroad。",
        "tags": [
            "agent"
        ],
        "importance": 90,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "030",
        "title": "AI 设计系统组件库",
        "id_slug": "ai-design-component-library",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Figma",
            "Tokens Studio",
            "Storybook",
            "Claude",
            "v0",
            "Chromatic",
            "npm publish",
            "设计研发对齐"
        ],
        "steps": [
            "Figma 已有 token",
            "Tokens Studio 同步",
            "Storybook 生成文档",
            "Claude 写组件 props",
            "v0 生成新组件",
            "Chromatic 视觉回归",
            "npm publish，设计研发对齐。"
        ],
        "outputs": [
            "AI 设计系统组件库"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 设计系统组件库。工具链：Figma + Tokens Studio + Storybook + Claude + v0 + Chromatic + npm publish + 设计研发对齐。",
        "tags": [
            "coding"
        ],
        "importance": 89,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "031",
        "title": "知识工作者第二大脑",
        "id_slug": "second-brain",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Readwise",
            "Heptabase",
            "Mem",
            "Obsidian Copilot",
            "Notion",
            "Granola"
        ],
        "steps": [
            "Readwise 抓高亮",
            "Heptabase 卡片化",
            "Mem AI 自动连接",
            "Obsidian Copilot 本地总结",
            "Notion 周报输出",
            "Granola 接会议纪要，研究员/PM 知识复用率激增。"
        ],
        "outputs": [
            "知识工作者第二大脑"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：知识工作者第二大脑。工具链：Readwise + Heptabase + Mem + Obsidian Copilot + Notion + Granola。",
        "tags": [
            "media"
        ],
        "importance": 89,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "032",
        "title": "AI 视频换脸+配音本地化",
        "id_slug": "ai-face-swap-dubbing-localization",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Akool",
            "HeyGen Avatar IV",
            "ElevenLabs",
            "Sync.so",
            "Topaz",
            "CapCut"
        ],
        "steps": [
            "Akool/HeyGen Avatar IV 换脸",
            "ElevenLabs Dubbing 多语",
            "Sync.so 精准对口型",
            "Topaz 提画质",
            "CapCut 加本地化字幕，海外授权内容快速本土化。"
        ],
        "outputs": [
            "AI 视频换脸+配音本地化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 视频换脸+配音本地化。工具链：Akool + HeyGen Avatar IV + ElevenLabs + Sync.so + Topaz + CapCut。",
        "tags": [
            "media"
        ],
        "importance": 89,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "033",
        "title": "3D 资产 AI 生成管线",
        "id_slug": "3d-asset-ai",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Midjourney",
            "Trellis",
            "Tripo3D",
            "Meshy",
            "Blender",
            "Unity",
            "UE"
        ],
        "steps": [
            "Midjourney 出概念图",
            "Trellis/Tripo3D 转 3D mesh",
            "Meshy 加贴图",
            "Blender 调整",
            "Unity/UE 入引擎，独立游戏美术 1 人当 5 人。"
        ],
        "outputs": [
            "3D 资产 AI 生成管线"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：3D 资产 AI 生成管线。工具链：Midjourney + Trellis + Tripo3D + Meshy + Blender + Unity + UE。",
        "tags": [
            "coding"
        ],
        "importance": 89,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "034",
        "title": "AI 漫画生产流水线",
        "id_slug": "ai-comic",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "ChatGPT",
            "Midjourney",
            "ComfyUI",
            "IP-Adapter",
            "Photoshop Generative",
            "Clip Studio",
            "公众号",
            "Webtoon"
        ],
        "steps": [
            "ChatGPT 写脚本分镜",
            "Midjourney+cref 锁角色",
            "ComfyUI Flux+IP-Adapter 保一致",
            "Photoshop Generative 调画面",
            "Clip Studio 描线上色",
            "公众号/Webtoon 上架。"
        ],
        "outputs": [
            "AI 漫画生产流水线"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 漫画生产流水线。工具链：ChatGPT + Midjourney + ComfyUI + IP-Adapter + Photoshop Generative + Clip Studio + 公众号 + Webtoon。",
        "tags": [
            "visual"
        ],
        "importance": 89,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "035",
        "title": "AI 助手 Mac 全局加速",
        "id_slug": "ai-assistant-mac-global-boost",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Raycast AI",
            "Superwhisper",
            "Granola",
            "BoltAI",
            "Maccy",
            "Karabiner",
            "键盘流效率爆表"
        ],
        "steps": [
            "Raycast AI 全局唤起 GPT",
            "Superwhisper 语音输入",
            "Granola 后台听会",
            "BoltAI 多模型切换",
            "Maccy 剪贴板",
            "Karabiner 绑快捷键，键盘流效率爆表。"
        ],
        "outputs": [
            "AI 助手 Mac 全局加速"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 助手 Mac 全局加速。工具链：Raycast AI + Superwhisper + Granola + BoltAI + Maccy + Karabiner + 键盘流效率爆表。",
        "tags": [
            "agent"
        ],
        "importance": 88,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "036",
        "title": "跨工具个人 CRM",
        "id_slug": "crm",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Superhuman",
            "Cal.com",
            "Notion",
            "Clay",
            "Dex",
            "ChatGPT",
            "社交资产化"
        ],
        "steps": [
            "Superhuman 收邮件",
            "Cal.com 约会",
            "Notion 记联系人",
            "Clay 自动 enrich",
            "Dex 提醒跟进",
            "ChatGPT 起草问候",
            "关系网络可视化，社交资产化。"
        ],
        "outputs": [
            "跨工具个人 CRM"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：跨工具个人 CRM。工具链：Superhuman + Cal.com + Notion + Clay + Dex + ChatGPT + 社交资产化。",
        "tags": [
            "visual",
            "crm"
        ],
        "importance": 88,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "037",
        "title": "AI 健身私教",
        "id_slug": "ai-fitness",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "MyFitnessPal",
            "Whoop",
            "ChatGPT",
            "Caliber",
            "Future",
            "Form AI",
            "Apple Health",
            "私教成本 1"
        ],
        "steps": [
            "MyFitnessPal 记饮食",
            "Whoop 监测心率",
            "ChatGPT 分析数据",
            "Caliber/Future 出训练计划",
            "Form AI 视频纠动作",
            "Apple Health 闭环，私教成本 1/10。"
        ],
        "outputs": [
            "AI 健身私教"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 健身私教。工具链：MyFitnessPal + Whoop + ChatGPT + Caliber + Future + Form AI + Apple Health + 私教成本 1。",
        "tags": [
            "media",
            "health"
        ],
        "importance": 88,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "038",
        "title": "AI 学英语沉浸训练",
        "id_slug": "ai-english",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ChatGPT",
            "Speak App",
            "ElevenLabs",
            "LingQ",
            "Anki",
            "Pimsleur"
        ],
        "steps": [
            "ChatGPT 角色扮演对话",
            "Speak App 发音矫正",
            "ElevenLabs 听力素材",
            "LingQ 阅读",
            "Anki+GPT 生成卡片",
            "Pimsleur 通勤听，6 月雅思 7.0。"
        ],
        "outputs": [
            "AI 学英语沉浸训练"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 学英语沉浸训练。工具链：ChatGPT + Speak App + ElevenLabs + LingQ + Anki + Pimsleur。",
        "tags": [
            "agent"
        ],
        "importance": 88,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "039",
        "title": "个人投资研究助手",
        "id_slug": "assistant",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Perplexity Finance",
            "Koyfin",
            "ChatGPT",
            "Claude",
            "TradingView",
            "Composer",
            "IBKR",
            "散户机构化"
        ],
        "steps": [
            "Perplexity Finance 抓财报",
            "Koyfin 数据",
            "ChatGPT 做 DCF",
            "Claude 写投资备忘录",
            "TradingView 画线",
            "Composer 量化回测",
            "IBKR 下单，散户机构化。"
        ],
        "outputs": [
            "个人投资研究助手"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：个人投资研究助手。工具链：Perplexity Finance + Koyfin + ChatGPT + Claude + TradingView + Composer + IBKR + 散户机构化。",
        "tags": [
            "research",
            "finance"
        ],
        "importance": 88,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "040",
        "title": "AI 旅行规划",
        "id_slug": "ai-travel",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Wanderboat",
            "Google Maps",
            "Skyscanner",
            "Booking",
            "Wallet",
            "Polarsteps"
        ],
        "steps": [
            "ChatGPT 出行程",
            "Wanderboat 优化路线",
            "Google Maps MCP 校时",
            "Skyscanner 抓机票",
            "Booking 订房",
            "Wallet 收车票",
            "Polarsteps 记录，自由行省时省心。"
        ],
        "outputs": [
            "AI 旅行规划"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 旅行规划。工具链：ChatGPT + Wanderboat + Google Maps + Skyscanner + Booking + Wallet + Polarsteps。",
        "tags": [
            "media"
        ],
        "importance": 87,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "041",
        "title": "AI 短篇小说生产",
        "id_slug": "ai-fiction",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ChatGPT",
            "Sudowrite",
            "NovelAI",
            "Claude",
            "Midjourney",
            "Substack",
            "Patreon",
            "网文作者新打法"
        ],
        "steps": [
            "ChatGPT 出梗概",
            "Sudowrite 扩写",
            "NovelAI 风格化",
            "Claude 改人物弧光",
            "Midjourney 出插图",
            "Substack 连载",
            "Patreon 付费，网文作者新打法。"
        ],
        "outputs": [
            "AI 短篇小说生产"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 短篇小说生产。工具链：ChatGPT + Sudowrite + NovelAI + Claude + Midjourney + Substack + Patreon + 网文作者新打法。",
        "tags": [
            "agent"
        ],
        "importance": 87,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "042",
        "title": "AI 音乐 EP 制作",
        "id_slug": "ai-music-ep",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Suno v4",
            "Udio Extend",
            "Logic Pro",
            "LANDR",
            "DistroKid"
        ],
        "steps": [
            "ChatGPT 写歌词主题",
            "Suno v4 生成 demo",
            "Udio Extend 续写",
            "抽 Stems",
            "Logic Pro 后期",
            "LANDR 母带",
            "DistroKid 全平台分发，独立音乐人零门槛。"
        ],
        "outputs": [
            "AI 音乐 EP 制作"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 音乐 EP 制作。工具链：ChatGPT + Suno v4 + Udio Extend + Logic Pro + LANDR + DistroKid。",
        "tags": [
            "media"
        ],
        "importance": 87,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "043",
        "title": "AI 摄影后期批处理",
        "id_slug": "ai-photo",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Lightroom AI",
            "Imagen",
            "Topaz",
            "Magnific",
            "ChatGPT",
            "Pixieset",
            "婚摄"
        ],
        "steps": [
            "Lightroom AI Mask 选区",
            "Imagen AI 套用风格",
            "Topaz Photo AI 修锐降噪",
            "Magnific 放大",
            "ChatGPT 写图说",
            "Pixieset 交付客户，婚摄出片速度翻倍。"
        ],
        "outputs": [
            "AI 摄影后期批处理"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 摄影后期批处理。工具链：Lightroom AI + Imagen + Topaz + Magnific + ChatGPT + Pixieset + 婚摄。",
        "tags": [
            "visual"
        ],
        "importance": 87,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "044",
        "title": "AI 直播字幕同传",
        "id_slug": "ai-livestream",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "OBS",
            "Whisper Streaming",
            "DeepL",
            "vMix",
            "Restream"
        ],
        "steps": [
            "OBS 抓音频",
            "Whisper Streaming 转录",
            "DeepL 实时翻译",
            "vMix 上字幕",
            "多语推流",
            "Restream 多平台分发，国际会议无需人工同传。"
        ],
        "outputs": [
            "AI 直播字幕同传"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 直播字幕同传。工具链：OBS + Whisper Streaming + DeepL + vMix + Restream。",
        "tags": [
            "media"
        ],
        "importance": 87,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "045",
        "title": "AI 电话客服机器人",
        "id_slug": "ai-phone-support",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Twilio",
            "Vapi",
            "Bland AI",
            "ChatGPT",
            "Cal.com",
            "HubSpot",
            "Slack"
        ],
        "steps": [
            "Twilio 接来电",
            "Vapi/Bland AI 跑对话",
            "ChatGPT 调用 RAG",
            "Cal.com 约会",
            "HubSpot 入库",
            "Slack 通知，餐厅诊所 24h 不漏单。"
        ],
        "outputs": [
            "AI 电话客服机器人"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 电话客服机器人。工具链：Twilio + Vapi + Bland AI + ChatGPT + Cal.com + HubSpot + Slack。",
        "tags": [
            "business",
            "rag"
        ],
        "importance": 86,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "046",
        "title": "DevOps AI 巡检",
        "id_slug": "devops-ai-ops-check",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Datadog",
            "PagerDuty",
            "Claude Code",
            "Runbook",
            "Slack",
            "Postmortem AI"
        ],
        "steps": [
            "Datadog 抓异常",
            "PagerDuty 告警",
            "Claude Code 自动诊断",
            "Runbook 执行修复脚本",
            "Slack 报告",
            "Postmortem AI 写复盘，SRE 半夜不再被叫。"
        ],
        "outputs": [
            "DevOps AI 巡检"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：DevOps AI 巡检。工具链：Datadog + PagerDuty + Claude Code + Runbook + Slack + Postmortem AI。",
        "tags": [
            "coding",
            "data"
        ],
        "importance": 86,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "047",
        "title": "AI 招商资料一键生成",
        "id_slug": "ai-fundraising",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Crunchbase",
            "ChatGPT",
            "Gamma",
            "Midjourney",
            "Tome",
            "DocSend"
        ],
        "steps": [
            "Crunchbase 抓数据",
            "ChatGPT 写商业计划",
            "Gamma 出 pitch deck",
            "Midjourney 配视觉",
            "Tome 备演讲版",
            "DocSend 跟踪投资人阅读，融资效率拉满。"
        ],
        "outputs": [
            "AI 招商资料一键生成"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 招商资料一键生成。工具链：Crunchbase + ChatGPT + Gamma + Midjourney + Tome + DocSend。",
        "tags": [
            "visual"
        ],
        "importance": 86,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "048",
        "title": "AI 教学题库出题阅卷",
        "id_slug": "ai-teaching-question-bank",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Quizlet",
            "Gradescope",
            "Claude",
            "Khanmigo",
            "Notion",
            "老师工作量减半"
        ],
        "steps": [
            "ChatGPT 按知识点出题",
            "Quizlet 转闪卡",
            "Gradescope OCR 阅卷",
            "Claude 写个性化反馈",
            "Khanmigo 答疑",
            "Notion 班级仪表盘，老师工作量减半。"
        ],
        "outputs": [
            "AI 教学题库出题阅卷"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 教学题库出题阅卷。工具链：ChatGPT + Quizlet + Gradescope + Claude + Khanmigo + Notion + 老师工作量减半。",
        "tags": [
            "office"
        ],
        "importance": 86,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "049",
        "title": "AI 房产经纪助手",
        "id_slug": "ai-real-estate-assistant",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Zillow",
            "ChatGPT",
            "Virtual Staging AI",
            "Matterport",
            "ElevenLabs",
            "HeyGen",
            "挂牌一天成交"
        ],
        "steps": [
            "Zillow 抓房源",
            "ChatGPT 写描述",
            "Virtual Staging AI 一键摆家具",
            "Matterport 3D 看房",
            "ElevenLabs 录介绍",
            "HeyGen 数字人讲解，挂牌一天成交。"
        ],
        "outputs": [
            "AI 房产经纪助手"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 房产经纪助手。工具链：Zillow + ChatGPT + Virtual Staging AI + Matterport + ElevenLabs + HeyGen + 挂牌一天成交。",
        "tags": [
            "coding"
        ],
        "importance": 86,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "050",
        "title": "AI 医疗文书助手",
        "id_slug": "ai-medical-assistant",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Whisper",
            "DAX",
            "Abridge",
            "Epic",
            "Claude",
            "Tally",
            "医生省 2 小时"
        ],
        "steps": [
            "Whisper 录诊间对话",
            "DAX/Abridge 生成 SOAP 病历",
            "Epic EMR 入档",
            "Claude 翻译患者教育材料",
            "Tally 表单收随访，医生省 2 小时/天。"
        ],
        "outputs": [
            "AI 医疗文书助手"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 医疗文书助手。工具链：Whisper + DAX + Abridge + Epic + Claude + Tally + 医生省 2 小时。",
        "tags": [
            "media"
        ],
        "importance": 85,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "051",
        "title": "AI 短视频图文混剪",
        "id_slug": "ai-short-video",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "小红书爆文",
            "ChatGPT",
            "Midjourney",
            "CapCut",
            "Canva",
            "矩阵号",
            "飞瓜监测",
            "单号月涨万粉"
        ],
        "steps": [
            "小红书爆文抓取",
            "ChatGPT 提炼结构",
            "Midjourney 配图",
            "CapCut 模板套用",
            "Canva 改字",
            "矩阵号分发",
            "飞瓜监测，单号月涨万粉。"
        ],
        "outputs": [
            "AI 短视频图文混剪"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 短视频图文混剪。工具链：小红书爆文 + ChatGPT + Midjourney + CapCut + Canva + 矩阵号 + 飞瓜监测 + 单号月涨万粉。",
        "tags": [
            "media"
        ],
        "importance": 85,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "052",
        "title": "AI 游戏 NPC 智能化",
        "id_slug": "ai-game-npc",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Inworld AI",
            "ElevenLabs",
            "Convai",
            "Ready Player Me",
            "行为树驱动剧情"
        ],
        "steps": [
            "Inworld AI 设角色性格",
            "ElevenLabs 配音",
            "Convai 接 Unity",
            "Ready Player Me 角色",
            "玩家对话",
            "行为树驱动剧情，独立游戏体验大升级。"
        ],
        "outputs": [
            "AI 游戏 NPC 智能化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 游戏 NPC 智能化。工具链：Inworld AI + ElevenLabs + Convai + Ready Player Me + 行为树驱动剧情。",
        "tags": [
            "coding"
        ],
        "importance": 85,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "053",
        "title": "AI 简短播客 newsletter",
        "id_slug": "ai-podcast-newsletter",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "RSS",
            "Claude",
            "ElevenLabs",
            "Beehiiv",
            "Apple Podcasts",
            "Spotify",
            "通勤听完一天信息"
        ],
        "steps": [
            "RSS 聚合行业新闻",
            "Claude 总结 5 条",
            "ElevenLabs 转 3 分钟音频",
            "Beehiiv 发邮件",
            "Apple Podcast 同步",
            "Spotify 短播，通勤听完一天信息。"
        ],
        "outputs": [
            "AI 简短播客 newsletter"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 简短播客 newsletter。工具链：RSS + Claude + ElevenLabs + Beehiiv + Apple Podcasts + Spotify + 通勤听完一天信息。",
        "tags": [
            "media",
            "podcast"
        ],
        "importance": 85,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "054",
        "title": "AI 求职公司情报",
        "id_slug": "ai-job-search",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "LinkedIn",
            "Crystal Knows",
            "Glassdoor",
            "Perplexity",
            "ChatGPT",
            "Yoodli",
            "offer"
        ],
        "steps": [
            "LinkedIn 找面试官",
            "Crystal Knows 性格分析",
            "Glassdoor 抓面经",
            "Perplexity 找近期产品动态",
            "ChatGPT 出针对问题",
            "Yoodli 模拟，offer 命中率翻倍。"
        ],
        "outputs": [
            "AI 求职公司情报"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 求职公司情报。工具链：LinkedIn + Crystal Knows + Glassdoor + Perplexity + ChatGPT + Yoodli + offer。",
        "tags": [
            "research"
        ],
        "importance": 85,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "055",
        "title": "AI 法律咨询自助",
        "id_slug": "ai-legal-help",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "DoNotPay",
            "Harvey",
            "ChatGPT",
            "DocuSign",
            "Court Buddy",
            "Calendar",
            "小额纠纷无需律师"
        ],
        "steps": [
            "DoNotPay 流程",
            "Harvey 解读合同",
            "ChatGPT 写律师函",
            "DocuSign 签",
            "Court Buddy 提交",
            "Calendar 跟踪进度，小额纠纷无需律师。"
        ],
        "outputs": [
            "AI 法律咨询自助"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 法律咨询自助。工具链：DoNotPay + Harvey + ChatGPT + DocuSign + Court Buddy + Calendar + 小额纠纷无需律师。",
        "tags": [
            "research"
        ],
        "importance": 84,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "056",
        "title": "AI 一人公司财税",
        "id_slug": "ai-tax",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Stripe",
            "Mercury",
            "Pilot",
            "Bench AI",
            "Ramp",
            "ChatGPT",
            "TurboTax",
            "DocuSign"
        ],
        "steps": [
            "Stripe 收款",
            "Mercury 银行",
            "Pilot/Bench AI 记账",
            "Ramp 报销",
            "ChatGPT 出月报",
            "TurboTax 报税",
            "DocuSign 签 W-9，独立开发者 0 行政开销。"
        ],
        "outputs": [
            "AI 一人公司财税"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 一人公司财税。工具链：Stripe + Mercury + Pilot + Bench AI + Ramp + ChatGPT + TurboTax + DocuSign。",
        "tags": [
            "business"
        ],
        "importance": 84,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "057",
        "title": "AI 运营周报自动化",
        "id_slug": "ai-weekly-report",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Mixpanel",
            "PostHog",
            "BigQuery",
            "Cube",
            "Claude",
            "Hex",
            "Notion",
            "Slack",
            "PM"
        ],
        "steps": [
            "Mixpanel/PostHog 抓数据",
            "BigQuery 仓",
            "Cube 语义层",
            "Claude 写解读",
            "Hex 出图",
            "Notion 模板填充",
            "Slack 推送，PM 不用熬夜写周报。"
        ],
        "outputs": [
            "AI 运营周报自动化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 运营周报自动化。工具链：Mixpanel + PostHog + BigQuery + Cube + Claude + Hex + Notion + Slack。",
        "tags": [
            "office"
        ],
        "importance": 84,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "058",
        "title": "AI 内容审核合规",
        "id_slug": "ai-content-moderation",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Hive",
            "OpenAI Moderation",
            "Lasso",
            "Claude",
            "Trust&Safety;",
            "UGC"
        ],
        "steps": [
            "Hive Moderation 过滤图",
            "OpenAI Moderation 过滤文",
            "Lasso 检测违规",
            "Claude 二次复核",
            "Trust&Safety; dashboard，UGC 平台合规上线。"
        ],
        "outputs": [
            "AI 内容审核合规"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 内容审核合规。工具链：Hive + OpenAI Moderation + Lasso + Claude + Trust&Safety; + UGC。",
        "tags": [
            "business"
        ],
        "importance": 84,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "059",
        "title": "AI 二语阅读流水线",
        "id_slug": "ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Readlang",
            "LingQ",
            "Anki",
            "Speak",
            "ChatGPT",
            "Audible"
        ],
        "steps": [
            "Readlang/LingQ 标生词",
            "Anki AI 自动出卡",
            "Speak 跟读",
            "ChatGPT 解析语法",
            "Audible 同步听书，英语晋级靠系统化。"
        ],
        "outputs": [
            "AI 二语阅读流水线"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 二语阅读流水线。工具链：Readlang + LingQ + Anki + Speak + ChatGPT + Audible。",
        "tags": [
            "agent"
        ],
        "importance": 84,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "060",
        "title": "AI 婚礼策划全流程",
        "id_slug": "ai-wedding",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Pinterest",
            "Midjourney",
            "Canva",
            "HoneyBook",
            "ElevenLabs",
            "Runway"
        ],
        "steps": [
            "ChatGPT 出主题",
            "Pinterest+MJ 做 mood board",
            "Canva 邀请函",
            "HoneyBook 客户管理",
            "Eleven Labs 录誓词",
            "Runway 视频回放，新人 DIY 节省 50% 预算。"
        ],
        "outputs": [
            "AI 婚礼策划全流程"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 婚礼策划全流程。工具链：ChatGPT + Pinterest + Midjourney + Canva + HoneyBook + ElevenLabs + Runway。",
        "tags": [
            "media"
        ],
        "importance": 83,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "061",
        "title": "AI 健康饮食定制",
        "id_slug": "ai-diet",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Cronometer",
            "Levels",
            "Whoop",
            "ChatGPT",
            "Mealime",
            "Instacart"
        ],
        "steps": [
            "Cronometer 记录营养",
            "Levels 血糖监测",
            "Whoop 恢复",
            "ChatGPT 分析",
            "Mealime 出菜单",
            "Instacart 自动下单，慢病管理数据驱动。"
        ],
        "outputs": [
            "AI 健康饮食定制"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 健康饮食定制。工具链：Cronometer + Levels + Whoop + ChatGPT + Mealime + Instacart。",
        "tags": [
            "agent"
        ],
        "importance": 83,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "062",
        "title": "AI 学术答辩准备",
        "id_slug": "ai-defense",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "NotebookLM",
            "Claude",
            "Yoodli",
            "Beautiful.ai",
            "Granola"
        ],
        "steps": [
            "NotebookLM 上传论文",
            "Claude 模拟答辩问题",
            "Yoodli 练表达",
            "Beautiful.ai 出答辩 PPT",
            "Granola 录预答辩反馈，博士答辩无忧。"
        ],
        "outputs": [
            "AI 学术答辩准备"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 学术答辩准备。工具链：NotebookLM + Claude + Yoodli + Beautiful.ai + Granola。",
        "tags": [
            "office"
        ],
        "importance": 83,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "063",
        "title": "AI 跨境客服多语化",
        "id_slug": "ai",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Crisp",
            "Intercom",
            "DeepL",
            "Claude",
            "转人工时",
            "Help Scout"
        ],
        "steps": [
            "Crisp/Intercom 收消息",
            "DeepL 实时翻译",
            "Claude RAG 答复",
            "转人工时同步上下文",
            "Helpscout KB 沉淀，全球团队 24h 覆盖。"
        ],
        "outputs": [
            "AI 跨境客服多语化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 跨境客服多语化。工具链：Crisp + Intercom + DeepL + Claude + 转人工时 + Help Scout。",
        "tags": [
            "media",
            "rag"
        ],
        "importance": 83,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "064",
        "title": "AI 产品反馈闭环",
        "id_slug": "ai-product-feedback",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Canny",
            "Productboard",
            "ChatGPT",
            "Linear",
            "Loom",
            "PMF"
        ],
        "steps": [
            "Canny 收建议",
            "Productboard 优先级",
            "ChatGPT 聚类",
            "Linear 立项",
            "Loom 同步",
            "上线后 Sprig 调研体验，PMF 迭代加速。"
        ],
        "outputs": [
            "AI 产品反馈闭环"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 产品反馈闭环。工具链：Canny + Productboard + ChatGPT + Linear + Loom + PMF。",
        "tags": [
            "agent"
        ],
        "importance": 83,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "065",
        "title": "AI 电商客评分析",
        "id_slug": "ai-review-analysis",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Apify",
            "Claude",
            "Sentiment",
            "Looker",
            "ChatGPT",
            "Helium10",
            "选品决策数据化"
        ],
        "steps": [
            "Apify 抓亚马逊评论",
            "Claude 提取卖点痛点",
            "Sentiment 打分",
            "Looker 仪表盘",
            "ChatGPT 写改进意见",
            "Helium10 反推关键词，选品决策数据化。"
        ],
        "outputs": [
            "AI 电商客评分析"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 电商客评分析。工具链：Apify + Claude + Sentiment + Looker + ChatGPT + Helium10 + 选品决策数据化。",
        "tags": [
            "business"
        ],
        "importance": 82,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "066",
        "title": "AI 直播脚本到分发",
        "id_slug": "ai-livestream",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "ElevenLabs",
            "OBS",
            "Streamyard",
            "Restream",
            "Opus",
            "YouTube",
            "单场素材榨干"
        ],
        "steps": [
            "ChatGPT 写直播大纲",
            "Eleven Labs 录暖场",
            "OBS 推流",
            "Streamyard 多平台",
            "Restream 录像",
            "Opus 切片回放",
            "YouTube/B站二发，单场素材榨干。"
        ],
        "outputs": [
            "AI 直播脚本到分发"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 直播脚本到分发。工具链：ChatGPT + ElevenLabs + OBS + Streamyard + Restream + Opus + YouTube + 单场素材榨干。",
        "tags": [
            "media",
            "youtube"
        ],
        "importance": 82,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "067",
        "title": "AI 内部通讯本地化",
        "id_slug": "ai-internal-comms-localization",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Slack AI",
            "DeepL",
            "Loom",
            "Notion",
            "ElevenLabs"
        ],
        "steps": [
            "全员 Slack 公告",
            "Slack AI 总结",
            "DeepL 翻多语",
            "Loom 录视频版",
            "Notion 沉淀",
            "Eleven Labs 多语播报，跨国团队信息对齐。"
        ],
        "outputs": [
            "AI 内部通讯本地化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 内部通讯本地化。工具链：Slack AI + DeepL + Loom + Notion + ElevenLabs。",
        "tags": [
            "media"
        ],
        "importance": 82,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "068",
        "title": "AI 个人 OKR 跟踪",
        "id_slug": "ai-okr",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Notion AI",
            "Sunsama",
            "Reclaim AI",
            "Granola",
            "Claude",
            "Substack",
            "自驱力满格"
        ],
        "steps": [
            "Notion AI 拆 OKR",
            "Sunsama 日规划",
            "Reclaim AI 排日历",
            "Granola 复盘会议",
            "Claude 周报反思",
            "Substack 公开问责，自驱力满格。"
        ],
        "outputs": [
            "AI 个人 OKR 跟踪"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 个人 OKR 跟踪。工具链：Notion AI + Sunsama + Reclaim AI + Granola + Claude + Substack + 自驱力满格。",
        "tags": [
            "office"
        ],
        "importance": 82,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "069",
        "title": "AI 跨境社媒运营",
        "id_slug": "ai",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Buffer",
            "Hootsuite",
            "Mention",
            "ChatGPT",
            "Canva",
            "Triple Whale"
        ],
        "steps": [
            "Buffer AI 排程",
            "Hootsuite 监听",
            "Mention 监品牌",
            "ChatGPT 多语本地化",
            "Canva Magic 多尺寸",
            "Triple Whale 看 ROAS，DTC 全球账号矩阵。"
        ],
        "outputs": [
            "AI 跨境社媒运营"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 跨境社媒运营。工具链：Buffer + Hootsuite + Mention + ChatGPT + Canva + Triple Whale。",
        "tags": [
            "visual"
        ],
        "importance": 82,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "070",
        "title": "AI 灵感素材库管理",
        "id_slug": "ai-inspiration",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Eagle",
            "Raindrop",
            "CLIP",
            "Pinecone",
            "Claude"
        ],
        "steps": [
            "Eagle/Raindrop 收集",
            "CLIP 嵌入",
            "Pinecone 检索",
            "Claude 关联标签",
            "出图时一键参考，设计师/写手灵感不枯竭。"
        ],
        "outputs": [
            "AI 灵感素材库管理"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 灵感素材库管理。工具链：Eagle + Raindrop + CLIP + Pinecone + Claude。",
        "tags": [
            "visual"
        ],
        "importance": 81,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "071",
        "title": "AI 投资人 DD 加速",
        "id_slug": "ai-investor-dd",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "DocSend",
            "Claude",
            "Public Comps",
            "Crunchbase",
            "Reference",
            "Notion"
        ],
        "steps": [
            "DocSend 收 deck",
            "Claude 解析财务",
            "Public Comps 估值",
            "Crunchbase 创始人背调",
            "Reference 自动找推荐人",
            "Notion 投决备忘录，VC 一周看 10 个项目。"
        ],
        "outputs": [
            "AI 投资人 DD 加速"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 投资人 DD 加速。工具链：DocSend + Claude + Public Comps + Crunchbase + Reference + Notion。",
        "tags": [
            "research"
        ],
        "importance": 81,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "072",
        "title": "AI 监控合同到期",
        "id_slug": "ai-contract-expiry",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Ironclad",
            "PandaDoc",
            "Zapier",
            "Claude",
            "Lemlist",
            "DocuSign"
        ],
        "steps": [
            "Ironclad/PandaDoc 存档",
            "Zapier 监到期日",
            "Claude 提示重谈",
            "Lemlist 群发续约",
            "DocuSign 重签",
            "CFO 报表，0 漏续约。"
        ],
        "outputs": [
            "AI 监控合同到期"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 监控合同到期。工具链：Ironclad + PandaDoc + Zapier + Claude + Lemlist + DocuSign。",
        "tags": [
            "research"
        ],
        "importance": 81,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "073",
        "title": "AI 产品视频教程批量",
        "id_slug": "ai-tutorial",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Loom",
            "Tella",
            "ElevenLabs",
            "CapCut",
            "Wistia",
            "Intercom",
            "新功能上线即"
        ],
        "steps": [
            "ChatGPT 写脚本",
            "Loom 录屏",
            "Tella 美化",
            "ElevenLabs 配音",
            "CapCut 字幕",
            "Wistia 托管",
            "Intercom 内嵌产品，新功能上线即配教程。"
        ],
        "outputs": [
            "AI 产品视频教程批量"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 产品视频教程批量。工具链：ChatGPT + Loom + Tella + ElevenLabs + CapCut + Wistia + Intercom + 新功能上线即。",
        "tags": [
            "media"
        ],
        "importance": 81,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "074",
        "title": "AI 求职邮件 follow-up",
        "id_slug": "ai-job-search-email-follow-up",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Apollo",
            "ChatGPT",
            "Mixmax",
            "Calendly",
            "DocuSign",
            "offer"
        ],
        "steps": [
            "Apollo 找邮箱",
            "ChatGPT 写感谢信",
            "Mixmax 跟踪打开",
            "Calendly 二轮约",
            "ChatGPT 写薪资谈判脚本",
            "DocuSign 签 offer，offer 谈判提分 20%。"
        ],
        "outputs": [
            "AI 求职邮件 follow-up"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 求职邮件 follow-up。工具链：Apollo + ChatGPT + Mixmax + Calendly + DocuSign + offer。",
        "tags": [
            "business"
        ],
        "importance": 81,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "075",
        "title": "AI 电邮归档检索",
        "id_slug": "ai-archive",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Gmail",
            "Superhuman",
            "Shortwave",
            "Mem",
            "Claude",
            "Reflect"
        ],
        "steps": [
            "Gmail 全量",
            "Superhuman/Shortwave 智能分类",
            "Mem 索引",
            "Claude RAG 问答",
            "Reflect 周回顾，10 年邮件秒搜任何线索。"
        ],
        "outputs": [
            "AI 电邮归档检索"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 电邮归档检索。工具链：Gmail + Superhuman + Shortwave + Mem + Claude + Reflect。",
        "tags": [
            "office",
            "rag"
        ],
        "importance": 80,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "076",
        "title": "AI 远程协作日报",
        "id_slug": "ai-remote-collab-daily-report",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "GitHub",
            "Linear",
            "Slack",
            "Granola",
            "Claude",
            "Notion",
            "远程信任"
        ],
        "steps": [
            "GitHub Activity",
            "Linear 进度",
            "Slack 消息",
            "Granola 会议",
            "Claude 聚合写日报",
            "Notion 周报",
            "老板 Loom 视频版，远程信任建立。"
        ],
        "outputs": [
            "AI 远程协作日报"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 远程协作日报。工具链：GitHub + Linear + Slack + Granola + Claude + Notion + 远程信任。",
        "tags": [
            "media"
        ],
        "importance": 80,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "077",
        "title": "AI 多模态搜索品控",
        "id_slug": "ai-quality-control",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "CLIP",
            "ChatGPT",
            "Sift",
            "Slack",
            "Trello",
            "电商假货识别"
        ],
        "steps": [
            "上传产品图",
            "CLIP 找相似",
            "ChatGPT 描述差异",
            "Sift 反欺诈",
            "Slack 通知 QA",
            "Trello 跟踪问题，电商假货识别。"
        ],
        "outputs": [
            "AI 多模态搜索品控"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 多模态搜索品控。工具链：CLIP + ChatGPT + Sift + Slack + Trello + 电商假货识别。",
        "tags": [
            "research"
        ],
        "importance": 80,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "078",
        "title": "AI 房屋装修规划",
        "id_slug": "ai-renovation",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Houzz",
            "Midjourney",
            "Planner 5D",
            "ChatGPT",
            "Thumbtack",
            "Notion",
            "装修不踩坑"
        ],
        "steps": [
            "Houzz 找灵感",
            "Midjourney+cref 出渲染",
            "Planner 5D 量尺寸",
            "ChatGPT 出预算",
            "Thumbtack 找工人",
            "Notion 跟进度，装修不踩坑。"
        ],
        "outputs": [
            "AI 房屋装修规划"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 房屋装修规划。工具链：Houzz + Midjourney + Planner 5D + ChatGPT + Thumbtack + Notion + 装修不踩坑。",
        "tags": [
            "visual"
        ],
        "importance": 80,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "079",
        "title": "AI 短剧爆款生产",
        "id_slug": "ai-micro-drama",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Claude",
            "Midjourney",
            "Runway",
            "Kling",
            "ElevenLabs",
            "CapCut",
            "红果",
            "抖音"
        ],
        "steps": [
            "ChatGPT 出钩子开场",
            "Claude 写 60 集分镜",
            "Midjourney 角色设计",
            "Runway/Kling 出镜头",
            "ElevenLabs 配音",
            "CapCut 剪辑",
            "红果/抖音上架，单人短剧厂牌。"
        ],
        "outputs": [
            "AI 短剧爆款生产"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 短剧爆款生产。工具链：ChatGPT + Claude + Midjourney + Runway + Kling + ElevenLabs + CapCut + 红果。",
        "tags": [
            "media"
        ],
        "importance": 80,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "080",
        "title": "AI 演讲准备到现场",
        "id_slug": "ai-speech",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ChatGPT",
            "Beautiful.ai",
            "Yoodli",
            "Krisp",
            "Otter",
            "Granola"
        ],
        "steps": [
            "ChatGPT 写演讲稿",
            "Beautiful.ai 出 slides",
            "Yoodli 练表达",
            "Krisp 现场降噪",
            "Otter 实时字幕",
            "Granola 现场录",
            "复盘文档生成，TED 级输出。"
        ],
        "outputs": [
            "AI 演讲准备到现场"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 演讲准备到现场。工具链：ChatGPT + Beautiful.ai + Yoodli + Krisp + Otter + Granola。",
        "tags": [
            "media"
        ],
        "importance": 79,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "081",
        "title": "AI 一人电商品牌",
        "id_slug": "ai",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Spate",
            "Midjourney",
            "Printify POD",
            "Shopify",
            "v0",
            "Klaviyo",
            "Meta AI",
            "Gorgias",
            "月入 5 万美金"
        ],
        "steps": [
            "Spate 找趋势",
            "Midjourney 设计 LOGO",
            "Printify POD 生产",
            "Shopify+v0 建站",
            "Klaviyo 邮件",
            "Meta AI 投放",
            "Gorgias AI 客服，月入 5 万美金。"
        ],
        "outputs": [
            "AI 一人电商品牌"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 一人电商品牌。工具链：Spate + Midjourney + Printify POD + Shopify + v0 + Klaviyo + Meta AI + Gorgias。",
        "tags": [
            "visual"
        ],
        "importance": 79,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "082",
        "title": "AI 求婚/婚礼短片",
        "id_slug": "ai-wedding",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Apple Photos",
            "ChatGPT",
            "Runway",
            "ElevenLabs",
            "Suno",
            "CapCut",
            "现场播放",
            "感动全场"
        ],
        "steps": [
            "Apple Photos 选素材",
            "ChatGPT 写脚本",
            "Runway 修复老照片",
            "ElevenLabs 克隆双方声音",
            "Suno 写定制歌",
            "CapCut 剪辑",
            "现场播放，感动全场。"
        ],
        "outputs": [
            "AI 求婚/婚礼短片"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 求婚/婚礼短片。工具链：Apple Photos + ChatGPT + Runway + ElevenLabs + Suno + CapCut + 现场播放 + 感动全场。",
        "tags": [
            "media"
        ],
        "importance": 79,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "083",
        "title": "AI 社区内容审核",
        "id_slug": "ai-community-content-moderation",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Discord",
            "Slack",
            "OpenAI Moderation",
            "Hive",
            "Claude",
            "Modmail"
        ],
        "steps": [
            "Discord/Slack 抓消息",
            "OpenAI Moderation",
            "Hive 检测毒性",
            "Claude 审查上下文",
            "自动 mute",
            "Modmail 通知，社区 0 翻车。"
        ],
        "outputs": [
            "AI 社区内容审核"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 社区内容审核。工具链：Discord + Slack + OpenAI Moderation + Hive + Claude + Modmail。",
        "tags": [
            "business"
        ],
        "importance": 79,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "084",
        "title": "AI 政府事务自动化",
        "id_slug": "ai-government",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Granicus",
            "OpenStates",
            "Claude",
            "ChatGPT",
            "DocuSign",
            "Phone2Action"
        ],
        "steps": [
            "Granicus/Open States 抓法案",
            "Claude 解读影响",
            "ChatGPT 写公关稿",
            "DocuSign 收议员签",
            "Phone2Action 群众动员，倡导组织 10 倍效率。"
        ],
        "outputs": [
            "AI 政府事务自动化"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 政府事务自动化。工具链：Granicus + OpenStates + Claude + ChatGPT + DocuSign + Phone2Action。",
        "tags": [
            "business"
        ],
        "importance": 79,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "085",
        "title": "AI 家庭日程管家",
        "id_slug": "ai-family",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Google Calendar",
            "Motion",
            "Reclaim",
            "ChatGPT",
            "Cozi",
            "Alexa",
            "二孩家庭不混乱"
        ],
        "steps": [
            "Google Calendar 全家共享",
            "Motion AI 智能排",
            "Reclaim 占块",
            "ChatGPT 提醒接娃",
            "Cozi 杂事清单",
            "Alexa 语音查，二孩家庭不混乱。"
        ],
        "outputs": [
            "AI 家庭日程管家"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 家庭日程管家。工具链：Google Calendar + Motion + Reclaim + ChatGPT + Cozi + Alexa + 二孩家庭不混乱。",
        "tags": [
            "agent"
        ],
        "importance": 78,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "086",
        "title": "AI 软件本地化全自动",
        "id_slug": "ai-software-localization",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Locize",
            "Lokalise",
            "DeepL",
            "Claude",
            "Crowdin",
            "Figma",
            "Sentry"
        ],
        "steps": [
            "Locize/Lokalise 收原文",
            "DeepL 机翻",
            "Claude 校术语",
            "Crowdin 众包",
            "Figma 截图自动同步",
            "Sentry 监 i18n 漏译，10 语言版本同步发布。"
        ],
        "outputs": [
            "AI 软件本地化全自动"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 软件本地化全自动。工具链：Locize + Lokalise + DeepL + Claude + Crowdin + Figma + Sentry。",
        "tags": [
            "coding"
        ],
        "importance": 78,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "087",
        "title": "AI 个人 IP 视频引擎",
        "id_slug": "ai-personal-ip",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Descript",
            "Submagic",
            "Opus",
            "Hypefury",
            "Beehiiv",
            "多端复"
        ],
        "steps": [
            "选题 ChatGPT",
            "脚本 Claude",
            "拍摄提词 Teleprompter+",
            "Descript 剪",
            "Submagic 字幕",
            "Opus 切片",
            "Hypefury 长推",
            "Beehiiv 邮件，多端复用一份内容。"
        ],
        "outputs": [
            "AI 个人 IP 视频引擎"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 个人 IP 视频引擎。工具链：Descript + Submagic + Opus + Hypefury + Beehiiv + 多端复。",
        "tags": [
            "media"
        ],
        "importance": 78,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "088",
        "title": "AI Newsletter 长尾变现",
        "id_slug": "ai-newsletter",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "RSS",
            "Perplexity",
            "Claude",
            "Midjourney",
            "Beehiiv",
            "ConvertKit",
            "Stripe",
            "Twitter",
            "万粉月入过万"
        ],
        "steps": [
            "RSS+Perplexity 找选题",
            "Claude 写正文",
            "Midjourney 配图",
            "Beehiiv 发送",
            "ConvertKit 自动化序列",
            "Stripe 付费墙",
            "Twitter 多线 promo，万粉月入过万。"
        ],
        "outputs": [
            "AI Newsletter 长尾变现"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI Newsletter 长尾变现。工具链：RSS + Perplexity + Claude + Midjourney + Beehiiv + ConvertKit + Stripe + Twitter。",
        "tags": [
            "agent"
        ],
        "importance": 78,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "089",
        "title": "AI 课程销售漏斗",
        "id_slug": "ai-course-sales",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Carrd",
            "ConvertKit",
            "Loom",
            "Stripe",
            "Circle",
            "Zapier",
            "转化率倍增"
        ],
        "steps": [
            "ChatGPT 出 Lead Magnet",
            "Carrd 落地页",
            "ConvertKit 免费序列",
            "Loom 演示课",
            "Stripe 收付费",
            "Circle 社区",
            "Zapier 进群，转化率倍增。"
        ],
        "outputs": [
            "AI 课程销售漏斗"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 课程销售漏斗。工具链：ChatGPT + Carrd + ConvertKit + Loom + Stripe + Circle + Zapier + 转化率倍增。",
        "tags": [
            "office"
        ],
        "importance": 78,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "090",
        "title": "AI 智能合同审查批量",
        "id_slug": "ai-contract",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DocSign",
            "Spellbook",
            "Harvey",
            "ChatGPT",
            "Slack",
            "Ironclad"
        ],
        "steps": [
            "DocSign 入箱",
            "Spellbook 模板比对",
            "Harvey 标条款",
            "ChatGPT 起草修订",
            "Slack 通知对方",
            "Ironclad 走流程，法务团队规模化。"
        ],
        "outputs": [
            "AI 智能合同审查批量"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 智能合同审查批量。工具链：DocSign + Spellbook + Harvey + ChatGPT + Slack + Ironclad。",
        "tags": [
            "business"
        ],
        "importance": 77,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "091",
        "title": "AI 数据可视化叙事",
        "id_slug": "ai-visualization",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Snowflake",
            "Hex",
            "Claude",
            "Flourish",
            "Gamma",
            "Loom"
        ],
        "steps": [
            "Snowflake 查",
            "Hex 笔记本",
            "Claude 写解读",
            "Flourish 动效图",
            "Gamma 串成 PPT",
            "Loom 录解说，数据故事力升维。"
        ],
        "outputs": [
            "AI 数据可视化叙事"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 数据可视化叙事。工具链：Snowflake + Hex + Claude + Flourish + Gamma + Loom。",
        "tags": [
            "office"
        ],
        "importance": 77,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "092",
        "title": "AI 多 Agent 复杂调研",
        "id_slug": "ai-agent",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "CrewAI",
            "Writer",
            "Tavily",
            "LangGraph",
            "Claude",
            "Notion"
        ],
        "steps": [
            "CrewAI 定义 Researcher/Analyst/Writer",
            "Tavily 搜索工具",
            "LangGraph 状态机控流",
            "Claude 主推理",
            "GPT 校对",
            "Notion 输出，深度报告自动产出。"
        ],
        "outputs": [
            "AI 多 Agent 复杂调研"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 多 Agent 复杂调研。工具链：CrewAI + Writer + Tavily + LangGraph + Claude + Notion。",
        "tags": [
            "coding",
            "research",
            "agent"
        ],
        "importance": 77,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "093",
        "title": "AI 本地隐私 RAG",
        "id_slug": "ai-rag",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Ollama",
            "Open WebUI",
            "AnythingLLM",
            "ChromaDB",
            "Tailscale",
            "敏感行业零上云"
        ],
        "steps": [
            "Ollama 跑 Qwen2.5/Llama3.3",
            "Open WebUI 界面",
            "AnythingLLM 索引文档",
            "ChromaDB 本地向量",
            "Tailscale 远程访问，敏感行业零上云。"
        ],
        "outputs": [
            "AI 本地隐私 RAG"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 本地隐私 RAG。工具链：Ollama + Open WebUI + AnythingLLM + ChromaDB + Tailscale + 敏感行业零上云。",
        "tags": [
            "office",
            "rag"
        ],
        "importance": 77,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "094",
        "title": "AI 浏览器自动化爬数据",
        "id_slug": "ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Browser Use",
            "Claude",
            "Skyvern",
            "Apify",
            "Bright Data",
            "Supabase",
            "Retool"
        ],
        "steps": [
            "Browser Use+Claude 操控 Chrome",
            "Skyvern 看 DOM",
            "Apify 调度",
            "Bright Data 代理",
            "Supabase 入库",
            "Retool 看板，无 API 数据也能拿。"
        ],
        "outputs": [
            "AI 浏览器自动化爬数据"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 浏览器自动化爬数据。工具链：Browser Use + Claude + Skyvern + Apify + Bright Data + Supabase + Retool。",
        "tags": [
            "agent",
            "data"
        ],
        "importance": 77,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "095",
        "title": "AI 二级市场量化助手",
        "id_slug": "ai-quant-assistant",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Polygon",
            "ChatGPT",
            "QuantConnect",
            "Claude",
            "Composer",
            "Alpaca",
            "Telegram",
            "散户半量化"
        ],
        "steps": [
            "Polygon 行情",
            "ChatGPT 选股逻辑",
            "QuantConnect 回测",
            "Claude 解读结果",
            "Composer/Alpaca 实盘",
            "Telegram 报警，散户半量化。"
        ],
        "outputs": [
            "AI 二级市场量化助手"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 二级市场量化助手。工具链：Polygon + ChatGPT + QuantConnect + Claude + Composer + Alpaca + Telegram + 散户半量化。",
        "tags": [
            "agent"
        ],
        "importance": 76,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "096",
        "title": "AI 婚介相亲匹配",
        "id_slug": "ai-dating",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Hinge",
            "Bumble",
            "ChatGPT",
            "Crystal",
            "Cal.com",
            "Yoodli"
        ],
        "steps": [
            "Hinge/Bumble 抓资料",
            "ChatGPT 起 opener",
            "Crystal 性格分析",
            "Cal.com 约线下",
            "Yoodli 练话术，约会成功率显著提升。"
        ],
        "outputs": [
            "AI 婚介相亲匹配"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 婚介相亲匹配。工具链：Hinge + Bumble + ChatGPT + Crystal + Cal.com + Yoodli。",
        "tags": [
            "business"
        ],
        "importance": 76,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "097",
        "title": "AI 直播购物选品",
        "id_slug": "ai-livestream",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "TikTok Shop",
            "Spate",
            "Helium10",
            "Midjourney",
            "Alibaba 1688",
            "ShipStation",
            "TikTok"
        ],
        "steps": [
            "TikTok Shop 数据",
            "Spate 趋势",
            "Helium10 找蓝海",
            "Midjourney 概念图",
            "Alibaba 1688 找货",
            "ShipStation 物流，TikTok 主播闭环选品。"
        ],
        "outputs": [
            "AI 直播购物选品"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 直播购物选品。工具链：TikTok Shop + Spate + Helium10 + Midjourney + Alibaba 1688 + ShipStation + TikTok。",
        "tags": [
            "media"
        ],
        "importance": 76,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "098",
        "title": "AI 学术导师答疑",
        "id_slug": "ai-tutor",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "NotebookLM",
            "Khanmigo",
            "Claude",
            "Anki",
            "ChatGPT",
            "Quizlet"
        ],
        "steps": [
            "上传课件",
            "NotebookLM 生成播客",
            "Khanmigo 答疑",
            "Claude 出习题",
            "Anki 排间隔重复",
            "ChatGPT 模考",
            "Quizlet 同步，学生自适应学习。"
        ],
        "outputs": [
            "AI 学术导师答疑"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 学术导师答疑。工具链：NotebookLM + Khanmigo + Claude + Anki + ChatGPT + Quizlet。",
        "tags": [
            "media"
        ],
        "importance": 76,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "099",
        "title": "AI 科技评测创作",
        "id_slug": "ai-tech-review",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "GSMArena",
            "ChatGPT",
            "Runway",
            "ElevenLabs",
            "Magnific",
            "CapCut",
            "YouTube"
        ],
        "steps": [
            "GSMArena 抓参数",
            "ChatGPT 对比卖点",
            "Runway 拼镜头",
            "ElevenLabs 配音",
            "Magnific 放产品图",
            "CapCut 剪辑",
            "YouTube 上架，科技博主低成本。"
        ],
        "outputs": [
            "AI 科技评测创作"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 科技评测创作。工具链：GSMArena + ChatGPT + Runway + ElevenLabs + Magnific + CapCut + YouTube。",
        "tags": [
            "media",
            "youtube"
        ],
        "importance": 76,
        "source_section": "AI工作流100条.pdf"
    },
    {
        "num": "100",
        "title": "AI 心理减压日记",
        "id_slug": "ai-mental-health",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Apple Journal",
            "ChatGPT",
            "Claude",
            "Calm",
            "Wysa AI",
            "Reflect"
        ],
        "steps": [
            "Apple Journal 提示",
            "ChatGPT 引导反思",
            "Claude 提取情绪模式",
            "Calm 推冥想",
            "Wysa AI 对话",
            "Reflect 周复盘，自我觉察提升。"
        ],
        "outputs": [
            "AI 心理减压日记"
        ],
        "summary": "来自《AI工作流100条》的端到端流程：AI 心理减压日记。工具链：Apple Journal + ChatGPT + Claude + Calm + Wysa AI + Reflect。",
        "tags": [
            "agent"
        ],
        "importance": 75,
        "source_section": "AI工作流100条.pdf"
    }
]

AIW100_MISSING_TOOL_SKILLS = [
    {
        "tool": "yt-dlp",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 长视频→多平台短视频矩阵"
    },
    {
        "tool": "Whisper",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 长视频→多平台短视频矩阵"
    },
    {
        "tool": "AssemblyAI",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 长视频→多平台短视频矩阵"
    },
    {
        "tool": "Opus Clip",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 长视频→多平台短视频矩阵"
    },
    {
        "tool": "Submagic",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 长视频→多平台短视频矩阵"
    },
    {
        "tool": "Buffer",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 长视频→多平台短视频矩阵"
    },
    {
        "tool": "Stripe",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "saas"
        ],
        "example": "PRD→上线 SaaS 全栈一日流"
    },
    {
        "tool": "Vercel",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "saas"
        ],
        "example": "PRD→上线 SaaS 全栈一日流"
    },
    {
        "tool": "PostHog",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "saas"
        ],
        "example": "PRD→上线 SaaS 全栈一日流"
    },
    {
        "tool": "Notion",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "Confluence",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "Unstructured",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "LlamaIndex",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "Qdrant",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "Slack",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "Langfuse",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "企业内部知识库智能问答"
    },
    {
        "tool": "Clay",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "crm"
        ],
        "example": "销售外联个性化批量化"
    },
    {
        "tool": "Lavender",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "crm"
        ],
        "example": "销售外联个性化批量化"
    },
    {
        "tool": "Smartlead",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "crm"
        ],
        "example": "销售外联个性化批量化"
    },
    {
        "tool": "Gong",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "crm"
        ],
        "example": "销售外联个性化批量化"
    },
    {
        "tool": "1688",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "seo"
        ],
        "example": "跨境电商商品页全自动化"
    },
    {
        "tool": "Magnific",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "seo"
        ],
        "example": "跨境电商商品页全自动化"
    },
    {
        "tool": "DeepL",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "seo"
        ],
        "example": "跨境电商商品页全自动化"
    },
    {
        "tool": "Shopify",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "seo"
        ],
        "example": "跨境电商商品页全自动化"
    },
    {
        "tool": "Perplexity Deep Research",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "research"
        ],
        "example": "行业深度研究报告"
    },
    {
        "tool": "Stanford Storm",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "research"
        ],
        "example": "行业深度研究报告"
    },
    {
        "tool": "VidIQ",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 频道选题到成片流水线"
    },
    {
        "tool": "TubeBuddy",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 频道选题到成片流水线"
    },
    {
        "tool": "Descript",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "YouTube 频道选题到成片流水线"
    },
    {
        "tool": "HeyGen Interactive Avatar",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 数字人带货直播"
    },
    {
        "tool": "飞瓜",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 数字人带货直播"
    },
    {
        "tool": "OBS",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 数字人带货直播"
    },
    {
        "tool": "Taplio",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "个人品牌 LinkedIn 增长引擎"
    },
    {
        "tool": "Phantombuster",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "个人品牌 LinkedIn 增长引擎"
    },
    {
        "tool": "Instantly",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "Cold Email→Demo 预约自动化"
    },
    {
        "tool": "Lemlist",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "Cold Email→Demo 预约自动化"
    },
    {
        "tool": "Calendly",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "Cold Email→Demo 预约自动化"
    },
    {
        "tool": "Fireflies",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "Cold Email→Demo 预约自动化"
    },
    {
        "tool": "Pipedrive",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "Cold Email→Demo 预约自动化"
    },
    {
        "tool": "Otter",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "用户研究访谈全闭环"
    },
    {
        "tool": "Dovetail",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "用户研究访谈全闭环"
    },
    {
        "tool": "Figma",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "用户研究访谈全闭环"
    },
    {
        "tool": "Sentry",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "Linear",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "复现",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "二分",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "gh pr create",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "Greptile",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "合并",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "软件 Bug 定位到修复"
    },
    {
        "tool": "Mintlify",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "产品文档双语同步"
    },
    {
        "tool": "Crowdin",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "产品文档双语同步"
    },
    {
        "tool": "Algolia DocSearch",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "产品文档双语同步"
    },
    {
        "tool": "Discord",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "产品文档双语同步"
    },
    {
        "tool": "Riverside.fm",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 播客制作流水线"
    },
    {
        "tool": "Auphonic",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 播客制作流水线"
    },
    {
        "tool": "Castmagic",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 播客制作流水线"
    },
    {
        "tool": "Spotify",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 播客制作流水线"
    },
    {
        "tool": "Apple",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 播客制作流水线"
    },
    {
        "tool": "YouTube",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "跨境出海视频本地化"
    },
    {
        "tool": "Synthesia",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 课程设计与售卖"
    },
    {
        "tool": "Heptabase",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 课程设计与售卖"
    },
    {
        "tool": "Teachable",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 课程设计与售卖"
    },
    {
        "tool": "Beehiiv",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 课程设计与售卖"
    },
    {
        "tool": "独立讲师月入过万",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 课程设计与售卖"
    },
    {
        "tool": "Visualping",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "竞品监控自动情报"
    },
    {
        "tool": "Diffbot",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "竞品监控自动情报"
    },
    {
        "tool": "BuiltWith",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "竞品监控自动情报"
    },
    {
        "tool": "GitHub Actions",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "data"
        ],
        "example": "AI 代码审查机器人"
    },
    {
        "tool": "Metabase",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "个人财务智能管家"
    },
    {
        "tool": "SciSpace",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "学术论文写作助手"
    },
    {
        "tool": "Grammarly",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "学术论文写作助手"
    },
    {
        "tool": "QuillBot",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "学术论文写作助手"
    },
    {
        "tool": "Overleaf",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "学术论文写作助手"
    },
    {
        "tool": "Turnitin",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "学术论文写作助手"
    },
    {
        "tool": "Snowflake",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "dbt",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "Cube.dev",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "MCP",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "自然语言",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "Hex",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "Mode",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "业务团队不",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "数据分析自然语言查询"
    },
    {
        "tool": "Mobbin",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "UI 设计→可点击原型"
    },
    {
        "tool": "Galileo AI",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "UI 设计→可点击原型"
    },
    {
        "tool": "Magician",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "UI 设计→可点击原型"
    },
    {
        "tool": "Anima",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "UI 设计→可点击原型"
    },
    {
        "tool": "Teal HQ",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 简历优化求职流"
    },
    {
        "tool": "Resume Worded",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 简历优化求职流"
    },
    {
        "tool": "Earkick",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 简历优化求职流"
    },
    {
        "tool": "Yoodli",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 简历优化求职流"
    },
    {
        "tool": "LinkedIn Recruiter",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 简历优化求职流"
    },
    {
        "tool": "Ahrefs",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "seo"
        ],
        "example": "内容 SEO 全栈打法"
    },
    {
        "tool": "Surfer SEO",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "seo"
        ],
        "example": "内容 SEO 全栈打法"
    },
    {
        "tool": "Frase",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "seo"
        ],
        "example": "内容 SEO 全栈打法"
    },
    {
        "tool": "Wordable",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "seo"
        ],
        "example": "内容 SEO 全栈打法"
    },
    {
        "tool": "Schema",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "seo"
        ],
        "example": "内容 SEO 全栈打法"
    },
    {
        "tool": "Google Search Console",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "seo"
        ],
        "example": "内容 SEO 全栈打法"
    },
    {
        "tool": "JobScan",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 招聘到入职闭环"
    },
    {
        "tool": "Hireflix",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 招聘到入职闭环"
    },
    {
        "tool": "Greenhouse",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 招聘到入职闭环"
    },
    {
        "tool": "DocuSign",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 招聘到入职闭环"
    },
    {
        "tool": "BambooHR",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 招聘到入职闭环"
    },
    {
        "tool": "PandaDoc",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "法务合同 AI 审查"
    },
    {
        "tool": "Spellbook",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "法务合同 AI 审查"
    },
    {
        "tool": "Harvey",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "法务合同 AI 审查"
    },
    {
        "tool": "Robin",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "法务合同 AI 审查"
    },
    {
        "tool": "Ironclad",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "法务合同 AI 审查"
    },
    {
        "tool": "Intercom",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "rag"
        ],
        "example": "客户支持 Tier1 自动化"
    },
    {
        "tool": "Pylon",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "rag"
        ],
        "example": "客户支持 Tier1 自动化"
    },
    {
        "tool": "Loom",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "rag"
        ],
        "example": "客户支持 Tier1 自动化"
    },
    {
        "tool": "Meta Advantage",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "营销活动从创意到投放"
    },
    {
        "tool": "Triple Whale",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "营销活动从创意到投放"
    },
    {
        "tool": "Northbeam",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "营销活动从创意到投放"
    },
    {
        "tool": "Sudowrite",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "电子书写作出版一条龙"
    },
    {
        "tool": "Atticus",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "电子书写作出版一条龙"
    },
    {
        "tool": "KDP",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "电子书写作出版一条龙"
    },
    {
        "tool": "Gumroad",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "电子书写作出版一条龙"
    },
    {
        "tool": "自媒体被动收入",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "电子书写作出版一条龙"
    },
    {
        "tool": "Tokens Studio",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 设计系统组件库"
    },
    {
        "tool": "Storybook",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 设计系统组件库"
    },
    {
        "tool": "Chromatic",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 设计系统组件库"
    },
    {
        "tool": "npm publish",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 设计系统组件库"
    },
    {
        "tool": "设计研发对齐",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 设计系统组件库"
    },
    {
        "tool": "Readwise",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "知识工作者第二大脑"
    },
    {
        "tool": "Mem",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "知识工作者第二大脑"
    },
    {
        "tool": "Obsidian Copilot",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "知识工作者第二大脑"
    },
    {
        "tool": "Akool",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 视频换脸+配音本地化"
    },
    {
        "tool": "HeyGen Avatar IV",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 视频换脸+配音本地化"
    },
    {
        "tool": "Sync.so",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 视频换脸+配音本地化"
    },
    {
        "tool": "Topaz",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 视频换脸+配音本地化"
    },
    {
        "tool": "Trellis",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "3D 资产 AI 生成管线"
    },
    {
        "tool": "Tripo3D",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "3D 资产 AI 生成管线"
    },
    {
        "tool": "Blender",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "3D 资产 AI 生成管线"
    },
    {
        "tool": "Unity",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "3D 资产 AI 生成管线"
    },
    {
        "tool": "UE",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "3D 资产 AI 生成管线"
    },
    {
        "tool": "ComfyUI",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 漫画生产流水线"
    },
    {
        "tool": "IP-Adapter",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 漫画生产流水线"
    },
    {
        "tool": "Photoshop Generative",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 漫画生产流水线"
    },
    {
        "tool": "Clip Studio",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 漫画生产流水线"
    },
    {
        "tool": "公众号",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 漫画生产流水线"
    },
    {
        "tool": "Webtoon",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 漫画生产流水线"
    },
    {
        "tool": "Superwhisper",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 助手 Mac 全局加速"
    },
    {
        "tool": "BoltAI",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 助手 Mac 全局加速"
    },
    {
        "tool": "Maccy",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 助手 Mac 全局加速"
    },
    {
        "tool": "Karabiner",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 助手 Mac 全局加速"
    },
    {
        "tool": "键盘流效率爆表",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 助手 Mac 全局加速"
    },
    {
        "tool": "Superhuman",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual",
            "crm"
        ],
        "example": "跨工具个人 CRM"
    },
    {
        "tool": "Cal.com",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual",
            "crm"
        ],
        "example": "跨工具个人 CRM"
    },
    {
        "tool": "Dex",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual",
            "crm"
        ],
        "example": "跨工具个人 CRM"
    },
    {
        "tool": "社交资产化",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual",
            "crm"
        ],
        "example": "跨工具个人 CRM"
    },
    {
        "tool": "MyFitnessPal",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "Whoop",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "Caliber",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "Future",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "Form AI",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "Apple Health",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "私教成本 1",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "health"
        ],
        "example": "AI 健身私教"
    },
    {
        "tool": "Speak App",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 学英语沉浸训练"
    },
    {
        "tool": "LingQ",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 学英语沉浸训练"
    },
    {
        "tool": "Anki",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 学英语沉浸训练"
    },
    {
        "tool": "Pimsleur",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 学英语沉浸训练"
    },
    {
        "tool": "Perplexity Finance",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "finance"
        ],
        "example": "个人投资研究助手"
    },
    {
        "tool": "Koyfin",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "finance"
        ],
        "example": "个人投资研究助手"
    },
    {
        "tool": "TradingView",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "finance"
        ],
        "example": "个人投资研究助手"
    },
    {
        "tool": "Composer",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "finance"
        ],
        "example": "个人投资研究助手"
    },
    {
        "tool": "IBKR",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "finance"
        ],
        "example": "个人投资研究助手"
    },
    {
        "tool": "散户机构化",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research",
            "finance"
        ],
        "example": "个人投资研究助手"
    },
    {
        "tool": "Wanderboat",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 旅行规划"
    },
    {
        "tool": "Google Maps",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 旅行规划"
    },
    {
        "tool": "Skyscanner",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 旅行规划"
    },
    {
        "tool": "Booking",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 旅行规划"
    },
    {
        "tool": "Wallet",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 旅行规划"
    },
    {
        "tool": "Polarsteps",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 旅行规划"
    },
    {
        "tool": "NovelAI",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 短篇小说生产"
    },
    {
        "tool": "Substack",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 短篇小说生产"
    },
    {
        "tool": "Patreon",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 短篇小说生产"
    },
    {
        "tool": "网文作者新打法",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 短篇小说生产"
    },
    {
        "tool": "Suno v4",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 音乐 EP 制作"
    },
    {
        "tool": "Udio Extend",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 音乐 EP 制作"
    },
    {
        "tool": "Logic Pro",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 音乐 EP 制作"
    },
    {
        "tool": "LANDR",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 音乐 EP 制作"
    },
    {
        "tool": "DistroKid",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 音乐 EP 制作"
    },
    {
        "tool": "Lightroom AI",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 摄影后期批处理"
    },
    {
        "tool": "Pixieset",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 摄影后期批处理"
    },
    {
        "tool": "婚摄",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 摄影后期批处理"
    },
    {
        "tool": "Whisper Streaming",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播字幕同传"
    },
    {
        "tool": "vMix",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播字幕同传"
    },
    {
        "tool": "Restream",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播字幕同传"
    },
    {
        "tool": "Twilio",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "rag"
        ],
        "example": "AI 电话客服机器人"
    },
    {
        "tool": "Vapi",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "rag"
        ],
        "example": "AI 电话客服机器人"
    },
    {
        "tool": "Bland AI",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business",
            "rag"
        ],
        "example": "AI 电话客服机器人"
    },
    {
        "tool": "Datadog",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "data"
        ],
        "example": "DevOps AI 巡检"
    },
    {
        "tool": "PagerDuty",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "data"
        ],
        "example": "DevOps AI 巡检"
    },
    {
        "tool": "Runbook",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "data"
        ],
        "example": "DevOps AI 巡检"
    },
    {
        "tool": "Postmortem AI",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "data"
        ],
        "example": "DevOps AI 巡检"
    },
    {
        "tool": "Crunchbase",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 招商资料一键生成"
    },
    {
        "tool": "Tome",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 招商资料一键生成"
    },
    {
        "tool": "DocSend",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 招商资料一键生成"
    },
    {
        "tool": "Gradescope",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 教学题库出题阅卷"
    },
    {
        "tool": "老师工作量减半",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 教学题库出题阅卷"
    },
    {
        "tool": "Zillow",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 房产经纪助手"
    },
    {
        "tool": "Virtual Staging AI",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 房产经纪助手"
    },
    {
        "tool": "Matterport",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 房产经纪助手"
    },
    {
        "tool": "挂牌一天成交",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 房产经纪助手"
    },
    {
        "tool": "DAX",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 医疗文书助手"
    },
    {
        "tool": "Abridge",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 医疗文书助手"
    },
    {
        "tool": "Epic",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 医疗文书助手"
    },
    {
        "tool": "Tally",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 医疗文书助手"
    },
    {
        "tool": "医生省 2 小时",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 医疗文书助手"
    },
    {
        "tool": "小红书爆文",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 短视频图文混剪"
    },
    {
        "tool": "矩阵号",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 短视频图文混剪"
    },
    {
        "tool": "飞瓜监测",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 短视频图文混剪"
    },
    {
        "tool": "单号月涨万粉",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 短视频图文混剪"
    },
    {
        "tool": "Inworld AI",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 游戏 NPC 智能化"
    },
    {
        "tool": "Convai",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 游戏 NPC 智能化"
    },
    {
        "tool": "Ready Player Me",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 游戏 NPC 智能化"
    },
    {
        "tool": "行为树驱动剧情",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 游戏 NPC 智能化"
    },
    {
        "tool": "RSS",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "podcast"
        ],
        "example": "AI 简短播客 newsletter"
    },
    {
        "tool": "Apple Podcasts",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "podcast"
        ],
        "example": "AI 简短播客 newsletter"
    },
    {
        "tool": "通勤听完一天信息",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "podcast"
        ],
        "example": "AI 简短播客 newsletter"
    },
    {
        "tool": "LinkedIn",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 求职公司情报"
    },
    {
        "tool": "Crystal Knows",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 求职公司情报"
    },
    {
        "tool": "Glassdoor",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 求职公司情报"
    },
    {
        "tool": "offer",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 求职公司情报"
    },
    {
        "tool": "DoNotPay",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 法律咨询自助"
    },
    {
        "tool": "Court Buddy",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 法律咨询自助"
    },
    {
        "tool": "Calendar",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 法律咨询自助"
    },
    {
        "tool": "小额纠纷无需律师",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 法律咨询自助"
    },
    {
        "tool": "Mercury",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 一人公司财税"
    },
    {
        "tool": "Pilot",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 一人公司财税"
    },
    {
        "tool": "Bench AI",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 一人公司财税"
    },
    {
        "tool": "Ramp",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 一人公司财税"
    },
    {
        "tool": "TurboTax",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 一人公司财税"
    },
    {
        "tool": "Mixpanel",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 运营周报自动化"
    },
    {
        "tool": "BigQuery",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 运营周报自动化"
    },
    {
        "tool": "Cube",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 运营周报自动化"
    },
    {
        "tool": "PM",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 运营周报自动化"
    },
    {
        "tool": "Hive",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 内容审核合规"
    },
    {
        "tool": "OpenAI Moderation",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 内容审核合规"
    },
    {
        "tool": "Lasso",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 内容审核合规"
    },
    {
        "tool": "Trust&Safety;",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 内容审核合规"
    },
    {
        "tool": "UGC",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 内容审核合规"
    },
    {
        "tool": "Readlang",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二语阅读流水线"
    },
    {
        "tool": "Speak",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二语阅读流水线"
    },
    {
        "tool": "Audible",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二语阅读流水线"
    },
    {
        "tool": "Pinterest",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 婚礼策划全流程"
    },
    {
        "tool": "HoneyBook",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 婚礼策划全流程"
    },
    {
        "tool": "Cronometer",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 健康饮食定制"
    },
    {
        "tool": "Levels",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 健康饮食定制"
    },
    {
        "tool": "Mealime",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 健康饮食定制"
    },
    {
        "tool": "Instacart",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 健康饮食定制"
    },
    {
        "tool": "Crisp",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "rag"
        ],
        "example": "AI 跨境客服多语化"
    },
    {
        "tool": "转人工时",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "rag"
        ],
        "example": "AI 跨境客服多语化"
    },
    {
        "tool": "Help Scout",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "rag"
        ],
        "example": "AI 跨境客服多语化"
    },
    {
        "tool": "Canny",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 产品反馈闭环"
    },
    {
        "tool": "Productboard",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 产品反馈闭环"
    },
    {
        "tool": "PMF",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 产品反馈闭环"
    },
    {
        "tool": "Apify",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 电商客评分析"
    },
    {
        "tool": "Sentiment",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 电商客评分析"
    },
    {
        "tool": "Looker",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 电商客评分析"
    },
    {
        "tool": "Helium10",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 电商客评分析"
    },
    {
        "tool": "选品决策数据化",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 电商客评分析"
    },
    {
        "tool": "Streamyard",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "AI 直播脚本到分发"
    },
    {
        "tool": "Opus",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "AI 直播脚本到分发"
    },
    {
        "tool": "单场素材榨干",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "AI 直播脚本到分发"
    },
    {
        "tool": "Slack AI",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 内部通讯本地化"
    },
    {
        "tool": "Sunsama",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 个人 OKR 跟踪"
    },
    {
        "tool": "Reclaim AI",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 个人 OKR 跟踪"
    },
    {
        "tool": "自驱力满格",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 个人 OKR 跟踪"
    },
    {
        "tool": "Hootsuite",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 跨境社媒运营"
    },
    {
        "tool": "Mention",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 跨境社媒运营"
    },
    {
        "tool": "Eagle",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 灵感素材库管理"
    },
    {
        "tool": "Raindrop",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 灵感素材库管理"
    },
    {
        "tool": "CLIP",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 灵感素材库管理"
    },
    {
        "tool": "Pinecone",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 灵感素材库管理"
    },
    {
        "tool": "Public Comps",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 投资人 DD 加速"
    },
    {
        "tool": "Reference",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 投资人 DD 加速"
    },
    {
        "tool": "Zapier",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 监控合同到期"
    },
    {
        "tool": "Tella",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 产品视频教程批量"
    },
    {
        "tool": "Wistia",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 产品视频教程批量"
    },
    {
        "tool": "新功能上线即",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 产品视频教程批量"
    },
    {
        "tool": "Mixmax",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 求职邮件 follow-up"
    },
    {
        "tool": "Gmail",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 电邮归档检索"
    },
    {
        "tool": "Shortwave",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 电邮归档检索"
    },
    {
        "tool": "Reflect",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 电邮归档检索"
    },
    {
        "tool": "GitHub",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 远程协作日报"
    },
    {
        "tool": "远程信任",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 远程协作日报"
    },
    {
        "tool": "Sift",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 多模态搜索品控"
    },
    {
        "tool": "Trello",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 多模态搜索品控"
    },
    {
        "tool": "电商假货识别",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "research"
        ],
        "example": "AI 多模态搜索品控"
    },
    {
        "tool": "Houzz",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 房屋装修规划"
    },
    {
        "tool": "Planner 5D",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 房屋装修规划"
    },
    {
        "tool": "Thumbtack",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 房屋装修规划"
    },
    {
        "tool": "装修不踩坑",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 房屋装修规划"
    },
    {
        "tool": "红果",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 短剧爆款生产"
    },
    {
        "tool": "抖音",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 短剧爆款生产"
    },
    {
        "tool": "Krisp",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 演讲准备到现场"
    },
    {
        "tool": "Spate",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 一人电商品牌"
    },
    {
        "tool": "Printify POD",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 一人电商品牌"
    },
    {
        "tool": "Meta AI",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 一人电商品牌"
    },
    {
        "tool": "Gorgias",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 一人电商品牌"
    },
    {
        "tool": "月入 5 万美金",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "visual"
        ],
        "example": "AI 一人电商品牌"
    },
    {
        "tool": "Apple Photos",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 求婚/婚礼短片"
    },
    {
        "tool": "现场播放",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 求婚/婚礼短片"
    },
    {
        "tool": "感动全场",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 求婚/婚礼短片"
    },
    {
        "tool": "Modmail",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 社区内容审核"
    },
    {
        "tool": "Granicus",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 政府事务自动化"
    },
    {
        "tool": "OpenStates",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 政府事务自动化"
    },
    {
        "tool": "Phone2Action",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 政府事务自动化"
    },
    {
        "tool": "Google Calendar",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 家庭日程管家"
    },
    {
        "tool": "Motion",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 家庭日程管家"
    },
    {
        "tool": "Reclaim",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 家庭日程管家"
    },
    {
        "tool": "Cozi",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 家庭日程管家"
    },
    {
        "tool": "Alexa",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 家庭日程管家"
    },
    {
        "tool": "二孩家庭不混乱",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 家庭日程管家"
    },
    {
        "tool": "Locize",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 软件本地化全自动"
    },
    {
        "tool": "Lokalise",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding"
        ],
        "example": "AI 软件本地化全自动"
    },
    {
        "tool": "Hypefury",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 个人 IP 视频引擎"
    },
    {
        "tool": "多端复",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 个人 IP 视频引擎"
    },
    {
        "tool": "ConvertKit",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI Newsletter 长尾变现"
    },
    {
        "tool": "Twitter",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI Newsletter 长尾变现"
    },
    {
        "tool": "万粉月入过万",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI Newsletter 长尾变现"
    },
    {
        "tool": "Carrd",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 课程销售漏斗"
    },
    {
        "tool": "Circle",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 课程销售漏斗"
    },
    {
        "tool": "转化率倍增",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 课程销售漏斗"
    },
    {
        "tool": "DocSign",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 智能合同审查批量"
    },
    {
        "tool": "Flourish",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office"
        ],
        "example": "AI 数据可视化叙事"
    },
    {
        "tool": "CrewAI",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "research",
            "agent"
        ],
        "example": "AI 多 Agent 复杂调研"
    },
    {
        "tool": "Writer",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "research",
            "agent"
        ],
        "example": "AI 多 Agent 复杂调研"
    },
    {
        "tool": "Tavily",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "research",
            "agent"
        ],
        "example": "AI 多 Agent 复杂调研"
    },
    {
        "tool": "LangGraph",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "coding",
            "research",
            "agent"
        ],
        "example": "AI 多 Agent 复杂调研"
    },
    {
        "tool": "Ollama",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 本地隐私 RAG"
    },
    {
        "tool": "Open WebUI",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 本地隐私 RAG"
    },
    {
        "tool": "AnythingLLM",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 本地隐私 RAG"
    },
    {
        "tool": "ChromaDB",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 本地隐私 RAG"
    },
    {
        "tool": "Tailscale",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 本地隐私 RAG"
    },
    {
        "tool": "敏感行业零上云",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "office",
            "rag"
        ],
        "example": "AI 本地隐私 RAG"
    },
    {
        "tool": "Browser Use",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent",
            "data"
        ],
        "example": "AI 浏览器自动化爬数据"
    },
    {
        "tool": "Skyvern",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent",
            "data"
        ],
        "example": "AI 浏览器自动化爬数据"
    },
    {
        "tool": "Bright Data",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent",
            "data"
        ],
        "example": "AI 浏览器自动化爬数据"
    },
    {
        "tool": "Supabase",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent",
            "data"
        ],
        "example": "AI 浏览器自动化爬数据"
    },
    {
        "tool": "Retool",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent",
            "data"
        ],
        "example": "AI 浏览器自动化爬数据"
    },
    {
        "tool": "Polygon",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二级市场量化助手"
    },
    {
        "tool": "QuantConnect",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二级市场量化助手"
    },
    {
        "tool": "Alpaca",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二级市场量化助手"
    },
    {
        "tool": "Telegram",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二级市场量化助手"
    },
    {
        "tool": "散户半量化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 二级市场量化助手"
    },
    {
        "tool": "Hinge",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 婚介相亲匹配"
    },
    {
        "tool": "Bumble",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 婚介相亲匹配"
    },
    {
        "tool": "Crystal",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "business"
        ],
        "example": "AI 婚介相亲匹配"
    },
    {
        "tool": "TikTok Shop",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播购物选品"
    },
    {
        "tool": "Alibaba 1688",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播购物选品"
    },
    {
        "tool": "ShipStation",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播购物选品"
    },
    {
        "tool": "TikTok",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media"
        ],
        "example": "AI 直播购物选品"
    },
    {
        "tool": "GSMArena",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "media",
            "youtube"
        ],
        "example": "AI 科技评测创作"
    },
    {
        "tool": "Apple Journal",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 心理减压日记"
    },
    {
        "tool": "Calm",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 心理减压日记"
    },
    {
        "tool": "Wysa AI",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "agent"
        ],
        "example": "AI 心理减压日记"
    }
]


def _slugify_tool(tool: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", tool.lower()).strip("-")
    if slug:
        return slug[:54]
    return "tool-" + str(abs(hash(tool)))[:12]


def _unique_item_id(prefix: str, slug: str, used: set[str]) -> str:
    base = f"{prefix}-{slug}"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def _is_valid_tool(tool: str) -> bool:
    if not tool:
        return False
    value = tool.strip()
    if len(value) > 32:
        return False
    has_latin = bool(re.search(r"[A-Za-z]", value))
    has_digit = bool(re.search(r"\d", value))
    has_cjk = bool(re.search(r"[\u3400-\u9fff]", value))
    if has_cjk and not has_latin and not has_digit:
        return False
    noise_words = (
        "成本", "月入", "成交", "全场", "无需", "效率", "翻倍", "省",
        "涨粉", "决策", "上线即", "不再", "不踩坑", "满格", "打法",
        "矩阵号", "自然语言", "合并", "复现", "二分", "多端复",
    )
    if any(word in value for word in noise_words):
        return False
    return True


def _tool_profile(tool: str, category_id: str) -> tuple[str, str, str]:
    value = tool.lower()
    rules = [
        (("yt-dlp",), "下载和整理视频素材", "媒体素材采集", "从公开视频平台下载源素材，作为后续转写、切片、字幕和多平台分发的输入。"),
        (("whisper", "assemblyai", "otter", "riverside", "fireflies", "superwhisper"), "做语音转写", "语音转写和会议记录", "把音频或会议内容转成可搜索、可总结的文字材料，方便后续摘要、切片、跟进和知识沉淀。"),
        (("opus clip", "submagic", "descript", "capcut", "tella", "wistia"), "做短视频剪辑和字幕包装", "短视频剪辑与字幕包装", "把长内容拆成可发布的短视频，处理字幕、停顿、片段节奏和多平台分发前的包装。"),
        (("heygen", "synthesia", "akool", "sync.so", "ready player me"), "生成数字人和口型视频", "数字人和口型视频", "生成数字人、avatar 视频或多语口型同步，让脚本内容可以变成可观看的讲解、带货或培训素材。"),
        (("elevenlabs", "vapi", "bland ai", "twilio"), "生成语音和语音交互", "语音生成和语音交互", "负责配音、克隆声音、电话对话或语音客服，把文字脚本连接到真实语音体验。"),
        (("suno", "udio", "landr", "logic pro", "stable audio"), "制作音乐和音频资产", "音乐和音频制作", "生成歌曲、BGM、分轨、母带或声音素材，适合把创意主题变成可发布的音频资产。"),
        (("midjourney", "ideogram", "flux", "firefly", "photoshop", "magnific", "topaz", "imagen", "lightroom"), "生成和精修视觉素材", "图像生成与视觉精修", "处理概念图、商品图、海报、修图、放大和视觉一致性，是图像类流程里的核心生产能力。"),
        (("figma", "v0", "anima", "galileo", "magician", "mobbin", "storybook", "chromatic"), "设计界面和交付前端组件", "界面设计和前端交付", "把产品想法、设计参考或组件规范转成可迭代的 UI、原型、组件代码和设计系统材料。"),
        (("stripe",), "接入支付和订阅", "支付接入", "负责产品收费、订阅、付款链路和商业化闭环，常用于 SaaS MVP 或一人公司项目上线。"),
        (("vercel",), "部署 Web 产品", "部署上线", "把前端或全栈应用发布到线上环境，方便快速预览、迭代和交付真实用户。"),
        (("posthog",), "追踪产品数据", "产品分析", "记录用户行为、转化路径和功能使用情况，帮助判断产品是否真的被使用。"),
        (("cursor", "claude code", "supabase", "sentry", "linear", "github", "vitest", "eslint", "semgrep", "greptile"), "完成工程开发和协作", "软件开发和上线", "用于代码生成、缺陷定位、测试、监控和工程协作，帮助把想法推进到可运行产品。"),
        (("snowflake", "bigquery", "hex", "cube", "metabase", "looker", "dbt", "mode", "flourish"), "分析数据并生成可视化", "数据分析和可视化", "连接数据仓库、语义层、分析笔记本或图表工具，把业务数据变成洞察、仪表盘和可汇报内容。"),
        (("datadog", "pagerduty", "runbook", "postmortem"), "监控系统并处理故障", "运维监控和故障处理", "用于告警、异常诊断、修复流程和复盘记录，适合 DevOps 或 SRE 自动化巡检场景。"),
        (("apollo", "clay", "hubspot", "gong", "lemlist", "instantly", "lavender", "smartlead", "pipedrive", "calendly", "outreach", "close"), "管理销售外联和 CRM", "销售外联和 CRM", "用于找线索、补全客户信息、生成外联话术、安排会议、记录跟进并同步 CRM。"),
        (("shopify", "helium10", "shipstation", "printify", "spate", "triple whale", "gorgias", "klaviyo"), "运营电商和增长链路", "电商运营和增长", "用于商品上架、选品研究、物流、归因、客服和邮件营销，支撑跨境电商或 DTC 增长链路。"),
        (("perplexity", "genspark", "notebooklm", "scite", "consensus", "zotero", "scispace", "elicit", "koyfin", "crunchbase"), "检索资料和整理研究", "研究检索和资料整理", "搜索资料、消化论文或公司信息、管理引用，并把多源材料整理成报告、备忘录或研究结论。"),
        (("notion", "confluence", "llamaindex", "qdrant", "dify", "langfuse", "unstructured", "pinecone", "chromadb"), "搭建知识库和 RAG 问答", "知识库和 RAG", "负责文档解析、切块、向量检索、RAG 编排和效果监控，让内部资料可以被问答系统可靠调用。"),
        (("deepl", "crowdin", "lokalise", "locize", "algolia docsearch"), "处理翻译、本地化和文档搜索", "翻译、本地化和文档搜索", "用于多语言翻译、术语校对、版本管理和文档检索，适合产品国际化和内容本地化。"),
        (("beehiiv", "substack", "buffer", "hootsuite", "hypefury", "mailchimp", "convertkit", "carrd", "circle"), "分发内容和运营社群", "内容分发和社群增长", "用于 newsletter、社媒排程、邮件自动化、落地页和社区运营，把内容资产转成持续触达。"),
        (("docusign", "ironclad", "pandadoc", "spellbook", "harvey", "court buddy"), "处理合同和法务流程", "合同和法务流程", "用于合同生成、条款审查、签署、审批和归档，适合法务审核或销售合同自动化。"),
        (("quizlet", "khanmigo", "gradescope", "anki", "speak", "lingq", "readlang", "yoodli"), "制作学习训练和反馈", "学习训练和反馈", "把资料转成练习、闪卡、口语反馈或个性化辅导，用于课程、语言学习和答辩准备。"),
        (("apple health", "whoop", "levels", "cronometer", "mealime", "myfitnesspal", "calm", "wysa"), "管理健康数据和个人习惯", "健康数据和个人管理", "记录健康、饮食、恢复、心理状态或习惯数据，再交给 AI 做计划、提醒和复盘。"),
    ]
    for keywords, action, label, detail in rules:
        if any(keyword in value for keyword in keywords):
            return action, label, detail

    category_profiles = {
        "ai-coding": ("完成工程实现", "工程实现、自动化或产品交付", "用于把需求转成可运行代码、自动化脚本、部署流程或产品交付物。"),
        "ai-media": ("制作多媒体内容", "视频、音频或多媒体内容制作", "用于视频、播客、直播、字幕、音频或多平台内容的制作与发布。"),
        "ai-visual": ("制作视觉资产", "视觉设计、图像处理或创意资产生产", "用于生成、整理或加工图片、设计参考、品牌视觉和创意素材。"),
        "ai-office": ("整理办公和知识材料", "办公文档、会议、课程或知识整理", "用于会议、文档、课程、邮件、日程或个人知识管理。"),
        "ai-research": ("做研究和决策分析", "资料检索、研究分析或决策支持", "用于收集资料、比较信息、分析证据并形成可行动结论。"),
        "ai-agent": ("编排自动化任务", "多工具自动化、Agent 编排或任务执行", "用于连接多个工具、触发动作、传递上下文并完成跨步骤任务。"),
        "ai-business": ("优化商业流程", "营销、销售、运营、客服或商业流程", "用于获客、转化、支持、运营、合规或收入相关的业务环节。"),
        "ai-models": ("调用模型能力", "模型调用、本地模型或 AI 基础能力", "用于模型接入、推理调用、本地部署或基础 AI 能力扩展。"),
    }
    return category_profiles.get(category_id, ("完成 AI 任务", "AI 工作流", "用于把输入材料加工成下一步可使用的结果。"))


def _tool_description(tool: str, category_id: str, example: str) -> str:
    action, label, detail = _tool_profile(tool, category_id)
    return f"{tool} 主要用于{label}。{detail}在「{example}」这个场景里，它的作用是{action.replace('做', '').replace('完成', '').replace('处理', '')}，而不是单纯记录为一个工具名。"


def workflow_skill_items() -> list[dict]:
    items: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    for item in AIW100_MISSING_TOOL_SKILLS:
        tool = item["tool"]
        if not _is_valid_tool(tool):
            continue
        action, _, _ = _tool_profile(tool, item["category_id"])
        name = f"用 {tool} {action}"
        key = (name, item["category_id"], tool)
        if key in seen:
            continue
        seen.add(key)
        tags = list(dict.fromkeys([tool.lower(), "workflow", *item.get("tags", [])]))[:8]
        items.append({
            "id": f"aiw100-tool-{_slugify_tool(tool)}",
            "name": name,
            "category_id": item["category_id"],
            "category_label": item["category_label"],
            "tool": tool,
            "stage": "workflow",
            "description": _tool_description(tool, item["category_id"], item.get("example", "AI 工作流组合")),
            "tags": tags,
            "examples": [item.get("example", "AI 工作流组合")],
            "input_types": ["text", "file", "prompt"],
            "output_types": ["workflow", "asset", "automation"],
            "difficulty": 2,
            "importance": 62,
            "is_core": False,
            "is_active": True,
        })
    return items


def workflow_library_items() -> list[dict]:
    items: list[dict] = []
    used_ids: set[str] = set()
    for item in AIW100_WORKFLOWS:
        workflow_id = _unique_item_id("workflow-aiw100", item["id_slug"], used_ids)
        combo_id = _unique_item_id("combo-aiw100", item["id_slug"], used_ids)
        tools = [tool for tool in item["tools"] if _is_valid_tool(tool)]
        role_text = "；".join(item["steps"][:8])
        combo_summary = f"来自《AI工作流100条》的工具组合：{item['title']}。工具分工：{role_text}"
        workflow_summary = f"来自《AI工作流100条》的端到端流程：{item['title']}。工具分工：{role_text}"
        common = {
            "category_id": item["category_id"],
            "category_label": item["category_label"],
            "tools": tools,
            "tags": item["tags"],
            "source_section": AIW100_SOURCE,
            "importance": item["importance"],
            "is_active": True,
        }
        items.append({
            "id": combo_id,
            "item_type": "combination",
            "title": item["title"],
            "summary": combo_summary,
            "steps": item["steps"],
            "outputs": [],
            **common,
        })
        items.append({
            "id": workflow_id,
            "item_type": "workflow",
            "title": item["title"],
            "summary": workflow_summary,
            "steps": item["steps"],
            "outputs": item["outputs"],
            **common,
        })
    return items
