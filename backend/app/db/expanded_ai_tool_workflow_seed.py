from __future__ import annotations

import hashlib
import re

EXPANDED_AI_SOURCE = "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf"

EXPANDED_AI_WORKFLOWS = [
    {
        "num": "01",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Claude + Gamma",
        "combo": "Claude + Gamma",
        "id_slug": "ppt-claude-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Gamma"
        ],
        "steps": [
            "Claude 先把访谈/资料整理成叙事大纲、页标题、每页要点",
            "Gamma 生成初版 deck",
            "Claude 再做逻辑审稿和演讲稿"
        ],
        "workflow": "Claude 先把访谈/资料整理成叙事大纲、页标题、每页要点；Gamma 生成初版 deck；Claude 再做逻辑审稿和演讲稿。",
        "outputs": [
            "咨询、销售、课程、融资路演"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Claude + Gamma。工具分工：Claude 先把访谈/资料整理成叙事大纲、页标题、每页要点；Gamma 生成初版 deck；Claude 再做逻辑审稿和演讲稿。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "咨询、销售、课程、融资路演"
    },
    {
        "num": "02",
        "scenario": "PPT/提案",
        "title": "PPT/提案：ChatGPT Deep Research + Gamma",
        "combo": "ChatGPT Deep Research + Gamma",
        "id_slug": "ppt-chatgpt-deep-research-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT Deep Research",
            "Gamma"
        ],
        "steps": [
            "ChatGPT 深研收集市场/竞品/引用",
            "输出结构化简报",
            "Gamma 变成演示文稿",
            "人工补品牌视觉"
        ],
        "workflow": "ChatGPT 深研收集市场/竞品/引用；输出结构化简报；Gamma 变成演示文稿；人工补品牌视觉。",
        "outputs": [
            "市场研究、行业报告转 PPT"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：ChatGPT Deep Research + Gamma。工具分工：ChatGPT 深研收集市场/竞品/引用；输出结构化简报；Gamma 变成演示文稿；人工补品牌视觉。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "市场研究、行业报告转 PPT"
    },
    {
        "num": "03",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Perplexity + Claude + Canva",
        "combo": "Perplexity + Claude + Canva",
        "id_slug": "ppt-perplexity-claude-canva",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Perplexity",
            "Claude",
            "Canva"
        ],
        "steps": [
            "Perplexity 找带来源的信息",
            "Claude 压成故事线",
            "Canva 套品牌模板生成图文页"
        ],
        "workflow": "Perplexity 找带来源的信息；Claude 压成故事线；Canva 套品牌模板生成图文页。",
        "outputs": [
            "内容团队、轻量品牌提案"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Perplexity + Claude + Canva。工具分工：Perplexity 找带来源的信息；Claude 压成故事线；Canva 套品牌模板生成图文页。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "内容团队、轻量品牌提案"
    },
    {
        "num": "04",
        "scenario": "PPT/提案",
        "title": "PPT/提案：ChatGPT + Canva app",
        "combo": "ChatGPT + Canva app",
        "id_slug": "ppt-chatgpt-canva-app",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Canva app"
        ],
        "steps": [
            "在 ChatGPT 里沉淀定位、标语、页面结构",
            "调用 Canva app 直接生成宣传页或简报"
        ],
        "workflow": "在 ChatGPT 里沉淀定位、标语、页面结构；调用 Canva app 直接生成宣传页或简报。",
        "outputs": [
            "小团队快速出图出 deck"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：ChatGPT + Canva app。工具分工：在 ChatGPT 里沉淀定位、标语、页面结构；调用 Canva app 直接生成宣传页或简报。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "小团队快速出图出 deck"
    },
    {
        "num": "05",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Claude Design + Canva",
        "combo": "Claude Design + Canva",
        "id_slug": "ppt-claude-design-canva",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude Design",
            "Canva"
        ],
        "steps": [
            "Claude Design 快速探索界面/产品概念",
            "导出到 Canva",
            "再做视觉统一和版式整理"
        ],
        "workflow": "Claude Design 快速探索界面/产品概念；导出到 Canva；再做视觉统一和版式整理。",
        "outputs": [
            "产品概念、设计汇报"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Claude Design + Canva。工具分工：Claude Design 快速探索界面/产品概念；导出到 Canva；再做视觉统一和版式整理。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品概念、设计汇报"
    },
    {
        "num": "06",
        "scenario": "PPT/提案",
        "title": "PPT/提案：NotebookLM + Claude + Gamma",
        "combo": "NotebookLM + Claude + Gamma",
        "id_slug": "ppt-notebooklm-claude-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "NotebookLM",
            "Claude",
            "Gamma"
        ],
        "steps": [
            "NotebookLM 汇总长资料和音视频",
            "Claude 提炼核心观点",
            "Gamma 生成培训/分享 PPT"
        ],
        "workflow": "NotebookLM 汇总长资料和音视频；Claude 提炼核心观点；Gamma 生成培训/分享 PPT。",
        "outputs": [
            "学习型组织、课程制作"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：NotebookLM + Claude + Gamma。工具分工：NotebookLM 汇总长资料和音视频；Claude 提炼核心观点；Gamma 生成培训/分享 PPT。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "学习型组织、课程制作"
    },
    {
        "num": "07",
        "scenario": "PPT/提案",
        "title": "PPT/提案：ChatGPT + Google Drive connector + Slides/Canva",
        "combo": "ChatGPT + Google Drive connector + Slides/Canva",
        "id_slug": "ppt-chatgpt-google-drive-connector-slides-canva",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Google Drive connector",
            "Slides",
            "Canva"
        ],
        "steps": [
            "ChatGPT 读取 Drive 内文档，生成会议汇报结构",
            "再用 Slides 或 Canva 做版式"
        ],
        "workflow": "ChatGPT 读取 Drive 内文档，生成会议汇报结构；再用 Slides 或 Canva 做版式。",
        "outputs": [
            "企业内部周报/月报"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：ChatGPT + Google Drive connector + Slides/Canva。工具分工：ChatGPT 读取 Drive 内文档，生成会议汇报结构；再用 Slides 或 Canva 做版式。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "企业内部周报/月报"
    },
    {
        "num": "08",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Claude + Notion connector + Gamma",
        "combo": "Claude + Notion connector + Gamma",
        "id_slug": "ppt-claude-notion-connector-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Notion connector",
            "Gamma"
        ],
        "steps": [
            "Claude 搜 Notion 项目资料，生成客户化方案",
            "Gamma 输出 deck",
            "Notion 回写版本记录"
        ],
        "workflow": "Claude 搜 Notion 项目资料，生成客户化方案；Gamma 输出 deck；Notion 回写版本记录。",
        "outputs": [
            "客户成功、项目经理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Claude + Notion connector + Gamma。工具分工：Claude 搜 Notion 项目资料，生成客户化方案；Gamma 输出 deck；Notion 回写版本记录。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客户成功、项目经理"
    },
    {
        "num": "09",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Genspark/Manus + Claude + Gamma",
        "combo": "Genspark/Manus + Claude + Gamma",
        "id_slug": "ppt-genspark-manus-claude-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Genspark",
            "Manus",
            "Claude",
            "Gamma"
        ],
        "steps": [
            "让代理先做网页调研和资料收集",
            "Claude 做去噪和观点排序",
            "Gamma 出简报"
        ],
        "workflow": "让代理先做网页调研和资料收集；Claude 做去噪和观点排序；Gamma 出简报。",
        "outputs": [
            "需要快调研的 BD/投资人"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Genspark/Manus + Claude + Gamma。工具分工：让代理先做网页调研和资料收集；Claude 做去噪和观点排序；Gamma 出简报。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "需要快调研的 BD/投资人"
    },
    {
        "num": "10",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Gemini + Google Workspace + Canva",
        "combo": "Gemini + Google Workspace + Canva",
        "id_slug": "ppt-gemini-google-workspace-canva",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Gemini",
            "Google Workspace",
            "Canva"
        ],
        "steps": [
            "Gemini 从 Docs/Sheets 摘要数据",
            "Canva 生成视觉稿",
            "ChatGPT/Claude 做文案润色"
        ],
        "workflow": "Gemini 从 Docs/Sheets 摘要数据；Canva 生成视觉稿；ChatGPT/Claude 做文案润色。",
        "outputs": [
            "Google Workspace 重度用户"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Gemini + Google Workspace + Canva。工具分工：Gemini 从 Docs/Sheets 摘要数据；Canva 生成视觉稿；ChatGPT/Claude 做文案润色。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "Google Workspace 重度用户"
    },
    {
        "num": "11",
        "scenario": "研究",
        "title": "研究：Perplexity + Claude",
        "combo": "Perplexity + Claude",
        "id_slug": "perplexity-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Perplexity",
            "Claude"
        ],
        "steps": [
            "Perplexity 搜索并给来源",
            "Claude 长上下文吸收资料，输出框架、洞察、反方观点和结论"
        ],
        "workflow": "Perplexity 搜索并给来源；Claude 长上下文吸收资料，输出框架、洞察、反方观点和结论。",
        "outputs": [
            "研究员、创作者、顾问"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Perplexity + Claude。工具分工：Perplexity 搜索并给来源；Claude 长上下文吸收资料，输出框架、洞察、反方观点和结论。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "研究员、创作者、顾问"
    },
    {
        "num": "12",
        "scenario": "研究",
        "title": "研究：ChatGPT Deep Research + Claude",
        "combo": "ChatGPT Deep Research + Claude",
        "id_slug": "chatgpt-deep-research-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "ChatGPT Deep Research",
            "Claude"
        ],
        "steps": [
            "ChatGPT 先做广域多源研究",
            "Claude 负责压缩、重排、写成更有人味的报告"
        ],
        "workflow": "ChatGPT 先做广域多源研究；Claude 负责压缩、重排、写成更有人味的报告。",
        "outputs": [
            "深度报告、白皮书"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：ChatGPT Deep Research + Claude。工具分工：ChatGPT 先做广域多源研究；Claude 负责压缩、重排、写成更有人味的报告。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "深度报告、白皮书"
    },
    {
        "num": "13",
        "scenario": "研究",
        "title": "研究：Perplexity + ChatGPT + Notion",
        "combo": "Perplexity + ChatGPT + Notion",
        "id_slug": "perplexity-chatgpt-notion",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Perplexity",
            "ChatGPT",
            "Notion"
        ],
        "steps": [
            "Perplexity 建引用清单",
            "ChatGPT 做问答/表格",
            "Notion 保存知识库与复用模板"
        ],
        "workflow": "Perplexity 建引用清单；ChatGPT 做问答/表格；Notion 保存知识库与复用模板。",
        "outputs": [
            "个人知识管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Perplexity + ChatGPT + Notion。工具分工：Perplexity 建引用清单；ChatGPT 做问答/表格；Notion 保存知识库与复用模板。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "个人知识管理"
    },
    {
        "num": "14",
        "scenario": "研究",
        "title": "研究：Claude + Notion AI",
        "combo": "Claude + Notion AI",
        "id_slug": "claude-notion-ai",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Claude",
            "Notion AI"
        ],
        "steps": [
            "Claude 做长文档理解和推理",
            "Notion AI 把结果嵌入项目页、任务页、数据库"
        ],
        "workflow": "Claude 做长文档理解和推理；Notion AI 把结果嵌入项目页、任务页、数据库。",
        "outputs": [
            "团队研究沉淀"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Claude + Notion AI。工具分工：Claude 做长文档理解和推理；Notion AI 把结果嵌入项目页、任务页、数据库。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "团队研究沉淀"
    },
    {
        "num": "15",
        "scenario": "研究",
        "title": "研究：NotebookLM + Gemini + Claude",
        "combo": "NotebookLM + Gemini + Claude",
        "id_slug": "notebooklm-gemini-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "NotebookLM",
            "Gemini",
            "Claude"
        ],
        "steps": [
            "NotebookLM 处理私有资料",
            "Gemini 补 Google 生态检索",
            "Claude 输出最终观点"
        ],
        "workflow": "NotebookLM 处理私有资料；Gemini 补 Google 生态检索；Claude 输出最终观点。",
        "outputs": [
            "学术/培训资料整理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：NotebookLM + Gemini + Claude。工具分工：NotebookLM 处理私有资料；Gemini 补 Google 生态检索；Claude 输出最终观点。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 94,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "学术/培训资料整理"
    },
    {
        "num": "16",
        "scenario": "研究",
        "title": "研究：ChatGPT + SharePoint connector",
        "combo": "ChatGPT + SharePoint connector",
        "id_slug": "chatgpt-sharepoint-connector",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "ChatGPT",
            "SharePoint connector"
        ],
        "steps": [
            "ChatGPT 从 SharePoint 找内部制度、历史报告、模板",
            "生成带出处的内部问答"
        ],
        "workflow": "ChatGPT 从 SharePoint 找内部制度、历史报告、模板；生成带出处的内部问答。",
        "outputs": [
            "大公司知识检索"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：ChatGPT + SharePoint connector。工具分工：ChatGPT 从 SharePoint 找内部制度、历史报告、模板；生成带出处的内部问答。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "大公司知识检索"
    },
    {
        "num": "17",
        "scenario": "研究",
        "title": "研究：Claude + Google Drive connector",
        "combo": "Claude + Google Drive connector",
        "id_slug": "claude-google-drive-connector",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Claude",
            "Google Drive connector"
        ],
        "steps": [
            "Claude 搜合同/文档/会议纪要，比较版本差异并生成行动项"
        ],
        "workflow": "Claude 搜合同/文档/会议纪要，比较版本差异并生成行动项。",
        "outputs": [
            "法务、运营、项目 PM"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Claude + Google Drive connector。工具分工：Claude 搜合同/文档/会议纪要，比较版本差异并生成行动项。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "法务、运营、项目 PM"
    },
    {
        "num": "18",
        "scenario": "研究",
        "title": "研究：Perplexity + Elicit + Claude",
        "combo": "Perplexity + Elicit + Claude",
        "id_slug": "perplexity-elicit-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Perplexity",
            "Elicit",
            "Claude"
        ],
        "steps": [
            "Perplexity 找现实资料",
            "Elicit 找论文",
            "Claude 做文献综述和研究假设"
        ],
        "workflow": "Perplexity 找现实资料；Elicit 找论文；Claude 做文献综述和研究假设。",
        "outputs": [
            "科研、医学/政策研究"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Perplexity + Elicit + Claude。工具分工：Perplexity 找现实资料；Elicit 找论文；Claude 做文献综述和研究假设。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "科研、医学/政策研究"
    },
    {
        "num": "19",
        "scenario": "研究",
        "title": "研究：ChatGPT + Consensus + Zotero",
        "combo": "ChatGPT + Consensus + Zotero",
        "id_slug": "chatgpt-consensus-zotero",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "ChatGPT",
            "Consensus",
            "Zotero"
        ],
        "steps": [
            "ChatGPT 生成问题树",
            "Consensus 查论文证据",
            "Zotero 管引用"
        ],
        "workflow": "ChatGPT 生成问题树；Consensus 查论文证据；Zotero 管引用。",
        "outputs": [
            "论文写作、证据型内容"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：ChatGPT + Consensus + Zotero。工具分工：ChatGPT 生成问题树；Consensus 查论文证据；Zotero 管引用。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "论文写作、证据型内容"
    },
    {
        "num": "20",
        "scenario": "研究",
        "title": "研究：Grok + Perplexity + Claude",
        "combo": "Grok + Perplexity + Claude",
        "id_slug": "grok-perplexity-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Grok",
            "Perplexity",
            "Claude"
        ],
        "steps": [
            "Grok 抓 X 实时舆情",
            "Perplexity 验证外部来源",
            "Claude 写洞察摘要"
        ],
        "workflow": "Grok 抓 X 实时舆情；Perplexity 验证外部来源；Claude 写洞察摘要。",
        "outputs": [
            "趋势研究、社媒分析"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Grok + Perplexity + Claude。工具分工：Grok 抓 X 实时舆情；Perplexity 验证外部来源；Claude 写洞察摘要。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "趋势研究、社媒分析"
    },
    {
        "num": "21",
        "scenario": "写作",
        "title": "写作：Claude + Grammarly",
        "combo": "Claude + Grammarly",
        "id_slug": "claude-grammarly",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Grammarly"
        ],
        "steps": [
            "Claude 起草长文和结构",
            "Grammarly 做语法、语气、清晰度 QA"
        ],
        "workflow": "Claude 起草长文和结构；Grammarly 做语法、语气、清晰度 QA。",
        "outputs": [
            "英文博客、邮件、方案"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Claude + Grammarly。工具分工：Claude 起草长文和结构；Grammarly 做语法、语气、清晰度 QA。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "英文博客、邮件、方案"
    },
    {
        "num": "22",
        "scenario": "写作",
        "title": "写作：ChatGPT + Claude",
        "combo": "ChatGPT + Claude",
        "id_slug": "chatgpt-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Claude"
        ],
        "steps": [
            "ChatGPT 发散选题和角度",
            "Claude 统一成稳定语气、长文结构和精修稿"
        ],
        "workflow": "ChatGPT 发散选题和角度；Claude 统一成稳定语气、长文结构和精修稿。",
        "outputs": [
            "创作者、品牌内容"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：ChatGPT + Claude。工具分工：ChatGPT 发散选题和角度；Claude 统一成稳定语气、长文结构和精修稿。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "创作者、品牌内容"
    },
    {
        "num": "23",
        "scenario": "写作",
        "title": "写作：Perplexity + Claude + Substack",
        "combo": "Perplexity + Claude + Substack",
        "id_slug": "perplexity-claude-substack",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Perplexity",
            "Claude",
            "Substack"
        ],
        "steps": [
            "Perplexity 找素材",
            "Claude 写 newsletter",
            "Substack 发布并复盘数据"
        ],
        "workflow": "Perplexity 找素材；Claude 写 newsletter；Substack 发布并复盘数据。",
        "outputs": [
            "newsletter 作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Perplexity + Claude + Substack。工具分工：Perplexity 找素材；Claude 写 newsletter；Substack 发布并复盘数据。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "newsletter 作者"
    },
    {
        "num": "24",
        "scenario": "写作",
        "title": "写作：Claude custom style + Notion",
        "combo": "Claude custom style + Notion",
        "id_slug": "claude-custom-style-notion",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude custom style",
            "Notion"
        ],
        "steps": [
            "Claude 学习个人写作样本",
            "Notion 管选题库、草稿和发布状态"
        ],
        "workflow": "Claude 学习个人写作样本；Notion 管选题库、草稿和发布状态。",
        "outputs": [
            "个人 IP、CEO ghostwriting"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Claude custom style + Notion。工具分工：Claude 学习个人写作样本；Notion 管选题库、草稿和发布状态。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "个人 IP、CEO ghostwriting"
    },
    {
        "num": "25",
        "scenario": "写作",
        "title": "写作：ChatGPT + Hemingway/LanguageTool",
        "combo": "ChatGPT + Hemingway/LanguageTool",
        "id_slug": "chatgpt-hemingway-languagetool",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Hemingway",
            "LanguageTool"
        ],
        "steps": [
            "ChatGPT 快速起草",
            "Hemingway 或 LanguageTool 控制可读性和错误"
        ],
        "workflow": "ChatGPT 快速起草；Hemingway 或 LanguageTool 控制可读性和错误。",
        "outputs": [
            "短文、官网文案"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：ChatGPT + Hemingway/LanguageTool。工具分工：ChatGPT 快速起草；Hemingway 或 LanguageTool 控制可读性和错误。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "短文、官网文案"
    },
    {
        "num": "26",
        "scenario": "写作",
        "title": "写作：Claude + Readwise + Obsidian",
        "combo": "Claude + Readwise + Obsidian",
        "id_slug": "claude-readwise-obsidian",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Readwise",
            "Obsidian"
        ],
        "steps": [
            "Readwise 收集高亮信息",
            "Obsidian 建本地知识库",
            "Claude 生成文章/脚本"
        ],
        "workflow": "Readwise 收集高亮信息；Obsidian 建本地知识库；Claude 生成文章/脚本。",
        "outputs": [
            "深度创作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Claude + Readwise + Obsidian。工具分工：Readwise 收集高亮信息；Obsidian 建本地知识库；Claude 生成文章/脚本。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "深度创作者"
    },
    {
        "num": "27",
        "scenario": "写作",
        "title": "写作：ChatGPT + Jasper/Copy.ai",
        "combo": "ChatGPT + Jasper/Copy.ai",
        "id_slug": "chatgpt-jasper-copy-ai",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Jasper",
            "Copy.ai"
        ],
        "steps": [
            "ChatGPT 做定位和产品卖点",
            "Jasper/Copy.ai 批量生成广告版本"
        ],
        "workflow": "ChatGPT 做定位和产品卖点；Jasper/Copy.ai 批量生成广告版本。",
        "outputs": [
            "投放、增长团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：ChatGPT + Jasper/Copy.ai。工具分工：ChatGPT 做定位和产品卖点；Jasper/Copy.ai 批量生成广告版本。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "投放、增长团队"
    },
    {
        "num": "28",
        "scenario": "写作",
        "title": "写作：Claude + Google Docs",
        "combo": "Claude + Google Docs",
        "id_slug": "claude-google-docs",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Google Docs"
        ],
        "steps": [
            "Claude 负责结构和改写",
            "Docs 负责协作评论、版本控制和交付"
        ],
        "workflow": "Claude 负责结构和改写；Docs 负责协作评论、版本控制和交付。",
        "outputs": [
            "团队文档协作"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Claude + Google Docs。工具分工：Claude 负责结构和改写；Docs 负责协作评论、版本控制和交付。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "团队文档协作"
    },
    {
        "num": "29",
        "scenario": "写作",
        "title": "写作：ChatGPT voice + Claude",
        "combo": "ChatGPT voice + Claude",
        "id_slug": "chatgpt-voice-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT voice",
            "Claude"
        ],
        "steps": [
            "ChatGPT 语音记录想法",
            "Claude 把口述内容重构成文章/方案"
        ],
        "workflow": "ChatGPT 语音记录想法；Claude 把口述内容重构成文章/方案。",
        "outputs": [
            "移动办公、创始人"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：ChatGPT voice + Claude。工具分工：ChatGPT 语音记录想法；Claude 把口述内容重构成文章/方案。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "移动办公、创始人"
    },
    {
        "num": "30",
        "scenario": "写作",
        "title": "写作：Perplexity Pages + Claude",
        "combo": "Perplexity Pages + Claude",
        "id_slug": "perplexity-pages-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Perplexity Pages",
            "Claude"
        ],
        "steps": [
            "Perplexity Pages 做信息页雏形",
            "Claude 改成观点型长文"
        ],
        "workflow": "Perplexity Pages 做信息页雏形；Claude 改成观点型长文。",
        "outputs": [
            "SEO、教育内容"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Perplexity Pages + Claude。工具分工：Perplexity Pages 做信息页雏形；Claude 改成观点型长文。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "SEO、教育内容"
    },
    {
        "num": "31",
        "scenario": "社媒",
        "title": "社媒：Claude + OpenTweet",
        "combo": "Claude + OpenTweet",
        "id_slug": "claude-opentweet",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "OpenTweet"
        ],
        "steps": [
            "Claude 学习声音、批量生成推文",
            "OpenTweet 排程、循环 evergreen 内容、回收 analytics"
        ],
        "workflow": "Claude 学习声音、批量生成推文；OpenTweet 排程、循环 evergreen 内容、回收 analytics。",
        "outputs": [
            "X/Twitter 创作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Claude + OpenTweet。工具分工：Claude 学习声音、批量生成推文；OpenTweet 排程、循环 evergreen 内容、回收 analytics。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 93,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "X/Twitter 创作者"
    },
    {
        "num": "32",
        "scenario": "社媒",
        "title": "社媒：Grok + ChatGPT",
        "combo": "Grok + ChatGPT",
        "id_slug": "grok-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Grok",
            "ChatGPT"
        ],
        "steps": [
            "Grok 看 X 热点和评论语境",
            "ChatGPT 生成多平台短帖版本"
        ],
        "workflow": "Grok 看 X 热点和评论语境；ChatGPT 生成多平台短帖版本。",
        "outputs": [
            "热点运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Grok + ChatGPT。工具分工：Grok 看 X 热点和评论语境；ChatGPT 生成多平台短帖版本。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "热点运营"
    },
    {
        "num": "33",
        "scenario": "社媒",
        "title": "社媒：Perplexity + Claude + Buffer",
        "combo": "Perplexity + Claude + Buffer",
        "id_slug": "perplexity-claude-buffer",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Perplexity",
            "Claude",
            "Buffer"
        ],
        "steps": [
            "Perplexity 找资料",
            "Claude 写系列帖",
            "Buffer 排程到 LinkedIn/X"
        ],
        "workflow": "Perplexity 找资料；Claude 写系列帖；Buffer 排程到 LinkedIn/X。",
        "outputs": [
            "B2B 内容"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Perplexity + Claude + Buffer。工具分工：Perplexity 找资料；Claude 写系列帖；Buffer 排程到 LinkedIn/X。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "B2B 内容"
    },
    {
        "num": "34",
        "scenario": "社媒",
        "title": "社媒：ChatGPT + Canva + Later",
        "combo": "ChatGPT + Canva + Later",
        "id_slug": "chatgpt-canva-later",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Canva",
            "Later"
        ],
        "steps": [
            "ChatGPT 生成图文脚本",
            "Canva 做视觉",
            "Later 排程 Instagram/LinkedIn"
        ],
        "workflow": "ChatGPT 生成图文脚本；Canva 做视觉；Later 排程 Instagram/LinkedIn。",
        "outputs": [
            "品牌社媒"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：ChatGPT + Canva + Later。工具分工：ChatGPT 生成图文脚本；Canva 做视觉；Later 排程 Instagram/LinkedIn。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "品牌社媒"
    },
    {
        "num": "35",
        "scenario": "社媒",
        "title": "社媒：Claude + Hypefury/Tweethunter",
        "combo": "Claude + Hypefury/Tweethunter",
        "id_slug": "claude-hypefury-tweethunter",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "Hypefury",
            "Tweethunter"
        ],
        "steps": [
            "Claude 写 thread 和 hooks",
            "工具排程、复用、分析爆款"
        ],
        "workflow": "Claude 写 thread 和 hooks；工具排程、复用、分析爆款。",
        "outputs": [
            "X 增长"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Claude + Hypefury/Tweethunter。工具分工：Claude 写 thread 和 hooks；工具排程、复用、分析爆款。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "X 增长"
    },
    {
        "num": "36",
        "scenario": "社媒",
        "title": "社媒：OpusClip + ChatGPT + CapCut",
        "combo": "OpusClip + ChatGPT + CapCut",
        "id_slug": "opusclip-chatgpt-capcut",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "OpusClip",
            "ChatGPT",
            "CapCut"
        ],
        "steps": [
            "OpusClip 切长视频",
            "ChatGPT 写标题/描述",
            "CapCut 精修字幕和节奏"
        ],
        "workflow": "OpusClip 切长视频；ChatGPT 写标题/描述；CapCut 精修字幕和节奏。",
        "outputs": [
            "短视频团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：OpusClip + ChatGPT + CapCut。工具分工：OpusClip 切长视频；ChatGPT 写标题/描述；CapCut 精修字幕和节奏。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "短视频团队"
    },
    {
        "num": "37",
        "scenario": "社媒",
        "title": "社媒：Descript + Claude + YouTube Studio",
        "combo": "Descript + Claude + YouTube Studio",
        "id_slug": "descript-claude-youtube-studio",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Descript",
            "Claude",
            "YouTube Studio"
        ],
        "steps": [
            "Descript 转写剪辑",
            "Claude 生成章节、标题、简介",
            "YouTube Studio 发布"
        ],
        "workflow": "Descript 转写剪辑；Claude 生成章节、标题、简介；YouTube Studio 发布。",
        "outputs": [
            "播客/视频号"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Descript + Claude + YouTube Studio。工具分工：Descript 转写剪辑；Claude 生成章节、标题、简介；YouTube Studio 发布。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "播客/视频号"
    },
    {
        "num": "38",
        "scenario": "社媒",
        "title": "社媒：ChatGPT + Midjourney + Canva",
        "combo": "ChatGPT + Midjourney + Canva",
        "id_slug": "chatgpt-midjourney-canva",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Midjourney",
            "Canva"
        ],
        "steps": [
            "ChatGPT 生成视觉 brief",
            "Midjourney 出主图",
            "Canva 适配多平台尺寸"
        ],
        "workflow": "ChatGPT 生成视觉 brief；Midjourney 出主图；Canva 适配多平台尺寸。",
        "outputs": [
            "活动海报、广告素材"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：ChatGPT + Midjourney + Canva。工具分工：ChatGPT 生成视觉 brief；Midjourney 出主图；Canva 适配多平台尺寸。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "活动海报、广告素材"
    },
    {
        "num": "39",
        "scenario": "社媒",
        "title": "社媒：Claude + Taplio",
        "combo": "Claude + Taplio",
        "id_slug": "claude-taplio",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "Taplio"
        ],
        "steps": [
            "Claude 写 LinkedIn 长帖和评论回复",
            "Taplio 做排程和表现复盘"
        ],
        "workflow": "Claude 写 LinkedIn 长帖和评论回复；Taplio 做排程和表现复盘。",
        "outputs": [
            "LinkedIn 个人品牌"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Claude + Taplio。工具分工：Claude 写 LinkedIn 长帖和评论回复；Taplio 做排程和表现复盘。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "LinkedIn 个人品牌"
    },
    {
        "num": "40",
        "scenario": "社媒",
        "title": "社媒：Grok + Perplexity + Notion",
        "combo": "Grok + Perplexity + Notion",
        "id_slug": "grok-perplexity-notion",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Grok",
            "Perplexity",
            "Notion"
        ],
        "steps": [
            "Grok 监控实时讨论",
            "Perplexity 补证据",
            "Notion 建选题雷达"
        ],
        "workflow": "Grok 监控实时讨论；Perplexity 补证据；Notion 建选题雷达。",
        "outputs": [
            "趋势型账号"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Grok + Perplexity + Notion。工具分工：Grok 监控实时讨论；Perplexity 补证据；Notion 建选题雷达。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "趋势型账号"
    },
    {
        "num": "41",
        "scenario": "编程",
        "title": "编程：Cursor + Claude",
        "combo": "Cursor + Claude",
        "id_slug": "cursor-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Cursor",
            "Claude"
        ],
        "steps": [
            "Cursor 负责多文件编辑和 diff",
            "Claude 负责架构推理、复杂 bug、重构计划"
        ],
        "workflow": "Cursor 负责多文件编辑和 diff；Claude 负责架构推理、复杂 bug、重构计划。",
        "outputs": [
            "全栈开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Cursor + Claude。工具分工：Cursor 负责多文件编辑和 diff；Claude 负责架构推理、复杂 bug、重构计划。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "全栈开发者"
    },
    {
        "num": "42",
        "scenario": "编程",
        "title": "编程：Claude Code + GitHub",
        "combo": "Claude Code + GitHub",
        "id_slug": "claude-code-github",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Claude Code",
            "GitHub"
        ],
        "steps": [
            "Claude Code 读 repo、改代码、跑测试",
            "GitHub PR 承载审查和合并"
        ],
        "workflow": "Claude Code 读 repo、改代码、跑测试；GitHub PR 承载审查和合并。",
        "outputs": [
            "工程团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Claude Code + GitHub。工具分工：Claude Code 读 repo、改代码、跑测试；GitHub PR 承载审查和合并。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "工程团队"
    },
    {
        "num": "43",
        "scenario": "编程",
        "title": "编程：ChatGPT/Codex + GitHub",
        "combo": "ChatGPT/Codex + GitHub",
        "id_slug": "chatgpt-codex-github",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "ChatGPT",
            "Codex",
            "GitHub"
        ],
        "steps": [
            "Codex 处理 issue 到 PR 的实现",
            "ChatGPT 帮忙解释方案、生成测试和文档"
        ],
        "workflow": "Codex 处理 issue 到 PR 的实现；ChatGPT 帮忙解释方案、生成测试和文档。",
        "outputs": [
            "产品工程"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：ChatGPT/Codex + GitHub。工具分工：Codex 处理 issue 到 PR 的实现；ChatGPT 帮忙解释方案、生成测试和文档。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品工程"
    },
    {
        "num": "44",
        "scenario": "编程",
        "title": "编程：GitHub Copilot + Claude",
        "combo": "GitHub Copilot + Claude",
        "id_slug": "github-copilot-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "GitHub Copilot",
            "Claude"
        ],
        "steps": [
            "Copilot 在 IDE 补全和小改",
            "Claude 处理大上下文设计和代码审稿"
        ],
        "workflow": "Copilot 在 IDE 补全和小改；Claude 处理大上下文设计和代码审稿。",
        "outputs": [
            "需要稳定 IDE 集成的团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：GitHub Copilot + Claude。工具分工：Copilot 在 IDE 补全和小改；Claude 处理大上下文设计和代码审稿。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "需要稳定 IDE 集成的团队"
    },
    {
        "num": "45",
        "scenario": "编程",
        "title": "编程：Cursor + ChatGPT 5.x",
        "combo": "Cursor + ChatGPT 5.x",
        "id_slug": "cursor-chatgpt-5-x",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Cursor",
            "ChatGPT"
        ],
        "steps": [
            "Cursor 负责上下文编辑",
            "ChatGPT 做困难算法、调试思路、单测用例"
        ],
        "workflow": "Cursor 负责上下文编辑；ChatGPT 做困难算法、调试思路、单测用例。",
        "outputs": [
            "算法/后端工程"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Cursor + ChatGPT 5.x。工具分工：Cursor 负责上下文编辑；ChatGPT 做困难算法、调试思路、单测用例。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "算法/后端工程"
    },
    {
        "num": "46",
        "scenario": "编程",
        "title": "编程：Claude Code + ccusage + CLAUDE.md",
        "combo": "Claude Code + ccusage + CLAUDE.md",
        "id_slug": "claude-code-ccusage-claude-md",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Claude Code",
            "ccusage",
            "CLAUDE.md"
        ],
        "steps": [
            "用 CLAUDE.md 约束项目规则",
            "ccusage 监控成本",
            "Claude Code 执行任务"
        ],
        "workflow": "用 CLAUDE.md 约束项目规则；ccusage 监控成本；Claude Code 执行任务。",
        "outputs": [
            "控制 token 成本的开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Claude Code + ccusage + CLAUDE.md。工具分工：用 CLAUDE.md 约束项目规则；ccusage 监控成本；Claude Code 执行任务。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "控制 token 成本的开发者"
    },
    {
        "num": "47",
        "scenario": "编程",
        "title": "编程：Claude Code + subagents + hooks",
        "combo": "Claude Code + subagents + hooks",
        "id_slug": "claude-code-subagents-hooks",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Claude Code",
            "subagents",
            "hooks"
        ],
        "steps": [
            "主 agent 分解任务",
            "子 agent 并行查找/实现/审查",
            "hooks 做安全和质量门禁"
        ],
        "workflow": "主 agent 分解任务；子 agent 并行查找/实现/审查；hooks 做安全和质量门禁。",
        "outputs": [
            "复杂代码库"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Claude Code + subagents + hooks。工具分工：主 agent 分解任务；子 agent 并行查找/实现/审查；hooks 做安全和质量门禁。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 92,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "复杂代码库"
    },
    {
        "num": "48",
        "scenario": "编程",
        "title": "编程：Codex + Claude Code",
        "combo": "Codex + Claude Code",
        "id_slug": "codex-claude-code",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Codex",
            "Claude Code"
        ],
        "steps": [
            "Codex 做 OpenAI 生态/桌面任务",
            "Claude Code 处理长上下文和重构",
            "互相审稿"
        ],
        "workflow": "Codex 做 OpenAI 生态/桌面任务；Claude Code 处理长上下文和重构；互相审稿。",
        "outputs": [
            "双模型交叉验证"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Codex + Claude Code。工具分工：Codex 做 OpenAI 生态/桌面任务；Claude Code 处理长上下文和重构；互相审稿。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "双模型交叉验证"
    },
    {
        "num": "49",
        "scenario": "编程",
        "title": "编程：Replit + ChatGPT",
        "combo": "Replit + ChatGPT",
        "id_slug": "replit-chatgpt",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Replit",
            "ChatGPT"
        ],
        "steps": [
            "Replit 快速搭云端原型",
            "ChatGPT 生成需求、调试和部署说明"
        ],
        "workflow": "Replit 快速搭云端原型；ChatGPT 生成需求、调试和部署说明。",
        "outputs": [
            "非专业开发者、黑客松"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Replit + ChatGPT。工具分工：Replit 快速搭云端原型；ChatGPT 生成需求、调试和部署说明。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "非专业开发者、黑客松"
    },
    {
        "num": "50",
        "scenario": "编程",
        "title": "编程：Lovable/Bolt + Claude",
        "combo": "Lovable/Bolt + Claude",
        "id_slug": "lovable-bolt-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Lovable",
            "Bolt",
            "Claude"
        ],
        "steps": [
            "Lovable/Bolt 生成前端原型",
            "Claude 审查业务逻辑、状态和安全风险"
        ],
        "workflow": "Lovable/Bolt 生成前端原型；Claude 审查业务逻辑、状态和安全风险。",
        "outputs": [
            "MVP 快速验证"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Lovable/Bolt + Claude。工具分工：Lovable/Bolt 生成前端原型；Claude 审查业务逻辑、状态和安全风险。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "MVP 快速验证"
    },
    {
        "num": "51",
        "scenario": "编程",
        "title": "编程：v0 + Cursor + Claude",
        "combo": "v0 + Cursor + Claude",
        "id_slug": "v0-cursor-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "v0",
            "Cursor",
            "Claude"
        ],
        "steps": [
            "v0 出 UI",
            "Cursor 接入项目并改文件",
            "Claude 做产品逻辑和代码审查"
        ],
        "workflow": "v0 出 UI；Cursor 接入项目并改文件；Claude 做产品逻辑和代码审查。",
        "outputs": [
            "SaaS 前端"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：v0 + Cursor + Claude。工具分工：v0 出 UI；Cursor 接入项目并改文件；Claude 做产品逻辑和代码审查。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "SaaS 前端"
    },
    {
        "num": "52",
        "scenario": "编程",
        "title": "编程：Windsurf + Claude",
        "combo": "Windsurf + Claude",
        "id_slug": "windsurf-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Windsurf",
            "Claude"
        ],
        "steps": [
            "Windsurf 做 agentic IDE 流程",
            "Claude 负责解释、规划、复杂改造"
        ],
        "workflow": "Windsurf 做 agentic IDE 流程；Claude 负责解释、规划、复杂改造。",
        "outputs": [
            "IDE-first 开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Windsurf + Claude。工具分工：Windsurf 做 agentic IDE 流程；Claude 负责解释、规划、复杂改造。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "IDE-first 开发者"
    },
    {
        "num": "53",
        "scenario": "编程",
        "title": "编程：OpenCode + Ollama/Kimi + Claude",
        "combo": "OpenCode + Ollama/Kimi + Claude",
        "id_slug": "opencode-ollama-kimi-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "OpenCode",
            "Ollama",
            "Kimi",
            "Claude"
        ],
        "steps": [
            "OpenCode 跑开源/低成本模型",
            "Claude 处理关键难题",
            "保留隐私和成本弹性"
        ],
        "workflow": "OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。",
        "outputs": [
            "开源/本地优先团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：OpenCode + Ollama/Kimi + Claude。工具分工：OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "开源/本地优先团队"
    },
    {
        "num": "54",
        "scenario": "编程",
        "title": "编程：Scion + Claude/Gemini/Codex",
        "combo": "Scion + Claude/Gemini/Codex",
        "id_slug": "scion-claude-gemini-codex",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Scion",
            "Claude",
            "Gemini",
            "Codex"
        ],
        "steps": [
            "Scion 用容器和 git worktree 隔离多 agent",
            "不同模型并行做功能"
        ],
        "workflow": "Scion 用容器和 git worktree 隔离多 agent；不同模型并行做功能。",
        "outputs": [
            "多 agent 实验团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Scion + Claude/Gemini/Codex。工具分工：Scion 用容器和 git worktree 隔离多 agent；不同模型并行做功能。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "多 agent 实验团队"
    },
    {
        "num": "55",
        "scenario": "编程",
        "title": "编程：Paseo + Claude Code + Codex + OpenCode",
        "combo": "Paseo + Claude Code + Codex + OpenCode",
        "id_slug": "paseo-claude-code-codex-opencode",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Paseo",
            "Claude Code",
            "Codex",
            "OpenCode"
        ],
        "steps": [
            "Paseo 统一管理多个 coding agent，减少复制粘贴和上下文断裂"
        ],
        "workflow": "Paseo 统一管理多个 coding agent，减少复制粘贴和上下文断裂。",
        "outputs": [
            "多模型开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Paseo + Claude Code + Codex + OpenCode。工具分工：Paseo 统一管理多个 coding agent，减少复制粘贴和上下文断裂。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "多模型开发者"
    },
    {
        "num": "56",
        "scenario": "编程",
        "title": "编程：AgentAuditKit + Claude Code",
        "combo": "AgentAuditKit + Claude Code",
        "id_slug": "agentauditkit-claude-code",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "AgentAuditKit",
            "Claude Code"
        ],
        "steps": [
            "Claude Code 写代码",
            "AgentAuditKit 本地扫描 prompt/tool/secret 风险"
        ],
        "workflow": "Claude Code 写代码；AgentAuditKit 本地扫描 prompt/tool/secret 风险。",
        "outputs": [
            "AI agent 安全"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：AgentAuditKit + Claude Code。工具分工：Claude Code 写代码；AgentAuditKit 本地扫描 prompt/tool/secret 风险。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "AI agent 安全"
    },
    {
        "num": "57",
        "scenario": "编程",
        "title": "编程：Snyk/Socket + Copilot/Claude",
        "combo": "Snyk/Socket + Copilot/Claude",
        "id_slug": "snyk-socket-copilot-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Snyk",
            "Socket",
            "Copilot",
            "Claude"
        ],
        "steps": [
            "AI 写依赖和代码",
            "Snyk/Socket 查漏洞、恶意包和许可证"
        ],
        "workflow": "AI 写依赖和代码；Snyk/Socket 查漏洞、恶意包和许可证。",
        "outputs": [
            "供应链安全"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Snyk/Socket + Copilot/Claude。工具分工：AI 写依赖和代码；Snyk/Socket 查漏洞、恶意包和许可证。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "供应链安全"
    },
    {
        "num": "58",
        "scenario": "编程",
        "title": "编程：Linear + ChatGPT/Codex",
        "combo": "Linear + ChatGPT/Codex",
        "id_slug": "linear-chatgpt-codex",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Linear",
            "ChatGPT",
            "Codex"
        ],
        "steps": [
            "Linear issue 自动生成实现计划",
            "Codex 实现",
            "ChatGPT 生成验收标准"
        ],
        "workflow": "Linear issue 自动生成实现计划；Codex 实现；ChatGPT 生成验收标准。",
        "outputs": [
            "产品研发闭环"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Linear + ChatGPT/Codex。工具分工：Linear issue 自动生成实现计划；Codex 实现；ChatGPT 生成验收标准。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品研发闭环"
    },
    {
        "num": "59",
        "scenario": "编程",
        "title": "编程：Jira + Claude + GitHub",
        "combo": "Jira + Claude + GitHub",
        "id_slug": "jira-claude-github",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Jira",
            "Claude",
            "GitHub"
        ],
        "steps": [
            "Claude 从 Jira 需求生成技术方案",
            "GitHub PR 关联 issue",
            "Claude 审稿"
        ],
        "workflow": "Claude 从 Jira 需求生成技术方案；GitHub PR 关联 issue；Claude 审稿。",
        "outputs": [
            "企业研发"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Jira + Claude + GitHub。工具分工：Claude 从 Jira 需求生成技术方案；GitHub PR 关联 issue；Claude 审稿。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "企业研发"
    },
    {
        "num": "60",
        "scenario": "编程",
        "title": "编程：Databricks Genie + Claude",
        "combo": "Databricks Genie + Claude",
        "id_slug": "databricks-genie-claude",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Databricks Genie",
            "Claude"
        ],
        "steps": [
            "Genie 用自然语言处理数据管道/Spark",
            "Claude 写解释、文档和异常分析"
        ],
        "workflow": "Genie 用自然语言处理数据管道/Spark；Claude 写解释、文档和异常分析。",
        "outputs": [
            "数据工程"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Databricks Genie + Claude。工具分工：Genie 用自然语言处理数据管道/Spark；Claude 写解释、文档和异常分析。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "数据工程"
    },
    {
        "num": "61",
        "scenario": "数据",
        "title": "数据：ChatGPT Advanced Data Analysis + Sheets",
        "combo": "ChatGPT Advanced Data Analysis + Sheets",
        "id_slug": "chatgpt-advanced-data-analysis-sheets",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT Advanced Data Analysis",
            "Sheets"
        ],
        "steps": [
            "上传 CSV/Excel 到 ChatGPT 做清洗、透视和图表",
            "结果回写 Sheets"
        ],
        "workflow": "上传 CSV/Excel 到 ChatGPT 做清洗、透视和图表；结果回写 Sheets。",
        "outputs": [
            "运营分析"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：ChatGPT Advanced Data Analysis + Sheets。工具分工：上传 CSV/Excel 到 ChatGPT 做清洗、透视和图表；结果回写 Sheets。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "运营分析"
    },
    {
        "num": "62",
        "scenario": "数据",
        "title": "数据：Claude + Excel connector",
        "combo": "Claude + Excel connector",
        "id_slug": "claude-excel-connector",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "Excel connector"
        ],
        "steps": [
            "Claude 读取工作簿、解释公式和风险",
            "Excel 负责最终模型和审阅"
        ],
        "workflow": "Claude 读取工作簿、解释公式和风险；Excel 负责最终模型和审阅。",
        "outputs": [
            "财务分析"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Claude + Excel connector。工具分工：Claude 读取工作簿、解释公式和风险；Excel 负责最终模型和审阅。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "财务分析"
    },
    {
        "num": "63",
        "scenario": "数据",
        "title": "数据：Perplexity + ChatGPT ADA",
        "combo": "Perplexity + ChatGPT ADA",
        "id_slug": "perplexity-chatgpt-ada",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Perplexity",
            "ChatGPT ADA"
        ],
        "steps": [
            "Perplexity 找外部指标",
            "ChatGPT 做数据处理和可视化"
        ],
        "workflow": "Perplexity 找外部指标；ChatGPT 做数据处理和可视化。",
        "outputs": [
            "市场/投资研究"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Perplexity + ChatGPT ADA。工具分工：Perplexity 找外部指标；ChatGPT 做数据处理和可视化。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 91,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "市场/投资研究"
    },
    {
        "num": "64",
        "scenario": "数据",
        "title": "数据：Notion database + Claude",
        "combo": "Notion database + Claude",
        "id_slug": "notion-database-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Notion database",
            "Claude"
        ],
        "steps": [
            "Notion 管项目/客户数据",
            "Claude 按条件生成周报、风险清单和下一步"
        ],
        "workflow": "Notion 管项目/客户数据；Claude 按条件生成周报、风险清单和下一步。",
        "outputs": [
            "运营管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Notion database + Claude。工具分工：Notion 管项目/客户数据；Claude 按条件生成周报、风险清单和下一步。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "运营管理"
    },
    {
        "num": "65",
        "scenario": "数据",
        "title": "数据：Airtable + Zapier AI + ChatGPT",
        "combo": "Airtable + Zapier AI + ChatGPT",
        "id_slug": "airtable-zapier-ai-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Airtable",
            "Zapier AI",
            "ChatGPT"
        ],
        "steps": [
            "Airtable 存结构化数据",
            "Zapier 触发",
            "ChatGPT 生成摘要/邮件/任务"
        ],
        "workflow": "Airtable 存结构化数据；Zapier 触发；ChatGPT 生成摘要/邮件/任务。",
        "outputs": [
            "销售运营、CRM"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Airtable + Zapier AI + ChatGPT。工具分工：Airtable 存结构化数据；Zapier 触发；ChatGPT 生成摘要/邮件/任务。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售运营、CRM"
    },
    {
        "num": "66",
        "scenario": "数据",
        "title": "数据：BigQuery + Gemini + Looker",
        "combo": "BigQuery + Gemini + Looker",
        "id_slug": "bigquery-gemini-looker",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "BigQuery",
            "Gemini",
            "Looker"
        ],
        "steps": [
            "Gemini 帮写 SQL/解释指标",
            "Looker 做仪表盘"
        ],
        "workflow": "Gemini 帮写 SQL/解释指标；Looker 做仪表盘。",
        "outputs": [
            "数据团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：BigQuery + Gemini + Looker。工具分工：Gemini 帮写 SQL/解释指标；Looker 做仪表盘。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "数据团队"
    },
    {
        "num": "67",
        "scenario": "数据",
        "title": "数据：Snowflake Cortex + Claude/ChatGPT",
        "combo": "Snowflake Cortex + Claude/ChatGPT",
        "id_slug": "snowflake-cortex-claude-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Snowflake Cortex",
            "Claude",
            "ChatGPT"
        ],
        "steps": [
            "Snowflake 内做企业数据 AI",
            "Claude/ChatGPT 写解释和业务行动建议"
        ],
        "workflow": "Snowflake 内做企业数据 AI；Claude/ChatGPT 写解释和业务行动建议。",
        "outputs": [
            "企业 BI"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Snowflake Cortex + Claude/ChatGPT。工具分工：Snowflake 内做企业数据 AI；Claude/ChatGPT 写解释和业务行动建议。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "企业 BI"
    },
    {
        "num": "68",
        "scenario": "数据",
        "title": "数据：Power BI Copilot + ChatGPT",
        "combo": "Power BI Copilot + ChatGPT",
        "id_slug": "power-bi-copilot-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Power BI Copilot",
            "ChatGPT"
        ],
        "steps": [
            "Power BI Copilot 建报表",
            "ChatGPT 生成高管摘要和故事线"
        ],
        "workflow": "Power BI Copilot 建报表；ChatGPT 生成高管摘要和故事线。",
        "outputs": [
            "管理汇报"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Power BI Copilot + ChatGPT。工具分工：Power BI Copilot 建报表；ChatGPT 生成高管摘要和故事线。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "管理汇报"
    },
    {
        "num": "69",
        "scenario": "数据",
        "title": "数据：Rows + ChatGPT",
        "combo": "Rows + ChatGPT",
        "id_slug": "rows-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Rows",
            "ChatGPT"
        ],
        "steps": [
            "Rows 把电子表格和 API 结合",
            "ChatGPT 做公式、摘要、批量文案"
        ],
        "workflow": "Rows 把电子表格和 API 结合；ChatGPT 做公式、摘要、批量文案。",
        "outputs": [
            "轻量增长分析"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Rows + ChatGPT。工具分工：Rows 把电子表格和 API 结合；ChatGPT 做公式、摘要、批量文案。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "轻量增长分析"
    },
    {
        "num": "70",
        "scenario": "数据",
        "title": "数据：Julius AI + Claude",
        "combo": "Julius AI + Claude",
        "id_slug": "julius-ai-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Julius AI",
            "Claude"
        ],
        "steps": [
            "Julius 做数据探索",
            "Claude 解释洞察、生成报告和下一步实验"
        ],
        "workflow": "Julius 做数据探索；Claude 解释洞察、生成报告和下一步实验。",
        "outputs": [
            "非技术分析者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Julius AI + Claude。工具分工：Julius 做数据探索；Claude 解释洞察、生成报告和下一步实验。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "非技术分析者"
    },
    {
        "num": "71",
        "scenario": "会议",
        "title": "会议：Fireflies/Otter + Claude",
        "combo": "Fireflies/Otter + Claude",
        "id_slug": "fireflies-otter-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Fireflies",
            "Otter",
            "Claude"
        ],
        "steps": [
            "会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件"
        ],
        "workflow": "会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件。",
        "outputs": [
            "项目经理、销售"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Fireflies/Otter + Claude。工具分工：会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "项目经理、销售"
    },
    {
        "num": "72",
        "scenario": "会议",
        "title": "会议：ChatGPT record mode + Notion",
        "combo": "ChatGPT record mode + Notion",
        "id_slug": "chatgpt-record-mode-notion",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT record mode",
            "Notion"
        ],
        "steps": [
            "ChatGPT 记录/总结会议",
            "Notion 建任务页和纪要库"
        ],
        "workflow": "ChatGPT 记录/总结会议；Notion 建任务页和纪要库。",
        "outputs": [
            "创业团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：ChatGPT record mode + Notion。工具分工：ChatGPT 记录/总结会议；Notion 建任务页和纪要库。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "创业团队"
    },
    {
        "num": "73",
        "scenario": "会议",
        "title": "会议：Tactiq + Notion AI",
        "combo": "Tactiq + Notion AI",
        "id_slug": "tactiq-notion-ai",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Tactiq",
            "Notion AI"
        ],
        "steps": [
            "Tactiq 获取会议转写",
            "Notion AI 按模板沉淀客户/项目记录"
        ],
        "workflow": "Tactiq 获取会议转写；Notion AI 按模板沉淀客户/项目记录。",
        "outputs": [
            "客户成功"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Tactiq + Notion AI。工具分工：Tactiq 获取会议转写；Notion AI 按模板沉淀客户/项目记录。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客户成功"
    },
    {
        "num": "74",
        "scenario": "会议",
        "title": "会议：Fathom + HubSpot + ChatGPT",
        "combo": "Fathom + HubSpot + ChatGPT",
        "id_slug": "fathom-hubspot-chatgpt",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Fathom",
            "HubSpot",
            "ChatGPT"
        ],
        "steps": [
            "Fathom 总结销售通话",
            "HubSpot 更新 CRM",
            "ChatGPT 写 follow-up"
        ],
        "workflow": "Fathom 总结销售通话；HubSpot 更新 CRM；ChatGPT 写 follow-up。",
        "outputs": [
            "销售团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Fathom + HubSpot + ChatGPT。工具分工：Fathom 总结销售通话；HubSpot 更新 CRM；ChatGPT 写 follow-up。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售团队"
    },
    {
        "num": "75",
        "scenario": "会议",
        "title": "会议：Zoom AI Companion + Claude",
        "combo": "Zoom AI Companion + Claude",
        "id_slug": "zoom-ai-companion-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Zoom AI Companion",
            "Claude"
        ],
        "steps": [
            "Zoom 生成摘要",
            "Claude 做复盘、反对意见和项目计划"
        ],
        "workflow": "Zoom 生成摘要；Claude 做复盘、反对意见和项目计划。",
        "outputs": [
            "远程团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Zoom AI Companion + Claude。工具分工：Zoom 生成摘要；Claude 做复盘、反对意见和项目计划。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "远程团队"
    },
    {
        "num": "76",
        "scenario": "会议",
        "title": "会议：Teams Copilot + ChatGPT",
        "combo": "Teams Copilot + ChatGPT",
        "id_slug": "teams-copilot-chatgpt",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Teams Copilot",
            "ChatGPT"
        ],
        "steps": [
            "Teams Copilot 总结内部会议",
            "ChatGPT 把结论转成对外邮件/方案"
        ],
        "workflow": "Teams Copilot 总结内部会议；ChatGPT 把结论转成对外邮件/方案。",
        "outputs": [
            "Microsoft 365 团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Teams Copilot + ChatGPT。工具分工：Teams Copilot 总结内部会议；ChatGPT 把结论转成对外邮件/方案。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "Microsoft 365 团队"
    },
    {
        "num": "77",
        "scenario": "会议",
        "title": "会议：Google Meet + Gemini + Claude",
        "combo": "Google Meet + Gemini + Claude",
        "id_slug": "google-meet-gemini-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Google Meet",
            "Gemini",
            "Claude"
        ],
        "steps": [
            "Gemini 汇总会议",
            "Claude 写客户化纪要和下一步提案"
        ],
        "workflow": "Gemini 汇总会议；Claude 写客户化纪要和下一步提案。",
        "outputs": [
            "Google 生态团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Google Meet + Gemini + Claude。工具分工：Gemini 汇总会议；Claude 写客户化纪要和下一步提案。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "Google 生态团队"
    },
    {
        "num": "78",
        "scenario": "会议",
        "title": "会议：Granola + Claude",
        "combo": "Granola + Claude",
        "id_slug": "granola-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Granola",
            "Claude"
        ],
        "steps": [
            "Granola 记录个人会议笔记",
            "Claude 清理成可发版本和任务表"
        ],
        "workflow": "Granola 记录个人会议笔记；Claude 清理成可发版本和任务表。",
        "outputs": [
            "高频会议个人"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Granola + Claude。工具分工：Granola 记录个人会议笔记；Claude 清理成可发版本和任务表。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "高频会议个人"
    },
    {
        "num": "79",
        "scenario": "会议",
        "title": "会议：Supernormal + Linear",
        "combo": "Supernormal + Linear",
        "id_slug": "supernormal-linear",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Supernormal",
            "Linear"
        ],
        "steps": [
            "Supernormal 摘要 standup",
            "Linear 自动创建 bug/任务"
        ],
        "workflow": "Supernormal 摘要 standup；Linear 自动创建 bug/任务。",
        "outputs": [
            "研发团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Supernormal + Linear。工具分工：Supernormal 摘要 standup；Linear 自动创建 bug/任务。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 90,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "研发团队"
    },
    {
        "num": "80",
        "scenario": "会议",
        "title": "会议：Read.ai + Slack + Claude",
        "combo": "Read.ai + Slack + Claude",
        "id_slug": "read-ai-slack-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Read.ai",
            "Slack",
            "Claude"
        ],
        "steps": [
            "Read.ai 量化会议和情绪",
            "Slack 分发",
            "Claude 做改进建议"
        ],
        "workflow": "Read.ai 量化会议和情绪；Slack 分发；Claude 做改进建议。",
        "outputs": [
            "管理者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Read.ai + Slack + Claude。工具分工：Read.ai 量化会议和情绪；Slack 分发；Claude 做改进建议。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "管理者"
    },
    {
        "num": "81",
        "scenario": "自动化",
        "title": "自动化：Zapier AI + ChatGPT",
        "combo": "Zapier AI + ChatGPT",
        "id_slug": "zapier-ai-chatgpt",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Zapier AI",
            "ChatGPT"
        ],
        "steps": [
            "Zapier 监听表单/邮件/CRM",
            "ChatGPT 生成回复、分类和任务"
        ],
        "workflow": "Zapier 监听表单/邮件/CRM；ChatGPT 生成回复、分类和任务。",
        "outputs": [
            "无代码自动化"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Zapier AI + ChatGPT。工具分工：Zapier 监听表单/邮件/CRM；ChatGPT 生成回复、分类和任务。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "无代码自动化"
    },
    {
        "num": "82",
        "scenario": "自动化",
        "title": "自动化：Make + Claude",
        "combo": "Make + Claude",
        "id_slug": "make-claude",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Make",
            "Claude"
        ],
        "steps": [
            "Make 编排多工具流程",
            "Claude 处理复杂文本判断和报告生成"
        ],
        "workflow": "Make 编排多工具流程；Claude 处理复杂文本判断和报告生成。",
        "outputs": [
            "运营自动化"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Make + Claude。工具分工：Make 编排多工具流程；Claude 处理复杂文本判断和报告生成。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "运营自动化"
    },
    {
        "num": "83",
        "scenario": "自动化",
        "title": "自动化：n8n + OpenAI/Anthropic API",
        "combo": "n8n + OpenAI/Anthropic API",
        "id_slug": "n8n-openai-anthropic-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "n8n",
            "OpenAI",
            "Anthropic API"
        ],
        "steps": [
            "自托管 n8n 调模型 API，处理工单、数据、通知和审批"
        ],
        "workflow": "自托管 n8n 调模型 API，处理工单、数据、通知和审批。",
        "outputs": [
            "注重隐私/成本的团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：n8n + OpenAI/Anthropic API。工具分工：自托管 n8n 调模型 API，处理工单、数据、通知和审批。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "注重隐私/成本的团队"
    },
    {
        "num": "84",
        "scenario": "自动化",
        "title": "自动化：Slack + Claude + Linear",
        "combo": "Slack + Claude + Linear",
        "id_slug": "slack-claude-linear",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Slack",
            "Claude",
            "Linear"
        ],
        "steps": [
            "Slack 对话触发 Claude 总结需求",
            "Linear 创建 issue 并分配优先级"
        ],
        "workflow": "Slack 对话触发 Claude 总结需求；Linear 创建 issue 并分配优先级。",
        "outputs": [
            "产品团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Slack + Claude + Linear。工具分工：Slack 对话触发 Claude 总结需求；Linear 创建 issue 并分配优先级。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品团队"
    },
    {
        "num": "85",
        "scenario": "自动化",
        "title": "自动化：Gmail/Outlook + ChatGPT",
        "combo": "Gmail/Outlook + ChatGPT",
        "id_slug": "gmail-outlook-chatgpt",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Gmail",
            "Outlook",
            "ChatGPT"
        ],
        "steps": [
            "ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议"
        ],
        "workflow": "ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议。",
        "outputs": [
            "高邮件量岗位"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Gmail/Outlook + ChatGPT。工具分工：ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "高邮件量岗位"
    },
    {
        "num": "86",
        "scenario": "自动化",
        "title": "自动化：Notion + Zapier + ChatGPT",
        "combo": "Notion + Zapier + ChatGPT",
        "id_slug": "notion-zapier-chatgpt",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Notion",
            "Zapier",
            "ChatGPT"
        ],
        "steps": [
            "Notion 状态变化触发 Zapier",
            "ChatGPT 生成周报/提醒/客户邮件"
        ],
        "workflow": "Notion 状态变化触发 Zapier；ChatGPT 生成周报/提醒/客户邮件。",
        "outputs": [
            "项目运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Notion + Zapier + ChatGPT。工具分工：Notion 状态变化触发 Zapier；ChatGPT 生成周报/提醒/客户邮件。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "项目运营"
    },
    {
        "num": "87",
        "scenario": "自动化",
        "title": "自动化：Airtable AI + Slack",
        "combo": "Airtable AI + Slack",
        "id_slug": "airtable-ai-slack",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Airtable AI",
            "Slack"
        ],
        "steps": [
            "Airtable AI 分类记录",
            "Slack 推送异常和摘要"
        ],
        "workflow": "Airtable AI 分类记录；Slack 推送异常和摘要。",
        "outputs": [
            "客服/销售运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Airtable AI + Slack。工具分工：Airtable AI 分类记录；Slack 推送异常和摘要。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客服/销售运营"
    },
    {
        "num": "88",
        "scenario": "自动化",
        "title": "自动化：Clay + ChatGPT + HubSpot",
        "combo": "Clay + ChatGPT + HubSpot",
        "id_slug": "clay-chatgpt-hubspot",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Clay",
            "ChatGPT",
            "HubSpot"
        ],
        "steps": [
            "Clay enrich leads",
            "ChatGPT 个性化邮件",
            "HubSpot 追踪"
        ],
        "workflow": "Clay enrich leads；ChatGPT 个性化邮件；HubSpot 追踪。",
        "outputs": [
            "B2B outbound"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Clay + ChatGPT + HubSpot。工具分工：Clay enrich leads；ChatGPT 个性化邮件；HubSpot 追踪。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "B2B outbound"
    },
    {
        "num": "89",
        "scenario": "自动化",
        "title": "自动化：Apollo + Clay + Claude",
        "combo": "Apollo + Clay + Claude",
        "id_slug": "apollo-clay-claude",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Apollo",
            "Clay",
            "Claude"
        ],
        "steps": [
            "Apollo 找线索",
            "Clay 丰富数据",
            "Claude 写高质量个性化触达"
        ],
        "workflow": "Apollo 找线索；Clay 丰富数据；Claude 写高质量个性化触达。",
        "outputs": [
            "销售开发"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Apollo + Clay + Claude。工具分工：Apollo 找线索；Clay 丰富数据；Claude 写高质量个性化触达。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售开发"
    },
    {
        "num": "90",
        "scenario": "自动化",
        "title": "自动化：Retool + OpenAI API",
        "combo": "Retool + OpenAI API",
        "id_slug": "retool-openai-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Retool",
            "OpenAI API"
        ],
        "steps": [
            "Retool 搭内部工具",
            "OpenAI API 做文本分类、摘要和操作建议"
        ],
        "workflow": "Retool 搭内部工具；OpenAI API 做文本分类、摘要和操作建议。",
        "outputs": [
            "内部运营工具"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Retool + OpenAI API。工具分工：Retool 搭内部工具；OpenAI API 做文本分类、摘要和操作建议。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "内部运营工具"
    },
    {
        "num": "91",
        "scenario": "设计",
        "title": "设计：Claude + Adobe Creative Cloud",
        "combo": "Claude + Adobe Creative Cloud",
        "id_slug": "claude-adobe-creative-cloud",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Claude",
            "Adobe Creative Cloud"
        ],
        "steps": [
            "Claude 通过创意连接器辅助 Photoshop/Premiere/Express 等工具的批处理和资产流转"
        ],
        "workflow": "Claude 通过创意连接器辅助 Photoshop/Premiere/Express 等工具的批处理和资产流转。",
        "outputs": [
            "设计/视频团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Claude + Adobe Creative Cloud。工具分工：Claude 通过创意连接器辅助 Photoshop/Premiere/Express 等工具的批处理和资产流转。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "设计/视频团队"
    },
    {
        "num": "92",
        "scenario": "设计",
        "title": "设计：Claude + Blender",
        "combo": "Claude + Blender",
        "id_slug": "claude-blender",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Claude",
            "Blender"
        ],
        "steps": [
            "Claude 分析/调试 Blender 场景，写 Python 脚本批量修改对象"
        ],
        "workflow": "Claude 分析/调试 Blender 场景，写 Python 脚本批量修改对象。",
        "outputs": [
            "3D、建筑可视化、游戏"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Claude + Blender。工具分工：Claude 分析/调试 Blender 场景，写 Python 脚本批量修改对象。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "3D、建筑可视化、游戏"
    },
    {
        "num": "93",
        "scenario": "设计",
        "title": "设计：ChatGPT + Midjourney + Photoshop",
        "combo": "ChatGPT + Midjourney + Photoshop",
        "id_slug": "chatgpt-midjourney-photoshop",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "ChatGPT",
            "Midjourney",
            "Photoshop"
        ],
        "steps": [
            "ChatGPT 写 prompt 和风格规范",
            "Midjourney 出图",
            "Photoshop 精修"
        ],
        "workflow": "ChatGPT 写 prompt 和风格规范；Midjourney 出图；Photoshop 精修。",
        "outputs": [
            "广告视觉"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：ChatGPT + Midjourney + Photoshop。工具分工：ChatGPT 写 prompt 和风格规范；Midjourney 出图；Photoshop 精修。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "广告视觉"
    },
    {
        "num": "94",
        "scenario": "设计",
        "title": "设计：Canva + ChatGPT",
        "combo": "Canva + ChatGPT",
        "id_slug": "canva-chatgpt",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Canva",
            "ChatGPT"
        ],
        "steps": [
            "ChatGPT 写品牌文案和版式要求",
            "Canva 快速生成海报、简报、社媒图"
        ],
        "workflow": "ChatGPT 写品牌文案和版式要求；Canva 快速生成海报、简报、社媒图。",
        "outputs": [
            "非设计师"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Canva + ChatGPT。工具分工：ChatGPT 写品牌文案和版式要求；Canva 快速生成海报、简报、社媒图。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "非设计师"
    },
    {
        "num": "95",
        "scenario": "设计",
        "title": "设计：Figma AI + Claude",
        "combo": "Figma AI + Claude",
        "id_slug": "figma-ai-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Figma AI",
            "Claude"
        ],
        "steps": [
            "Figma AI 快速生成/整理 UI",
            "Claude 输出交互逻辑、文案和设计评审"
        ],
        "workflow": "Figma AI 快速生成/整理 UI；Claude 输出交互逻辑、文案和设计评审。",
        "outputs": [
            "产品设计"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Figma AI + Claude。工具分工：Figma AI 快速生成/整理 UI；Claude 输出交互逻辑、文案和设计评审。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 89,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品设计"
    },
    {
        "num": "96",
        "scenario": "设计",
        "title": "设计：Framer + ChatGPT",
        "combo": "Framer + ChatGPT",
        "id_slug": "framer-chatgpt",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Framer",
            "ChatGPT"
        ],
        "steps": [
            "ChatGPT 生成网站结构和文案",
            "Framer 快速建交互页面"
        ],
        "workflow": "ChatGPT 生成网站结构和文案；Framer 快速建交互页面。",
        "outputs": [
            "落地页、个人网站"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Framer + ChatGPT。工具分工：ChatGPT 生成网站结构和文案；Framer 快速建交互页面。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "落地页、个人网站"
    },
    {
        "num": "97",
        "scenario": "设计",
        "title": "设计：Uizard/Galileo + Claude",
        "combo": "Uizard/Galileo + Claude",
        "id_slug": "uizard-galileo-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Uizard",
            "Galileo",
            "Claude"
        ],
        "steps": [
            "AI UI 工具出线框",
            "Claude 写产品说明和验收标准"
        ],
        "workflow": "AI UI 工具出线框；Claude 写产品说明和验收标准。",
        "outputs": [
            "需求到原型"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Uizard/Galileo + Claude。工具分工：AI UI 工具出线框；Claude 写产品说明和验收标准。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "需求到原型"
    },
    {
        "num": "98",
        "scenario": "设计",
        "title": "设计：Runway + Claude",
        "combo": "Runway + Claude",
        "id_slug": "runway-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Runway",
            "Claude"
        ],
        "steps": [
            "Claude 写分镜、镜头和旁白",
            "Runway 生成/编辑视频"
        ],
        "workflow": "Claude 写分镜、镜头和旁白；Runway 生成/编辑视频。",
        "outputs": [
            "视频创意"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Runway + Claude。工具分工：Claude 写分镜、镜头和旁白；Runway 生成/编辑视频。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "视频创意"
    },
    {
        "num": "99",
        "scenario": "设计",
        "title": "设计：HeyGen + Claude",
        "combo": "HeyGen + Claude",
        "id_slug": "heygen-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "HeyGen",
            "Claude"
        ],
        "steps": [
            "Claude 写脚本和多语言版本",
            "HeyGen 生成数字人视频"
        ],
        "workflow": "Claude 写脚本和多语言版本；HeyGen 生成数字人视频。",
        "outputs": [
            "培训、销售启发"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：HeyGen + Claude。工具分工：Claude 写脚本和多语言版本；HeyGen 生成数字人视频。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "培训、销售启发"
    },
    {
        "num": "100",
        "scenario": "设计",
        "title": "设计：Suno/Udio + Claude",
        "combo": "Suno/Udio + Claude",
        "id_slug": "suno-udio-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Suno",
            "Udio",
            "Claude"
        ],
        "steps": [
            "Claude 写歌词/风格 brief",
            "Suno/Udio 生成音乐",
            "Claude 迭代版本说明"
        ],
        "workflow": "Claude 写歌词/风格 brief；Suno/Udio 生成音乐；Claude 迭代版本说明。",
        "outputs": [
            "广告音乐、短视频 BGM"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Suno/Udio + Claude。工具分工：Claude 写歌词/风格 brief；Suno/Udio 生成音乐；Claude 迭代版本说明。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "广告音乐、短视频 BGM"
    },
    {
        "num": "101",
        "scenario": "音视频",
        "title": "音视频：Descript + ChatGPT",
        "combo": "Descript + ChatGPT",
        "id_slug": "descript-chatgpt",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Descript",
            "ChatGPT"
        ],
        "steps": [
            "Descript 转写和剪辑",
            "ChatGPT 写标题、摘要、show notes"
        ],
        "workflow": "Descript 转写和剪辑；ChatGPT 写标题、摘要、show notes。",
        "outputs": [
            "播客"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：Descript + ChatGPT。工具分工：Descript 转写和剪辑；ChatGPT 写标题、摘要、show notes。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "播客"
    },
    {
        "num": "102",
        "scenario": "音视频",
        "title": "音视频：ElevenLabs + Claude",
        "combo": "ElevenLabs + Claude",
        "id_slug": "elevenlabs-claude",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "ElevenLabs",
            "Claude"
        ],
        "steps": [
            "Claude 写旁白脚本",
            "ElevenLabs 生成多语言配音"
        ],
        "workflow": "Claude 写旁白脚本；ElevenLabs 生成多语言配音。",
        "outputs": [
            "课程、广告"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：ElevenLabs + Claude。工具分工：Claude 写旁白脚本；ElevenLabs 生成多语言配音。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "课程、广告"
    },
    {
        "num": "103",
        "scenario": "音视频",
        "title": "音视频：Premiere + Claude connector",
        "combo": "Premiere + Claude connector",
        "id_slug": "premiere-claude-connector",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Premiere",
            "Claude connector"
        ],
        "steps": [
            "Claude 辅助素材整理、批处理和编辑建议",
            "Premiere 完成专业剪辑"
        ],
        "workflow": "Claude 辅助素材整理、批处理和编辑建议；Premiere 完成专业剪辑。",
        "outputs": [
            "视频团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：Premiere + Claude connector。工具分工：Claude 辅助素材整理、批处理和编辑建议；Premiere 完成专业剪辑。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "视频团队"
    },
    {
        "num": "104",
        "scenario": "音视频",
        "title": "音视频：Ableton + Claude connector",
        "combo": "Ableton + Claude connector",
        "id_slug": "ableton-claude-connector",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Ableton",
            "Claude connector"
        ],
        "steps": [
            "Claude 基于 Live/Push 文档辅助制作步骤、排错和工程整理"
        ],
        "workflow": "Claude 基于 Live/Push 文档辅助制作步骤、排错和工程整理。",
        "outputs": [
            "音乐制作"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：Ableton + Claude connector。工具分工：Claude 基于 Live/Push 文档辅助制作步骤、排错和工程整理。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "音乐制作"
    },
    {
        "num": "105",
        "scenario": "音视频",
        "title": "音视频：HyperFrames + Hermes Agent",
        "combo": "HyperFrames + Hermes Agent",
        "id_slug": "hyperframes-hermes-agent",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "HyperFrames",
            "Hermes Agent"
        ],
        "steps": [
            "Hermes agent 调 HyperFrames，把一行描述渲染成视频片段"
        ],
        "workflow": "Hermes agent 调 HyperFrames，把一行描述渲染成视频片段。",
        "outputs": [
            "agentic 视频原型"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：HyperFrames + Hermes Agent。工具分工：Hermes agent 调 HyperFrames，把一行描述渲染成视频片段。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "agentic 视频原型"
    },
    {
        "num": "106",
        "scenario": "音视频",
        "title": "音视频：CapCut + ChatGPT",
        "combo": "CapCut + ChatGPT",
        "id_slug": "capcut-chatgpt",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "CapCut",
            "ChatGPT"
        ],
        "steps": [
            "ChatGPT 生成短视频脚本、字幕、标题",
            "CapCut 快速成片"
        ],
        "workflow": "ChatGPT 生成短视频脚本、字幕、标题；CapCut 快速成片。",
        "outputs": [
            "短视频运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：CapCut + ChatGPT。工具分工：ChatGPT 生成短视频脚本、字幕、标题；CapCut 快速成片。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "短视频运营"
    },
    {
        "num": "107",
        "scenario": "商务",
        "title": "商务：Claude + HubSpot",
        "combo": "Claude + HubSpot",
        "id_slug": "claude-hubspot",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "HubSpot"
        ],
        "steps": [
            "Claude 分析客户记录、邮件和会议纪要，生成下一步策略和跟进邮件"
        ],
        "workflow": "Claude 分析客户记录、邮件和会议纪要，生成下一步策略和跟进邮件。",
        "outputs": [
            "销售/客户成功"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Claude + HubSpot。工具分工：Claude 分析客户记录、邮件和会议纪要，生成下一步策略和跟进邮件。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售/客户成功"
    },
    {
        "num": "108",
        "scenario": "商务",
        "title": "商务：ChatGPT + Salesforce",
        "combo": "ChatGPT + Salesforce",
        "id_slug": "chatgpt-salesforce",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Salesforce"
        ],
        "steps": [
            "ChatGPT 汇总机会、风险、竞争态势，生成销售行动计划"
        ],
        "workflow": "ChatGPT 汇总机会、风险、竞争态势，生成销售行动计划。",
        "outputs": [
            "企业销售"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：ChatGPT + Salesforce。工具分工：ChatGPT 汇总机会、风险、竞争态势，生成销售行动计划。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "企业销售"
    },
    {
        "num": "109",
        "scenario": "商务",
        "title": "商务：Perplexity + Clay + Claude",
        "combo": "Perplexity + Clay + Claude",
        "id_slug": "perplexity-clay-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Perplexity",
            "Clay",
            "Claude"
        ],
        "steps": [
            "Perplexity 找公司背景",
            "Clay enrich",
            "Claude 写个性化 pitch"
        ],
        "workflow": "Perplexity 找公司背景；Clay enrich；Claude 写个性化 pitch。",
        "outputs": [
            "BD/outbound"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Perplexity + Clay + Claude。工具分工：Perplexity 找公司背景；Clay enrich；Claude 写个性化 pitch。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "BD/outbound"
    },
    {
        "num": "110",
        "scenario": "商务",
        "title": "商务：ChatGPT + DocuSign + Claude",
        "combo": "ChatGPT + DocuSign + Claude",
        "id_slug": "chatgpt-docusign-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "DocuSign",
            "Claude"
        ],
        "steps": [
            "ChatGPT 生成合同摘要",
            "Claude 比较条款风险",
            "DocuSign 走签署"
        ],
        "workflow": "ChatGPT 生成合同摘要；Claude 比较条款风险；DocuSign 走签署。",
        "outputs": [
            "法务/销售运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：ChatGPT + DocuSign + Claude。工具分工：ChatGPT 生成合同摘要；Claude 比较条款风险；DocuSign 走签署。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "法务/销售运营"
    },
    {
        "num": "111",
        "scenario": "商务",
        "title": "商务：Claude + ServiceNow",
        "combo": "Claude + ServiceNow",
        "id_slug": "claude-servicenow",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "ServiceNow"
        ],
        "steps": [
            "用 Claude 驱动 ServiceNow Build Agent，把自然语言需求转成工作流/内部应用"
        ],
        "workflow": "用 Claude 驱动 ServiceNow Build Agent，把自然语言需求转成工作流/内部应用。",
        "outputs": [
            "企业 IT/运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Claude + ServiceNow。工具分工：用 Claude 驱动 ServiceNow Build Agent，把自然语言需求转成工作流/内部应用。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 88,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "企业 IT/运营"
    },
    {
        "num": "112",
        "scenario": "商务",
        "title": "商务：ChatGPT + Intercom/Zendesk",
        "combo": "ChatGPT + Intercom/Zendesk",
        "id_slug": "chatgpt-intercom-zendesk",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Intercom",
            "Zendesk"
        ],
        "steps": [
            "ChatGPT 分类工单、草拟回复",
            "客服平台保留人工审核和历史记录"
        ],
        "workflow": "ChatGPT 分类工单、草拟回复；客服平台保留人工审核和历史记录。",
        "outputs": [
            "客服团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：ChatGPT + Intercom/Zendesk。工具分工：ChatGPT 分类工单、草拟回复；客服平台保留人工审核和历史记录。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客服团队"
    },
    {
        "num": "113",
        "scenario": "商务",
        "title": "商务：Claude + Linear + Notion",
        "combo": "Claude + Linear + Notion",
        "id_slug": "claude-linear-notion",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "Linear",
            "Notion"
        ],
        "steps": [
            "Claude 把客户反馈归类，Linear 建任务，Notion 写路线图摘要"
        ],
        "workflow": "Claude 把客户反馈归类，Linear 建任务，Notion 写路线图摘要。",
        "outputs": [
            "产品经理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Claude + Linear + Notion。工具分工：Claude 把客户反馈归类，Linear 建任务，Notion 写路线图摘要。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品经理"
    },
    {
        "num": "114",
        "scenario": "商务",
        "title": "商务：Gong + Claude",
        "combo": "Gong + Claude",
        "id_slug": "gong-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Gong",
            "Claude"
        ],
        "steps": [
            "Gong 分析销售通话",
            "Claude 生成教练反馈、异议处理和复盘"
        ],
        "workflow": "Gong 分析销售通话；Claude 生成教练反馈、异议处理和复盘。",
        "outputs": [
            "销售管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Gong + Claude。工具分工：Gong 分析销售通话；Claude 生成教练反馈、异议处理和复盘。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售管理"
    },
    {
        "num": "115",
        "scenario": "商务",
        "title": "商务：ChatGPT + Shopify + Canva",
        "combo": "ChatGPT + Shopify + Canva",
        "id_slug": "chatgpt-shopify-canva",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Shopify",
            "Canva"
        ],
        "steps": [
            "ChatGPT 生成商品文案/FAQ",
            "Canva 做商品图",
            "Shopify 发布"
        ],
        "workflow": "ChatGPT 生成商品文案/FAQ；Canva 做商品图；Shopify 发布。",
        "outputs": [
            "电商"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：ChatGPT + Shopify + Canva。工具分工：ChatGPT 生成商品文案/FAQ；Canva 做商品图；Shopify 发布。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "电商"
    },
    {
        "num": "116",
        "scenario": "商务",
        "title": "商务：",
        "combo": "",
        "id_slug": "item",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [],
        "steps": [
            "Claude + TurboTax/财税工具 Claude 整理凭证问题和税务问答",
            "财税工具完成申报流程"
        ],
        "workflow": "Claude + TurboTax/财税工具 Claude 整理凭证问题和税务问答；财税工具完成申报流程。",
        "outputs": [
            "个体户/小企业"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：。工具分工：Claude + TurboTax/财税工具 Claude 整理凭证问题和税务问答；财税工具完成申报流程。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "个体户/小企业"
    },
    {
        "num": "117",
        "scenario": "个人效率",
        "title": "个人效率：ChatGPT + Todoist",
        "combo": "ChatGPT + Todoist",
        "id_slug": "chatgpt-todoist",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Todoist"
        ],
        "steps": [
            "ChatGPT 拆解目标和日程",
            "Todoist 管任务提醒"
        ],
        "workflow": "ChatGPT 拆解目标和日程；Todoist 管任务提醒。",
        "outputs": [
            "个人执行"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：ChatGPT + Todoist。工具分工：ChatGPT 拆解目标和日程；Todoist 管任务提醒。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "个人执行"
    },
    {
        "num": "118",
        "scenario": "个人效率",
        "title": "个人效率：Claude + Apple Notes/Obsidian",
        "combo": "Claude + Apple Notes/Obsidian",
        "id_slug": "claude-apple-notes-obsidian",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Apple Notes",
            "Obsidian"
        ],
        "steps": [
            "Claude 帮你把碎片笔记整理成项目计划、文章或决策 memo"
        ],
        "workflow": "Claude 帮你把碎片笔记整理成项目计划、文章或决策 memo。",
        "outputs": [
            "知识工作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：Claude + Apple Notes/Obsidian。工具分工：Claude 帮你把碎片笔记整理成项目计划、文章或决策 memo。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "知识工作者"
    },
    {
        "num": "119",
        "scenario": "个人效率",
        "title": "个人效率：",
        "combo": "",
        "id_slug": "item",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [],
        "steps": [
            "Grok + ayewatch/新闻监控 Grok/监控工具跟踪实时信息",
            "Claude/ChatGPT 每天生成摘要和行动建议"
        ],
        "workflow": "Grok + ayewatch/新闻监控 Grok/监控工具跟踪实时信息；Claude/ChatGPT 每天生成摘要和行动建议。",
        "outputs": [
            "投资、媒体、创始人"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：。工具分工：Grok + ayewatch/新闻监控 Grok/监控工具跟踪实时信息；Claude/ChatGPT 每天生成摘要和行动建议。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "投资、媒体、创始人"
    },
    {
        "num": "120",
        "scenario": "个人效率",
        "title": "个人效率：ChatGPT + Claude + Perplexity",
        "combo": "ChatGPT + Claude + Perplexity",
        "id_slug": "chatgpt-claude-perplexity",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT",
            "Claude",
            "Perplexity"
        ],
        "steps": [
            "ChatGPT 做默认助手",
            "Claude 做长文和高质量判断",
            "Perplexity 做带来源检索"
        ],
        "workflow": "ChatGPT 做默认助手；Claude 做长文和高质量判断；Perplexity 做带来源检索。",
        "outputs": [
            "三者分工固定，减少来回切换。 通用高效工作流"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：ChatGPT + Claude + Perplexity。工具分工：ChatGPT 做默认助手；Claude 做长文和高质量判断；Perplexity 做带来源检索。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "三者分工固定，减少来回切换。 通用高效工作流"
    },
    {
        "num": "121",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Claude/ChatGPT + Gamma Connector",
        "combo": "Claude/ChatGPT + Gamma Connector",
        "id_slug": "ppt-claude-chatgpt-gamma-connector",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "ChatGPT",
            "Gamma Connector"
        ],
        "steps": [
            "在 Claude 或 ChatGPT 对话中直接生成 Gamma deck，减少复制粘贴",
            "再用 Gamma 模板和品牌设置收尾"
        ],
        "workflow": "在 Claude 或 ChatGPT 对话中直接生成 Gamma deck，减少复制粘贴；再用 Gamma 模板和品牌设置收尾。",
        "outputs": [
            "高频做简报的人"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Claude/ChatGPT + Gamma Connector。工具分工：在 Claude 或 ChatGPT 对话中直接生成 Gamma deck，减少复制粘贴；再用 Gamma 模板和品牌设置收尾。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "高频做简报的人"
    },
    {
        "num": "122",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Notion + Claude + Gamma API/n8n",
        "combo": "Notion + Claude + Gamma API/n8n",
        "id_slug": "ppt-notion-claude-gamma-api-n8n",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Notion",
            "Claude",
            "Gamma API",
            "n8n"
        ],
        "steps": [
            "Notion 立项页变更触发 n8n",
            "Claude 总结内容",
            "Gamma API 自动生成项目汇报"
        ],
        "workflow": "Notion 立项页变更触发 n8n；Claude 总结内容；Gamma API 自动生成项目汇报。",
        "outputs": [
            "PMO、咨询公司"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Notion + Claude + Gamma API/n8n。工具分工：Notion 立项页变更触发 n8n；Claude 总结内容；Gamma API 自动生成项目汇报。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "PMO、咨询公司"
    },
    {
        "num": "123",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Airtable + Zapier + Gamma",
        "combo": "Airtable + Zapier + Gamma",
        "id_slug": "ppt-airtable-zapier-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Airtable",
            "Zapier",
            "Gamma"
        ],
        "steps": [
            "Airtable 新增客户记录后，Zapier 把字段送入 Gamma 生成客户化介绍 deck"
        ],
        "workflow": "Airtable 新增客户记录后，Zapier 把字段送入 Gamma 生成客户化介绍 deck。",
        "outputs": [
            "销售运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Airtable + Zapier + Gamma。工具分工：Airtable 新增客户记录后，Zapier 把字段送入 Gamma 生成客户化介绍 deck。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售运营"
    },
    {
        "num": "124",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Superhuman Go + Gamma + Claude",
        "combo": "Superhuman Go + Gamma + Claude",
        "id_slug": "ppt-superhuman-go-gamma-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Superhuman Go",
            "Gamma",
            "Claude"
        ],
        "steps": [
            "邮件里收到客户需求后，Superhuman Go 调 Gamma 生成初版资料，Claude 优化话术"
        ],
        "workflow": "邮件里收到客户需求后，Superhuman Go 调 Gamma 生成初版资料，Claude 优化话术。",
        "outputs": [
            "BD、客户成功"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Superhuman Go + Gamma + Claude。工具分工：邮件里收到客户需求后，Superhuman Go 调 Gamma 生成初版资料，Claude 优化话术。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "BD、客户成功"
    },
    {
        "num": "125",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Atlassian Rovo + Gamma",
        "combo": "Atlassian Rovo + Gamma",
        "id_slug": "ppt-atlassian-rovo-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Atlassian Rovo",
            "Gamma"
        ],
        "steps": [
            "从 Confluence/Jira 项目资料生成发布说明或路线图 deck"
        ],
        "workflow": "从 Confluence/Jira 项目资料生成发布说明或路线图 deck。",
        "outputs": [
            "研发管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Atlassian Rovo + Gamma。工具分工：从 Confluence/Jira 项目资料生成发布说明或路线图 deck。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "研发管理"
    },
    {
        "num": "126",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Perplexity + Claude + Close",
        "combo": "Perplexity + Claude + Close",
        "id_slug": "ppt-perplexity-claude-close",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Perplexity",
            "Claude",
            "Close"
        ],
        "steps": [
            "Perplexity 做客户/行业研究",
            "Claude 写 pitch",
            "Gamma 可视化",
            "Close 跟进 pipeline"
        ],
        "workflow": "Perplexity 做客户/行业研究；Claude 写 pitch；Gamma 可视化；Close 跟进 pipeline。",
        "outputs": [
            "内容到销售闭环"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Perplexity + Claude + Close。工具分工：Perplexity 做客户/行业研究；Claude 写 pitch；Gamma 可视化；Close 跟进 pipeline。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "内容到销售闭环"
    },
    {
        "num": "127",
        "scenario": "PPT/提案",
        "title": "PPT/提案：Effy + Claude + Canva/Gamma",
        "combo": "Effy + Claude + Canva/Gamma",
        "id_slug": "ppt-effy-claude-canva-gamma",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Effy",
            "Claude",
            "Canva",
            "Gamma"
        ],
        "steps": [
            "Effy 生成 HR 反馈/绩效素材",
            "Claude 梳理为管理层叙事",
            "Canva/Gamma 出汇报"
        ],
        "workflow": "Effy 生成 HR 反馈/绩效素材；Claude 梳理为管理层叙事；Canva/Gamma 出汇报。",
        "outputs": [
            "HR、团队负责人"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：PPT/提案：Effy + Claude + Canva/Gamma。工具分工：Effy 生成 HR 反馈/绩效素材；Claude 梳理为管理层叙事；Canva/Gamma 出汇报。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "importance": 87,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "HR、团队负责人"
    },
    {
        "num": "128",
        "scenario": "研究",
        "title": "研究：ChatGPT Deep Research + trusted-site filter",
        "combo": "ChatGPT Deep Research + trusted-site filter",
        "id_slug": "chatgpt-deep-research-trusted-site-filter",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "ChatGPT Deep Research",
            "trusted-site filter"
        ],
        "steps": [
            "限制检索到可信站点或内部 MCP",
            "输出带来源报告，再由 Claude 压缩成执行摘要"
        ],
        "workflow": "限制检索到可信站点或内部 MCP；输出带来源报告，再由 Claude 压缩成执行摘要。",
        "outputs": [
            "政策、金融、技术研究"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：ChatGPT Deep Research + trusted-site filter。工具分工：限制检索到可信站点或内部 MCP；输出带来源报告，再由 Claude 压缩成执行摘要。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "政策、金融、技术研究"
    },
    {
        "num": "129",
        "scenario": "研究",
        "title": "研究：Grok DeeperSearch + Claude",
        "combo": "Grok DeeperSearch + Claude",
        "id_slug": "grok-deepersearch-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Grok DeeperSearch",
            "Claude"
        ],
        "steps": [
            "Grok 看 X 和实时网络讨论",
            "Claude 做立场归类、可信度判断和摘要"
        ],
        "workflow": "Grok 看 X 和实时网络讨论；Claude 做立场归类、可信度判断和摘要。",
        "outputs": [
            "舆情、投资、媒体"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Grok DeeperSearch + Claude。工具分工：Grok 看 X 和实时网络讨论；Claude 做立场归类、可信度判断和摘要。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "舆情、投资、媒体"
    },
    {
        "num": "130",
        "scenario": "研究",
        "title": "研究：SubQ + Claude/ChatGPT",
        "combo": "SubQ + Claude/ChatGPT",
        "id_slug": "subq-claude-chatgpt",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "SubQ",
            "Claude",
            "ChatGPT"
        ],
        "steps": [
            "把大规模上下文交给 SubQ 长上下文层",
            "Claude/ChatGPT 做结论、反例和行动方案"
        ],
        "workflow": "把大规模上下文交给 SubQ 长上下文层；Claude/ChatGPT 做结论、反例和行动方案。",
        "outputs": [
            "超长资料研究"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：SubQ + Claude/ChatGPT。工具分工：把大规模上下文交给 SubQ 长上下文层；Claude/ChatGPT 做结论、反例和行动方案。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "超长资料研究"
    },
    {
        "num": "131",
        "scenario": "研究",
        "title": "研究：GBrain + Claude",
        "combo": "GBrain + Claude",
        "id_slug": "gbrain-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "GBrain",
            "Claude"
        ],
        "steps": [
            "GBrain 做夜间记忆整理和实体清理",
            "Claude 白天基于记忆做计划/写作"
        ],
        "workflow": "GBrain 做夜间记忆整理和实体清理；Claude 白天基于记忆做计划/写作。",
        "outputs": [
            "长期项目管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：GBrain + Claude。工具分工：GBrain 做夜间记忆整理和实体清理；Claude 白天基于记忆做计划/写作。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "长期项目管理"
    },
    {
        "num": "132",
        "scenario": "研究",
        "title": "研究：Fire-PDF + Claude",
        "combo": "Fire-PDF + Claude",
        "id_slug": "fire-pdf-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Fire-PDF",
            "Claude"
        ],
        "steps": [
            "Fire-PDF 快速把 PDF 转 markdown",
            "Claude 汇总条款、证据和风险"
        ],
        "workflow": "Fire-PDF 快速把 PDF 转 markdown；Claude 汇总条款、证据和风险。",
        "outputs": [
            "法务、学术、财务"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Fire-PDF + Claude。工具分工：Fire-PDF 快速把 PDF 转 markdown；Claude 汇总条款、证据和风险。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "法务、学术、财务"
    },
    {
        "num": "133",
        "scenario": "研究",
        "title": "研究：NotebookLM + Perplexity + Claude",
        "combo": "NotebookLM + Perplexity + Claude",
        "id_slug": "notebooklm-perplexity-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "NotebookLM",
            "Perplexity",
            "Claude"
        ],
        "steps": [
            "NotebookLM 锚定私有资料",
            "Perplexity 补公开资料",
            "Claude 做最终判断"
        ],
        "workflow": "NotebookLM 锚定私有资料；Perplexity 补公开资料；Claude 做最终判断。",
        "outputs": [
            "课程、行业分析"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：NotebookLM + Perplexity + Claude。工具分工：NotebookLM 锚定私有资料；Perplexity 补公开资料；Claude 做最终判断。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "课程、行业分析"
    },
    {
        "num": "134",
        "scenario": "研究",
        "title": "研究：OpenAI GPT-Rosalind + Codex/API",
        "combo": "OpenAI GPT-Rosalind + Codex/API",
        "id_slug": "openai-gpt-rosalind-codex-api",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "OpenAI GPT-Rosalind",
            "Codex",
            "API"
        ],
        "steps": [
            "GPT-Rosalind 做生命科学推理",
            "Codex/API 连接分析脚本和实验工具"
        ],
        "workflow": "GPT-Rosalind 做生命科学推理；Codex/API 连接分析脚本和实验工具。",
        "outputs": [
            "生物医药研发"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：OpenAI GPT-Rosalind + Codex/API。工具分工：GPT-Rosalind 做生命科学推理；Codex/API 连接分析脚本和实验工具。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "生物医药研发"
    },
    {
        "num": "135",
        "scenario": "研究",
        "title": "研究：Elicit + GPT-Rosalind + Claude",
        "combo": "Elicit + GPT-Rosalind + Claude",
        "id_slug": "elicit-gpt-rosalind-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Elicit",
            "GPT-Rosalind",
            "Claude"
        ],
        "steps": [
            "Elicit 找文献",
            "GPT-Rosalind 做生物机制推理",
            "Claude 写综述和实验计划"
        ],
        "workflow": "Elicit 找文献；GPT-Rosalind 做生物机制推理；Claude 写综述和实验计划。",
        "outputs": [
            "生命科学研究"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：Elicit + GPT-Rosalind + Claude。工具分工：Elicit 找文献；GPT-Rosalind 做生物机制推理；Claude 写综述和实验计划。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "生命科学研究"
    },
    {
        "num": "136",
        "scenario": "研究",
        "title": "研究：TradingAgents + Perplexity + Claude",
        "combo": "TradingAgents + Perplexity + Claude",
        "id_slug": "tradingagents-perplexity-claude",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "TradingAgents",
            "Perplexity",
            "Claude"
        ],
        "steps": [
            "多 agent 做基本面/情绪/技术/风险",
            "Perplexity 查证",
            "Claude 写投资 memo"
        ],
        "workflow": "多 agent 做基本面/情绪/技术/风险；Perplexity 查证；Claude 写投资 memo。",
        "outputs": [
            "量化/投资研究"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：研究：TradingAgents + Perplexity + Claude。工具分工：多 agent 做基本面/情绪/技术/风险；Perplexity 查证；Claude 写投资 memo。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "量化/投资研究"
    },
    {
        "num": "137",
        "scenario": "写作",
        "title": "写作：ChatGPT planner + Claude executor",
        "combo": "ChatGPT planner + Claude executor",
        "id_slug": "chatgpt-planner-claude-executor",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ChatGPT planner",
            "Claude executor"
        ],
        "steps": [
            "ChatGPT 负责拆结构、受众、角度",
            "Claude 负责长文执行和润色"
        ],
        "workflow": "ChatGPT 负责拆结构、受众、角度；Claude 负责长文执行和润色。",
        "outputs": [
            "商业写作"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：ChatGPT planner + Claude executor。工具分工：ChatGPT 负责拆结构、受众、角度；Claude 负责长文执行和润色。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "商业写作"
    },
    {
        "num": "138",
        "scenario": "写作",
        "title": "写作：Claude + Writeless/QuillBot",
        "combo": "Claude + Writeless/QuillBot",
        "id_slug": "claude-writeless-quillbot",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Writeless",
            "QuillBot"
        ],
        "steps": [
            "Claude 产出高质量初稿",
            "Writeless 或 QuillBot 做改写、降重复和语气调整"
        ],
        "workflow": "Claude 产出高质量初稿；Writeless 或 QuillBot 做改写、降重复和语气调整。",
        "outputs": [
            "SEO、学生、内容团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Claude + Writeless/QuillBot。工具分工：Claude 产出高质量初稿；Writeless 或 QuillBot 做改写、降重复和语气调整。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "SEO、学生、内容团队"
    },
    {
        "num": "139",
        "scenario": "写作",
        "title": "写作：Claude + Rankprompt",
        "combo": "Claude + Rankprompt",
        "id_slug": "claude-rankprompt",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Claude",
            "Rankprompt"
        ],
        "steps": [
            "Claude 写品牌内容",
            "Rankprompt 追踪品牌在 AI 回答里的提及和竞品引用"
        ],
        "workflow": "Claude 写品牌内容；Rankprompt 追踪品牌在 AI 回答里的提及和竞品引用。",
        "outputs": [
            "AI SEO、品牌监控"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Claude + Rankprompt。工具分工：Claude 写品牌内容；Rankprompt 追踪品牌在 AI 回答里的提及和竞品引用。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "AI SEO、品牌监控"
    },
    {
        "num": "140",
        "scenario": "写作",
        "title": "写作：ScriptWrite + ChatGPT + Midjourney",
        "combo": "ScriptWrite + ChatGPT + Midjourney",
        "id_slug": "scriptwrite-chatgpt-midjourney",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "ScriptWrite",
            "ChatGPT",
            "Midjourney"
        ],
        "steps": [
            "ScriptWrite 结构化脚本",
            "ChatGPT 发散",
            "Midjourney 做视觉 moodboard"
        ],
        "workflow": "ScriptWrite 结构化脚本；ChatGPT 发散；Midjourney 做视觉 moodboard。",
        "outputs": [
            "短视频/广告脚本"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：ScriptWrite + ChatGPT + Midjourney。工具分工：ScriptWrite 结构化脚本；ChatGPT 发散；Midjourney 做视觉 moodboard。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "短视频/广告脚本"
    },
    {
        "num": "141",
        "scenario": "写作",
        "title": "写作：Readwise + NotebookLM + Claude",
        "combo": "Readwise + NotebookLM + Claude",
        "id_slug": "readwise-notebooklm-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Readwise",
            "NotebookLM",
            "Claude"
        ],
        "steps": [
            "Readwise 收集高亮",
            "NotebookLM 限定来源问答",
            "Claude 写长文"
        ],
        "workflow": "Readwise 收集高亮；NotebookLM 限定来源问答；Claude 写长文。",
        "outputs": [
            "知识型创作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：写作：Readwise + NotebookLM + Claude。工具分工：Readwise 收集高亮；NotebookLM 限定来源问答；Claude 写长文。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "知识型创作者"
    },
    {
        "num": "142",
        "scenario": "社媒",
        "title": "社媒：Grok + Canva + Buffer",
        "combo": "Grok + Canva + Buffer",
        "id_slug": "grok-canva-buffer",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Grok",
            "Canva",
            "Buffer"
        ],
        "steps": [
            "Grok 抓实时热点",
            "Canva 做图",
            "Buffer 排程多平台"
        ],
        "workflow": "Grok 抓实时热点；Canva 做图；Buffer 排程多平台。",
        "outputs": [
            "热点运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Grok + Canva + Buffer。工具分工：Grok 抓实时热点；Canva 做图；Buffer 排程多平台。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "热点运营"
    },
    {
        "num": "143",
        "scenario": "社媒",
        "title": "社媒：ChatGPT + Leonardo AI + Descript",
        "combo": "ChatGPT + Leonardo AI + Descript",
        "id_slug": "chatgpt-leonardo-ai-descript",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ChatGPT",
            "Leonardo AI",
            "Descript"
        ],
        "steps": [
            "ChatGPT 写播客标题和摘要",
            "Leonardo 生成封面",
            "Descript 剪辑"
        ],
        "workflow": "ChatGPT 写播客标题和摘要；Leonardo 生成封面；Descript 剪辑。",
        "outputs": [
            "播客创作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：ChatGPT + Leonardo AI + Descript。工具分工：ChatGPT 写播客标题和摘要；Leonardo 生成封面；Descript 剪辑。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 86,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "播客创作者"
    },
    {
        "num": "144",
        "scenario": "社媒",
        "title": "社媒：Clipto AI + ChatGPT + Descript",
        "combo": "Clipto AI + ChatGPT + Descript",
        "id_slug": "clipto-ai-chatgpt-descript",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Clipto AI",
            "ChatGPT",
            "Descript"
        ],
        "steps": [
            "Clipto 本地转写敏感采访",
            "ChatGPT 写 show notes",
            "Descript 清理音频"
        ],
        "workflow": "Clipto 本地转写敏感采访；ChatGPT 写 show notes；Descript 清理音频。",
        "outputs": [
            "客户访谈、播客"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Clipto AI + ChatGPT + Descript。工具分工：Clipto 本地转写敏感采访；ChatGPT 写 show notes；Descript 清理音频。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客户访谈、播客"
    },
    {
        "num": "145",
        "scenario": "社媒",
        "title": "社媒：OpusClip + Claude + Hypefury",
        "combo": "OpusClip + Claude + Hypefury",
        "id_slug": "opusclip-claude-hypefury",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "OpusClip",
            "Claude",
            "Hypefury"
        ],
        "steps": [
            "OpusClip 切长视频",
            "Claude 写 thread",
            "Hypefury 排程复用"
        ],
        "workflow": "OpusClip 切长视频；Claude 写 thread；Hypefury 排程复用。",
        "outputs": [
            "视频转 X 内容"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：OpusClip + Claude + Hypefury。工具分工：OpusClip 切长视频；Claude 写 thread；Hypefury 排程复用。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "视频转 X 内容"
    },
    {
        "num": "146",
        "scenario": "社媒",
        "title": "社媒：Claude + OpenTweet + Perplexity",
        "combo": "Claude + OpenTweet + Perplexity",
        "id_slug": "claude-opentweet-perplexity",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Claude",
            "OpenTweet",
            "Perplexity"
        ],
        "steps": [
            "Claude 批量生成推文",
            "OpenTweet 排程和 evergreen",
            "Perplexity 定期补新资料"
        ],
        "workflow": "Claude 批量生成推文；OpenTweet 排程和 evergreen；Perplexity 定期补新资料。",
        "outputs": [
            "X 创作者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：社媒：Claude + OpenTweet + Perplexity。工具分工：Claude 批量生成推文；OpenTweet 排程和 evergreen；Perplexity 定期补新资料。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "X 创作者"
    },
    {
        "num": "147",
        "scenario": "编程",
        "title": "编程：Runtime + Claude Code/Codex /Gemini/OpenCode",
        "combo": "Runtime + Claude Code/Codex /Gemini/OpenCode",
        "id_slug": "runtime-claude-code-codex-gemini-opencode",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Runtime",
            "Claude Code",
            "Codex",
            "Gemini",
            "OpenCode"
        ],
        "steps": [
            "Runtime 提供沙箱、花费限制、文件保护和观测",
            "多 coding agent 在受控环境执行"
        ],
        "workflow": "Runtime 提供沙箱、花费限制、文件保护和观测；多 coding agent 在受控环境执行。",
        "outputs": [
            "生产级 agent 开发"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Runtime + Claude Code/Codex /Gemini/OpenCode。工具分工：Runtime 提供沙箱、花费限制、文件保护和观测；多 coding agent 在受控环境执行。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "生产级 agent 开发"
    },
    {
        "num": "148",
        "scenario": "编程",
        "title": "编程：Claude Code + /goal + GitHub",
        "combo": "Claude Code + /goal + GitHub",
        "id_slug": "claude-code-goal-github",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Claude Code",
            "goal",
            "GitHub"
        ],
        "steps": [
            "用 /goal 写多日执行计划",
            "Claude Code 实现",
            "GitHub PR 作为人工 checkpoint"
        ],
        "workflow": "用 /goal 写多日执行计划；Claude Code 实现；GitHub PR 作为人工 checkpoint。",
        "outputs": [
            "长任务工程"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Claude Code + /goal + GitHub。工具分工：用 /goal 写多日执行计划；Claude Code 实现；GitHub PR 作为人工 checkpoint。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "长任务工程"
    },
    {
        "num": "149",
        "scenario": "编程",
        "title": "编程：Insforge Skills + Claude Code",
        "combo": "Insforge Skills + Claude Code",
        "id_slug": "insforge-skills-claude-code",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Insforge Skills",
            "Claude Code"
        ],
        "steps": [
            "用 Insforge 做上下文工程，降低 token 消耗和错误率",
            "Claude Code 执行编码"
        ],
        "workflow": "用 Insforge 做上下文工程，降低 token 消耗和错误率；Claude Code 执行编码。",
        "outputs": [
            "高频 agent 使用者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Insforge Skills + Claude Code。工具分工：用 Insforge 做上下文工程，降低 token 消耗和错误率；Claude Code 执行编码。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "高频 agent 使用者"
    },
    {
        "num": "150",
        "scenario": "编程",
        "title": "编程：everything-claude-code + Cursor/Codex",
        "combo": "everything-claude-code + Cursor/Codex",
        "id_slug": "everything-claude-code-cursor-codex",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "everything-claude-code",
            "Cursor",
            "Codex"
        ],
        "steps": [
            "用预设 agents、skills、hooks 和安全扫描增强 Claude/Cursor/Codex 工作流"
        ],
        "workflow": "用预设 agents、skills、hooks 和安全扫描增强 Claude/Cursor/Codex 工作流。",
        "outputs": [
            "想快速搭 harness 的开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：everything-claude-code + Cursor/Codex。工具分工：用预设 agents、skills、hooks 和安全扫描增强 Claude/Cursor/Codex 工作流。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "想快速搭 harness 的开发者"
    },
    {
        "num": "151",
        "scenario": "编程",
        "title": "编程：OpenClaw + Hermes + Ollama",
        "combo": "OpenClaw + Hermes + Ollama",
        "id_slug": "openclaw-hermes-ollama",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "OpenClaw",
            "Hermes",
            "Ollama"
        ],
        "steps": [
            "OpenClaw/Hermes 编排",
            "Ollama 跑本地模型",
            "关键任务再切 Claude/ChatGPT"
        ],
        "workflow": "OpenClaw/Hermes 编排；Ollama 跑本地模型；关键任务再切 Claude/ChatGPT。",
        "outputs": [
            "本地/低成本优先"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：OpenClaw + Hermes + Ollama。工具分工：OpenClaw/Hermes 编排；Ollama 跑本地模型；关键任务再切 Claude/ChatGPT。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "本地/低成本优先"
    },
    {
        "num": "152",
        "scenario": "编程",
        "title": "编程：DeepSeek TUI + Git",
        "combo": "DeepSeek TUI + Git",
        "id_slug": "deepseek-tui-git",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "DeepSeek TUI",
            "Git"
        ],
        "steps": [
            "终端式 coding agent 处理 1M 上下文、子 agent、git 管理"
        ],
        "workflow": "终端式 coding agent 处理 1M 上下文、子 agent、git 管理。",
        "outputs": [
            "键盘流开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：DeepSeek TUI + Git。工具分工：终端式 coding agent 处理 1M 上下文、子 agent、git 管理。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "键盘流开发者"
    },
    {
        "num": "153",
        "scenario": "编程",
        "title": "编程：Letta Code + recall subagent",
        "combo": "Letta Code + recall subagent",
        "id_slug": "letta-code-recall-subagent",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Letta Code",
            "recall subagent"
        ],
        "steps": [
            "主 agent 执行任务",
            "recall 子 agent 从长记忆检索相关上下文"
        ],
        "workflow": "主 agent 执行任务；recall 子 agent 从长记忆检索相关上下文。",
        "outputs": [
            "长期代码库"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Letta Code + recall subagent。工具分工：主 agent 执行任务；recall 子 agent 从长记忆检索相关上下文。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "长期代码库"
    },
    {
        "num": "154",
        "scenario": "编程",
        "title": "编程：Entire CLI Skills + Claude/Codex",
        "combo": "Entire CLI Skills + Claude/Codex",
        "id_slug": "entire-cli-skills-claude-codex",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Entire CLI Skills",
            "Claude",
            "Codex"
        ],
        "steps": [
            "把 prompts、transcripts、决策和 commit context 暴露给 agent，改善交接"
        ],
        "workflow": "把 prompts、transcripts、决策和 commit context 暴露给 agent，改善交接。",
        "outputs": [
            "多人/多 agent 项目"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Entire CLI Skills + Claude/Codex。工具分工：把 prompts、transcripts、决策和 commit context 暴露给 agent，改善交接。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "多人/多 agent 项目"
    },
    {
        "num": "155",
        "scenario": "编程",
        "title": "编程：AutoSwarm + Claude/Gemini/Codex",
        "combo": "AutoSwarm + Claude/Gemini/Codex",
        "id_slug": "autoswarm-claude-gemini-codex",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "AutoSwarm",
            "Claude",
            "Gemini",
            "Codex"
        ],
        "steps": [
            "用 meta-agent 自动优化多 agent pipeline，从单点优化转向团队优化"
        ],
        "workflow": "用 meta-agent 自动优化多 agent pipeline，从单点优化转向团队优化。",
        "outputs": [
            "复杂自动化实验"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：AutoSwarm + Claude/Gemini/Codex。工具分工：用 meta-agent 自动优化多 agent pipeline，从单点优化转向团队优化。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "复杂自动化实验"
    },
    {
        "num": "156",
        "scenario": "编程",
        "title": "编程：AgentAuditKit + Laureum AI",
        "combo": "AgentAuditKit + Laureum AI",
        "id_slug": "agentauditkit-laureum-ai",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "AgentAuditKit",
            "Laureum AI"
        ],
        "steps": [
            "本地扫描 agent 安全",
            "Laureum/MCP 质量评分作为上线门禁"
        ],
        "workflow": "本地扫描 agent 安全；Laureum/MCP 质量评分作为上线门禁。",
        "outputs": [
            "agent 平台团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：AgentAuditKit + Laureum AI。工具分工：本地扫描 agent 安全；Laureum/MCP 质量评分作为上线门禁。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "agent 平台团队"
    },
    {
        "num": "157",
        "scenario": "编程",
        "title": "编程：SWE-CI + Opik Test Suites",
        "combo": "SWE-CI + Opik Test Suites",
        "id_slug": "swe-ci-opik-test-suites",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "SWE-CI",
            "Opik Test Suites"
        ],
        "steps": [
            "SWE-CI 检查长期维护回归",
            "Opik 从 traces 自动生成 agent 回归测试"
        ],
        "workflow": "SWE-CI 检查长期维护回归；Opik 从 traces 自动生成 agent 回归测试。",
        "outputs": [
            "AI 代码维护"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：SWE-CI + Opik Test Suites。工具分工：SWE-CI 检查长期维护回归；Opik 从 traces 自动生成 agent 回归测试。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "AI 代码维护"
    },
    {
        "num": "158",
        "scenario": "编程",
        "title": "编程：Kilo Code + Lovable",
        "combo": "Kilo Code + Lovable",
        "id_slug": "kilo-code-lovable",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Kilo Code",
            "Lovable"
        ],
        "steps": [
            "Lovable 快速生成 UI",
            "Kilo Code 在 VS Code 里接手工程化和修 bug"
        ],
        "workflow": "Lovable 快速生成 UI；Kilo Code 在 VS Code 里接手工程化和修 bug。",
        "outputs": [
            "MVP 到可维护代码"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Kilo Code + Lovable。工具分工：Lovable 快速生成 UI；Kilo Code 在 VS Code 里接手工程化和修 bug。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "MVP 到可维护代码"
    },
    {
        "num": "159",
        "scenario": "编程",
        "title": "编程：Windsurf + Claude Code + cc-switch",
        "combo": "Windsurf + Claude Code + cc-switch",
        "id_slug": "windsurf-claude-code-cc-switch",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Windsurf",
            "Claude Code",
            "cc-switch"
        ],
        "steps": [
            "Windsurf 做 IDE 代理",
            "Claude Code 做终端任务",
            "cc-switch 切模型/配置"
        ],
        "workflow": "Windsurf 做 IDE 代理；Claude Code 做终端任务；cc-switch 切模型/配置。",
        "outputs": [
            "多工具开发者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Windsurf + Claude Code + cc-switch。工具分工：Windsurf 做 IDE 代理；Claude Code 做终端任务；cc-switch 切模型/配置。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 85,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "多工具开发者"
    },
    {
        "num": "160",
        "scenario": "编程",
        "title": "编程：Google ADK + Gemini + LangGraph",
        "combo": "Google ADK + Gemini + LangGraph",
        "id_slug": "google-adk-gemini-langgraph",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Google ADK",
            "Gemini",
            "LangGraph"
        ],
        "steps": [
            "Google ADK 构建 Gemini agent",
            "LangGraph 控流程和状态"
        ],
        "workflow": "Google ADK 构建 Gemini agent；LangGraph 控流程和状态。",
        "outputs": [
            "Google 云/agent 工程"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：编程：Google ADK + Gemini + LangGraph。工具分工：Google ADK 构建 Gemini agent；LangGraph 控流程和状态。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "Google 云/agent 工程"
    },
    {
        "num": "161",
        "scenario": "数据",
        "title": "数据：Databricks Genie Code + Spark",
        "combo": "Databricks Genie Code + Spark",
        "id_slug": "databricks-genie-code-spark",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Databricks Genie Code",
            "Spark"
        ],
        "steps": [
            "自然语言生成/调试 Spark pipelines",
            "Claude 写业务解释和数据质量报告"
        ],
        "workflow": "自然语言生成/调试 Spark pipelines；Claude 写业务解释和数据质量报告。",
        "outputs": [
            "数据工程"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Databricks Genie Code + Spark。工具分工：自然语言生成/调试 Spark pipelines；Claude 写业务解释和数据质量报告。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "数据工程"
    },
    {
        "num": "162",
        "scenario": "数据",
        "title": "数据：OpenSRE + Slack/PagerDuty/Grafana",
        "combo": "OpenSRE + Slack/PagerDuty/Grafana",
        "id_slug": "opensre-slack-pagerduty-grafana",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "OpenSRE",
            "Slack",
            "PagerDuty",
            "Grafana"
        ],
        "steps": [
            "OpenSRE 连接 60+ 工具做 incident 测试和诊断",
            "Slack 分发修复建议"
        ],
        "workflow": "OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。",
        "outputs": [
            "SRE/DevOps"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：OpenSRE + Slack/PagerDuty/Grafana。工具分工：OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "SRE/DevOps"
    },
    {
        "num": "163",
        "scenario": "数据",
        "title": "数据：Spectrum + Claude",
        "combo": "Spectrum + Claude",
        "id_slug": "spectrum-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Spectrum",
            "Claude"
        ],
        "steps": [
            "统一 iMessage/WhatsApp/Telegram/Slack/SMS 入口",
            "Claude 分类、回复和路由"
        ],
        "workflow": "统一 iMessage/WhatsApp/Telegram/Slack/SMS 入口；Claude 分类、回复和路由。",
        "outputs": [
            "客服/社群运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Spectrum + Claude。工具分工：统一 iMessage/WhatsApp/Telegram/Slack/SMS 入口；Claude 分类、回复和路由。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客服/社群运营"
    },
    {
        "num": "164",
        "scenario": "数据",
        "title": "数据：OpenClaw + Gemma + Ollama",
        "combo": "OpenClaw + Gemma + Ollama",
        "id_slug": "openclaw-gemma-ollama",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "OpenClaw",
            "Gemma",
            "Ollama"
        ],
        "steps": [
            "本地私有 AI stack，避免云锁定",
            "用于摘要、分类、提取和内部问答"
        ],
        "workflow": "本地私有 AI stack，避免云锁定；用于摘要、分类、提取和内部问答。",
        "outputs": [
            "隐私敏感团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：OpenClaw + Gemma + Ollama。工具分工：本地私有 AI stack，避免云锁定；用于摘要、分类、提取和内部问答。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "隐私敏感团队"
    },
    {
        "num": "165",
        "scenario": "数据",
        "title": "数据：Bifrost + LangGraph + n8n",
        "combo": "Bifrost + LangGraph + n8n",
        "id_slug": "bifrost-langgraph-n8n",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Bifrost",
            "LangGraph",
            "n8n"
        ],
        "steps": [
            "Bifrost 做模型路由和成本控制",
            "LangGraph 管 agent 状态",
            "n8n 接业务系统"
        ],
        "workflow": "Bifrost 做模型路由和成本控制；LangGraph 管 agent 状态；n8n 接业务系统。",
        "outputs": [
            "生产自动化"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：数据：Bifrost + LangGraph + n8n。工具分工：Bifrost 做模型路由和成本控制；LangGraph 管 agent 状态；n8n 接业务系统。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "生产自动化"
    },
    {
        "num": "166",
        "scenario": "会议",
        "title": "会议：Granola + Claude + Linear",
        "combo": "Granola + Claude + Linear",
        "id_slug": "granola-claude-linear",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Granola",
            "Claude",
            "Linear"
        ],
        "steps": [
            "Granola 做轻量会议笔记",
            "Claude 提炼需求",
            "Linear 建 issue"
        ],
        "workflow": "Granola 做轻量会议笔记；Claude 提炼需求；Linear 建 issue。",
        "outputs": [
            "产品/工程会议"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Granola + Claude + Linear。工具分工：Granola 做轻量会议笔记；Claude 提炼需求；Linear 建 issue。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "产品/工程会议"
    },
    {
        "num": "167",
        "scenario": "会议",
        "title": "会议：Tactiq + Claude + HubSpot",
        "combo": "Tactiq + Claude + HubSpot",
        "id_slug": "tactiq-claude-hubspot",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Tactiq",
            "Claude",
            "HubSpot"
        ],
        "steps": [
            "Tactiq 转写销售电话",
            "Claude 生成摘要和风险",
            "HubSpot 更新字段"
        ],
        "workflow": "Tactiq 转写销售电话；Claude 生成摘要和风险；HubSpot 更新字段。",
        "outputs": [
            "销售团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Tactiq + Claude + HubSpot。工具分工：Tactiq 转写销售电话；Claude 生成摘要和风险；HubSpot 更新字段。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售团队"
    },
    {
        "num": "168",
        "scenario": "会议",
        "title": "会议：Superhuman Go + HeyGen Agent",
        "combo": "Superhuman Go + HeyGen Agent",
        "id_slug": "superhuman-go-heygen-agent",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Superhuman Go",
            "HeyGen Agent"
        ],
        "steps": [
            "把邮件/更新转成视频或语音，减少会议和反复 follow-up"
        ],
        "workflow": "把邮件/更新转成视频或语音，减少会议和反复 follow-up。",
        "outputs": [
            "异步管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Superhuman Go + HeyGen Agent。工具分工：把邮件/更新转成视频或语音，减少会议和反复 follow-up。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "异步管理"
    },
    {
        "num": "169",
        "scenario": "会议",
        "title": "会议：LiveKit Agent Console + Pipecat",
        "combo": "LiveKit Agent Console + Pipecat",
        "id_slug": "livekit-agent-console-pipecat",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "LiveKit Agent Console",
            "Pipecat"
        ],
        "steps": [
            "Pipecat 构建实时语音 agent",
            "LiveKit Console 调试延迟、工具调用和流水线"
        ],
        "workflow": "Pipecat 构建实时语音 agent；LiveKit Console 调试延迟、工具调用和流水线。",
        "outputs": [
            "语音 agent 团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：LiveKit Agent Console + Pipecat。工具分工：Pipecat 构建实时语音 agent；LiveKit Console 调试延迟、工具调用和流水线。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "语音 agent 团队"
    },
    {
        "num": "170",
        "scenario": "会议",
        "title": "会议：Deepgram + Together + Claude",
        "combo": "Deepgram + Together + Claude",
        "id_slug": "deepgram-together-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Deepgram",
            "Together",
            "Claude"
        ],
        "steps": [
            "Deepgram 语音转文本",
            "Together 跑模型",
            "Claude 做纪要/行动项"
        ],
        "workflow": "Deepgram 语音转文本；Together 跑模型；Claude 做纪要/行动项。",
        "outputs": [
            "语音应用"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：会议：Deepgram + Together + Claude。工具分工：Deepgram 语音转文本；Together 跑模型；Claude 做纪要/行动项。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "语音应用"
    },
    {
        "num": "171",
        "scenario": "自动化",
        "title": "自动化：Claude + n8n",
        "combo": "Claude + n8n",
        "id_slug": "claude-n8n",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Claude",
            "n8n"
        ],
        "steps": [
            "Claude 生成流程草稿和 JS/JSON",
            "n8n 负责 webhook、重试、鉴权、日志和人工调试"
        ],
        "workflow": "Claude 生成流程草稿和 JS/JSON；n8n 负责 webhook、重试、鉴权、日志和人工调试。",
        "outputs": [
            "业务自动化"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Claude + n8n。工具分工：Claude 生成流程草稿和 JS/JSON；n8n 负责 webhook、重试、鉴权、日志和人工调试。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "业务自动化"
    },
    {
        "num": "172",
        "scenario": "自动化",
        "title": "自动化：ChatGPT + n8n error logs",
        "combo": "ChatGPT + n8n error logs",
        "id_slug": "chatgpt-n8n-error-logs",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ChatGPT",
            "n8n error logs"
        ],
        "steps": [
            "把 n8n 报错和 execution data 丢给 ChatGPT，解释数据结构并给修复表达式"
        ],
        "workflow": "把 n8n 报错和 execution data 丢给 ChatGPT，解释数据结构并给修复表达式。",
        "outputs": [
            "n8n 初学者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：ChatGPT + n8n error logs。工具分工：把 n8n 报错和 execution data 丢给 ChatGPT，解释数据结构并给修复表达式。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "n8n 初学者"
    },
    {
        "num": "173",
        "scenario": "自动化",
        "title": "自动化：Zapier quick glue + n8n heavy logic",
        "combo": "Zapier quick glue + n8n heavy logic",
        "id_slug": "zapier-quick-glue-n8n-heavy-logic",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Zapier quick glue",
            "n8n heavy logic"
        ],
        "steps": [
            "Zapier 处理简单跨 app 触发",
            "复杂状态、循环、错误处理放 n8n"
        ],
        "workflow": "Zapier 处理简单跨 app 触发；复杂状态、循环、错误处理放 n8n。",
        "outputs": [
            "中小企业运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Zapier quick glue + n8n heavy logic。工具分工：Zapier 处理简单跨 app 触发；复杂状态、循环、错误处理放 n8n。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "中小企业运营"
    },
    {
        "num": "174",
        "scenario": "自动化",
        "title": "自动化：Make Grid + Claude",
        "combo": "Make Grid + Claude",
        "id_slug": "make-grid-claude",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Make Grid",
            "Claude"
        ],
        "steps": [
            "Make Grid 管复杂自动化版图",
            "Claude 写节点逻辑、文档和异常处理说明"
        ],
        "workflow": "Make Grid 管复杂自动化版图；Claude 写节点逻辑、文档和异常处理说明。",
        "outputs": [
            "自动化顾问"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Make Grid + Claude。工具分工：Make Grid 管复杂自动化版图；Claude 写节点逻辑、文档和异常处理说明。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "自动化顾问"
    },
    {
        "num": "175",
        "scenario": "自动化",
        "title": "自动化：Pipedream + OpenAI/Claude API",
        "combo": "Pipedream + OpenAI/Claude API",
        "id_slug": "pipedream-openai-claude-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Pipedream",
            "OpenAI",
            "Claude API"
        ],
        "steps": [
            "Pipedream 写轻量 serverless workflow",
            "模型负责摘要、分类、回复"
        ],
        "workflow": "Pipedream 写轻量 serverless workflow；模型负责摘要、分类、回复。",
        "outputs": [
            "开发型运营"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Pipedream + OpenAI/Claude API。工具分工：Pipedream 写轻量 serverless workflow；模型负责摘要、分类、回复。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 84,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "开发型运营"
    },
    {
        "num": "176",
        "scenario": "自动化",
        "title": "自动化：Runable + ChatGPT",
        "combo": "Runable + ChatGPT",
        "id_slug": "runable-chatgpt",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Runable",
            "ChatGPT"
        ],
        "steps": [
            "一个 prompt 触发多步骤链路",
            "ChatGPT 生成每步文案和条件判断"
        ],
        "workflow": "一个 prompt 触发多步骤链路；ChatGPT 生成每步文案和条件判断。",
        "outputs": [
            "轻量运营自动化"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：Runable + ChatGPT。工具分工：一个 prompt 触发多步骤链路；ChatGPT 生成每步文案和条件判断。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "轻量运营自动化"
    },
    {
        "num": "177",
        "scenario": "自动化",
        "title": "自动化：MindStudio + Claude/ChatGPT",
        "combo": "MindStudio + Claude/ChatGPT",
        "id_slug": "mindstudio-claude-chatgpt",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "MindStudio",
            "Claude",
            "ChatGPT"
        ],
        "steps": [
            "MindStudio 搭多步骤 AI workflow",
            "Claude/ChatGPT 分别处理推理和通用输出"
        ],
        "workflow": "MindStudio 搭多步骤 AI workflow；Claude/ChatGPT 分别处理推理和通用输出。",
        "outputs": [
            "非工程团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：MindStudio + Claude/ChatGPT。工具分工：MindStudio 搭多步骤 AI workflow；Claude/ChatGPT 分别处理推理和通用输出。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "非工程团队"
    },
    {
        "num": "178",
        "scenario": "自动化",
        "title": "自动化：ServiceNow Build Agent + Claude",
        "combo": "ServiceNow Build Agent + Claude",
        "id_slug": "servicenow-build-agent-claude",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ServiceNow Build Agent",
            "Claude"
        ],
        "steps": [
            "用自然语言构建企业 app/workflow",
            "Claude 作为复杂推理和代码生成核心"
        ],
        "workflow": "用自然语言构建企业 app/workflow；Claude 作为复杂推理和代码生成核心。",
        "outputs": [
            "企业 IT"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：ServiceNow Build Agent + Claude。工具分工：用自然语言构建企业 app/workflow；Claude 作为复杂推理和代码生成核心。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "企业 IT"
    },
    {
        "num": "179",
        "scenario": "自动化",
        "title": "自动化：ServiceNow Action Fabric + Claude/Copilot",
        "combo": "ServiceNow Action Fabric + Claude/Copilot",
        "id_slug": "servicenow-action-fabric-claude-copilot",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ServiceNow Action Fabric",
            "Claude",
            "Copilot"
        ],
        "steps": [
            "任何 agent 直接触发 ServiceNow onboarding、审批、工单等系统动作，并由平台治理"
        ],
        "workflow": "任何 agent 直接触发 ServiceNow onboarding、审批、工单等系统动作，并由平台治理。",
        "outputs": [
            "大型企业"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：ServiceNow Action Fabric + Claude/Copilot。工具分工：任何 agent 直接触发 ServiceNow onboarding、审批、工单等系统动作，并由平台治理。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "大型企业"
    },
    {
        "num": "180",
        "scenario": "自动化",
        "title": "自动化：ServiceNow AI Control Tower + OpenAI/Anthropic agents",
        "combo": "ServiceNow AI Control Tower + OpenAI/Anthropic agents",
        "id_slug": "servicenow-ai-control-tower-openai-anthropic-agents",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ServiceNow AI Control Tower",
            "OpenAI",
            "Anthropic agents"
        ],
        "steps": [
            "统一发现、观测、治理和必要时关闭越权 agent"
        ],
        "workflow": "统一发现、观测、治理和必要时关闭越权 agent。",
        "outputs": [
            "AI 治理团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：自动化：ServiceNow AI Control Tower + OpenAI/Anthropic agents。工具分工：统一发现、观测、治理和必要时关闭越权 agent。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "AI 治理团队"
    },
    {
        "num": "181",
        "scenario": "设计",
        "title": "设计：Gamma Imagine + Claude",
        "combo": "Gamma Imagine + Claude",
        "id_slug": "gamma-imagine-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Gamma Imagine",
            "Claude"
        ],
        "steps": [
            "Claude 生成故事线和视觉 brief",
            "Gamma Imagine 生成图形和 deck"
        ],
        "workflow": "Claude 生成故事线和视觉 brief；Gamma Imagine 生成图形和 deck。",
        "outputs": [
            "品牌/销售内容"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Gamma Imagine + Claude。工具分工：Claude 生成故事线和视觉 brief；Gamma Imagine 生成图形和 deck。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "品牌/销售内容"
    },
    {
        "num": "182",
        "scenario": "设计",
        "title": "设计：Canva AI + Adobe Express",
        "combo": "Canva AI + Adobe Express",
        "id_slug": "canva-ai-adobe-express",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Canva AI",
            "Adobe Express"
        ],
        "steps": [
            "Canva 做社媒和 deck",
            "Adobe Express 做轻量图形补充",
            "ChatGPT/Claude 写文案"
        ],
        "workflow": "Canva 做社媒和 deck；Adobe Express 做轻量图形补充；ChatGPT/Claude 写文案。",
        "outputs": [
            "低预算创作"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Canva AI + Adobe Express。工具分工：Canva 做社媒和 deck；Adobe Express 做轻量图形补充；ChatGPT/Claude 写文案。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "低预算创作"
    },
    {
        "num": "183",
        "scenario": "设计",
        "title": "设计：Claude + Adobe + Blender",
        "combo": "Claude + Adobe + Blender",
        "id_slug": "claude-adobe-blender",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Claude",
            "Adobe",
            "Blender"
        ],
        "steps": [
            "Claude 在 Adobe 做素材/视频批处理，在 Blender 做 3D 场景脚本，连接跨媒体资产"
        ],
        "workflow": "Claude 在 Adobe 做素材/视频批处理，在 Blender 做 3D 场景脚本，连接跨媒体资产。",
        "outputs": [
            "创意工作室"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Claude + Adobe + Blender。工具分工：Claude 在 Adobe 做素材/视频批处理，在 Blender 做 3D 场景脚本，连接跨媒体资产。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "创意工作室"
    },
    {
        "num": "184",
        "scenario": "设计",
        "title": "设计：PhysiOpt + Gemini/Claude",
        "combo": "PhysiOpt + Gemini/Claude",
        "id_slug": "physiopt-gemini-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "PhysiOpt",
            "Gemini",
            "Claude"
        ],
        "steps": [
            "生成式设计后用物理仿真校验",
            "Claude/Gemini 解释约束和优化方向"
        ],
        "workflow": "生成式设计后用物理仿真校验；Claude/Gemini 解释约束和优化方向。",
        "outputs": [
            "工程设计"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：PhysiOpt + Gemini/Claude。工具分工：生成式设计后用物理仿真校验；Claude/Gemini 解释约束和优化方向。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "工程设计"
    },
    {
        "num": "185",
        "scenario": "设计",
        "title": "设计：Magnific + Midjourney + Claude",
        "combo": "Magnific + Midjourney + Claude",
        "id_slug": "magnific-midjourney-claude",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "Magnific",
            "Midjourney",
            "Claude"
        ],
        "steps": [
            "Midjourney 出概念图",
            "Magnific 放大/增强",
            "Claude 写视觉规范"
        ],
        "workflow": "Midjourney 出概念图；Magnific 放大/增强；Claude 写视觉规范。",
        "outputs": [
            "视觉提案"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：设计：Magnific + Midjourney + Claude。工具分工：Midjourney 出概念图；Magnific 放大/增强；Claude 写视觉规范。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "视觉提案"
    },
    {
        "num": "186",
        "scenario": "音视频",
        "title": "音视频：Hermes + HyperFrames",
        "combo": "Hermes + HyperFrames",
        "id_slug": "hermes-hyperframes",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Hermes",
            "HyperFrames"
        ],
        "steps": [
            "Hermes agent 写 HTML/场景",
            "HyperFrames 渲染 MP4，无需传统时间线编辑"
        ],
        "workflow": "Hermes agent 写 HTML/场景；HyperFrames 渲染 MP4，无需传统时间线编辑。",
        "outputs": [
            "agentic 视频原型"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：Hermes + HyperFrames。工具分工：Hermes agent 写 HTML/场景；HyperFrames 渲染 MP4，无需传统时间线编辑。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "agentic 视频原型"
    },
    {
        "num": "187",
        "scenario": "音视频",
        "title": "音视频：HeyGen Agent + Superhuman Go",
        "combo": "HeyGen Agent + Superhuman Go",
        "id_slug": "heygen-agent-superhuman-go",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "HeyGen Agent",
            "Superhuman Go"
        ],
        "steps": [
            "把邮件更新、销售跟进、内部通知转成个性化视频/语音"
        ],
        "workflow": "把邮件更新、销售跟进、内部通知转成个性化视频/语音。",
        "outputs": [
            "异步沟通"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：HeyGen Agent + Superhuman Go。工具分工：把邮件更新、销售跟进、内部通知转成个性化视频/语音。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "异步沟通"
    },
    {
        "num": "188",
        "scenario": "音视频",
        "title": "音视频：xAI Custom Voices + Grok API",
        "combo": "xAI Custom Voices + Grok API",
        "id_slug": "xai-custom-voices-grok-api",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "xAI Custom Voices",
            "Grok API"
        ],
        "steps": [
            "快速克隆并部署多语言语音",
            "Grok/Claude 写脚本和对话流"
        ],
        "workflow": "快速克隆并部署多语言语音；Grok/Claude 写脚本和对话流。",
        "outputs": [
            "语音产品"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：xAI Custom Voices + Grok API。工具分工：快速克隆并部署多语言语音；Grok/Claude 写脚本和对话流。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "语音产品"
    },
    {
        "num": "189",
        "scenario": "音视频",
        "title": "音视频：CapCut + Gemini image + ChatGPT",
        "combo": "CapCut + Gemini image + ChatGPT",
        "id_slug": "capcut-gemini-image-chatgpt",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "CapCut",
            "Gemini image",
            "ChatGPT"
        ],
        "steps": [
            "Gemini 生成基础图片",
            "ChatGPT 写脚本/标题",
            "CapCut 剪辑发布"
        ],
        "workflow": "Gemini 生成基础图片；ChatGPT 写脚本/标题；CapCut 剪辑发布。",
        "outputs": [
            "短视频"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：音视频：CapCut + Gemini image + ChatGPT。工具分工：Gemini 生成基础图片；ChatGPT 写脚本/标题；CapCut 剪辑发布。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "短视频"
    },
    {
        "num": "190",
        "scenario": "商务",
        "title": "商务：Devi AI + Claude",
        "combo": "Devi AI + Claude",
        "id_slug": "devi-ai-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Devi AI",
            "Claude"
        ],
        "steps": [
            "Devi 监控社媒社区线索",
            "Claude 生成个性化触达和跟进策略"
        ],
        "workflow": "Devi 监控社媒社区线索；Claude 生成个性化触达和跟进策略。",
        "outputs": [
            "社群获客"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Devi AI + Claude。工具分工：Devi 监控社媒社区线索；Claude 生成个性化触达和跟进策略。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "社群获客"
    },
    {
        "num": "191",
        "scenario": "商务",
        "title": "商务：Bookkeeping.ai + ChatGPT",
        "combo": "Bookkeeping.ai + ChatGPT",
        "id_slug": "bookkeeping-ai-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Bookkeeping.ai",
            "ChatGPT"
        ],
        "steps": [
            "Bookkeeping.ai 做财务 admin",
            "ChatGPT 解释现金流、异常和待办"
        ],
        "workflow": "Bookkeeping.ai 做财务 admin；ChatGPT 解释现金流、异常和待办。",
        "outputs": [
            "小企业财务"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Bookkeeping.ai + ChatGPT。工具分工：Bookkeeping.ai 做财务 admin；ChatGPT 解释现金流、异常和待办。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 83,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "小企业财务"
    },
    {
        "num": "192",
        "scenario": "商务",
        "title": "商务：Close + Gamma + Claude",
        "combo": "Close + Gamma + Claude",
        "id_slug": "close-gamma-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Close",
            "Gamma",
            "Claude"
        ],
        "steps": [
            "Close 追踪机会",
            "Claude 写邮件和提案",
            "Gamma 生成客户 deck"
        ],
        "workflow": "Close 追踪机会；Claude 写邮件和提案；Gamma 生成客户 deck。",
        "outputs": [
            "销售团队"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Close + Gamma + Claude。工具分工：Close 追踪机会；Claude 写邮件和提案；Gamma 生成客户 deck。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "销售团队"
    },
    {
        "num": "193",
        "scenario": "商务",
        "title": "商务：YourGPT + Zendesk + Claude",
        "combo": "YourGPT + Zendesk + Claude",
        "id_slug": "yourgpt-zendesk-claude",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "YourGPT",
            "Zendesk",
            "Claude"
        ],
        "steps": [
            "YourGPT 处理客服自动回复",
            "Zendesk 管工单",
            "Claude 做升级问题摘要"
        ],
        "workflow": "YourGPT 处理客服自动回复；Zendesk 管工单；Claude 做升级问题摘要。",
        "outputs": [
            "客服自动化"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：YourGPT + Zendesk + Claude。工具分工：YourGPT 处理客服自动回复；Zendesk 管工单；Claude 做升级问题摘要。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "客服自动化"
    },
    {
        "num": "194",
        "scenario": "商务",
        "title": "商务：Alsona + ChatGPT",
        "combo": "Alsona + ChatGPT",
        "id_slug": "alsona-chatgpt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Alsona",
            "ChatGPT"
        ],
        "steps": [
            "Alsona 管多账号 LinkedIn 外联",
            "ChatGPT 写不同 persona 的跟进文案"
        ],
        "workflow": "Alsona 管多账号 LinkedIn 外联；ChatGPT 写不同 persona 的跟进文案。",
        "outputs": [
            "LinkedIn outbound"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Alsona + ChatGPT。工具分工：Alsona 管多账号 LinkedIn 外联；ChatGPT 写不同 persona 的跟进文案。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "LinkedIn outbound"
    },
    {
        "num": "195",
        "scenario": "商务",
        "title": "商务：Brew + Claude + Notion",
        "combo": "Brew + Claude + Notion",
        "id_slug": "brew-claude-notion",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Brew",
            "Claude",
            "Notion"
        ],
        "steps": [
            "Brew 做邮件营销自动化",
            "Claude 写内容计划",
            "Notion 管 campaign"
        ],
        "workflow": "Brew 做邮件营销自动化；Claude 写内容计划；Notion 管 campaign。",
        "outputs": [
            "邮件营销"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：商务：Brew + Claude + Notion。工具分工：Brew 做邮件营销自动化；Claude 写内容计划；Notion 管 campaign。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "邮件营销"
    },
    {
        "num": "196",
        "scenario": "个人效率",
        "title": "个人效率：Wispr Flow + Claude",
        "combo": "Wispr Flow + Claude",
        "id_slug": "wispr-flow-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Wispr Flow",
            "Claude"
        ],
        "steps": [
            "Wispr Flow 语音输入想法",
            "Claude 整理为任务、邮件、文章或计划"
        ],
        "workflow": "Wispr Flow 语音输入想法；Claude 整理为任务、邮件、文章或计划。",
        "outputs": [
            "移动办公"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：Wispr Flow + Claude。工具分工：Wispr Flow 语音输入想法；Claude 整理为任务、邮件、文章或计划。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "移动办公"
    },
    {
        "num": "197",
        "scenario": "个人效率",
        "title": "个人效率：Clico + ChatGPT/Claude",
        "combo": "Clico + ChatGPT/Claude",
        "id_slug": "clico-chatgpt-claude",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Clico",
            "ChatGPT",
            "Claude"
        ],
        "steps": [
            "Clico 减少在浏览器工具间复制粘贴",
            "ChatGPT/Claude 保持上下文"
        ],
        "workflow": "Clico 减少在浏览器工具间复制粘贴；ChatGPT/Claude 保持上下文。",
        "outputs": [
            "浏览器优先工作流"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：Clico + ChatGPT/Claude。工具分工：Clico 减少在浏览器工具间复制粘贴；ChatGPT/Claude 保持上下文。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "浏览器优先工作流"
    },
    {
        "num": "198",
        "scenario": "个人效率",
        "title": "个人效率：Obsidian Vault + coding agents",
        "combo": "Obsidian Vault + coding agents",
        "id_slug": "obsidian-vault-coding-agents",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Obsidian Vault",
            "coding agents"
        ],
        "steps": [
            "Obsidian 做持久项目记忆",
            "Claude Code/Codex 读取上下文后执行任务"
        ],
        "workflow": "Obsidian 做持久项目记忆；Claude Code/Codex 读取上下文后执行任务。",
        "outputs": [
            "长期个人项目"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：Obsidian Vault + coding agents。工具分工：Obsidian 做持久项目记忆；Claude Code/Codex 读取上下文后执行任务。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "长期个人项目"
    },
    {
        "num": "199",
        "scenario": "个人效率",
        "title": "个人效率：Todoist + Calendar + ChatGPT",
        "combo": "Todoist + Calendar + ChatGPT",
        "id_slug": "todoist-calendar-chatgpt",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Todoist",
            "Calendar",
            "ChatGPT"
        ],
        "steps": [
            "ChatGPT 把目标拆成任务和日程",
            "Todoist/Calendar 负责执行提醒"
        ],
        "workflow": "ChatGPT 把目标拆成任务和日程；Todoist/Calendar 负责执行提醒。",
        "outputs": [
            "个人管理"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：Todoist + Calendar + ChatGPT。工具分工：ChatGPT 把目标拆成任务和日程；Todoist/Calendar 负责执行提醒。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "个人管理"
    },
    {
        "num": "200",
        "scenario": "个人效率",
        "title": "个人效率：One-person team stack: Perplexity + Claude + Cursor + Gamma + Zapier/n8n",
        "combo": "One-person team stack: Perplexity + Claude + Cursor + Gamma + Zapier/n8n",
        "id_slug": "one-person-team-stack-perplexity-claude-cursor-gamma-zapier-n8n",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Perplexity",
            "Claude",
            "Cursor",
            "Gamma",
            "Zapier",
            "n8n"
        ],
        "steps": [
            "Perplexity 研究，Claude 决策/写作，Cursor 实现，Gamma 表达，Zapier/n8n 自动化"
        ],
        "workflow": "Perplexity 研究，Claude 决策/写作，Cursor 实现，Gamma 表达，Zapier/n8n 自动化。",
        "outputs": [
            "单人创业者"
        ],
        "summary": "来自《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的工具组合：个人效率：One-person team stack: Perplexity + Claude + Cursor + Gamma + Zapier/n8n。工具分工：Perplexity 研究，Claude 决策/写作，Cursor 实现，Gamma 表达，Zapier/n8n 自动化。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "importance": 82,
        "source_section": "ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf",
        "audience": "单人创业者"
    }
]

EXPANDED_AI_TOOL_SKILLS = [
    {
        "id": "expanded-tool-claude",
        "name": "用 Claude 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Claude",
        "stage": "workflow",
        "description": "Claude 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Claude 先把访谈/资料整理成叙事大纲、页标题、每页要点",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Claude 先把访谈/资料整理成叙事大纲、页标题、每页要点；Gamma 生成初版 deck；Claude 再做逻辑审稿和演讲稿。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gamma",
        "name": "用 Gamma 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Gamma",
        "stage": "workflow",
        "description": "Gamma 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Gamma 生成初版 deck",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Claude 先把访谈/资料整理成叙事大纲、页标题、每页要点；Gamma 生成初版 deck；Claude 再做逻辑审稿和演讲稿。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt-deep-research",
        "name": "用 ChatGPT Deep Research 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "ChatGPT Deep Research",
        "stage": "workflow",
        "description": "ChatGPT Deep Research 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：ChatGPT 深研收集市场/竞品/引用",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 深研收集市场/竞品/引用；输出结构化简报；Gamma 变成演示文稿；人工补品牌视觉。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-perplexity",
        "name": "用 Perplexity 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Perplexity",
        "stage": "workflow",
        "description": "Perplexity 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Perplexity 找带来源的信息",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 找带来源的信息；Claude 压成故事线；Canva 套品牌模板生成图文页。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-canva",
        "name": "用 Canva 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Canva",
        "stage": "workflow",
        "description": "Canva 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Canva 套品牌模板生成图文页",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 找带来源的信息；Claude 压成故事线；Canva 套品牌模板生成图文页。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt",
        "name": "用 ChatGPT 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "ChatGPT",
        "stage": "workflow",
        "description": "ChatGPT 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：在 ChatGPT 里沉淀定位、标语、页面结构",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "在 ChatGPT 里沉淀定位、标语、页面结构；调用 Canva app 直接生成宣传页或简报。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-canva-app",
        "name": "用 Canva app 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Canva app",
        "stage": "workflow",
        "description": "Canva app 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：调用 Canva app 直接生成宣传页或简报",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "在 ChatGPT 里沉淀定位、标语、页面结构；调用 Canva app 直接生成宣传页或简报。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-design",
        "name": "用 Claude Design 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Claude Design",
        "stage": "workflow",
        "description": "Claude Design 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Claude Design 快速探索界面/产品概念",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Claude Design 快速探索界面/产品概念；导出到 Canva；再做视觉统一和版式整理。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-notebooklm",
        "name": "用 NotebookLM 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "NotebookLM",
        "stage": "workflow",
        "description": "NotebookLM 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：NotebookLM 汇总长资料和音视频",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "NotebookLM 汇总长资料和音视频；Claude 提炼核心观点；Gamma 生成培训/分享 PPT。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-google-drive-connector",
        "name": "用 Google Drive connector 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Google Drive connector",
        "stage": "workflow",
        "description": "Google Drive connector 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：ChatGPT 读取 Drive 内文档，生成会议汇报结构；再用 Slides 或 Canva 做版式。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 读取 Drive 内文档，生成会议汇报结构；再用 Slides 或 Canva 做版式。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-slides",
        "name": "用 Slides 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Slides",
        "stage": "workflow",
        "description": "Slides 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：再用 Slides 或 Canva 做版式",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 读取 Drive 内文档，生成会议汇报结构；再用 Slides 或 Canva 做版式。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-notion-connector",
        "name": "用 Notion connector 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Notion connector",
        "stage": "workflow",
        "description": "Notion connector 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Claude 搜 Notion 项目资料，生成客户化方案",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Claude 搜 Notion 项目资料，生成客户化方案；Gamma 输出 deck；Notion 回写版本记录。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-genspark",
        "name": "用 Genspark 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Genspark",
        "stage": "workflow",
        "description": "Genspark 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：让代理先做网页调研和资料收集；Claude 做去噪和观点排序；Gamma 出简报。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "让代理先做网页调研和资料收集；Claude 做去噪和观点排序；Gamma 出简报。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-manus",
        "name": "用 Manus 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Manus",
        "stage": "workflow",
        "description": "Manus 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：让代理先做网页调研和资料收集；Claude 做去噪和观点排序；Gamma 出简报。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "让代理先做网页调研和资料收集；Claude 做去噪和观点排序；Gamma 出简报。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gemini",
        "name": "用 Gemini 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Gemini",
        "stage": "workflow",
        "description": "Gemini 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Gemini 从 Docs/Sheets 摘要数据",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Gemini 从 Docs/Sheets 摘要数据；Canva 生成视觉稿；ChatGPT/Claude 做文案润色。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-google-workspace",
        "name": "用 Google Workspace 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Google Workspace",
        "stage": "workflow",
        "description": "Google Workspace 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Gemini 从 Docs/Sheets 摘要数据；Canva 生成视觉稿；ChatGPT/Claude 做文案润色。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Gemini 从 Docs/Sheets 摘要数据；Canva 生成视觉稿；ChatGPT/Claude 做文案润色。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-notion",
        "name": "用 Notion 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Notion",
        "stage": "workflow",
        "description": "Notion 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Notion 保存知识库与复用模板",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 建引用清单；ChatGPT 做问答/表格；Notion 保存知识库与复用模板。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-notion-ai",
        "name": "用 Notion AI 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Notion AI",
        "stage": "workflow",
        "description": "Notion AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Notion AI 把结果嵌入项目页、任务页、数据库",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Claude 做长文档理解和推理；Notion AI 把结果嵌入项目页、任务页、数据库。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-sharepoint-connector",
        "name": "用 SharePoint connector 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "SharePoint connector",
        "stage": "workflow",
        "description": "SharePoint connector 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：ChatGPT 从 SharePoint 找内部制度、历史报告、模板",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 从 SharePoint 找内部制度、历史报告、模板；生成带出处的内部问答。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-elicit",
        "name": "用 Elicit 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Elicit",
        "stage": "workflow",
        "description": "Elicit 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Elicit 找论文",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 找现实资料；Elicit 找论文；Claude 做文献综述和研究假设。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-consensus",
        "name": "用 Consensus 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Consensus",
        "stage": "workflow",
        "description": "Consensus 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Consensus 查论文证据",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成问题树；Consensus 查论文证据；Zotero 管引用。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-zotero",
        "name": "用 Zotero 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Zotero",
        "stage": "workflow",
        "description": "Zotero 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Zotero 管引用",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成问题树；Consensus 查论文证据；Zotero 管引用。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-grok",
        "name": "用 Grok 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Grok",
        "stage": "workflow",
        "description": "Grok 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Grok 抓 X 实时舆情",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Grok 抓 X 实时舆情；Perplexity 验证外部来源；Claude 写洞察摘要。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-grammarly",
        "name": "用 Grammarly 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Grammarly",
        "stage": "workflow",
        "description": "Grammarly 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Grammarly 做语法、语气、清晰度 QA",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Claude 起草长文和结构；Grammarly 做语法、语气、清晰度 QA。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-substack",
        "name": "用 Substack 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Substack",
        "stage": "workflow",
        "description": "Substack 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Substack 发布并复盘数据",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 找素材；Claude 写 newsletter；Substack 发布并复盘数据。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-custom-style",
        "name": "用 Claude custom style 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Claude custom style",
        "stage": "workflow",
        "description": "Claude custom style 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Claude 学习个人写作样本",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Claude 学习个人写作样本；Notion 管选题库、草稿和发布状态。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hemingway",
        "name": "用 Hemingway 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Hemingway",
        "stage": "workflow",
        "description": "Hemingway 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Hemingway 或 LanguageTool 控制可读性和错误",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 快速起草；Hemingway 或 LanguageTool 控制可读性和错误。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-languagetool",
        "name": "用 LanguageTool 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "LanguageTool",
        "stage": "workflow",
        "description": "LanguageTool 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Hemingway 或 LanguageTool 控制可读性和错误",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 快速起草；Hemingway 或 LanguageTool 控制可读性和错误。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-readwise",
        "name": "用 Readwise 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Readwise",
        "stage": "workflow",
        "description": "Readwise 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Readwise 收集高亮信息",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Readwise 收集高亮信息；Obsidian 建本地知识库；Claude 生成文章/脚本。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-obsidian",
        "name": "用 Obsidian 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Obsidian",
        "stage": "workflow",
        "description": "Obsidian 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Obsidian 建本地知识库",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Readwise 收集高亮信息；Obsidian 建本地知识库；Claude 生成文章/脚本。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-jasper",
        "name": "用 Jasper 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Jasper",
        "stage": "workflow",
        "description": "Jasper 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Jasper/Copy.ai 批量生成广告版本",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 做定位和产品卖点；Jasper/Copy.ai 批量生成广告版本。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-copy-ai",
        "name": "用 Copy.ai 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Copy.ai",
        "stage": "workflow",
        "description": "Copy.ai 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Jasper/Copy.ai 批量生成广告版本",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 做定位和产品卖点；Jasper/Copy.ai 批量生成广告版本。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-google-docs",
        "name": "用 Google Docs 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Google Docs",
        "stage": "workflow",
        "description": "Google Docs 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Claude 负责结构和改写；Docs 负责协作评论、版本控制和交付。",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Claude 负责结构和改写；Docs 负责协作评论、版本控制和交付。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt-voice",
        "name": "用 ChatGPT voice 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "ChatGPT voice",
        "stage": "workflow",
        "description": "ChatGPT voice 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：ChatGPT 语音记录想法",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 语音记录想法；Claude 把口述内容重构成文章/方案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-perplexity-pages",
        "name": "用 Perplexity Pages 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Perplexity Pages",
        "stage": "workflow",
        "description": "Perplexity Pages 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Perplexity Pages 做信息页雏形",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity Pages 做信息页雏形；Claude 改成观点型长文。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-opentweet",
        "name": "用 OpenTweet 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "OpenTweet",
        "stage": "workflow",
        "description": "OpenTweet 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：OpenTweet 排程、循环 evergreen 内容、回收 analytics",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Claude 学习声音、批量生成推文；OpenTweet 排程、循环 evergreen 内容、回收 analytics。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-buffer",
        "name": "用 Buffer 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Buffer",
        "stage": "workflow",
        "description": "Buffer 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Buffer 排程到 LinkedIn/X",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 找资料；Claude 写系列帖；Buffer 排程到 LinkedIn/X。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-later",
        "name": "用 Later 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Later",
        "stage": "workflow",
        "description": "Later 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Later 排程 Instagram/LinkedIn",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成图文脚本；Canva 做视觉；Later 排程 Instagram/LinkedIn。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hypefury",
        "name": "用 Hypefury 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Hypefury",
        "stage": "workflow",
        "description": "Hypefury 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Claude 写 thread 和 hooks；工具排程、复用、分析爆款。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写 thread 和 hooks；工具排程、复用、分析爆款。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-tweethunter",
        "name": "用 Tweethunter 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Tweethunter",
        "stage": "workflow",
        "description": "Tweethunter 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Claude 写 thread 和 hooks；工具排程、复用、分析爆款。",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写 thread 和 hooks；工具排程、复用、分析爆款。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-opusclip",
        "name": "用 OpusClip 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "OpusClip",
        "stage": "workflow",
        "description": "OpusClip 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：OpusClip 切长视频",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "OpusClip 切长视频；ChatGPT 写标题/描述；CapCut 精修字幕和节奏。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-capcut",
        "name": "用 CapCut 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "CapCut",
        "stage": "workflow",
        "description": "CapCut 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：CapCut 精修字幕和节奏",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "OpusClip 切长视频；ChatGPT 写标题/描述；CapCut 精修字幕和节奏。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-descript",
        "name": "用 Descript 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Descript",
        "stage": "workflow",
        "description": "Descript 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Descript 转写剪辑",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Descript 转写剪辑；Claude 生成章节、标题、简介；YouTube Studio 发布。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-youtube-studio",
        "name": "用 YouTube Studio 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "YouTube Studio",
        "stage": "workflow",
        "description": "YouTube Studio 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：YouTube Studio 发布",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Descript 转写剪辑；Claude 生成章节、标题、简介；YouTube Studio 发布。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-midjourney",
        "name": "用 Midjourney 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Midjourney",
        "stage": "workflow",
        "description": "Midjourney 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Midjourney 出主图",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成视觉 brief；Midjourney 出主图；Canva 适配多平台尺寸。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-taplio",
        "name": "用 Taplio 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Taplio",
        "stage": "workflow",
        "description": "Taplio 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Taplio 做排程和表现复盘",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写 LinkedIn 长帖和评论回复；Taplio 做排程和表现复盘。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-cursor",
        "name": "用 Cursor 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Cursor",
        "stage": "workflow",
        "description": "Cursor 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Cursor 负责多文件编辑和 diff",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Cursor 负责多文件编辑和 diff；Claude 负责架构推理、复杂 bug、重构计划。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-code",
        "name": "用 Claude Code 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Claude Code",
        "stage": "workflow",
        "description": "Claude Code 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Claude Code 读 repo、改代码、跑测试",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Claude Code 读 repo、改代码、跑测试；GitHub PR 承载审查和合并。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-github",
        "name": "用 GitHub 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "GitHub",
        "stage": "workflow",
        "description": "GitHub 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：GitHub PR 承载审查和合并",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Claude Code 读 repo、改代码、跑测试；GitHub PR 承载审查和合并。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-codex",
        "name": "用 Codex 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Codex",
        "stage": "workflow",
        "description": "Codex 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Codex 处理 issue 到 PR 的实现",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Codex 处理 issue 到 PR 的实现；ChatGPT 帮忙解释方案、生成测试和文档。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-github-copilot",
        "name": "用 GitHub Copilot 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "GitHub Copilot",
        "stage": "workflow",
        "description": "GitHub Copilot 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Copilot 在 IDE 补全和小改；Claude 处理大上下文设计和代码审稿。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Copilot 在 IDE 补全和小改；Claude 处理大上下文设计和代码审稿。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-ccusage",
        "name": "用 ccusage 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "ccusage",
        "stage": "workflow",
        "description": "ccusage 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：ccusage 监控成本",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "用 CLAUDE.md 约束项目规则；ccusage 监控成本；Claude Code 执行任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-md",
        "name": "用 CLAUDE.md 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "CLAUDE.md",
        "stage": "workflow",
        "description": "CLAUDE.md 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：用 CLAUDE.md 约束项目规则",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "用 CLAUDE.md 约束项目规则；ccusage 监控成本；Claude Code 执行任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-subagents",
        "name": "用 subagents 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "subagents",
        "stage": "workflow",
        "description": "subagents 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：主 agent 分解任务；子 agent 并行查找/实现/审查；hooks 做安全和质量门禁。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "主 agent 分解任务；子 agent 并行查找/实现/审查；hooks 做安全和质量门禁。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hooks",
        "name": "用 hooks 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "hooks",
        "stage": "workflow",
        "description": "hooks 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：hooks 做安全和质量门禁",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "主 agent 分解任务；子 agent 并行查找/实现/审查；hooks 做安全和质量门禁。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-replit",
        "name": "用 Replit 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Replit",
        "stage": "workflow",
        "description": "Replit 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Replit 快速搭云端原型",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Replit 快速搭云端原型；ChatGPT 生成需求、调试和部署说明。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-lovable",
        "name": "用 Lovable 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Lovable",
        "stage": "workflow",
        "description": "Lovable 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Lovable/Bolt 生成前端原型",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Lovable/Bolt 生成前端原型；Claude 审查业务逻辑、状态和安全风险。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-bolt",
        "name": "用 Bolt 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Bolt",
        "stage": "workflow",
        "description": "Bolt 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Lovable/Bolt 生成前端原型",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Lovable/Bolt 生成前端原型；Claude 审查业务逻辑、状态和安全风险。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-v0",
        "name": "用 v0 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "v0",
        "stage": "workflow",
        "description": "v0 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：v0 出 UI",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "v0 出 UI；Cursor 接入项目并改文件；Claude 做产品逻辑和代码审查。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-windsurf",
        "name": "用 Windsurf 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Windsurf",
        "stage": "workflow",
        "description": "Windsurf 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Windsurf 做 agentic IDE 流程",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Windsurf 做 agentic IDE 流程；Claude 负责解释、规划、复杂改造。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-opencode",
        "name": "用 OpenCode 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "OpenCode",
        "stage": "workflow",
        "description": "OpenCode 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：OpenCode 跑开源/低成本模型",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-ollama",
        "name": "用 Ollama 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Ollama",
        "stage": "workflow",
        "description": "Ollama 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-kimi",
        "name": "用 Kimi 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Kimi",
        "stage": "workflow",
        "description": "Kimi 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "OpenCode 跑开源/低成本模型；Claude 处理关键难题；保留隐私和成本弹性。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-scion",
        "name": "用 Scion 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Scion",
        "stage": "workflow",
        "description": "Scion 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Scion 用容器和 git worktree 隔离多 agent",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Scion 用容器和 git worktree 隔离多 agent；不同模型并行做功能。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-paseo",
        "name": "用 Paseo 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Paseo",
        "stage": "workflow",
        "description": "Paseo 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Paseo 统一管理多个 coding agent，减少复制粘贴和上下文断裂",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Paseo 统一管理多个 coding agent，减少复制粘贴和上下文断裂。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-agentauditkit",
        "name": "用 AgentAuditKit 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "AgentAuditKit",
        "stage": "workflow",
        "description": "AgentAuditKit 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：AgentAuditKit 本地扫描 prompt/tool/secret 风险",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Claude Code 写代码；AgentAuditKit 本地扫描 prompt/tool/secret 风险。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-snyk",
        "name": "用 Snyk 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Snyk",
        "stage": "workflow",
        "description": "Snyk 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Snyk/Socket 查漏洞、恶意包和许可证",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "AI 写依赖和代码；Snyk/Socket 查漏洞、恶意包和许可证。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-socket",
        "name": "用 Socket 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Socket",
        "stage": "workflow",
        "description": "Socket 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Snyk/Socket 查漏洞、恶意包和许可证",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "AI 写依赖和代码；Snyk/Socket 查漏洞、恶意包和许可证。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-copilot",
        "name": "用 Copilot 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Copilot",
        "stage": "workflow",
        "description": "Copilot 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：AI 写依赖和代码；Snyk/Socket 查漏洞、恶意包和许可证。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "AI 写依赖和代码；Snyk/Socket 查漏洞、恶意包和许可证。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-linear",
        "name": "用 Linear 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Linear",
        "stage": "workflow",
        "description": "Linear 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Linear issue 自动生成实现计划",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Linear issue 自动生成实现计划；Codex 实现；ChatGPT 生成验收标准。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-jira",
        "name": "用 Jira 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Jira",
        "stage": "workflow",
        "description": "Jira 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Claude 从 Jira 需求生成技术方案",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Claude 从 Jira 需求生成技术方案；GitHub PR 关联 issue；Claude 审稿。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-databricks-genie",
        "name": "用 Databricks Genie 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Databricks Genie",
        "stage": "workflow",
        "description": "Databricks Genie 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Genie 用自然语言处理数据管道/Spark；Claude 写解释、文档和异常分析。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Genie 用自然语言处理数据管道/Spark；Claude 写解释、文档和异常分析。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt-advanced-data-analysis",
        "name": "用 ChatGPT Advanced Data Analysis 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "ChatGPT Advanced Data Analysis",
        "stage": "workflow",
        "description": "ChatGPT Advanced Data Analysis 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：上传 CSV/Excel 到 ChatGPT 做清洗、透视和图表",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "上传 CSV/Excel 到 ChatGPT 做清洗、透视和图表；结果回写 Sheets。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-sheets",
        "name": "用 Sheets 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Sheets",
        "stage": "workflow",
        "description": "Sheets 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：结果回写 Sheets",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "上传 CSV/Excel 到 ChatGPT 做清洗、透视和图表；结果回写 Sheets。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-excel-connector",
        "name": "用 Excel connector 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Excel connector",
        "stage": "workflow",
        "description": "Excel connector 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Excel 负责最终模型和审阅",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Claude 读取工作簿、解释公式和风险；Excel 负责最终模型和审阅。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt-ada",
        "name": "用 ChatGPT ADA 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "ChatGPT ADA",
        "stage": "workflow",
        "description": "ChatGPT ADA 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：ChatGPT 做数据处理和可视化",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 找外部指标；ChatGPT 做数据处理和可视化。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-notion-database",
        "name": "用 Notion database 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Notion database",
        "stage": "workflow",
        "description": "Notion database 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Notion 管项目/客户数据",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Notion 管项目/客户数据；Claude 按条件生成周报、风险清单和下一步。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-airtable",
        "name": "用 Airtable 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Airtable",
        "stage": "workflow",
        "description": "Airtable 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Airtable 存结构化数据",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Airtable 存结构化数据；Zapier 触发；ChatGPT 生成摘要/邮件/任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-zapier-ai",
        "name": "用 Zapier AI 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Zapier AI",
        "stage": "workflow",
        "description": "Zapier AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Zapier 触发",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Airtable 存结构化数据；Zapier 触发；ChatGPT 生成摘要/邮件/任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-bigquery",
        "name": "用 BigQuery 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "BigQuery",
        "stage": "workflow",
        "description": "BigQuery 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Gemini 帮写 SQL/解释指标；Looker 做仪表盘。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Gemini 帮写 SQL/解释指标；Looker 做仪表盘。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-looker",
        "name": "用 Looker 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Looker",
        "stage": "workflow",
        "description": "Looker 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Looker 做仪表盘",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Gemini 帮写 SQL/解释指标；Looker 做仪表盘。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-snowflake-cortex",
        "name": "用 Snowflake Cortex 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Snowflake Cortex",
        "stage": "workflow",
        "description": "Snowflake Cortex 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Snowflake 内做企业数据 AI",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Snowflake 内做企业数据 AI；Claude/ChatGPT 写解释和业务行动建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-power-bi-copilot",
        "name": "用 Power BI Copilot 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Power BI Copilot",
        "stage": "workflow",
        "description": "Power BI Copilot 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Power BI Copilot 建报表",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Power BI Copilot 建报表；ChatGPT 生成高管摘要和故事线。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-rows",
        "name": "用 Rows 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Rows",
        "stage": "workflow",
        "description": "Rows 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Rows 把电子表格和 API 结合",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Rows 把电子表格和 API 结合；ChatGPT 做公式、摘要、批量文案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-julius-ai",
        "name": "用 Julius AI 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Julius AI",
        "stage": "workflow",
        "description": "Julius AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Julius 做数据探索",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Julius 做数据探索；Claude 解释洞察、生成报告和下一步实验。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-fireflies",
        "name": "用 Fireflies 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Fireflies",
        "stage": "workflow",
        "description": "Fireflies 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-otter",
        "name": "用 Otter 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Otter",
        "stage": "workflow",
        "description": "Otter 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "会议转写后交给 Claude，总结决策、行动项、风险和跟进邮件。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt-record-mode",
        "name": "用 ChatGPT record mode 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "ChatGPT record mode",
        "stage": "workflow",
        "description": "ChatGPT record mode 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：ChatGPT 记录/总结会议",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 记录/总结会议；Notion 建任务页和纪要库。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-tactiq",
        "name": "用 Tactiq 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Tactiq",
        "stage": "workflow",
        "description": "Tactiq 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Tactiq 获取会议转写",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Tactiq 获取会议转写；Notion AI 按模板沉淀客户/项目记录。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-fathom",
        "name": "用 Fathom 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Fathom",
        "stage": "workflow",
        "description": "Fathom 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Fathom 总结销售通话",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Fathom 总结销售通话；HubSpot 更新 CRM；ChatGPT 写 follow-up。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hubspot",
        "name": "用 HubSpot 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "HubSpot",
        "stage": "workflow",
        "description": "HubSpot 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：HubSpot 更新 CRM",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Fathom 总结销售通话；HubSpot 更新 CRM；ChatGPT 写 follow-up。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-zoom-ai-companion",
        "name": "用 Zoom AI Companion 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Zoom AI Companion",
        "stage": "workflow",
        "description": "Zoom AI Companion 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Zoom 生成摘要",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Zoom 生成摘要；Claude 做复盘、反对意见和项目计划。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-teams-copilot",
        "name": "用 Teams Copilot 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Teams Copilot",
        "stage": "workflow",
        "description": "Teams Copilot 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Teams Copilot 总结内部会议",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Teams Copilot 总结内部会议；ChatGPT 把结论转成对外邮件/方案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-google-meet",
        "name": "用 Google Meet 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Google Meet",
        "stage": "workflow",
        "description": "Google Meet 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Gemini 汇总会议；Claude 写客户化纪要和下一步提案。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Gemini 汇总会议；Claude 写客户化纪要和下一步提案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-granola",
        "name": "用 Granola 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Granola",
        "stage": "workflow",
        "description": "Granola 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Granola 记录个人会议笔记",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Granola 记录个人会议笔记；Claude 清理成可发版本和任务表。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-supernormal",
        "name": "用 Supernormal 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Supernormal",
        "stage": "workflow",
        "description": "Supernormal 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Supernormal 摘要 standup",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Supernormal 摘要 standup；Linear 自动创建 bug/任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-read-ai",
        "name": "用 Read.ai 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Read.ai",
        "stage": "workflow",
        "description": "Read.ai 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Read.ai 量化会议和情绪",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Read.ai 量化会议和情绪；Slack 分发；Claude 做改进建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-slack",
        "name": "用 Slack 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Slack",
        "stage": "workflow",
        "description": "Slack 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Slack 分发",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Read.ai 量化会议和情绪；Slack 分发；Claude 做改进建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-make",
        "name": "用 Make 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Make",
        "stage": "workflow",
        "description": "Make 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Make 编排多工具流程",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Make 编排多工具流程；Claude 处理复杂文本判断和报告生成。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-n8n",
        "name": "用 n8n 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "n8n",
        "stage": "workflow",
        "description": "n8n 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：自托管 n8n 调模型 API，处理工单、数据、通知和审批",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "自托管 n8n 调模型 API，处理工单、数据、通知和审批。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-openai",
        "name": "用 OpenAI 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "OpenAI",
        "stage": "workflow",
        "description": "OpenAI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：自托管 n8n 调模型 API，处理工单、数据、通知和审批。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "自托管 n8n 调模型 API，处理工单、数据、通知和审批。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-anthropic-api",
        "name": "用 Anthropic API 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Anthropic API",
        "stage": "workflow",
        "description": "Anthropic API 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：自托管 n8n 调模型 API，处理工单、数据、通知和审批。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "自托管 n8n 调模型 API，处理工单、数据、通知和审批。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gmail",
        "name": "用 Gmail 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Gmail",
        "stage": "workflow",
        "description": "Gmail 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-outlook",
        "name": "用 Outlook 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Outlook",
        "stage": "workflow",
        "description": "Outlook 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 读邮件上下文，草拟回复、提取任务、生成日程建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-zapier",
        "name": "用 Zapier 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Zapier",
        "stage": "workflow",
        "description": "Zapier 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Notion 状态变化触发 Zapier",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Notion 状态变化触发 Zapier；ChatGPT 生成周报/提醒/客户邮件。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-airtable-ai",
        "name": "用 Airtable AI 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Airtable AI",
        "stage": "workflow",
        "description": "Airtable AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Airtable AI 分类记录",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Airtable AI 分类记录；Slack 推送异常和摘要。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-clay",
        "name": "用 Clay 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Clay",
        "stage": "workflow",
        "description": "Clay 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Clay enrich leads",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Clay enrich leads；ChatGPT 个性化邮件；HubSpot 追踪。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-apollo",
        "name": "用 Apollo 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Apollo",
        "stage": "workflow",
        "description": "Apollo 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Apollo 找线索",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Apollo 找线索；Clay 丰富数据；Claude 写高质量个性化触达。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-retool",
        "name": "用 Retool 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Retool",
        "stage": "workflow",
        "description": "Retool 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Retool 搭内部工具",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Retool 搭内部工具；OpenAI API 做文本分类、摘要和操作建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-openai-api",
        "name": "用 OpenAI API 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "OpenAI API",
        "stage": "workflow",
        "description": "OpenAI API 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：OpenAI API 做文本分类、摘要和操作建议",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Retool 搭内部工具；OpenAI API 做文本分类、摘要和操作建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-adobe-creative-cloud",
        "name": "用 Adobe Creative Cloud 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Adobe Creative Cloud",
        "stage": "workflow",
        "description": "Adobe Creative Cloud 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Claude 通过创意连接器辅助 Photoshop/Premiere/Express 等工具的批处理和资产流转。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 通过创意连接器辅助 Photoshop/Premiere/Express 等工具的批处理和资产流转。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-blender",
        "name": "用 Blender 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Blender",
        "stage": "workflow",
        "description": "Blender 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Claude 分析/调试 Blender 场景，写 Python 脚本批量修改对象",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 分析/调试 Blender 场景，写 Python 脚本批量修改对象。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-photoshop",
        "name": "用 Photoshop 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Photoshop",
        "stage": "workflow",
        "description": "Photoshop 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Photoshop 精修",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 写 prompt 和风格规范；Midjourney 出图；Photoshop 精修。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-figma-ai",
        "name": "用 Figma AI 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Figma AI",
        "stage": "workflow",
        "description": "Figma AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Figma AI 快速生成/整理 UI",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Figma AI 快速生成/整理 UI；Claude 输出交互逻辑、文案和设计评审。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-framer",
        "name": "用 Framer 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Framer",
        "stage": "workflow",
        "description": "Framer 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Framer 快速建交互页面",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成网站结构和文案；Framer 快速建交互页面。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-uizard",
        "name": "用 Uizard 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Uizard",
        "stage": "workflow",
        "description": "Uizard 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：AI UI 工具出线框；Claude 写产品说明和验收标准。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "AI UI 工具出线框；Claude 写产品说明和验收标准。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-galileo",
        "name": "用 Galileo 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Galileo",
        "stage": "workflow",
        "description": "Galileo 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：AI UI 工具出线框；Claude 写产品说明和验收标准。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "AI UI 工具出线框；Claude 写产品说明和验收标准。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-runway",
        "name": "用 Runway 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Runway",
        "stage": "workflow",
        "description": "Runway 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Runway 生成/编辑视频",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写分镜、镜头和旁白；Runway 生成/编辑视频。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-heygen",
        "name": "用 HeyGen 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "HeyGen",
        "stage": "workflow",
        "description": "HeyGen 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：HeyGen 生成数字人视频",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写脚本和多语言版本；HeyGen 生成数字人视频。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-suno",
        "name": "用 Suno 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Suno",
        "stage": "workflow",
        "description": "Suno 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Suno/Udio 生成音乐",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写歌词/风格 brief；Suno/Udio 生成音乐；Claude 迭代版本说明。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-udio",
        "name": "用 Udio 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Udio",
        "stage": "workflow",
        "description": "Udio 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Suno/Udio 生成音乐",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写歌词/风格 brief；Suno/Udio 生成音乐；Claude 迭代版本说明。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-elevenlabs",
        "name": "用 ElevenLabs 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "ElevenLabs",
        "stage": "workflow",
        "description": "ElevenLabs 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：ElevenLabs 生成多语言配音",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写旁白脚本；ElevenLabs 生成多语言配音。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-premiere",
        "name": "用 Premiere 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "Premiere",
        "stage": "workflow",
        "description": "Premiere 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Premiere 完成专业剪辑",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Claude 辅助素材整理、批处理和编辑建议；Premiere 完成专业剪辑。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-connector",
        "name": "用 Claude connector 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "Claude connector",
        "stage": "workflow",
        "description": "Claude connector 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Claude 辅助素材整理、批处理和编辑建议",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Claude 辅助素材整理、批处理和编辑建议；Premiere 完成专业剪辑。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-ableton",
        "name": "用 Ableton 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "Ableton",
        "stage": "workflow",
        "description": "Ableton 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Claude 基于 Live/Push 文档辅助制作步骤、排错和工程整理。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Claude 基于 Live/Push 文档辅助制作步骤、排错和工程整理。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hyperframes",
        "name": "用 HyperFrames 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "HyperFrames",
        "stage": "workflow",
        "description": "HyperFrames 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Hermes agent 调 HyperFrames，把一行描述渲染成视频片段",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Hermes agent 调 HyperFrames，把一行描述渲染成视频片段。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hermes-agent",
        "name": "用 Hermes Agent 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "Hermes Agent",
        "stage": "workflow",
        "description": "Hermes Agent 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Hermes agent 调 HyperFrames，把一行描述渲染成视频片段",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Hermes agent 调 HyperFrames，把一行描述渲染成视频片段。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-salesforce",
        "name": "用 Salesforce 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Salesforce",
        "stage": "workflow",
        "description": "Salesforce 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：ChatGPT 汇总机会、风险、竞争态势，生成销售行动计划。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 汇总机会、风险、竞争态势，生成销售行动计划。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-docusign",
        "name": "用 DocuSign 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "DocuSign",
        "stage": "workflow",
        "description": "DocuSign 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：DocuSign 走签署",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成合同摘要；Claude 比较条款风险；DocuSign 走签署。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-servicenow",
        "name": "用 ServiceNow 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "ServiceNow",
        "stage": "workflow",
        "description": "ServiceNow 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：用 Claude 驱动 ServiceNow Build Agent，把自然语言需求转成工作流/内部应用",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "用 Claude 驱动 ServiceNow Build Agent，把自然语言需求转成工作流/内部应用。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-intercom",
        "name": "用 Intercom 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Intercom",
        "stage": "workflow",
        "description": "Intercom 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：ChatGPT 分类工单、草拟回复；客服平台保留人工审核和历史记录。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 分类工单、草拟回复；客服平台保留人工审核和历史记录。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-zendesk",
        "name": "用 Zendesk 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Zendesk",
        "stage": "workflow",
        "description": "Zendesk 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：ChatGPT 分类工单、草拟回复；客服平台保留人工审核和历史记录。",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 分类工单、草拟回复；客服平台保留人工审核和历史记录。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gong",
        "name": "用 Gong 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Gong",
        "stage": "workflow",
        "description": "Gong 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：Gong 分析销售通话",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "Gong 分析销售通话；Claude 生成教练反馈、异议处理和复盘。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-shopify",
        "name": "用 Shopify 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Shopify",
        "stage": "workflow",
        "description": "Shopify 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：Shopify 发布",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 生成商品文案/FAQ；Canva 做商品图；Shopify 发布。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-todoist",
        "name": "用 Todoist 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Todoist",
        "stage": "workflow",
        "description": "Todoist 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Todoist 管任务提醒",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 拆解目标和日程；Todoist 管任务提醒。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-apple-notes",
        "name": "用 Apple Notes 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Apple Notes",
        "stage": "workflow",
        "description": "Apple Notes 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Claude 帮你把碎片笔记整理成项目计划、文章或决策 memo。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "Claude 帮你把碎片笔记整理成项目计划、文章或决策 memo。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gamma-connector",
        "name": "用 Gamma Connector 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Gamma Connector",
        "stage": "workflow",
        "description": "Gamma Connector 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：在 Claude 或 ChatGPT 对话中直接生成 Gamma deck，减少复制粘贴",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "在 Claude 或 ChatGPT 对话中直接生成 Gamma deck，减少复制粘贴；再用 Gamma 模板和品牌设置收尾。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gamma-api",
        "name": "用 Gamma API 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Gamma API",
        "stage": "workflow",
        "description": "Gamma API 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Gamma API 自动生成项目汇报",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Notion 立项页变更触发 n8n；Claude 总结内容；Gamma API 自动生成项目汇报。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-superhuman-go",
        "name": "用 Superhuman Go 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Superhuman Go",
        "stage": "workflow",
        "description": "Superhuman Go 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：邮件里收到客户需求后，Superhuman Go 调 Gamma 生成初版资料，Claude 优化话术",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "邮件里收到客户需求后，Superhuman Go 调 Gamma 生成初版资料，Claude 优化话术。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-atlassian-rovo",
        "name": "用 Atlassian Rovo 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Atlassian Rovo",
        "stage": "workflow",
        "description": "Atlassian Rovo 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：从 Confluence/Jira 项目资料生成发布说明或路线图 deck。",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "从 Confluence/Jira 项目资料生成发布说明或路线图 deck。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-close",
        "name": "用 Close 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Close",
        "stage": "workflow",
        "description": "Close 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Close 跟进 pipeline",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Perplexity 做客户/行业研究；Claude 写 pitch；Gamma 可视化；Close 跟进 pipeline。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-effy",
        "name": "用 Effy 支撑PPT/提案工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Effy",
        "stage": "workflow",
        "description": "Effy 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「PPT/提案」场景中出现，用途来自原文：Effy 生成 HR 反馈/绩效素材",
        "tags": [
            "presentation",
            "expanded-2026"
        ],
        "examples": [
            "Effy 生成 HR 反馈/绩效素材；Claude 梳理为管理层叙事；Canva/Gamma 出汇报。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-trusted-site-filter",
        "name": "用 trusted-site filter 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "trusted-site filter",
        "stage": "workflow",
        "description": "trusted-site filter 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：限制检索到可信站点或内部 MCP；输出带来源报告，再由 Claude 压缩成执行摘要。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "限制检索到可信站点或内部 MCP；输出带来源报告，再由 Claude 压缩成执行摘要。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-grok-deepersearch",
        "name": "用 Grok DeeperSearch 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Grok DeeperSearch",
        "stage": "workflow",
        "description": "Grok DeeperSearch 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Grok 看 X 和实时网络讨论",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Grok 看 X 和实时网络讨论；Claude 做立场归类、可信度判断和摘要。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-subq",
        "name": "用 SubQ 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "SubQ",
        "stage": "workflow",
        "description": "SubQ 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：把大规模上下文交给 SubQ 长上下文层",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "把大规模上下文交给 SubQ 长上下文层；Claude/ChatGPT 做结论、反例和行动方案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gbrain",
        "name": "用 GBrain 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "GBrain",
        "stage": "workflow",
        "description": "GBrain 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：GBrain 做夜间记忆整理和实体清理",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "GBrain 做夜间记忆整理和实体清理；Claude 白天基于记忆做计划/写作。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-fire-pdf",
        "name": "用 Fire-PDF 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "Fire-PDF",
        "stage": "workflow",
        "description": "Fire-PDF 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Fire-PDF 快速把 PDF 转 markdown",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Fire-PDF 快速把 PDF 转 markdown；Claude 汇总条款、证据和风险。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-openai-gpt-rosalind",
        "name": "用 OpenAI GPT-Rosalind 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "OpenAI GPT-Rosalind",
        "stage": "workflow",
        "description": "OpenAI GPT-Rosalind 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：GPT-Rosalind 做生命科学推理；Codex/API 连接分析脚本和实验工具。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "GPT-Rosalind 做生命科学推理；Codex/API 连接分析脚本和实验工具。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-api",
        "name": "用 API 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "API",
        "stage": "workflow",
        "description": "API 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：Codex/API 连接分析脚本和实验工具",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "GPT-Rosalind 做生命科学推理；Codex/API 连接分析脚本和实验工具。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gpt-rosalind",
        "name": "用 GPT-Rosalind 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "GPT-Rosalind",
        "stage": "workflow",
        "description": "GPT-Rosalind 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：GPT-Rosalind 做生物机制推理",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "Elicit 找文献；GPT-Rosalind 做生物机制推理；Claude 写综述和实验计划。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-tradingagents",
        "name": "用 TradingAgents 支撑研究工作流",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tool": "TradingAgents",
        "stage": "workflow",
        "description": "TradingAgents 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「研究」场景中出现，用途来自原文：多 agent 做基本面/情绪/技术/风险；Perplexity 查证；Claude 写投资 memo。",
        "tags": [
            "research",
            "expanded-2026"
        ],
        "examples": [
            "多 agent 做基本面/情绪/技术/风险；Perplexity 查证；Claude 写投资 memo。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-chatgpt-planner",
        "name": "用 ChatGPT planner 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "ChatGPT planner",
        "stage": "workflow",
        "description": "ChatGPT planner 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：ChatGPT 负责拆结构、受众、角度",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 负责拆结构、受众、角度；Claude 负责长文执行和润色。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-executor",
        "name": "用 Claude executor 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Claude executor",
        "stage": "workflow",
        "description": "Claude executor 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Claude 负责长文执行和润色",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 负责拆结构、受众、角度；Claude 负责长文执行和润色。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-writeless",
        "name": "用 Writeless 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Writeless",
        "stage": "workflow",
        "description": "Writeless 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Writeless 或 QuillBot 做改写、降重复和语气调整",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Claude 产出高质量初稿；Writeless 或 QuillBot 做改写、降重复和语气调整。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-quillbot",
        "name": "用 QuillBot 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "QuillBot",
        "stage": "workflow",
        "description": "QuillBot 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Writeless 或 QuillBot 做改写、降重复和语气调整",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Claude 产出高质量初稿；Writeless 或 QuillBot 做改写、降重复和语气调整。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-rankprompt",
        "name": "用 Rankprompt 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Rankprompt",
        "stage": "workflow",
        "description": "Rankprompt 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：Rankprompt 追踪品牌在 AI 回答里的提及和竞品引用",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "Claude 写品牌内容；Rankprompt 追踪品牌在 AI 回答里的提及和竞品引用。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-scriptwrite",
        "name": "用 ScriptWrite 支撑写作工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "ScriptWrite",
        "stage": "workflow",
        "description": "ScriptWrite 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「写作」场景中出现，用途来自原文：ScriptWrite 结构化脚本",
        "tags": [
            "writing",
            "expanded-2026"
        ],
        "examples": [
            "ScriptWrite 结构化脚本；ChatGPT 发散；Midjourney 做视觉 moodboard。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-leonardo-ai",
        "name": "用 Leonardo AI 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Leonardo AI",
        "stage": "workflow",
        "description": "Leonardo AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Leonardo 生成封面",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 写播客标题和摘要；Leonardo 生成封面；Descript 剪辑。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-clipto-ai",
        "name": "用 Clipto AI 支撑社媒工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Clipto AI",
        "stage": "workflow",
        "description": "Clipto AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「社媒」场景中出现，用途来自原文：Clipto 本地转写敏感采访",
        "tags": [
            "social",
            "expanded-2026"
        ],
        "examples": [
            "Clipto 本地转写敏感采访；ChatGPT 写 show notes；Descript 清理音频。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-runtime",
        "name": "用 Runtime 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Runtime",
        "stage": "workflow",
        "description": "Runtime 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Runtime 提供沙箱、花费限制、文件保护和观测",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Runtime 提供沙箱、花费限制、文件保护和观测；多 coding agent 在受控环境执行。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-goal",
        "name": "用 goal 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "goal",
        "stage": "workflow",
        "description": "goal 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：用 /goal 写多日执行计划",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "用 /goal 写多日执行计划；Claude Code 实现；GitHub PR 作为人工 checkpoint。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-insforge-skills",
        "name": "用 Insforge Skills 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Insforge Skills",
        "stage": "workflow",
        "description": "Insforge Skills 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：用 Insforge 做上下文工程，降低 token 消耗和错误率",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "用 Insforge 做上下文工程，降低 token 消耗和错误率；Claude Code 执行编码。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-everything-claude-code",
        "name": "用 everything-claude-code 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "everything-claude-code",
        "stage": "workflow",
        "description": "everything-claude-code 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：用预设 agents、skills、hooks 和安全扫描增强 Claude/Cursor/Codex 工作流。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "用预设 agents、skills、hooks 和安全扫描增强 Claude/Cursor/Codex 工作流。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-openclaw",
        "name": "用 OpenClaw 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "OpenClaw",
        "stage": "workflow",
        "description": "OpenClaw 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：OpenClaw/Hermes 编排",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "OpenClaw/Hermes 编排；Ollama 跑本地模型；关键任务再切 Claude/ChatGPT。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-hermes",
        "name": "用 Hermes 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Hermes",
        "stage": "workflow",
        "description": "Hermes 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：OpenClaw/Hermes 编排",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "OpenClaw/Hermes 编排；Ollama 跑本地模型；关键任务再切 Claude/ChatGPT。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-deepseek-tui",
        "name": "用 DeepSeek TUI 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "DeepSeek TUI",
        "stage": "workflow",
        "description": "DeepSeek TUI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：终端式 coding agent 处理 1M 上下文、子 agent、git 管理。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "终端式 coding agent 处理 1M 上下文、子 agent、git 管理。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-git",
        "name": "用 Git 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Git",
        "stage": "workflow",
        "description": "Git 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：终端式 coding agent 处理 1M 上下文、子 agent、git 管理",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "终端式 coding agent 处理 1M 上下文、子 agent、git 管理。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-letta-code",
        "name": "用 Letta Code 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Letta Code",
        "stage": "workflow",
        "description": "Letta Code 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：主 agent 执行任务；recall 子 agent 从长记忆检索相关上下文。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "主 agent 执行任务；recall 子 agent 从长记忆检索相关上下文。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-recall-subagent",
        "name": "用 recall subagent 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "recall subagent",
        "stage": "workflow",
        "description": "recall subagent 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：recall 子 agent 从长记忆检索相关上下文",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "主 agent 执行任务；recall 子 agent 从长记忆检索相关上下文。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-entire-cli-skills",
        "name": "用 Entire CLI Skills 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Entire CLI Skills",
        "stage": "workflow",
        "description": "Entire CLI Skills 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：把 prompts、transcripts、决策和 commit context 暴露给 agent，改善交接。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "把 prompts、transcripts、决策和 commit context 暴露给 agent，改善交接。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-autoswarm",
        "name": "用 AutoSwarm 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "AutoSwarm",
        "stage": "workflow",
        "description": "AutoSwarm 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：用 meta-agent 自动优化多 agent pipeline，从单点优化转向团队优化。",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "用 meta-agent 自动优化多 agent pipeline，从单点优化转向团队优化。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-laureum-ai",
        "name": "用 Laureum AI 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Laureum AI",
        "stage": "workflow",
        "description": "Laureum AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Laureum/MCP 质量评分作为上线门禁",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "本地扫描 agent 安全；Laureum/MCP 质量评分作为上线门禁。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-swe-ci",
        "name": "用 SWE-CI 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "SWE-CI",
        "stage": "workflow",
        "description": "SWE-CI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：SWE-CI 检查长期维护回归",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "SWE-CI 检查长期维护回归；Opik 从 traces 自动生成 agent 回归测试。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-opik-test-suites",
        "name": "用 Opik Test Suites 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Opik Test Suites",
        "stage": "workflow",
        "description": "Opik Test Suites 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Opik 从 traces 自动生成 agent 回归测试",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "SWE-CI 检查长期维护回归；Opik 从 traces 自动生成 agent 回归测试。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-kilo-code",
        "name": "用 Kilo Code 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Kilo Code",
        "stage": "workflow",
        "description": "Kilo Code 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Kilo Code 在 VS Code 里接手工程化和修 bug",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Lovable 快速生成 UI；Kilo Code 在 VS Code 里接手工程化和修 bug。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-cc-switch",
        "name": "用 cc-switch 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "cc-switch",
        "stage": "workflow",
        "description": "cc-switch 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：cc-switch 切模型/配置",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Windsurf 做 IDE 代理；Claude Code 做终端任务；cc-switch 切模型/配置。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-google-adk",
        "name": "用 Google ADK 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "Google ADK",
        "stage": "workflow",
        "description": "Google ADK 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：Google ADK 构建 Gemini agent",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Google ADK 构建 Gemini agent；LangGraph 控流程和状态。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-langgraph",
        "name": "用 LangGraph 支撑编程工作流",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tool": "LangGraph",
        "stage": "workflow",
        "description": "LangGraph 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「编程」场景中出现，用途来自原文：LangGraph 控流程和状态",
        "tags": [
            "coding",
            "expanded-2026"
        ],
        "examples": [
            "Google ADK 构建 Gemini agent；LangGraph 控流程和状态。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-databricks-genie-code",
        "name": "用 Databricks Genie Code 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Databricks Genie Code",
        "stage": "workflow",
        "description": "Databricks Genie Code 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：自然语言生成/调试 Spark pipelines；Claude 写业务解释和数据质量报告。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "自然语言生成/调试 Spark pipelines；Claude 写业务解释和数据质量报告。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-spark",
        "name": "用 Spark 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Spark",
        "stage": "workflow",
        "description": "Spark 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：自然语言生成/调试 Spark pipelines",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "自然语言生成/调试 Spark pipelines；Claude 写业务解释和数据质量报告。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-opensre",
        "name": "用 OpenSRE 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "OpenSRE",
        "stage": "workflow",
        "description": "OpenSRE 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：OpenSRE 连接 60+ 工具做 incident 测试和诊断",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-pagerduty",
        "name": "用 PagerDuty 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "PagerDuty",
        "stage": "workflow",
        "description": "PagerDuty 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-grafana",
        "name": "用 Grafana 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Grafana",
        "stage": "workflow",
        "description": "Grafana 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "OpenSRE 连接 60+ 工具做 incident 测试和诊断；Slack 分发修复建议。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-spectrum",
        "name": "用 Spectrum 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Spectrum",
        "stage": "workflow",
        "description": "Spectrum 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：统一 iMessage/WhatsApp/Telegram/Slack/SMS 入口；Claude 分类、回复和路由。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "统一 iMessage/WhatsApp/Telegram/Slack/SMS 入口；Claude 分类、回复和路由。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gemma",
        "name": "用 Gemma 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Gemma",
        "stage": "workflow",
        "description": "Gemma 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：本地私有 AI stack，避免云锁定；用于摘要、分类、提取和内部问答。",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "本地私有 AI stack，避免云锁定；用于摘要、分类、提取和内部问答。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-bifrost",
        "name": "用 Bifrost 支撑数据工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Bifrost",
        "stage": "workflow",
        "description": "Bifrost 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「数据」场景中出现，用途来自原文：Bifrost 做模型路由和成本控制",
        "tags": [
            "data",
            "expanded-2026"
        ],
        "examples": [
            "Bifrost 做模型路由和成本控制；LangGraph 管 agent 状态；n8n 接业务系统。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-heygen-agent",
        "name": "用 HeyGen Agent 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "HeyGen Agent",
        "stage": "workflow",
        "description": "HeyGen Agent 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：把邮件/更新转成视频或语音，减少会议和反复 follow-up。",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "把邮件/更新转成视频或语音，减少会议和反复 follow-up。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-livekit-agent-console",
        "name": "用 LiveKit Agent Console 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "LiveKit Agent Console",
        "stage": "workflow",
        "description": "LiveKit Agent Console 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：LiveKit Console 调试延迟、工具调用和流水线",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Pipecat 构建实时语音 agent；LiveKit Console 调试延迟、工具调用和流水线。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-pipecat",
        "name": "用 Pipecat 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Pipecat",
        "stage": "workflow",
        "description": "Pipecat 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Pipecat 构建实时语音 agent",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Pipecat 构建实时语音 agent；LiveKit Console 调试延迟、工具调用和流水线。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-deepgram",
        "name": "用 Deepgram 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Deepgram",
        "stage": "workflow",
        "description": "Deepgram 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Deepgram 语音转文本",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Deepgram 语音转文本；Together 跑模型；Claude 做纪要/行动项。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-together",
        "name": "用 Together 支撑会议工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Together",
        "stage": "workflow",
        "description": "Together 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「会议」场景中出现，用途来自原文：Together 跑模型",
        "tags": [
            "meeting",
            "expanded-2026"
        ],
        "examples": [
            "Deepgram 语音转文本；Together 跑模型；Claude 做纪要/行动项。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-n8n-error-logs",
        "name": "用 n8n error logs 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "n8n error logs",
        "stage": "workflow",
        "description": "n8n error logs 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：把 n8n 报错和 execution data 丢给 ChatGPT，解释数据结构并给修复表达式",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "把 n8n 报错和 execution data 丢给 ChatGPT，解释数据结构并给修复表达式。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-zapier-quick-glue",
        "name": "用 Zapier quick glue 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Zapier quick glue",
        "stage": "workflow",
        "description": "Zapier quick glue 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Zapier 处理简单跨 app 触发",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Zapier 处理简单跨 app 触发；复杂状态、循环、错误处理放 n8n。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-n8n-heavy-logic",
        "name": "用 n8n heavy logic 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "n8n heavy logic",
        "stage": "workflow",
        "description": "n8n heavy logic 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：复杂状态、循环、错误处理放 n8n",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Zapier 处理简单跨 app 触发；复杂状态、循环、错误处理放 n8n。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-make-grid",
        "name": "用 Make Grid 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Make Grid",
        "stage": "workflow",
        "description": "Make Grid 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Make Grid 管复杂自动化版图",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Make Grid 管复杂自动化版图；Claude 写节点逻辑、文档和异常处理说明。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-pipedream",
        "name": "用 Pipedream 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Pipedream",
        "stage": "workflow",
        "description": "Pipedream 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Pipedream 写轻量 serverless workflow",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Pipedream 写轻量 serverless workflow；模型负责摘要、分类、回复。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-claude-api",
        "name": "用 Claude API 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Claude API",
        "stage": "workflow",
        "description": "Claude API 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：Pipedream 写轻量 serverless workflow；模型负责摘要、分类、回复。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "Pipedream 写轻量 serverless workflow；模型负责摘要、分类、回复。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-runable",
        "name": "用 Runable 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Runable",
        "stage": "workflow",
        "description": "Runable 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：一个 prompt 触发多步骤链路；ChatGPT 生成每步文案和条件判断。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "一个 prompt 触发多步骤链路；ChatGPT 生成每步文案和条件判断。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-mindstudio",
        "name": "用 MindStudio 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "MindStudio",
        "stage": "workflow",
        "description": "MindStudio 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：MindStudio 搭多步骤 AI workflow",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "MindStudio 搭多步骤 AI workflow；Claude/ChatGPT 分别处理推理和通用输出。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-servicenow-build-agent",
        "name": "用 ServiceNow Build Agent 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "ServiceNow Build Agent",
        "stage": "workflow",
        "description": "ServiceNow Build Agent 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：用自然语言构建企业 app/workflow；Claude 作为复杂推理和代码生成核心。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "用自然语言构建企业 app/workflow；Claude 作为复杂推理和代码生成核心。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-servicenow-action-fabric",
        "name": "用 ServiceNow Action Fabric 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "ServiceNow Action Fabric",
        "stage": "workflow",
        "description": "ServiceNow Action Fabric 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：任何 agent 直接触发 ServiceNow onboarding、审批、工单等系统动作，并由平台治理",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "任何 agent 直接触发 ServiceNow onboarding、审批、工单等系统动作，并由平台治理。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-servicenow-ai-control-tower",
        "name": "用 ServiceNow AI Control Tower 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "ServiceNow AI Control Tower",
        "stage": "workflow",
        "description": "ServiceNow AI Control Tower 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：统一发现、观测、治理和必要时关闭越权 agent。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "统一发现、观测、治理和必要时关闭越权 agent。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-anthropic-agents",
        "name": "用 Anthropic agents 支撑自动化工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tool": "Anthropic agents",
        "stage": "workflow",
        "description": "Anthropic agents 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「自动化」场景中出现，用途来自原文：统一发现、观测、治理和必要时关闭越权 agent。",
        "tags": [
            "automation",
            "expanded-2026"
        ],
        "examples": [
            "统一发现、观测、治理和必要时关闭越权 agent。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gamma-imagine",
        "name": "用 Gamma Imagine 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Gamma Imagine",
        "stage": "workflow",
        "description": "Gamma Imagine 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Gamma Imagine 生成图形和 deck",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 生成故事线和视觉 brief；Gamma Imagine 生成图形和 deck。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-canva-ai",
        "name": "用 Canva AI 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Canva AI",
        "stage": "workflow",
        "description": "Canva AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Canva 做社媒和 deck",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Canva 做社媒和 deck；Adobe Express 做轻量图形补充；ChatGPT/Claude 写文案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-adobe-express",
        "name": "用 Adobe Express 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Adobe Express",
        "stage": "workflow",
        "description": "Adobe Express 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Adobe Express 做轻量图形补充",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Canva 做社媒和 deck；Adobe Express 做轻量图形补充；ChatGPT/Claude 写文案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-adobe",
        "name": "用 Adobe 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Adobe",
        "stage": "workflow",
        "description": "Adobe 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Claude 在 Adobe 做素材/视频批处理，在 Blender 做 3D 场景脚本，连接跨媒体资产",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Claude 在 Adobe 做素材/视频批处理，在 Blender 做 3D 场景脚本，连接跨媒体资产。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-physiopt",
        "name": "用 PhysiOpt 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "PhysiOpt",
        "stage": "workflow",
        "description": "PhysiOpt 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：生成式设计后用物理仿真校验；Claude/Gemini 解释约束和优化方向。",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "生成式设计后用物理仿真校验；Claude/Gemini 解释约束和优化方向。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-magnific",
        "name": "用 Magnific 支撑设计工作流",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tool": "Magnific",
        "stage": "workflow",
        "description": "Magnific 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「设计」场景中出现，用途来自原文：Magnific 放大/增强",
        "tags": [
            "design",
            "expanded-2026"
        ],
        "examples": [
            "Midjourney 出概念图；Magnific 放大/增强；Claude 写视觉规范。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-xai-custom-voices",
        "name": "用 xAI Custom Voices 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "xAI Custom Voices",
        "stage": "workflow",
        "description": "xAI Custom Voices 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：快速克隆并部署多语言语音；Grok/Claude 写脚本和对话流。",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "快速克隆并部署多语言语音；Grok/Claude 写脚本和对话流。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-grok-api",
        "name": "用 Grok API 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "Grok API",
        "stage": "workflow",
        "description": "Grok API 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Grok/Claude 写脚本和对话流",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "快速克隆并部署多语言语音；Grok/Claude 写脚本和对话流。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-gemini-image",
        "name": "用 Gemini image 支撑音视频工作流",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tool": "Gemini image",
        "stage": "workflow",
        "description": "Gemini image 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「音视频」场景中出现，用途来自原文：Gemini 生成基础图片",
        "tags": [
            "media",
            "expanded-2026"
        ],
        "examples": [
            "Gemini 生成基础图片；ChatGPT 写脚本/标题；CapCut 剪辑发布。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-devi-ai",
        "name": "用 Devi AI 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Devi AI",
        "stage": "workflow",
        "description": "Devi AI 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：Devi 监控社媒社区线索",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "Devi 监控社媒社区线索；Claude 生成个性化触达和跟进策略。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-bookkeeping-ai",
        "name": "用 Bookkeeping.ai 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Bookkeeping.ai",
        "stage": "workflow",
        "description": "Bookkeeping.ai 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：Bookkeeping.ai 做财务 admin",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "Bookkeeping.ai 做财务 admin；ChatGPT 解释现金流、异常和待办。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-yourgpt",
        "name": "用 YourGPT 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "YourGPT",
        "stage": "workflow",
        "description": "YourGPT 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：YourGPT 处理客服自动回复",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "YourGPT 处理客服自动回复；Zendesk 管工单；Claude 做升级问题摘要。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-alsona",
        "name": "用 Alsona 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Alsona",
        "stage": "workflow",
        "description": "Alsona 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：Alsona 管多账号 LinkedIn 外联",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "Alsona 管多账号 LinkedIn 外联；ChatGPT 写不同 persona 的跟进文案。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-brew",
        "name": "用 Brew 支撑商务工作流",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tool": "Brew",
        "stage": "workflow",
        "description": "Brew 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「商务」场景中出现，用途来自原文：Brew 做邮件营销自动化",
        "tags": [
            "business",
            "expanded-2026"
        ],
        "examples": [
            "Brew 做邮件营销自动化；Claude 写内容计划；Notion 管 campaign。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-wispr-flow",
        "name": "用 Wispr Flow 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Wispr Flow",
        "stage": "workflow",
        "description": "Wispr Flow 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Wispr Flow 语音输入想法",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "Wispr Flow 语音输入想法；Claude 整理为任务、邮件、文章或计划。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-clico",
        "name": "用 Clico 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Clico",
        "stage": "workflow",
        "description": "Clico 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Clico 减少在浏览器工具间复制粘贴",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "Clico 减少在浏览器工具间复制粘贴；ChatGPT/Claude 保持上下文。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-obsidian-vault",
        "name": "用 Obsidian Vault 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Obsidian Vault",
        "stage": "workflow",
        "description": "Obsidian Vault 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Obsidian 做持久项目记忆",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "Obsidian 做持久项目记忆；Claude Code/Codex 读取上下文后执行任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-coding-agents",
        "name": "用 coding agents 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "coding agents",
        "stage": "workflow",
        "description": "coding agents 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Obsidian 做持久项目记忆；Claude Code/Codex 读取上下文后执行任务。",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "Obsidian 做持久项目记忆；Claude Code/Codex 读取上下文后执行任务。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    },
    {
        "id": "expanded-tool-calendar",
        "name": "用 Calendar 支撑个人效率工作流",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tool": "Calendar",
        "stage": "workflow",
        "description": "Calendar 在《ai_tool_workflow_stacks_2026_recent_3_months_expanded.pdf》的「个人效率」场景中出现，用途来自原文：Todoist/Calendar 负责执行提醒",
        "tags": [
            "productivity",
            "expanded-2026"
        ],
        "examples": [
            "ChatGPT 把目标拆成任务和日程；Todoist/Calendar 负责执行提醒。"
        ],
        "input_types": [
            "text",
            "file",
            "prompt"
        ],
        "output_types": [
            "workflow",
            "asset",
            "automation"
        ],
        "difficulty": 2,
        "importance": 62,
        "is_core": False,
        "is_active": True
    }
]


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if slug:
        return slug[:70]
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    return f"item-{digest}"


def _unique_item_id(prefix: str, slug: str, used: set[str]) -> str:
    base = f"{prefix}-{slug}"[:92].rstrip("-")
    item_id = base
    counter = 2
    while item_id in used:
        suffix = f"-{counter}"
        item_id = f"{base[:100-len(suffix)]}{suffix}"
        counter += 1
    used.add(item_id)
    return item_id


def expanded_skill_items() -> list[dict]:
    return [dict(item) for item in EXPANDED_AI_TOOL_SKILLS]


def expanded_library_items() -> list[dict]:
    items: list[dict] = []
    used_ids: set[str] = set()
    for item in EXPANDED_AI_WORKFLOWS:
        combo_id = _unique_item_id("combo-expanded", item["id_slug"], used_ids)
        workflow_id = _unique_item_id("workflow-expanded", item["id_slug"], used_ids)
        common = {
            "title": item["title"],
            "category_id": item["category_id"],
            "category_label": item["category_label"],
            "tools": item["tools"],
            "steps": item["steps"],
            "outputs": item["outputs"],
            "tags": item["tags"],
            "source_section": EXPANDED_AI_SOURCE,
            "importance": item["importance"],
            "is_active": True,
        }
        items.append({
            "id": combo_id,
            "item_type": "combination",
            "summary": item["summary"],
            **common,
        })
        items.append({
            "id": workflow_id,
            "item_type": "workflow",
            "summary": f"来自《{EXPANDED_AI_SOURCE}》的工作流：{item['title']}。工具分工：{item['workflow']}",
            **common,
        })
    return items
