from __future__ import annotations

import hashlib
import re

CHINA_AI_SOURCE = "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf"

CHINA_AI_WORKFLOWS = [
    {
        "num": "001",
        "scenario": "通用助手",
        "title": "通用助手：豆包 + Kimi",
        "combo": "豆包 + Kimi",
        "id_slug": "general-assistant-doubao-kimi",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "豆包",
            "Kimi"
        ],
        "steps": [
            "豆包处理日常问答、短文案、语音/图片输入",
            "Kimi 接长PDF、合同、报告和长文总结"
        ],
        "outputs": [
            "个人日常、学生、职场"
        ],
        "summary": "国内 AI 工具组合：通用助手：豆包 + Kimi。适合个人日常、学生、职场，流程是：豆包处理日常问答、短文案、语音/图片输入；Kimi 接长PDF、合同、报告和长文总结。",
        "tags": [
            "通用助手",
            "legal"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包处理日常问答、短文案、语音/图片输入；Kimi 接长PDF、合同、报告和长文总结。",
        "audience": "个人日常、学生、职场"
    },
    {
        "num": "002",
        "scenario": "通用助手",
        "title": "通用助手：DeepSeek + Kimi",
        "combo": "DeepSeek + Kimi",
        "id_slug": "general-assistant-deepseek-kimi",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "DeepSeek",
            "Kimi"
        ],
        "steps": [
            "DeepSeek 做低成本推理、代码和批量初稿",
            "Kimi做长文档吸收和结构化报告"
        ],
        "outputs": [
            "技术用户、研究用户"
        ],
        "summary": "国内 AI 工具组合：通用助手：DeepSeek + Kimi。适合技术用户、研究用户，流程是：DeepSeek 做低成本推理、代码和批量初稿；Kimi做长文档吸收和结构化报告。",
        "tags": [
            "通用助手",
            "docs",
            "coding"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 做低成本推理、代码和批量初稿；Kimi做长文档吸收和结构化报告。",
        "audience": "技术用户、研究用户"
    },
    {
        "num": "003",
        "scenario": "通用助手",
        "title": "通用助手：通义 + WPS AI",
        "combo": "通义 + WPS AI",
        "id_slug": "general-assistant-qwen-wps-ai",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "通义",
            "WPS AI"
        ],
        "steps": [
            "通义做问答和多模态生成",
            "WPS AI 落到文档、表格、PPT 成品"
        ],
        "outputs": [
            "办公室用户"
        ],
        "summary": "国内 AI 工具组合：通用助手：通义 + WPS AI。适合办公室用户，流程是：通义做问答和多模态生成；WPS AI 落到文档、表格、PPT 成品。",
        "tags": [
            "通用助手",
            "docs",
            "spreadsheet"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "通义做问答和多模态生成；WPS AI 落到文档、表格、PPT 成品。",
        "audience": "办公室用户"
    },
    {
        "num": "004",
        "scenario": "通用助手",
        "title": "通用助手：腾讯元宝 + ima",
        "combo": "腾讯元宝 + ima",
        "id_slug": "general-assistant-yuanbao-ima",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "腾讯元宝",
            "ima"
        ],
        "steps": [
            "元宝查微信生态和联网信息",
            "ima 沉淀知识库并生成文章/纪要"
        ],
        "outputs": [
            "公众号、微信生态团队"
        ],
        "summary": "国内 AI 工具组合：通用助手：腾讯元宝 + ima。适合公众号、微信生态团队，流程是：元宝查微信生态和联网信息；ima 沉淀知识库并生成文章/纪要。",
        "tags": [
            "通用助手",
            "rag"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "元宝查微信生态和联网信息；ima 沉淀知识库并生成文章/纪要。",
        "audience": "公众号、微信生态团队"
    },
    {
        "num": "005",
        "scenario": "通用助手",
        "title": "通用助手：讯飞星火 + 通义听悟",
        "combo": "讯飞星火 + 通义听悟",
        "id_slug": "general-assistant-spark-qwen",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "讯飞星火",
            "通义听悟"
        ],
        "steps": [
            "星火做学习答疑和写作",
            "听悟转写课程/会议并输出摘要"
        ],
        "outputs": [
            "教育、培训"
        ],
        "summary": "国内 AI 工具组合：通用助手：讯飞星火 + 通义听悟。适合教育、培训，流程是：星火做学习答疑和写作；听悟转写课程/会议并输出摘要。",
        "tags": [
            "通用助手",
            "meeting"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "星火做学习答疑和写作；听悟转写课程/会议并输出摘要。",
        "audience": "教育、培训"
    },
    {
        "num": "006",
        "scenario": "通用助手",
        "title": "通用助手：文小言 + 百度文库 AI",
        "combo": "文小言 + 百度文库 AI",
        "id_slug": "general-assistant-wenxiaoyan-ai",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "文小言",
            "百度文库 AI"
        ],
        "steps": [
            "文小言做公文/论文/策划",
            "百度文库 AI 找模板和资料包"
        ],
        "outputs": [
            "行政、学生"
        ],
        "summary": "国内 AI 工具组合：通用助手：文小言 + 百度文库 AI。适合行政、学生，流程是：文小言做公文/论文/策划；百度文库 AI 找模板和资料包。",
        "tags": [
            "通用助手"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "文小言做公文/论文/策划；百度文库 AI 找模板和资料包。",
        "audience": "行政、学生"
    },
    {
        "num": "007",
        "scenario": "通用助手",
        "title": "通用助手：GLM/智谱清言 + 飞书",
        "combo": "GLM/智谱清言 + 飞书",
        "id_slug": "general-assistant-glm-feishu",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "GLM",
            "智谱清言",
            "飞书"
        ],
        "steps": [
            "GLM 做企业级问答和推理",
            "飞书承载文档、审批、任务"
        ],
        "outputs": [
            "企业团队"
        ],
        "summary": "国内 AI 工具组合：通用助手：GLM/智谱清言 + 飞书。适合企业团队，流程是：GLM 做企业级问答和推理；飞书承载文档、审批、任务。",
        "tags": [
            "通用助手",
            "docs"
        ],
        "importance": 92,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "GLM 做企业级问答和推理；飞书承载文档、审批、任务。",
        "audience": "企业团队"
    },
    {
        "num": "008",
        "scenario": "通用助手",
        "title": "通用助手：天工 Skywork + Kimi",
        "combo": "天工 Skywork + Kimi",
        "id_slug": "general-assistant-skywork-skywork-kimi",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "天工 Skywork",
            "Kimi"
        ],
        "steps": [
            "天工做 Deep Research、文档/PPT/表格",
            "Kimi 对超长资料二次理解"
        ],
        "outputs": [
            "报告型用户"
        ],
        "summary": "国内 AI 工具组合：通用助手：天工 Skywork + Kimi。适合报告型用户，流程是：天工做 Deep Research、文档/PPT/表格；Kimi 对超长资料二次理解。",
        "tags": [
            "通用助手",
            "docs",
            "spreadsheet"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "天工做 Deep Research、文档/PPT/表格；Kimi 对超长资料二次理解。",
        "audience": "报告型用户"
    },
    {
        "num": "009",
        "scenario": "通用助手",
        "title": "通用助手：纳米 AI 搜索 + 豆包",
        "combo": "纳米 AI 搜索 + 豆包",
        "id_slug": "general-assistant-nami-ai-doubao",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "纳米 AI 搜索",
            "豆包"
        ],
        "steps": [
            "纳米解析网页/PDF/视频并生成脑图",
            "豆包改写成短文案"
        ],
        "outputs": [
            "内容运营"
        ],
        "summary": "国内 AI 工具组合：通用助手：纳米 AI 搜索 + 豆包。适合内容运营，流程是：纳米解析网页/PDF/视频并生成脑图；豆包改写成短文案。",
        "tags": [
            "通用助手",
            "video"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "纳米解析网页/PDF/视频并生成脑图；豆包改写成短文案。",
        "audience": "内容运营"
    },
    {
        "num": "010",
        "scenario": "通用助手",
        "title": "通用助手：秘塔 AI 搜索 + DeepSeek",
        "combo": "秘塔 AI 搜索 + DeepSeek",
        "id_slug": "general-assistant-metaso-ai-deepseek",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "秘塔 AI 搜索",
            "DeepSeek"
        ],
        "steps": [
            "秘塔找资料和来源",
            "DeepSeek 做推理、分类和提纲"
        ],
        "outputs": [
            "研究、写作"
        ],
        "summary": "国内 AI 工具组合：通用助手：秘塔 AI 搜索 + DeepSeek。适合研究、写作，流程是：秘塔找资料和来源；DeepSeek 做推理、分类和提纲。",
        "tags": [
            "通用助手"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "秘塔找资料和来源；DeepSeek 做推理、分类和提纲。",
        "audience": "研究、写作"
    },
    {
        "num": "011",
        "scenario": "研究报告",
        "title": "研究报告：秘塔 AI 搜索 + Kimi",
        "combo": "秘塔 AI 搜索 + Kimi",
        "id_slug": "research-report-metaso-ai-kimi",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "秘塔 AI 搜索",
            "Kimi"
        ],
        "steps": [
            "秘塔先搜资料和来源",
            "Kimi 吃网页/PDF，生成长报告、摘要和引用清单"
        ],
        "outputs": [
            "行业研究"
        ],
        "summary": "国内 AI 工具组合：研究报告：秘塔 AI 搜索 + Kimi。适合行业研究，流程是：秘塔先搜资料和来源；Kimi 吃网页/PDF，生成长报告、摘要和引用清单。",
        "tags": [
            "研究报告",
            "research"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "秘塔先搜资料和来源；Kimi 吃网页/PDF，生成长报告、摘要和引用清单。",
        "audience": "行业研究"
    },
    {
        "num": "012",
        "scenario": "研究报告",
        "title": "研究报告：纳米 AI 搜索 + Kimi",
        "combo": "纳米 AI 搜索 + Kimi",
        "id_slug": "research-report-nami-ai-kimi",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "纳米 AI 搜索",
            "Kimi"
        ],
        "steps": [
            "纳米把网页/PDF/视频整理成脑图",
            "Kimi 扩写成正式报告"
        ],
        "outputs": [
            "知识整理"
        ],
        "summary": "国内 AI 工具组合：研究报告：纳米 AI 搜索 + Kimi。适合知识整理，流程是：纳米把网页/PDF/视频整理成脑图；Kimi 扩写成正式报告。",
        "tags": [
            "研究报告",
            "video",
            "research"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "纳米把网页/PDF/视频整理成脑图；Kimi 扩写成正式报告。",
        "audience": "知识整理"
    },
    {
        "num": "013",
        "scenario": "研究报告",
        "title": "研究报告：天工 Skywork + WPS AI",
        "combo": "天工 Skywork + WPS AI",
        "id_slug": "research-report-skywork-skywork-wps-ai",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "天工 Skywork",
            "WPS AI"
        ],
        "steps": [
            "天工做研究和报告初稿",
            "WPS AI 排版成 Word/PPT/表格"
        ],
        "outputs": [
            "咨询、学生"
        ],
        "summary": "国内 AI 工具组合：研究报告：天工 Skywork + WPS AI。适合咨询、学生，流程是：天工做研究和报告初稿；WPS AI 排版成 Word/PPT/表格。",
        "tags": [
            "研究报告",
            "spreadsheet",
            "research"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "天工做研究和报告初稿；WPS AI 排版成 Word/PPT/表格。",
        "audience": "咨询、学生"
    },
    {
        "num": "014",
        "scenario": "研究报告",
        "title": "研究报告：腾讯元宝 + ima + Kimi",
        "combo": "腾讯元宝 + ima + Kimi",
        "id_slug": "research-report-yuanbao-ima-kimi",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "腾讯元宝",
            "ima",
            "Kimi"
        ],
        "steps": [
            "元宝查公众号/视频号资料",
            "ima 存知识库",
            "Kimi 做深度综述"
        ],
        "outputs": [
            "微信生态研究"
        ],
        "summary": "国内 AI 工具组合：研究报告：腾讯元宝 + ima + Kimi。适合微信生态研究，流程是：元宝查公众号/视频号资料；ima 存知识库；Kimi 做深度综述。",
        "tags": [
            "研究报告",
            "video",
            "rag",
            "research"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "元宝查公众号/视频号资料；ima 存知识库；Kimi 做深度综述。",
        "audience": "微信生态研究"
    },
    {
        "num": "015",
        "scenario": "研究报告",
        "title": "研究报告：DeepSeek + 通义千问",
        "combo": "DeepSeek + 通义千问",
        "id_slug": "research-report-deepseek-qwen",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "DeepSeek",
            "通义千问"
        ],
        "steps": [
            "DeepSeek 做成本敏感的批量资料初筛",
            "通义做多模态补充和成稿"
        ],
        "outputs": [
            "企业资料处理"
        ],
        "summary": "国内 AI 工具组合：研究报告：DeepSeek + 通义千问。适合企业资料处理，流程是：DeepSeek 做成本敏感的批量资料初筛；通义做多模态补充和成稿。",
        "tags": [
            "研究报告",
            "research"
        ],
        "importance": 91,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 做成本敏感的批量资料初筛；通义做多模态补充和成稿。",
        "audience": "企业资料处理"
    },
    {
        "num": "016",
        "scenario": "研究报告",
        "title": "研究报告：Kimi Deep Research + Kimi Slides",
        "combo": "Kimi Deep Research + Kimi Slides",
        "id_slug": "research-report-kimi-deep-research-kimi-slides",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Kimi Deep Research",
            "Kimi Slides"
        ],
        "steps": [
            "Kimi 先生成万字研究报告，再用 Slides 入口生成演示稿"
        ],
        "outputs": [
            "报告到 PPT"
        ],
        "summary": "国内 AI 工具组合：研究报告：Kimi Deep Research + Kimi Slides。适合报告到 PPT，流程是：Kimi 先生成万字研究报告，再用 Slides 入口生成演示稿。",
        "tags": [
            "研究报告",
            "research"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 先生成万字研究报告，再用 Slides 入口生成演示稿。",
        "audience": "报告到 PPT"
    },
    {
        "num": "017",
        "scenario": "研究报告",
        "title": "研究报告：飞书知识库 + 飞书 aily",
        "combo": "飞书知识库 + 飞书 aily",
        "id_slug": "research-report-feishu-knowledge-base-feishu-aily",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "飞书知识库",
            "飞书 aily"
        ],
        "steps": [
            "飞书 aily 读取文档、会议和消息，自动整理项目背景、风险和周报"
        ],
        "outputs": [
            "企业内部研究"
        ],
        "summary": "国内 AI 工具组合：研究报告：飞书知识库 + 飞书 aily。适合企业内部研究，流程是：飞书 aily 读取文档、会议和消息，自动整理项目背景、风险和周报。",
        "tags": [
            "研究报告",
            "docs",
            "meeting",
            "rag",
            "automation",
            "research"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "飞书 aily 读取文档、会议和消息，自动整理项目背景、风险和周报。",
        "audience": "企业内部研究"
    },
    {
        "num": "018",
        "scenario": "研究报告",
        "title": "研究报告：钉钉文档 + 通义 AI 助理",
        "combo": "钉钉文档 + 通义 AI 助理",
        "id_slug": "research-report-dingtalk-qwen-ai",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "通义 AI 助理"
        ],
        "steps": [
            "钉钉 AI 助理从文档和消息提炼项目复盘、纪要和行动项"
        ],
        "outputs": [
            "钉钉团队"
        ],
        "summary": "国内 AI 工具组合：研究报告：钉钉文档 + 通义 AI 助理。适合钉钉团队，流程是：钉钉 AI 助理从文档和消息提炼项目复盘、纪要和行动项。",
        "tags": [
            "研究报告",
            "docs",
            "research"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "钉钉 AI 助理从文档和消息提炼项目复盘、纪要和行动项。",
        "audience": "钉钉团队"
    },
    {
        "num": "019",
        "scenario": "研究报告",
        "title": "研究报告：ima + DeepSeek API",
        "combo": "ima + DeepSeek API",
        "id_slug": "research-report-ima-deepseek-api",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "ima",
            "DeepSeek API"
        ],
        "steps": [
            "ima 建私域资料库",
            "DeepSeek API 做批量问答、分类和摘要"
        ],
        "outputs": [
            "知识库运营"
        ],
        "summary": "国内 AI 工具组合：研究报告：ima + DeepSeek API。适合知识库运营，流程是：ima 建私域资料库；DeepSeek API 做批量问答、分类和摘要。",
        "tags": [
            "研究报告",
            "research"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "ima 建私域资料库；DeepSeek API 做批量问答、分类和摘要。",
        "audience": "知识库运营"
    },
    {
        "num": "020",
        "scenario": "研究报告",
        "title": "研究报告：秘塔 + 文小言",
        "combo": "秘塔 + 文小言",
        "id_slug": "research-report-metaso-wenxiaoyan",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "秘塔",
            "文小言"
        ],
        "steps": [
            "秘塔查证",
            "文小言写公文、策划案和论文式结构"
        ],
        "outputs": [
            "行政、公文"
        ],
        "summary": "国内 AI 工具组合：研究报告：秘塔 + 文小言。适合行政、公文，流程是：秘塔查证；文小言写公文、策划案和论文式结构。",
        "tags": [
            "研究报告",
            "research"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "秘塔查证；文小言写公文、策划案和论文式结构。",
        "audience": "行政、公文"
    },
    {
        "num": "021",
        "scenario": "PPT/办公",
        "title": "PPT/办公：Kimi + WPS AI",
        "combo": "Kimi + WPS AI",
        "id_slug": "ppt-kimi-wps-ai",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Kimi",
            "WPS AI"
        ],
        "steps": [
            "Kimi 整理资料和页结构",
            "WPS AI 一键生成 PPT 并美化"
        ],
        "outputs": [
            "工作汇报"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：Kimi + WPS AI。适合工作汇报，流程是：Kimi 整理资料和页结构；WPS AI 一键生成 PPT 并美化。",
        "tags": [
            "ppt-办公"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 整理资料和页结构；WPS AI 一键生成 PPT 并美化。",
        "audience": "工作汇报"
    },
    {
        "num": "022",
        "scenario": "PPT/办公",
        "title": "PPT/办公：通义 + AiPPT",
        "combo": "通义 + AiPPT",
        "id_slug": "ppt-qwen-ai-ppt",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "通义",
            "AiPPT"
        ],
        "steps": [
            "通义生成大纲和讲稿",
            "AiPPT 输出可编辑源文件"
        ],
        "outputs": [
            "快速提案"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：通义 + AiPPT。适合快速提案，流程是：通义生成大纲和讲稿；AiPPT 输出可编辑源文件。",
        "tags": [
            "ppt-办公"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "通义生成大纲和讲稿；AiPPT 输出可编辑源文件。",
        "audience": "快速提案"
    },
    {
        "num": "023",
        "scenario": "PPT/办公",
        "title": "PPT/办公：天工 Skywork + WPS AI",
        "combo": "天工 Skywork + WPS AI",
        "id_slug": "ppt-skywork-skywork-wps-ai",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "天工 Skywork",
            "WPS AI"
        ],
        "steps": [
            "天工完成研究报告",
            "WPS AI 生成演示稿、表格和文档"
        ],
        "outputs": [
            "综合办公"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：天工 Skywork + WPS AI。适合综合办公，流程是：天工完成研究报告；WPS AI 生成演示稿、表格和文档。",
        "tags": [
            "ppt-办公",
            "docs",
            "spreadsheet",
            "research"
        ],
        "importance": 90,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "天工完成研究报告；WPS AI 生成演示稿、表格和文档。",
        "audience": "综合办公"
    },
    {
        "num": "024",
        "scenario": "PPT/办公",
        "title": "PPT/办公：Kimi Slides + 通义万相",
        "combo": "Kimi Slides + 通义万相",
        "id_slug": "ppt-kimi-slides-qwen",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "Kimi Slides",
            "通义万相"
        ],
        "steps": [
            "Kimi 生成 slides",
            "通义万相补图、海报和封面"
        ],
        "outputs": [
            "培训/路演"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：Kimi Slides + 通义万相。适合培训/路演，流程是：Kimi 生成 slides；通义万相补图、海报和封面。",
        "tags": [
            "ppt-办公"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 生成 slides；通义万相补图、海报和封面。",
        "audience": "培训/路演"
    },
    {
        "num": "025",
        "scenario": "PPT/办公",
        "title": "PPT/办公：豆包 + 即梦 + WPS AI",
        "combo": "豆包 + 即梦 + WPS AI",
        "id_slug": "ppt-doubao-jimeng-wps-ai",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "豆包",
            "即梦",
            "WPS AI"
        ],
        "steps": [
            "豆包写文案",
            "即梦生成视觉素材",
            "WPS AI 组装 PPT"
        ],
        "outputs": [
            "市场活动"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：豆包 + 即梦 + WPS AI。适合市场活动，流程是：豆包写文案；即梦生成视觉素材；WPS AI 组装 PPT。",
        "tags": [
            "ppt-办公"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写文案；即梦生成视觉素材；WPS AI 组装 PPT。",
        "audience": "市场活动"
    },
    {
        "num": "026",
        "scenario": "PPT/办公",
        "title": "PPT/办公：飞书妙搭 + 飞书文档",
        "combo": "飞书妙搭 + 飞书文档",
        "id_slug": "ppt-feishu-feishu",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "飞书妙搭",
            "飞书文档"
        ],
        "steps": [
            "用自然语言搭合同/表单工具，自动填字段并导出 Word"
        ],
        "outputs": [
            "商务合同"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：飞书妙搭 + 飞书文档。适合商务合同，流程是：用自然语言搭合同/表单工具，自动填字段并导出 Word。",
        "tags": [
            "ppt-办公",
            "docs",
            "automation",
            "legal"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用自然语言搭合同/表单工具，自动填字段并导出 Word。",
        "audience": "商务合同"
    },
    {
        "num": "027",
        "scenario": "PPT/办公",
        "title": "PPT/办公：飞书多维表格 Agent + 飞书文档",
        "combo": "飞书多维表格 Agent + 飞书文档",
        "id_slug": "ppt-feishu-base-agent-feishu",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "飞书多维表格 Agent",
            "飞书文档"
        ],
        "steps": [
            "表格数据一句话生成图表和洞察，再同步到飞书文档周报"
        ],
        "outputs": [
            "运营周报"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：飞书多维表格 Agent + 飞书文档。适合运营周报，流程是：表格数据一句话生成图表和洞察，再同步到飞书文档周报。",
        "tags": [
            "ppt-办公",
            "docs",
            "spreadsheet",
            "data"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "表格数据一句话生成图表和洞察，再同步到飞书文档周报。",
        "audience": "运营周报"
    },
    {
        "num": "028",
        "scenario": "PPT/办公",
        "title": "PPT/办公：钉钉 AI 助理 + 多维表格",
        "combo": "钉钉 AI 助理 + 多维表格",
        "id_slug": "ppt-dingtalk-ai-base",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "钉钉 AI 助理"
        ],
        "steps": [
            "导入销售数据，定时生成销售周报并推送管理层"
        ],
        "outputs": [
            "销售管理"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：钉钉 AI 助理 + 多维表格。适合销售管理，流程是：导入销售数据，定时生成销售周报并推送管理层。",
        "tags": [
            "ppt-办公",
            "spreadsheet",
            "sales",
            "data"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "导入销售数据，定时生成销售周报并推送管理层。",
        "audience": "销售管理"
    },
    {
        "num": "029",
        "scenario": "PPT/办公",
        "title": "PPT/办公：通义听悟 + WPS AI",
        "combo": "通义听悟 + WPS AI",
        "id_slug": "ppt-qwen-wps-ai",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "通义听悟",
            "WPS AI"
        ],
        "steps": [
            "音视频转写为纪要",
            "WPS AI 生成会议报告或 PPT"
        ],
        "outputs": [
            "会议复盘"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：通义听悟 + WPS AI。适合会议复盘，流程是：音视频转写为纪要；WPS AI 生成会议报告或 PPT。",
        "tags": [
            "ppt-办公",
            "meeting",
            "video"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "音视频转写为纪要；WPS AI 生成会议报告或 PPT。",
        "audience": "会议复盘"
    },
    {
        "num": "030",
        "scenario": "PPT/办公",
        "title": "PPT/办公：百度文库 AI + 文小言",
        "combo": "百度文库 AI + 文小言",
        "id_slug": "ppt-ai-wenxiaoyan",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tools": [
            "百度文库 AI",
            "文小言"
        ],
        "steps": [
            "文库找模板/资料",
            "文小言改写成公文、申请书、汇报稿"
        ],
        "outputs": [
            "行政材料"
        ],
        "summary": "国内 AI 工具组合：PPT/办公：百度文库 AI + 文小言。适合行政材料，流程是：文库找模板/资料；文小言改写成公文、申请书、汇报稿。",
        "tags": [
            "ppt-办公"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "文库找模板/资料；文小言改写成公文、申请书、汇报稿。",
        "audience": "行政材料"
    },
    {
        "num": "031",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书 aily + 飞书消息",
        "combo": "飞书 aily + 飞书消息",
        "id_slug": "feishu-workflow-feishu-aily-feishu",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书 aily"
        ],
        "steps": [
            "自动读取聊天、会议、任务，按模板生成个人或团队周报"
        ],
        "outputs": [
            "团队管理"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书 aily + 飞书消息。适合团队管理，流程是：自动读取聊天、会议、任务，按模板生成个人或团队周报。",
        "tags": [
            "飞书工作流",
            "meeting",
            "automation"
        ],
        "importance": 89,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "自动读取聊天、会议、任务，按模板生成个人或团队周报。",
        "audience": "团队管理"
    },
    {
        "num": "032",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书 aily + SkillHub",
        "combo": "飞书 aily + SkillHub",
        "id_slug": "feishu-workflow-feishu-aily-skillhub",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书 aily",
            "SkillHub"
        ],
        "steps": [
            "安装网页抓取/数据分析/文档生成技能，变成部门专用助手"
        ],
        "outputs": [
            "企业助手"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书 aily + SkillHub。适合企业助手，流程是：安装网页抓取/数据分析/文档生成技能，变成部门专用助手。",
        "tags": [
            "飞书工作流",
            "docs",
            "data"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "安装网页抓取/数据分析/文档生成技能，变成部门专用助手。",
        "audience": "企业助手"
    },
    {
        "num": "033",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书多维表格 + AI 问数据",
        "combo": "飞书多维表格 + AI 问数据",
        "id_slug": "feishu-workflow-feishu-base-ai-data",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书多维表格"
        ],
        "steps": [
            "自然语言问表格，自动统计、分析和给出业务洞察"
        ],
        "outputs": [
            "运营/数据"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书多维表格 + AI 问数据。适合运营/数据，流程是：自然语言问表格，自动统计、分析和给出业务洞察。",
        "tags": [
            "飞书工作流",
            "spreadsheet",
            "data",
            "automation"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "自然语言问表格，自动统计、分析和给出业务洞察。",
        "audience": "运营/数据"
    },
    {
        "num": "034",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书多维表格 + AI 生成图表",
        "combo": "飞书多维表格 + AI 生成图表",
        "id_slug": "feishu-workflow-feishu-base-ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书多维表格"
        ],
        "steps": [
            "一句话生成热力图、矩形树图、柱状图并写结论"
        ],
        "outputs": [
            "内容团队"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书多维表格 + AI 生成图表。适合内容团队，流程是：一句话生成热力图、矩形树图、柱状图并写结论。",
        "tags": [
            "飞书工作流",
            "spreadsheet"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "一句话生成热力图、矩形树图、柱状图并写结论。",
        "audience": "内容团队"
    },
    {
        "num": "035",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书多维表格 + AI 搭页面",
        "combo": "飞书多维表格 + AI 搭页面",
        "id_slug": "feishu-workflow-feishu-base-ai-2",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书多维表格"
        ],
        "steps": [
            "从表格生成 H5 战报页，数据实时同步更新"
        ],
        "outputs": [
            "电商/活动复盘"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书多维表格 + AI 搭页面。适合电商/活动复盘，流程是：从表格生成 H5 战报页，数据实时同步更新。",
        "tags": [
            "飞书工作流",
            "spreadsheet",
            "data"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "从表格生成 H5 战报页，数据实时同步更新。",
        "audience": "电商/活动复盘"
    },
    {
        "num": "036",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书多维表格 + AI 生成问卷",
        "combo": "飞书多维表格 + AI 生成问卷",
        "id_slug": "feishu-workflow-feishu-base-ai-3",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书多维表格"
        ],
        "steps": [
            "用自然语言生成巡检表、调研表、报名表并扫码收集"
        ],
        "outputs": [
            "制造/运营"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书多维表格 + AI 生成问卷。适合制造/运营，流程是：用自然语言生成巡检表、调研表、报名表并扫码收集。",
        "tags": [
            "飞书工作流",
            "spreadsheet"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用自然语言生成巡检表、调研表、报名表并扫码收集。",
        "audience": "制造/运营"
    },
    {
        "num": "037",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书妙搭 + 合同模板",
        "combo": "飞书妙搭 + 合同模板",
        "id_slug": "feishu-workflow-feishu-contract",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书妙搭"
        ],
        "steps": [
            "识别合同可变字段，生成表单、预览并一键导出 Word"
        ],
        "outputs": [
            "商务/法务"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书妙搭 + 合同模板。适合商务/法务，流程是：识别合同可变字段，生成表单、预览并一键导出 Word。",
        "tags": [
            "飞书工作流",
            "legal"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "识别合同可变字段，生成表单、预览并一键导出 Word。",
        "audience": "商务/法务"
    },
    {
        "num": "038",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书 CLI + OpenClaw 插件",
        "combo": "飞书 CLI + OpenClaw 插件",
        "id_slug": "feishu-workflow-feishu-cli-openclaw",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书 CLI",
            "OpenClaw 插件"
        ],
        "steps": [
            "开发 agent/插件自动读取项目资料、跑脚本和生成交付物"
        ],
        "outputs": [
            "开发/运维"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书 CLI + OpenClaw 插件。适合开发/运维，流程是：开发 agent/插件自动读取项目资料、跑脚本和生成交付物。",
        "tags": [
            "飞书工作流",
            "automation"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "开发 agent/插件自动读取项目资料、跑脚本和生成交付物。",
        "audience": "开发/运维"
    },
    {
        "num": "039",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书 aily + Kimi",
        "combo": "飞书 aily + Kimi",
        "id_slug": "feishu-workflow-feishu-aily-kimi",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书 aily",
            "Kimi"
        ],
        "steps": [
            "飞书 aily 汇总内部材料，Kimi 做长报告和对外版改写"
        ],
        "outputs": [
            "咨询/项目"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书 aily + Kimi。适合咨询/项目，流程是：飞书 aily 汇总内部材料，Kimi 做长报告和对外版改写。",
        "tags": [
            "飞书工作流"
        ],
        "importance": 88,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "飞书 aily 汇总内部材料，Kimi 做长报告和对外版改写。",
        "audience": "咨询/项目"
    },
    {
        "num": "040",
        "scenario": "飞书工作流",
        "title": "飞书工作流：飞书 + 扣子工作流",
        "combo": "飞书 + 扣子工作流",
        "id_slug": "feishu-workflow-feishu-coze-cn-workflow",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书",
            "扣子工作流"
        ],
        "steps": [
            "扣子编排外部工具，飞书负责消息、审批和团队分发"
        ],
        "outputs": [
            "企业自动化"
        ],
        "summary": "国内 AI 工具组合：飞书工作流：飞书 + 扣子工作流。适合企业自动化，流程是：扣子编排外部工具，飞书负责消息、审批和团队分发。",
        "tags": [
            "飞书工作流"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "扣子编排外部工具，飞书负责消息、审批和团队分发。",
        "audience": "企业自动化"
    },
    {
        "num": "041",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 AI 助理 + 消息",
        "combo": "钉钉 AI 助理 + 消息",
        "id_slug": "dingtalk-workflow-dingtalk-ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉 AI 助理"
        ],
        "steps": [
            "在聊天中调用 AI 摘要长讨论、生成待办和回复草稿"
        ],
        "outputs": [
            "钉钉团队"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 AI 助理 + 消息。适合钉钉团队，流程是：在聊天中调用 AI 摘要长讨论、生成待办和回复草稿。",
        "tags": [
            "钉钉工作流"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "在聊天中调用 AI 摘要长讨论、生成待办和回复草稿。",
        "audience": "钉钉团队"
    },
    {
        "num": "042",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 AI 助理 + 文档",
        "combo": "钉钉 AI 助理 + 文档",
        "id_slug": "dingtalk-workflow-dingtalk-ai-2",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉 AI 助理"
        ],
        "steps": [
            "从项目文档生成会议提纲、汇报稿和执行清单"
        ],
        "outputs": [
            "项目管理"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 AI 助理 + 文档。适合项目管理，流程是：从项目文档生成会议提纲、汇报稿和执行清单。",
        "tags": [
            "钉钉工作流",
            "docs",
            "meeting"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "从项目文档生成会议提纲、汇报稿和执行清单。",
        "audience": "项目管理"
    },
    {
        "num": "043",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 AI 助理 + 会议",
        "combo": "钉钉 AI 助理 + 会议",
        "id_slug": "dingtalk-workflow-dingtalk-ai-3",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉 AI 助理"
        ],
        "steps": [
            "会议转写、摘要、行动项和自动分发"
        ],
        "outputs": [
            "远程会议"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 AI 助理 + 会议。适合远程会议，流程是：会议转写、摘要、行动项和自动分发。",
        "tags": [
            "钉钉工作流",
            "meeting",
            "automation"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "会议转写、摘要、行动项和自动分发。",
        "audience": "远程会议"
    },
    {
        "num": "044",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉多维表格 + 通义",
        "combo": "钉钉多维表格 + 通义",
        "id_slug": "dingtalk-workflow-dingtalk-base-qwen",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉多维表格",
            "通义"
        ],
        "steps": [
            "多维表格沉淀数据",
            "通义生成分析结论和周报"
        ],
        "outputs": [
            "销售/行政"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉多维表格 + 通义。适合销售/行政，流程是：多维表格沉淀数据；通义生成分析结论和周报。",
        "tags": [
            "钉钉工作流",
            "spreadsheet",
            "data"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "多维表格沉淀数据；通义生成分析结论和周报。",
        "audience": "销售/行政"
    },
    {
        "num": "045",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：宜搭 + 通义 AI",
        "combo": "宜搭 + 通义 AI",
        "id_slug": "dingtalk-workflow-qwen-ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "宜搭",
            "通义 AI"
        ],
        "steps": [
            "自然语言生成内部应用、审批表单和业务流程"
        ],
        "outputs": [
            "企业数字化"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：宜搭 + 通义 AI。适合企业数字化，流程是：自然语言生成内部应用、审批表单和业务流程。",
        "tags": [
            "钉钉工作流"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "自然语言生成内部应用、审批表单和业务流程。",
        "audience": "企业数字化"
    },
    {
        "num": "046",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉酷应用 + AI 助理",
        "combo": "钉钉酷应用 + AI 助理",
        "id_slug": "dingtalk-workflow-dingtalk-ai-4",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉酷应用"
        ],
        "steps": [
            "把轻应用嵌入聊天窗口，减少系统切换"
        ],
        "outputs": [
            "一线业务"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉酷应用 + AI 助理。适合一线业务，流程是：把轻应用嵌入聊天窗口，减少系统切换。",
        "tags": [
            "钉钉工作流"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把轻应用嵌入聊天窗口，减少系统切换。",
        "audience": "一线业务"
    },
    {
        "num": "047",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 + WPS AI",
        "combo": "钉钉 + WPS AI",
        "id_slug": "dingtalk-workflow-dingtalk-wps-ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉",
            "WPS AI"
        ],
        "steps": [
            "钉钉沉淀任务和会议",
            "WPS AI 输出正式文档/PPT"
        ],
        "outputs": [
            "行政办公"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 + WPS AI。适合行政办公，流程是：钉钉沉淀任务和会议；WPS AI 输出正式文档/PPT。",
        "tags": [
            "钉钉工作流",
            "docs",
            "meeting"
        ],
        "importance": 87,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "钉钉沉淀任务和会议；WPS AI 输出正式文档/PPT。",
        "audience": "行政办公"
    },
    {
        "num": "048",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 + DeepSeek API",
        "combo": "钉钉 + DeepSeek API",
        "id_slug": "dingtalk-workflow-dingtalk-deepseek-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉",
            "DeepSeek API"
        ],
        "steps": [
            "钉钉机器人接 DeepSeek API 做工单分类、摘要和提醒"
        ],
        "outputs": [
            "客服/IT"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 + DeepSeek API。适合客服/IT，流程是：钉钉机器人接 DeepSeek API 做工单分类、摘要和提醒。",
        "tags": [
            "钉钉工作流"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "钉钉机器人接 DeepSeek API 做工单分类、摘要和提醒。",
        "audience": "客服/IT"
    },
    {
        "num": "049",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 + 通义听悟",
        "combo": "钉钉 + 通义听悟",
        "id_slug": "dingtalk-workflow-dingtalk-qwen",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉",
            "通义听悟"
        ],
        "steps": [
            "会议录音转写后同步到钉钉文档和任务"
        ],
        "outputs": [
            "培训/会议"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 + 通义听悟。适合培训/会议，流程是：会议录音转写后同步到钉钉文档和任务。",
        "tags": [
            "钉钉工作流",
            "docs",
            "meeting"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "会议录音转写后同步到钉钉文档和任务。",
        "audience": "培训/会议"
    },
    {
        "num": "050",
        "scenario": "钉钉工作流",
        "title": "钉钉工作流：钉钉 + 扣子",
        "combo": "钉钉 + 扣子",
        "id_slug": "dingtalk-workflow-dingtalk-coze-cn",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉",
            "扣子"
        ],
        "steps": [
            "扣子做智能体和外部 API，钉钉做入口和通知"
        ],
        "outputs": [
            "自动化顾问"
        ],
        "summary": "国内 AI 工具组合：钉钉工作流：钉钉 + 扣子。适合自动化顾问，流程是：扣子做智能体和外部 API，钉钉做入口和通知。",
        "tags": [
            "钉钉工作流"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "扣子做智能体和外部 API，钉钉做入口和通知。",
        "audience": "自动化顾问"
    },
    {
        "num": "051",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 + 豆包 Pro",
        "combo": "扣子 + 豆包 Pro",
        "id_slug": "coze-cn-agent-coze-cn-doubao-pro",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子",
            "豆包 Pro"
        ],
        "steps": [
            "用豆包 Pro 作为智能体大脑，结合知识库和插件做客服/咨询机器人"
        ],
        "outputs": [
            "客服/咨询"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 + 豆包 Pro。适合客服/咨询，流程是：用豆包 Pro 作为智能体大脑，结合知识库和插件做客服/咨询机器人。",
        "tags": [
            "扣子-agent",
            "rag",
            "support"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用豆包 Pro 作为智能体大脑，结合知识库和插件做客服/咨询机器人。",
        "audience": "客服/咨询"
    },
    {
        "num": "052",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子工作流 + 飞书",
        "combo": "扣子工作流 + 飞书",
        "id_slug": "coze-cn-agent-coze-cn-workflow-feishu",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子工作流",
            "飞书"
        ],
        "steps": [
            "可视化节点编排任务，一键发布到飞书群和飞书应用"
        ],
        "outputs": [
            "企业内部助手"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子工作流 + 飞书。适合企业内部助手，流程是：可视化节点编排任务，一键发布到飞书群和飞书应用。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "可视化节点编排任务，一键发布到飞书群和飞书应用。",
        "audience": "企业内部助手"
    },
    {
        "num": "053",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 + 微信公众号",
        "combo": "扣子 + 微信公众号",
        "id_slug": "coze-cn-agent-coze-cn",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子",
            "微信公众号"
        ],
        "steps": [
            "构建问答/资料查询 bot，发布到公众号接收用户咨询"
        ],
        "outputs": [
            "私域运营"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 + 微信公众号。适合私域运营，流程是：构建问答/资料查询 bot，发布到公众号接收用户咨询。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "构建问答/资料查询 bot，发布到公众号接收用户咨询。",
        "audience": "私域运营"
    },
    {
        "num": "054",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 + 抖音",
        "combo": "扣子 + 抖音",
        "id_slug": "coze-cn-agent-coze-cn-2",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子",
            "抖音"
        ],
        "steps": [
            "把短视频脚本、评论回复、私信问答做成可复用 bot"
        ],
        "outputs": [
            "抖音运营"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 + 抖音。适合抖音运营，流程是：把短视频脚本、评论回复、私信问答做成可复用 bot。",
        "tags": [
            "扣子-agent",
            "video"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把短视频脚本、评论回复、私信问答做成可复用 bot。",
        "audience": "抖音运营"
    },
    {
        "num": "055",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 + API + 网页",
        "combo": "扣子 + API + 网页",
        "id_slug": "coze-cn-agent-coze-cn-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子"
        ],
        "steps": [
            "把模型、检索、Python 节点封装成 Web 工具"
        ],
        "outputs": [
            "轻 SaaS"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 + API + 网页。适合轻 SaaS，流程是：把模型、检索、Python 节点封装成 Web 工具。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 86,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把模型、检索、Python 节点封装成 Web 工具。",
        "audience": "轻 SaaS"
    },
    {
        "num": "056",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 Agent Skills + 法律检索",
        "combo": "扣子 Agent Skills + 法律检索",
        "id_slug": "coze-cn-agent-coze-cn-agent-skills-legal",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子 Agent Skills"
        ],
        "steps": [
            "把法规检索、案例摘要、风险提示封成技能包"
        ],
        "outputs": [
            "法务助手"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 Agent Skills + 法律检索。适合法务助手，流程是：把法规检索、案例摘要、风险提示封成技能包。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把法规检索、案例摘要、风险提示封成技能包。",
        "audience": "法务助手"
    },
    {
        "num": "057",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 Agent Plan + 增长运营",
        "combo": "扣子 Agent Plan + 增长运营",
        "id_slug": "coze-cn-agent-coze-cn-agent-plan",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子 Agent Plan"
        ],
        "steps": [
            "设定 30 天涨粉目标，AI 拆成选题、发布、复盘任务"
        ],
        "outputs": [
            "自媒体增长"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 Agent Plan + 增长运营。适合自媒体增长，流程是：设定 30 天涨粉目标，AI 拆成选题、发布、复盘任务。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "设定 30 天涨粉目标，AI 拆成选题、发布、复盘任务。",
        "audience": "自媒体增长"
    },
    {
        "num": "058",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 Agent Coding + 业务流程",
        "combo": "扣子 Agent Coding + 业务流程",
        "id_slug": "coze-cn-agent-coze-cn-agent-coding",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子 Agent Coding"
        ],
        "steps": [
            "自然语言描述需求，生成完整工作流并部署"
        ],
        "outputs": [
            "非技术人员"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 Agent Coding + 业务流程。适合非技术人员，流程是：自然语言描述需求，生成完整工作流并部署。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "自然语言描述需求，生成完整工作流并部署。",
        "audience": "非技术人员"
    },
    {
        "num": "059",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子视频 Agent + 即梦/Seedance",
        "combo": "扣子视频 Agent + 即梦/Seedance",
        "id_slug": "coze-cn-agent-coze-cn-agent-jimeng-seedance",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子视频 Agent",
            "即梦",
            "Seedance"
        ],
        "steps": [
            "生成分镜、图生视频、配音和口型匹配，输出长视频雏形"
        ],
        "outputs": [
            "视频创作"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子视频 Agent + 即梦/Seedance。适合视频创作，流程是：生成分镜、图生视频、配音和口型匹配，输出长视频雏形。",
        "tags": [
            "扣子-agent",
            "video"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成分镜、图生视频、配音和口型匹配，输出长视频雏形。",
        "audience": "视频创作"
    },
    {
        "num": "060",
        "scenario": "扣子/Agent",
        "title": "扣子/Agent：扣子 + 火山引擎",
        "combo": "扣子 + 火山引擎",
        "id_slug": "coze-cn-agent-coze-cn-3",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子",
            "火山引擎"
        ],
        "steps": [
            "扣子做编排，火山引擎提供模型/API/部署能力"
        ],
        "outputs": [
            "企业 AI 应用"
        ],
        "summary": "国内 AI 工具组合：扣子/Agent：扣子 + 火山引擎。适合企业 AI 应用，流程是：扣子做编排，火山引擎提供模型/API/部署能力。",
        "tags": [
            "扣子-agent"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "扣子做编排，火山引擎提供模型/API/部署能力。",
        "audience": "企业 AI 应用"
    },
    {
        "num": "061",
        "scenario": "内容写作",
        "title": "内容写作：Kimi + 秘塔 + 即梦",
        "combo": "Kimi + 秘塔 + 即梦",
        "id_slug": "content-writing-kimi-metaso-jimeng",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi",
            "秘塔",
            "即梦"
        ],
        "steps": [
            "秘塔搜资料，Kimi 写长文和提纲，即梦生成封面图"
        ],
        "outputs": [
            "博客/内容站"
        ],
        "summary": "国内 AI 工具组合：内容写作：Kimi + 秘塔 + 即梦。适合博客/内容站，流程是：秘塔搜资料，Kimi 写长文和提纲，即梦生成封面图。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "秘塔搜资料，Kimi 写长文和提纲，即梦生成封面图。",
        "audience": "博客/内容站"
    },
    {
        "num": "062",
        "scenario": "内容写作",
        "title": "内容写作：豆包 + 小红书",
        "combo": "豆包 + 小红书",
        "id_slug": "content-writing-doubao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "豆包",
            "小红书"
        ],
        "steps": [
            "豆包生成标题、正文、评论回复和选题方向"
        ],
        "outputs": [
            "小红书运营"
        ],
        "summary": "国内 AI 工具组合：内容写作：豆包 + 小红书。适合小红书运营，流程是：豆包生成标题、正文、评论回复和选题方向。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包生成标题、正文、评论回复和选题方向。",
        "audience": "小红书运营"
    },
    {
        "num": "063",
        "scenario": "内容写作",
        "title": "内容写作：腾讯元宝 + 微信公众号",
        "combo": "腾讯元宝 + 微信公众号",
        "id_slug": "content-writing-yuanbao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "腾讯元宝",
            "微信公众号"
        ],
        "steps": [
            "元宝查公众号资料和热点",
            "生成公众号文章初稿"
        ],
        "outputs": [
            "公众号作者"
        ],
        "summary": "国内 AI 工具组合：内容写作：腾讯元宝 + 微信公众号。适合公众号作者，流程是：元宝查公众号资料和热点；生成公众号文章初稿。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 85,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "元宝查公众号资料和热点；生成公众号文章初稿。",
        "audience": "公众号作者"
    },
    {
        "num": "064",
        "scenario": "内容写作",
        "title": "内容写作：ima + 公众号素材",
        "combo": "ima + 公众号素材",
        "id_slug": "content-writing-ima",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ima"
        ],
        "steps": [
            "把公众号/报告/网页存入 ima，长期生成选题和文章"
        ],
        "outputs": [
            "知识博主"
        ],
        "summary": "国内 AI 工具组合：内容写作：ima + 公众号素材。适合知识博主，流程是：把公众号/报告/网页存入 ima，长期生成选题和文章。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把公众号/报告/网页存入 ima，长期生成选题和文章。",
        "audience": "知识博主"
    },
    {
        "num": "065",
        "scenario": "内容写作",
        "title": "内容写作：DeepSeek + 文小言",
        "combo": "DeepSeek + 文小言",
        "id_slug": "content-writing-deepseek-wenxiaoyan",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek",
            "文小言"
        ],
        "steps": [
            "DeepSeek 做观点和结构，文小言改成正式公文/策划"
        ],
        "outputs": [
            "企业文案"
        ],
        "summary": "国内 AI 工具组合：内容写作：DeepSeek + 文小言。适合企业文案，流程是：DeepSeek 做观点和结构，文小言改成正式公文/策划。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 做观点和结构，文小言改成正式公文/策划。",
        "audience": "企业文案"
    },
    {
        "num": "066",
        "scenario": "内容写作",
        "title": "内容写作：通义 + 通义万相",
        "combo": "通义 + 通义万相",
        "id_slug": "content-writing-qwen-qwen",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "通义",
            "通义万相"
        ],
        "steps": [
            "通义写文案，万相生成配图/海报"
        ],
        "outputs": [
            "营销内容"
        ],
        "summary": "国内 AI 工具组合：内容写作：通义 + 通义万相。适合营销内容，流程是：通义写文案，万相生成配图/海报。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "通义写文案，万相生成配图/海报。",
        "audience": "营销内容"
    },
    {
        "num": "067",
        "scenario": "内容写作",
        "title": "内容写作：讯飞星火 + 讯飞听见",
        "combo": "讯飞星火 + 讯飞听见",
        "id_slug": "content-writing-spark",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "讯飞星火",
            "讯飞听见"
        ],
        "steps": [
            "听见转写采访，星火整理成稿件"
        ],
        "outputs": [
            "媒体/访谈"
        ],
        "summary": "国内 AI 工具组合：内容写作：讯飞星火 + 讯飞听见。适合媒体/访谈，流程是：听见转写采访，星火整理成稿件。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "听见转写采访，星火整理成稿件。",
        "audience": "媒体/访谈"
    },
    {
        "num": "068",
        "scenario": "内容写作",
        "title": "内容写作：天工 + AiPPT",
        "combo": "天工 + AiPPT",
        "id_slug": "content-writing-skywork-ai-ppt",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "天工",
            "AiPPT"
        ],
        "steps": [
            "天工做研究和长文，AiPPT 做公开课/直播课件"
        ],
        "outputs": [
            "课程/培训"
        ],
        "summary": "国内 AI 工具组合：内容写作：天工 + AiPPT。适合课程/培训，流程是：天工做研究和长文，AiPPT 做公开课/直播课件。",
        "tags": [
            "内容写作",
            "research",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "天工做研究和长文，AiPPT 做公开课/直播课件。",
        "audience": "课程/培训"
    },
    {
        "num": "069",
        "scenario": "内容写作",
        "title": "内容写作：Kimi + 剪映",
        "combo": "Kimi + 剪映",
        "id_slug": "content-writing-kimi-jianying",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi",
            "剪映"
        ],
        "steps": [
            "Kimi 写脚本和分镜，剪映做剪辑和字幕"
        ],
        "outputs": [
            "短视频"
        ],
        "summary": "国内 AI 工具组合：内容写作：Kimi + 剪映。适合短视频，流程是：Kimi 写脚本和分镜，剪映做剪辑和字幕。",
        "tags": [
            "内容写作",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 写脚本和分镜，剪映做剪辑和字幕。",
        "audience": "短视频"
    },
    {
        "num": "070",
        "scenario": "内容写作",
        "title": "内容写作：豆包 + 即梦 + 剪映",
        "combo": "豆包 + 即梦 + 剪映",
        "id_slug": "content-writing-doubao-jimeng-jianying",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "豆包",
            "即梦",
            "剪映"
        ],
        "steps": [
            "豆包写脚本，即梦出图/视频，剪映成片"
        ],
        "outputs": [
            "抖音/视频号"
        ],
        "summary": "国内 AI 工具组合：内容写作：豆包 + 即梦 + 剪映。适合抖音/视频号，流程是：豆包写脚本，即梦出图/视频，剪映成片。",
        "tags": [
            "内容写作",
            "video",
            "content"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写脚本，即梦出图/视频，剪映成片。",
        "audience": "抖音/视频号"
    },
    {
        "num": "071",
        "scenario": "视频生成",
        "title": "视频生成：豆包 + 可灵 AI",
        "combo": "豆包 + 可灵 AI",
        "id_slug": "video-generation-doubao-kling-ai",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "豆包",
            "可灵 AI"
        ],
        "steps": [
            "豆包写剧情、镜头、旁白",
            "可灵生成视频片段"
        ],
        "outputs": [
            "短片创作"
        ],
        "summary": "国内 AI 工具组合：视频生成：豆包 + 可灵 AI。适合短片创作，流程是：豆包写剧情、镜头、旁白；可灵生成视频片段。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 84,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写剧情、镜头、旁白；可灵生成视频片段。",
        "audience": "短片创作"
    },
    {
        "num": "072",
        "scenario": "视频生成",
        "title": "视频生成：豆包 + 海螺 AI",
        "combo": "豆包 + 海螺 AI",
        "id_slug": "video-generation-doubao-hailuo-ai",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "豆包",
            "海螺 AI"
        ],
        "steps": [
            "豆包写口播脚本",
            "海螺生成镜头或人物视频"
        ],
        "outputs": [
            "口播/广告"
        ],
        "summary": "国内 AI 工具组合：视频生成：豆包 + 海螺 AI。适合口播/广告，流程是：豆包写口播脚本；海螺生成镜头或人物视频。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写口播脚本；海螺生成镜头或人物视频。",
        "audience": "口播/广告"
    },
    {
        "num": "073",
        "scenario": "视频生成",
        "title": "视频生成：即梦 + Seedance 2.0",
        "combo": "即梦 + Seedance 2.0",
        "id_slug": "video-generation-jimeng-seedance-2-0",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "即梦",
            "Seedance 2.0"
        ],
        "steps": [
            "即梦使用 Seedance 生成文生视频/图生视频，再人工剪辑"
        ],
        "outputs": [
            "视觉创作"
        ],
        "summary": "国内 AI 工具组合：视频生成：即梦 + Seedance 2.0。适合视觉创作，流程是：即梦使用 Seedance 生成文生视频/图生视频，再人工剪辑。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "即梦使用 Seedance 生成文生视频/图生视频，再人工剪辑。",
        "audience": "视觉创作"
    },
    {
        "num": "074",
        "scenario": "视频生成",
        "title": "视频生成：剪映 + 小云雀/Seedance",
        "combo": "剪映 + 小云雀/Seedance",
        "id_slug": "video-generation-jianying-seedance",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "剪映",
            "小云雀",
            "Seedance"
        ],
        "steps": [
            "剪映入口生成 AI 视频素材，接字幕、配乐和发布"
        ],
        "outputs": [
            "短视频团队"
        ],
        "summary": "国内 AI 工具组合：视频生成：剪映 + 小云雀/Seedance。适合短视频团队，流程是：剪映入口生成 AI 视频素材，接字幕、配乐和发布。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "剪映入口生成 AI 视频素材，接字幕、配乐和发布。",
        "audience": "短视频团队"
    },
    {
        "num": "075",
        "scenario": "视频生成",
        "title": "视频生成：Vidu + Kimi",
        "combo": "Vidu + Kimi",
        "id_slug": "video-generation-vidu-kimi",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Vidu",
            "Kimi"
        ],
        "steps": [
            "Kimi 写动画剧集大纲和分镜，Vidu 生成动画片段"
        ],
        "outputs": [
            "动画原型"
        ],
        "summary": "国内 AI 工具组合：视频生成：Vidu + Kimi。适合动画原型，流程是：Kimi 写动画剧集大纲和分镜，Vidu 生成动画片段。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 写动画剧集大纲和分镜，Vidu 生成动画片段。",
        "audience": "动画原型"
    },
    {
        "num": "076",
        "scenario": "视频生成",
        "title": "视频生成：SkyReels + 豆包",
        "combo": "SkyReels + 豆包",
        "id_slug": "video-generation-skyreels-doubao",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "SkyReels",
            "豆包"
        ],
        "steps": [
            "豆包写连续剧情，SkyReels 生成连续镜头"
        ],
        "outputs": [
            "短剧/剧情号"
        ],
        "summary": "国内 AI 工具组合：视频生成：SkyReels + 豆包。适合短剧/剧情号，流程是：豆包写连续剧情，SkyReels 生成连续镜头。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写连续剧情，SkyReels 生成连续镜头。",
        "audience": "短剧/剧情号"
    },
    {
        "num": "077",
        "scenario": "视频生成",
        "title": "视频生成：可灵 + 通义万相",
        "combo": "可灵 + 通义万相",
        "id_slug": "video-generation-kling-qwen",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "可灵",
            "通义万相"
        ],
        "steps": [
            "万相先生成角色/场景图，可灵图生视频"
        ],
        "outputs": [
            "品牌视频"
        ],
        "summary": "国内 AI 工具组合：视频生成：可灵 + 通义万相。适合品牌视频，流程是：万相先生成角色/场景图，可灵图生视频。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "万相先生成角色/场景图，可灵图生视频。",
        "audience": "品牌视频"
    },
    {
        "num": "078",
        "scenario": "视频生成",
        "title": "视频生成：海螺 AI + 通义听悟",
        "combo": "海螺 AI + 通义听悟",
        "id_slug": "video-generation-hailuo-ai-qwen",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "海螺 AI",
            "通义听悟"
        ],
        "steps": [
            "海螺生成视频",
            "听悟给成片转写、摘要和字幕稿"
        ],
        "outputs": [
            "视频复用"
        ],
        "summary": "国内 AI 工具组合：视频生成：海螺 AI + 通义听悟。适合视频复用，流程是：海螺生成视频；听悟给成片转写、摘要和字幕稿。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "海螺生成视频；听悟给成片转写、摘要和字幕稿。",
        "audience": "视频复用"
    },
    {
        "num": "079",
        "scenario": "视频生成",
        "title": "视频生成：即梦 + 剪映 + 豆包语音",
        "combo": "即梦 + 剪映 + 豆包语音",
        "id_slug": "video-generation-jimeng-jianying-doubao",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "即梦",
            "剪映",
            "豆包语音"
        ],
        "steps": [
            "即梦生成画面，豆包语音配音，剪映合成和调节节奏"
        ],
        "outputs": [
            "完整短视频"
        ],
        "summary": "国内 AI 工具组合：视频生成：即梦 + 剪映 + 豆包语音。适合完整短视频，流程是：即梦生成画面，豆包语音配音，剪映合成和调节节奏。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 83,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "即梦生成画面，豆包语音配音，剪映合成和调节节奏。",
        "audience": "完整短视频"
    },
    {
        "num": "080",
        "scenario": "视频生成",
        "title": "视频生成：Seedance API + 扣子",
        "combo": "Seedance API + 扣子",
        "id_slug": "video-generation-seedance-api-coze-cn",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tools": [
            "Seedance API",
            "扣子"
        ],
        "steps": [
            "扣子工作流调用 Seedance API 批量生成视频素材"
        ],
        "outputs": [
            "企业内容工厂"
        ],
        "summary": "国内 AI 工具组合：视频生成：Seedance API + 扣子。适合企业内容工厂，流程是：扣子工作流调用 Seedance API 批量生成视频素材。",
        "tags": [
            "视频生成",
            "video"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "扣子工作流调用 Seedance API 批量生成视频素材。",
        "audience": "企业内容工厂"
    },
    {
        "num": "081",
        "scenario": "图像设计",
        "title": "图像设计：通义万相 + 通义",
        "combo": "通义万相 + 通义",
        "id_slug": "image-design-qwen-qwen",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "通义万相",
            "通义"
        ],
        "steps": [
            "通义生成 prompt 和卖点，万相生成海报/商品图"
        ],
        "outputs": [
            "电商/营销"
        ],
        "summary": "国内 AI 工具组合：图像设计：通义万相 + 通义。适合电商/营销，流程是：通义生成 prompt 和卖点，万相生成海报/商品图。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "通义生成 prompt 和卖点，万相生成海报/商品图。",
        "audience": "电商/营销"
    },
    {
        "num": "082",
        "scenario": "图像设计",
        "title": "图像设计：即梦 + 豆包",
        "combo": "即梦 + 豆包",
        "id_slug": "image-design-jimeng-doubao",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "即梦",
            "豆包"
        ],
        "steps": [
            "豆包写视觉 brief，即梦出图和视觉风格探索"
        ],
        "outputs": [
            "社媒视觉"
        ],
        "summary": "国内 AI 工具组合：图像设计：即梦 + 豆包。适合社媒视觉，流程是：豆包写视觉 brief，即梦出图和视觉风格探索。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写视觉 brief，即梦出图和视觉风格探索。",
        "audience": "社媒视觉"
    },
    {
        "num": "083",
        "scenario": "图像设计",
        "title": "图像设计：文小言 + 百度 AI 修图",
        "combo": "文小言 + 百度 AI 修图",
        "id_slug": "image-design-wenxiaoyan-ai",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "文小言",
            "百度 AI 修图"
        ],
        "steps": [
            "文小言策划文案，百度系工具做对话式修图"
        ],
        "outputs": [
            "轻设计"
        ],
        "summary": "国内 AI 工具组合：图像设计：文小言 + 百度 AI 修图。适合轻设计，流程是：文小言策划文案，百度系工具做对话式修图。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "文小言策划文案，百度系工具做对话式修图。",
        "audience": "轻设计"
    },
    {
        "num": "084",
        "scenario": "图像设计",
        "title": "图像设计：美图设计室 + Kimi",
        "combo": "美图设计室 + Kimi",
        "id_slug": "image-design-kimi",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "美图设计室",
            "Kimi"
        ],
        "steps": [
            "Kimi 写营销文案，美图设计室批量生成海报"
        ],
        "outputs": [
            "新媒体"
        ],
        "summary": "国内 AI 工具组合：图像设计：美图设计室 + Kimi。适合新媒体，流程是：Kimi 写营销文案，美图设计室批量生成海报。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 写营销文案，美图设计室批量生成海报。",
        "audience": "新媒体"
    },
    {
        "num": "085",
        "scenario": "图像设计",
        "title": "图像设计：稿定 AI + 豆包",
        "combo": "稿定 AI + 豆包",
        "id_slug": "image-design-ai-doubao",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "稿定 AI",
            "豆包"
        ],
        "steps": [
            "豆包生成活动文案和尺寸要求，稿定套模板输出"
        ],
        "outputs": [
            "活动运营"
        ],
        "summary": "国内 AI 工具组合：图像设计：稿定 AI + 豆包。适合活动运营，流程是：豆包生成活动文案和尺寸要求，稿定套模板输出。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包生成活动文案和尺寸要求，稿定套模板输出。",
        "audience": "活动运营"
    },
    {
        "num": "086",
        "scenario": "图像设计",
        "title": "图像设计：通义万相 + WPS AI",
        "combo": "通义万相 + WPS AI",
        "id_slug": "image-design-qwen-wps-ai",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "通义万相",
            "WPS AI"
        ],
        "steps": [
            "万相生成插图，WPS AI 放入 PPT/文档"
        ],
        "outputs": [
            "报告视觉"
        ],
        "summary": "国内 AI 工具组合：图像设计：通义万相 + WPS AI。适合报告视觉，流程是：万相生成插图，WPS AI 放入 PPT/文档。",
        "tags": [
            "图像设计",
            "docs",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "万相生成插图，WPS AI 放入 PPT/文档。",
        "audience": "报告视觉"
    },
    {
        "num": "087",
        "scenario": "图像设计",
        "title": "图像设计：即梦 + 小红书",
        "combo": "即梦 + 小红书",
        "id_slug": "image-design-jimeng",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "即梦",
            "小红书"
        ],
        "steps": [
            "即梦生成封面/场景图，小红书发布测试标题"
        ],
        "outputs": [
            "种草账号"
        ],
        "summary": "国内 AI 工具组合：图像设计：即梦 + 小红书。适合种草账号，流程是：即梦生成封面/场景图，小红书发布测试标题。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 82,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "即梦生成封面/场景图，小红书发布测试标题。",
        "audience": "种草账号"
    },
    {
        "num": "088",
        "scenario": "图像设计",
        "title": "图像设计：可画/创客贴 + DeepSeek",
        "combo": "可画/创客贴 + DeepSeek",
        "id_slug": "image-design-deepseek",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "可画",
            "创客贴",
            "DeepSeek"
        ],
        "steps": [
            "DeepSeek 写信息架构，可画/创客贴设计成图文海报"
        ],
        "outputs": [
            "非设计师"
        ],
        "summary": "国内 AI 工具组合：图像设计：可画/创客贴 + DeepSeek。适合非设计师，流程是：DeepSeek 写信息架构，可画/创客贴设计成图文海报。",
        "tags": [
            "图像设计",
            "image"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 写信息架构，可画/创客贴设计成图文海报。",
        "audience": "非设计师"
    },
    {
        "num": "089",
        "scenario": "图像设计",
        "title": "图像设计：豆包图片 + 剪映",
        "combo": "豆包图片 + 剪映",
        "id_slug": "image-design-doubao-jianying",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "豆包图片",
            "剪映"
        ],
        "steps": [
            "豆包生成图片素材，剪映做图文视频"
        ],
        "outputs": [
            "短视频图文"
        ],
        "summary": "国内 AI 工具组合：图像设计：豆包图片 + 剪映。适合短视频图文，流程是：豆包生成图片素材，剪映做图文视频。",
        "tags": [
            "图像设计",
            "video",
            "image"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包生成图片素材，剪映做图文视频。",
        "audience": "短视频图文"
    },
    {
        "num": "090",
        "scenario": "图像设计",
        "title": "图像设计：通义万相 + 1688/淘宝素材",
        "combo": "通义万相 + 1688/淘宝素材",
        "id_slug": "image-design-qwen-1688",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tools": [
            "通义万相",
            "1688",
            "淘宝素材"
        ],
        "steps": [
            "万相生成场景图，结合电商素材做主图和详情页"
        ],
        "outputs": [
            "电商运营"
        ],
        "summary": "国内 AI 工具组合：图像设计：通义万相 + 1688/淘宝素材。适合电商运营，流程是：万相生成场景图，结合电商素材做主图和详情页。",
        "tags": [
            "图像设计",
            "image",
            "ecommerce"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "万相生成场景图，结合电商素材做主图和详情页。",
        "audience": "电商运营"
    },
    {
        "num": "091",
        "scenario": "AI 编程",
        "title": "AI 编程：Trae + DeepSeek",
        "combo": "Trae + DeepSeek",
        "id_slug": "ai-coding-trae-deepseek",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Trae",
            "DeepSeek"
        ],
        "steps": [
            "Trae 管工程上下文，DeepSeek 做推理、代码和错误解释"
        ],
        "outputs": [
            "个人开发者"
        ],
        "summary": "国内 AI 工具组合：AI 编程：Trae + DeepSeek。适合个人开发者，流程是：Trae 管工程上下文，DeepSeek 做推理、代码和错误解释。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Trae 管工程上下文，DeepSeek 做推理、代码和错误解释。",
        "audience": "个人开发者"
    },
    {
        "num": "092",
        "scenario": "AI 编程",
        "title": "AI 编程：Trae + 豆包模型",
        "combo": "Trae + 豆包模型",
        "id_slug": "ai-coding-trae-doubao",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Trae",
            "豆包模型"
        ],
        "steps": [
            "国内版 Trae 用豆包模型做 IDE 对话、补全和多文件修改"
        ],
        "outputs": [
            "中文开发"
        ],
        "summary": "国内 AI 工具组合：AI 编程：Trae + 豆包模型。适合中文开发，流程是：国内版 Trae 用豆包模型做 IDE 对话、补全和多文件修改。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "国内版 Trae 用豆包模型做 IDE 对话、补全和多文件修改。",
        "audience": "中文开发"
    },
    {
        "num": "093",
        "scenario": "AI 编程",
        "title": "AI 编程：通义灵码 + 阿里云",
        "combo": "通义灵码 + 阿里云",
        "id_slug": "ai-coding-qwen",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "通义灵码",
            "阿里云"
        ],
        "steps": [
            "灵码写代码/单测/审查，阿里云部署和云服务联动"
        ],
        "outputs": [
            "云原生/Java/Go"
        ],
        "summary": "国内 AI 工具组合：AI 编程：通义灵码 + 阿里云。适合云原生/Java/Go，流程是：灵码写代码/单测/审查，阿里云部署和云服务联动。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "灵码写代码/单测/审查，阿里云部署和云服务联动。",
        "audience": "云原生/Java/Go"
    },
    {
        "num": "094",
        "scenario": "AI 编程",
        "title": "AI 编程：CodeBuddy + 微信开发者工具",
        "combo": "CodeBuddy + 微信开发者工具",
        "id_slug": "ai-coding-codebuddy",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "CodeBuddy",
            "微信开发者工具"
        ],
        "steps": [
            "CodeBuddy 插件接微信开发者工具，做小程序补全和审查"
        ],
        "outputs": [
            "小程序开发"
        ],
        "summary": "国内 AI 工具组合：AI 编程：CodeBuddy + 微信开发者工具。适合小程序开发，流程是：CodeBuddy 插件接微信开发者工具，做小程序补全和审查。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "CodeBuddy 插件接微信开发者工具，做小程序补全和审查。",
        "audience": "小程序开发"
    },
    {
        "num": "095",
        "scenario": "AI 编程",
        "title": "AI 编程：CodeBuddy IDE + CLI",
        "combo": "CodeBuddy IDE + CLI",
        "id_slug": "ai-coding-codebuddy-ide-cli",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "CodeBuddy IDE",
            "CLI"
        ],
        "steps": [
            "IDE 做多文件开发，CLI 做终端任务和自动化"
        ],
        "outputs": [
            "全栈开发"
        ],
        "summary": "国内 AI 工具组合：AI 编程：CodeBuddy IDE + CLI。适合全栈开发，流程是：IDE 做多文件开发，CLI 做终端任务和自动化。",
        "tags": [
            "ai 编程",
            "coding",
            "automation"
        ],
        "importance": 81,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "IDE 做多文件开发，CLI 做终端任务和自动化。",
        "audience": "全栈开发"
    },
    {
        "num": "096",
        "scenario": "AI 编程",
        "title": "AI 编程：WorkBuddy + 飞书/钉钉",
        "combo": "WorkBuddy + 飞书/钉钉",
        "id_slug": "ai-coding-workbuddy-feishu-dingtalk",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "WorkBuddy",
            "飞书",
            "钉钉"
        ],
        "steps": [
            "用自然语言让 WorkBuddy 处理数据、文案和自动化办公"
        ],
        "outputs": [
            "非专业开发者"
        ],
        "summary": "国内 AI 工具组合：AI 编程：WorkBuddy + 飞书/钉钉。适合非专业开发者，流程是：用自然语言让 WorkBuddy 处理数据、文案和自动化办公。",
        "tags": [
            "ai 编程",
            "coding",
            "data",
            "automation"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用自然语言让 WorkBuddy 处理数据、文案和自动化办公。",
        "audience": "非专业开发者"
    },
    {
        "num": "097",
        "scenario": "AI 编程",
        "title": "AI 编程：文心快码 + 百度智能云",
        "combo": "文心快码 + 百度智能云",
        "id_slug": "ai-coding",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "文心快码",
            "百度智能云"
        ],
        "steps": [
            "快码理解项目并生成/修复代码，百度云承接部署"
        ],
        "outputs": [
            "政企/百度云"
        ],
        "summary": "国内 AI 工具组合：AI 编程：文心快码 + 百度智能云。适合政企/百度云，流程是：快码理解项目并生成/修复代码，百度云承接部署。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "快码理解项目并生成/修复代码，百度云承接部署。",
        "audience": "政企/百度云"
    },
    {
        "num": "098",
        "scenario": "AI 编程",
        "title": "AI 编程：MarsCode + 豆包",
        "combo": "MarsCode + 豆包",
        "id_slug": "ai-coding-marscode-doubao",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "MarsCode",
            "豆包"
        ],
        "steps": [
            "MarsCode 做 IDE 开发和 bug fix，豆包补充文档和解释"
        ],
        "outputs": [
            "前端/学生"
        ],
        "summary": "国内 AI 工具组合：AI 编程：MarsCode + 豆包。适合前端/学生，流程是：MarsCode 做 IDE 开发和 bug fix，豆包补充文档和解释。",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "MarsCode 做 IDE 开发和 bug fix，豆包补充文档和解释。",
        "audience": "前端/学生"
    },
    {
        "num": "099",
        "scenario": "AI 编程",
        "title": "AI 编程：CodeGeeX + GLM",
        "combo": "CodeGeeX + GLM",
        "id_slug": "ai-coding-codegeex-glm",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "CodeGeeX",
            "GLM"
        ],
        "steps": [
            "CodeGeeX 多 IDE 补全，GLM 做复杂问答和文档"
        ],
        "outputs": [
            "多语言开发"
        ],
        "summary": "国内 AI 工具组合：AI 编程：CodeGeeX + GLM。适合多语言开发，流程是：CodeGeeX 多 IDE 补全，GLM 做复杂问答和文档。",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "CodeGeeX 多 IDE 补全，GLM 做复杂问答和文档。",
        "audience": "多语言开发"
    },
    {
        "num": "100",
        "scenario": "AI 编程",
        "title": "AI 编程：iFlyCode + 星火",
        "combo": "iFlyCode + 星火",
        "id_slug": "ai-coding-iflycode",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "iFlyCode",
            "星火"
        ],
        "steps": [
            "iFlyCode 处理代码，星火做中文解释、学习和问答"
        ],
        "outputs": [
            "初学者"
        ],
        "summary": "国内 AI 工具组合：AI 编程：iFlyCode + 星火。适合初学者，流程是：iFlyCode 处理代码，星火做中文解释、学习和问答。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "iFlyCode 处理代码，星火做中文解释、学习和问答。",
        "audience": "初学者"
    },
    {
        "num": "101",
        "scenario": "AI 编程",
        "title": "AI 编程：DeepSeek API + Dify",
        "combo": "DeepSeek API + Dify",
        "id_slug": "ai-coding-deepseek-api-dify",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "DeepSeek API",
            "Dify"
        ],
        "steps": [
            "Dify 编排应用，DeepSeek API 负责低成本推理和代码分析"
        ],
        "outputs": [
            "内部工具"
        ],
        "summary": "国内 AI 工具组合：AI 编程：DeepSeek API + Dify。适合内部工具，流程是：Dify 编排应用，DeepSeek API 负责低成本推理和代码分析。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Dify 编排应用，DeepSeek API 负责低成本推理和代码分析。",
        "audience": "内部工具"
    },
    {
        "num": "102",
        "scenario": "AI 编程",
        "title": "AI 编程：FastGPT + DeepSeek",
        "combo": "FastGPT + DeepSeek",
        "id_slug": "ai-coding-fastgpt-deepseek",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "FastGPT",
            "DeepSeek"
        ],
        "steps": [
            "FastGPT 建企业知识库问答，DeepSeek 做模型底座"
        ],
        "outputs": [
            "私有知识库"
        ],
        "summary": "国内 AI 工具组合：AI 编程：FastGPT + DeepSeek。适合私有知识库，流程是：FastGPT 建企业知识库问答，DeepSeek 做模型底座。",
        "tags": [
            "ai 编程",
            "rag",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "FastGPT 建企业知识库问答，DeepSeek 做模型底座。",
        "audience": "私有知识库"
    },
    {
        "num": "103",
        "scenario": "AI 编程",
        "title": "AI 编程：RAGFlow + Qwen/DeepSeek",
        "combo": "RAGFlow + Qwen/DeepSeek",
        "id_slug": "ai-coding-rag-flow-qwen-deepseek",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "RAGFlow",
            "Qwen",
            "DeepSeek"
        ],
        "steps": [
            "RAGFlow 做文档解析和检索增强，Qwen/DeepSeek 生成回答"
        ],
        "outputs": [
            "文档问答"
        ],
        "summary": "国内 AI 工具组合：AI 编程：RAGFlow + Qwen/DeepSeek。适合文档问答，流程是：RAGFlow 做文档解析和检索增强，Qwen/DeepSeek 生成回答。",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "importance": 80,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "RAGFlow 做文档解析和检索增强，Qwen/DeepSeek 生成回答。",
        "audience": "文档问答"
    },
    {
        "num": "104",
        "scenario": "AI 编程",
        "title": "AI 编程：MaxKB + 通义/DeepSeek",
        "combo": "MaxKB + 通义/DeepSeek",
        "id_slug": "ai-coding-maxkb-qwen-deepseek",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "MaxKB",
            "通义",
            "DeepSeek"
        ],
        "steps": [
            "MaxKB 快速搭知识库应用，通义/DeepSeek 做问答"
        ],
        "outputs": [
            "中小企业"
        ],
        "summary": "国内 AI 工具组合：AI 编程：MaxKB + 通义/DeepSeek。适合中小企业，流程是：MaxKB 快速搭知识库应用，通义/DeepSeek 做问答。",
        "tags": [
            "ai 编程",
            "rag",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "MaxKB 快速搭知识库应用，通义/DeepSeek 做问答。",
        "audience": "中小企业"
    },
    {
        "num": "105",
        "scenario": "AI 编程",
        "title": "AI 编程：OpenClaw + 国内云",
        "combo": "OpenClaw + 国内云",
        "id_slug": "ai-coding-openclaw",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "OpenClaw"
        ],
        "steps": [
            "云端部署 OpenClaw，连接日程、消息、文件和代码任务"
        ],
        "outputs": [
            "agent 实验"
        ],
        "summary": "国内 AI 工具组合：AI 编程：OpenClaw + 国内云。适合agent 实验，流程是：云端部署 OpenClaw，连接日程、消息、文件和代码任务。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "云端部署 OpenClaw，连接日程、消息、文件和代码任务。",
        "audience": "agent 实验"
    },
    {
        "num": "106",
        "scenario": "AI 编程",
        "title": "AI 编程：OpenClaw + 飞书",
        "combo": "OpenClaw + 飞书",
        "id_slug": "ai-coding-openclaw-feishu",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "OpenClaw",
            "飞书"
        ],
        "steps": [
            "OpenClaw 接飞书消息和文档，执行整理、提醒、写作和脚本"
        ],
        "outputs": [
            "企业个人助手"
        ],
        "summary": "国内 AI 工具组合：AI 编程：OpenClaw + 飞书。适合企业个人助手，流程是：OpenClaw 接飞书消息和文档，执行整理、提醒、写作和脚本。",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "OpenClaw 接飞书消息和文档，执行整理、提醒、写作和脚本。",
        "audience": "企业个人助手"
    },
    {
        "num": "107",
        "scenario": "AI 编程",
        "title": "AI 编程：OpenClaw + CodeBuddy",
        "combo": "OpenClaw + CodeBuddy",
        "id_slug": "ai-coding-openclaw-codebuddy",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "OpenClaw",
            "CodeBuddy"
        ],
        "steps": [
            "OpenClaw 做任务调度，CodeBuddy 做代码实现和审查"
        ],
        "outputs": [
            "研发自动化"
        ],
        "summary": "国内 AI 工具组合：AI 编程：OpenClaw + CodeBuddy。适合研发自动化，流程是：OpenClaw 做任务调度，CodeBuddy 做代码实现和审查。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "OpenClaw 做任务调度，CodeBuddy 做代码实现和审查。",
        "audience": "研发自动化"
    },
    {
        "num": "108",
        "scenario": "AI 编程",
        "title": "AI 编程：Confucius Code Agent + Git",
        "combo": "Confucius Code Agent + Git",
        "id_slug": "ai-coding-confucius-code-agent-git",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Confucius Code Agent",
            "Git"
        ],
        "steps": [
            "开源软件工程 agent 处理 issue、代码修改和提交"
        ],
        "outputs": [
            "研究/开源"
        ],
        "summary": "国内 AI 工具组合：AI 编程：Confucius Code Agent + Git。适合研究/开源，流程是：开源软件工程 agent 处理 issue、代码修改和提交。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "开源软件工程 agent 处理 issue、代码修改和提交。",
        "audience": "研究/开源"
    },
    {
        "num": "109",
        "scenario": "AI 编程",
        "title": "AI 编程：Kimi K2.6 + Trae",
        "combo": "Kimi K2.6 + Trae",
        "id_slug": "ai-coding-kimi-k2-6-trae",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "Kimi K2.6",
            "Trae"
        ],
        "steps": [
            "Kimi 长上下文理解代码库，Trae 负责 IDE 编辑"
        ],
        "outputs": [
            "大项目维护"
        ],
        "summary": "国内 AI 工具组合：AI 编程：Kimi K2.6 + Trae。适合大项目维护，流程是：Kimi 长上下文理解代码库，Trae 负责 IDE 编辑。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 长上下文理解代码库，Trae 负责 IDE 编辑。",
        "audience": "大项目维护"
    },
    {
        "num": "110",
        "scenario": "AI 编程",
        "title": "AI 编程：DeepSeek V4 + 通义灵码",
        "combo": "DeepSeek V4 + 通义灵码",
        "id_slug": "ai-coding-deepseek-v4-qwen",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tools": [
            "DeepSeek V4",
            "通义灵码"
        ],
        "steps": [
            "DeepSeek 做低成本复杂推理，灵码在工程内落地修改"
        ],
        "outputs": [
            "开发团队"
        ],
        "summary": "国内 AI 工具组合：AI 编程：DeepSeek V4 + 通义灵码。适合开发团队，流程是：DeepSeek 做低成本复杂推理，灵码在工程内落地修改。",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 做低成本复杂推理，灵码在工程内落地修改。",
        "audience": "开发团队"
    },
    {
        "num": "111",
        "scenario": "电商",
        "title": "电商：通义万相 + 淘宝/天猫素材",
        "combo": "通义万相 + 淘宝/天猫素材",
        "id_slug": "ecommerce-qwen",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "通义万相"
        ],
        "steps": [
            "生成商品场景图、主图和详情页视觉"
        ],
        "outputs": [
            "电商设计"
        ],
        "summary": "国内 AI 工具组合：电商：通义万相 + 淘宝/天猫素材。适合电商设计，流程是：生成商品场景图、主图和详情页视觉。",
        "tags": [
            "电商",
            "ecommerce"
        ],
        "importance": 79,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成商品场景图、主图和详情页视觉。",
        "audience": "电商设计"
    },
    {
        "num": "112",
        "scenario": "电商",
        "title": "电商：豆包 + 巨量引擎",
        "combo": "豆包 + 巨量引擎",
        "id_slug": "ecommerce-doubao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "豆包",
            "巨量引擎"
        ],
        "steps": [
            "豆包生成广告卖点、脚本和投放文案，巨量引擎测试素材"
        ],
        "outputs": [
            "抖音投放"
        ],
        "summary": "国内 AI 工具组合：电商：豆包 + 巨量引擎。适合抖音投放，流程是：豆包生成广告卖点、脚本和投放文案，巨量引擎测试素材。",
        "tags": [
            "电商",
            "ecommerce"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包生成广告卖点、脚本和投放文案，巨量引擎测试素材。",
        "audience": "抖音投放"
    },
    {
        "num": "113",
        "scenario": "电商",
        "title": "电商：飞书多维表格 + AI 图表",
        "combo": "飞书多维表格 + AI 图表",
        "id_slug": "ecommerce-feishu-base-ai",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书多维表格",
            "AI 图表"
        ],
        "steps": [
            "沉淀商品/投放数据，自动生成战报和洞察"
        ],
        "outputs": [
            "电商运营"
        ],
        "summary": "国内 AI 工具组合：电商：飞书多维表格 + AI 图表。适合电商运营，流程是：沉淀商品/投放数据，自动生成战报和洞察。",
        "tags": [
            "电商",
            "spreadsheet",
            "ecommerce",
            "data",
            "automation"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "沉淀商品/投放数据，自动生成战报和洞察。",
        "audience": "电商运营"
    },
    {
        "num": "114",
        "scenario": "电商",
        "title": "电商：钉钉多维表格 + 通义",
        "combo": "钉钉多维表格 + 通义",
        "id_slug": "ecommerce-dingtalk-base-qwen",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "钉钉多维表格",
            "通义"
        ],
        "steps": [
            "同步订单/销售数据，自动生成门店日报"
        ],
        "outputs": [
            "零售管理"
        ],
        "summary": "国内 AI 工具组合：电商：钉钉多维表格 + 通义。适合零售管理，流程是：同步订单/销售数据，自动生成门店日报。",
        "tags": [
            "电商",
            "spreadsheet",
            "sales",
            "ecommerce",
            "data",
            "automation"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "同步订单/销售数据，自动生成门店日报。",
        "audience": "零售管理"
    },
    {
        "num": "115",
        "scenario": "电商",
        "title": "电商：Kimi + 1688/小红书资料",
        "combo": "Kimi + 1688/小红书资料",
        "id_slug": "ecommerce-kimi-1688",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi",
            "1688",
            "小红书资料"
        ],
        "steps": [
            "整理竞品卖点和用户评价，生成商品文案"
        ],
        "outputs": [
            "选品/文案"
        ],
        "summary": "国内 AI 工具组合：电商：Kimi + 1688/小红书资料。适合选品/文案，流程是：整理竞品卖点和用户评价，生成商品文案。",
        "tags": [
            "电商",
            "ecommerce"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "整理竞品卖点和用户评价，生成商品文案。",
        "audience": "选品/文案"
    },
    {
        "num": "116",
        "scenario": "电商",
        "title": "电商：即梦 + 剪映 + 豆包",
        "combo": "即梦 + 剪映 + 豆包",
        "id_slug": "ecommerce-jimeng-jianying-doubao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "即梦",
            "剪映",
            "豆包"
        ],
        "steps": [
            "生成产品短视频、字幕、口播脚本并发布"
        ],
        "outputs": [
            "带货短视频"
        ],
        "summary": "国内 AI 工具组合：电商：即梦 + 剪映 + 豆包。适合带货短视频，流程是：生成产品短视频、字幕、口播脚本并发布。",
        "tags": [
            "电商",
            "video",
            "ecommerce"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成产品短视频、字幕、口播脚本并发布。",
        "audience": "带货短视频"
    },
    {
        "num": "117",
        "scenario": "电商",
        "title": "电商：ima + 微信私域",
        "combo": "ima + 微信私域",
        "id_slug": "ecommerce-ima",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ima"
        ],
        "steps": [
            "沉淀客户问答、商品资料和 SOP，生成客服回复"
        ],
        "outputs": [
            "私域客服"
        ],
        "summary": "国内 AI 工具组合：电商：ima + 微信私域。适合私域客服，流程是：沉淀客户问答、商品资料和 SOP，生成客服回复。",
        "tags": [
            "电商",
            "support",
            "ecommerce"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "沉淀客户问答、商品资料和 SOP，生成客服回复。",
        "audience": "私域客服"
    },
    {
        "num": "118",
        "scenario": "电商",
        "title": "电商：扣子 + 微信客服",
        "combo": "扣子 + 微信客服",
        "id_slug": "ecommerce-coze-cn",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "扣子"
        ],
        "steps": [
            "构建商品咨询、售后 FAQ 和优惠引导 bot"
        ],
        "outputs": [
            "小店客服"
        ],
        "summary": "国内 AI 工具组合：电商：扣子 + 微信客服。适合小店客服，流程是：构建商品咨询、售后 FAQ 和优惠引导 bot。",
        "tags": [
            "电商",
            "support",
            "ecommerce"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "构建商品咨询、售后 FAQ 和优惠引导 bot。",
        "audience": "小店客服"
    },
    {
        "num": "119",
        "scenario": "电商",
        "title": "电商：DeepSeek + Excel/WPS 表格",
        "combo": "DeepSeek + Excel/WPS 表格",
        "id_slug": "ecommerce-deepseek-excel-wps",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek"
        ],
        "steps": [
            "批量清洗 SKU、分类评价、生成定价建议"
        ],
        "outputs": [
            "运营分析"
        ],
        "summary": "国内 AI 工具组合：电商：DeepSeek + Excel/WPS 表格。适合运营分析，流程是：批量清洗 SKU、分类评价、生成定价建议。",
        "tags": [
            "电商",
            "spreadsheet",
            "ecommerce"
        ],
        "importance": 78,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "批量清洗 SKU、分类评价、生成定价建议。",
        "audience": "运营分析"
    },
    {
        "num": "120",
        "scenario": "电商",
        "title": "电商：通义听悟 + 直播复盘",
        "combo": "通义听悟 + 直播复盘",
        "id_slug": "ecommerce-qwen-2",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "通义听悟"
        ],
        "steps": [
            "转写直播内容，提炼爆点、问题和下次脚本"
        ],
        "outputs": [
            "直播团队"
        ],
        "summary": "国内 AI 工具组合：电商：通义听悟 + 直播复盘。适合直播团队，流程是：转写直播内容，提炼爆点、问题和下次脚本。",
        "tags": [
            "电商",
            "ecommerce",
            "content"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "转写直播内容，提炼爆点、问题和下次脚本。",
        "audience": "直播团队"
    },
    {
        "num": "121",
        "scenario": "教育",
        "title": "教育：讯飞星火 + 通义听悟",
        "combo": "讯飞星火 + 通义听悟",
        "id_slug": "education-spark-qwen",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "讯飞星火",
            "通义听悟"
        ],
        "steps": [
            "课程音视频转写，星火生成知识点、练习和讲义"
        ],
        "outputs": [
            "教师/培训"
        ],
        "summary": "国内 AI 工具组合：教育：讯飞星火 + 通义听悟。适合教师/培训，流程是：课程音视频转写，星火生成知识点、练习和讲义。",
        "tags": [
            "教育",
            "video",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "课程音视频转写，星火生成知识点、练习和讲义。",
        "audience": "教师/培训"
    },
    {
        "num": "122",
        "scenario": "教育",
        "title": "教育：豆包爱学 + 豆包",
        "combo": "豆包爱学 + 豆包",
        "id_slug": "education-doubao-doubao",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "豆包爱学",
            "豆包"
        ],
        "steps": [
            "学生问答、作文修改、知识点讲解和学习计划"
        ],
        "outputs": [
            "学生家庭"
        ],
        "summary": "国内 AI 工具组合：教育：豆包爱学 + 豆包。适合学生家庭，流程是：学生问答、作文修改、知识点讲解和学习计划。",
        "tags": [
            "教育",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "学生问答、作文修改、知识点讲解和学习计划。",
        "audience": "学生家庭"
    },
    {
        "num": "123",
        "scenario": "教育",
        "title": "教育：Kimi + PDF 教材",
        "combo": "Kimi + PDF 教材",
        "id_slug": "education-kimi-pdf",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "Kimi"
        ],
        "steps": [
            "Kimi 阅读教材/论文，生成章节摘要和题目"
        ],
        "outputs": [
            "大学生"
        ],
        "summary": "国内 AI 工具组合：教育：Kimi + PDF 教材。适合大学生，流程是：Kimi 阅读教材/论文，生成章节摘要和题目。",
        "tags": [
            "教育",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 阅读教材/论文，生成章节摘要和题目。",
        "audience": "大学生"
    },
    {
        "num": "124",
        "scenario": "教育",
        "title": "教育：纳米 AI 搜索 + Kimi",
        "combo": "纳米 AI 搜索 + Kimi",
        "id_slug": "education-nami-ai-kimi",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "纳米 AI 搜索",
            "Kimi"
        ],
        "steps": [
            "纳米整理资料脑图，Kimi 写读书报告"
        ],
        "outputs": [
            "学习研究"
        ],
        "summary": "国内 AI 工具组合：教育：纳米 AI 搜索 + Kimi。适合学习研究，流程是：纳米整理资料脑图，Kimi 写读书报告。",
        "tags": [
            "教育",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "纳米整理资料脑图，Kimi 写读书报告。",
        "audience": "学习研究"
    },
    {
        "num": "125",
        "scenario": "教育",
        "title": "教育：WPS AI + 文小言",
        "combo": "WPS AI + 文小言",
        "id_slug": "education-wps-ai-wenxiaoyan",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "WPS AI",
            "文小言"
        ],
        "steps": [
            "文小言写论文框架，WPS AI 排版和生成答辩 PPT"
        ],
        "outputs": [
            "论文/答辩"
        ],
        "summary": "国内 AI 工具组合：教育：WPS AI + 文小言。适合论文/答辩，流程是：文小言写论文框架，WPS AI 排版和生成答辩 PPT。",
        "tags": [
            "教育",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "文小言写论文框架，WPS AI 排版和生成答辩 PPT。",
        "audience": "论文/答辩"
    },
    {
        "num": "126",
        "scenario": "教育",
        "title": "教育：飞书多维表格 + AI 问卷",
        "combo": "飞书多维表格 + AI 问卷",
        "id_slug": "education-feishu-base-ai",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "飞书多维表格",
            "AI 问卷"
        ],
        "steps": [
            "生成报名表、反馈表和数据分析"
        ],
        "outputs": [
            "培训机构"
        ],
        "summary": "国内 AI 工具组合：教育：飞书多维表格 + AI 问卷。适合培训机构，流程是：生成报名表、反馈表和数据分析。",
        "tags": [
            "教育",
            "spreadsheet",
            "data",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成报名表、反馈表和数据分析。",
        "audience": "培训机构"
    },
    {
        "num": "127",
        "scenario": "教育",
        "title": "教育：钉钉会议 + AI 助理",
        "combo": "钉钉会议 + AI 助理",
        "id_slug": "education-dingtalk-ai",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "钉钉会议"
        ],
        "steps": [
            "课堂/教研会议自动纪要和行动项"
        ],
        "outputs": [
            "学校/教培"
        ],
        "summary": "国内 AI 工具组合：教育：钉钉会议 + AI 助理。适合学校/教培，流程是：课堂/教研会议自动纪要和行动项。",
        "tags": [
            "教育",
            "meeting",
            "automation",
            "education"
        ],
        "importance": 77,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "课堂/教研会议自动纪要和行动项。",
        "audience": "学校/教培"
    },
    {
        "num": "128",
        "scenario": "教育",
        "title": "教育：可灵/即梦 + 豆包",
        "combo": "可灵/即梦 + 豆包",
        "id_slug": "education-kling-jimeng-doubao",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "可灵",
            "即梦",
            "豆包"
        ],
        "steps": [
            "把知识点做成短视频脚本和动画素材"
        ],
        "outputs": [
            "知识类短视频"
        ],
        "summary": "国内 AI 工具组合：教育：可灵/即梦 + 豆包。适合知识类短视频，流程是：把知识点做成短视频脚本和动画素材。",
        "tags": [
            "教育",
            "video",
            "education"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把知识点做成短视频脚本和动画素材。",
        "audience": "知识类短视频"
    },
    {
        "num": "129",
        "scenario": "教育",
        "title": "教育：讯飞听见 + 星火",
        "combo": "讯飞听见 + 星火",
        "id_slug": "education",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "讯飞听见",
            "星火"
        ],
        "steps": [
            "访谈/课堂录音转写，星火生成教案和总结"
        ],
        "outputs": [
            "老师/教研"
        ],
        "summary": "国内 AI 工具组合：教育：讯飞听见 + 星火。适合老师/教研，流程是：访谈/课堂录音转写，星火生成教案和总结。",
        "tags": [
            "教育",
            "education"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "访谈/课堂录音转写，星火生成教案和总结。",
        "audience": "老师/教研"
    },
    {
        "num": "130",
        "scenario": "教育",
        "title": "教育：DeepSeek + CodeGeeX",
        "combo": "DeepSeek + CodeGeeX",
        "id_slug": "education-deepseek-codegeex",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tools": [
            "DeepSeek",
            "CodeGeeX"
        ],
        "steps": [
            "DeepSeek 讲算法，CodeGeeX 补全代码练习"
        ],
        "outputs": [
            "编程学习"
        ],
        "summary": "国内 AI 工具组合：教育：DeepSeek + CodeGeeX。适合编程学习，流程是：DeepSeek 讲算法，CodeGeeX 补全代码练习。",
        "tags": [
            "教育",
            "coding",
            "education"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 讲算法，CodeGeeX 补全代码练习。",
        "audience": "编程学习"
    },
    {
        "num": "131",
        "scenario": "法律/合同",
        "title": "法律/合同：Kimi + 合同 PDF",
        "combo": "Kimi + 合同 PDF",
        "id_slug": "legal-contract-kimi-contract-pdf",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi",
            "合同 PDF"
        ],
        "steps": [
            "批量阅读合同，列出关键条款、风险和待确认项"
        ],
        "outputs": [
            "法务/商务"
        ],
        "summary": "国内 AI 工具组合：法律/合同：Kimi + 合同 PDF。适合法务/商务，流程是：批量阅读合同，列出关键条款、风险和待确认项。",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "批量阅读合同，列出关键条款、风险和待确认项。",
        "audience": "法务/商务"
    },
    {
        "num": "132",
        "scenario": "法律/合同",
        "title": "法律/合同：飞书妙搭 + 合同助手",
        "combo": "飞书妙搭 + 合同助手",
        "id_slug": "legal-contract-feishu-contract",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书妙搭",
            "合同助手"
        ],
        "steps": [
            "生成合同字段表单，自动填充、预览、导出 Word"
        ],
        "outputs": [
            "销售法务"
        ],
        "summary": "国内 AI 工具组合：法律/合同：飞书妙搭 + 合同助手。适合销售法务，流程是：生成合同字段表单，自动填充、预览、导出 Word。",
        "tags": [
            "法律-合同",
            "automation",
            "legal"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成合同字段表单，自动填充、预览、导出 Word。",
        "audience": "销售法务"
    },
    {
        "num": "133",
        "scenario": "法律/合同",
        "title": "法律/合同：扣子 + 法律检索技能",
        "combo": "扣子 + 法律检索技能",
        "id_slug": "legal-contract-coze-cn-legal",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "扣子",
            "法律检索技能"
        ],
        "steps": [
            "封装法规检索、案例摘要、风险问答"
        ],
        "outputs": [
            "法律咨询"
        ],
        "summary": "国内 AI 工具组合：法律/合同：扣子 + 法律检索技能。适合法律咨询，流程是：封装法规检索、案例摘要、风险问答。",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "封装法规检索、案例摘要、风险问答。",
        "audience": "法律咨询"
    },
    {
        "num": "134",
        "scenario": "法律/合同",
        "title": "法律/合同：文小言 + 百度文库",
        "combo": "文小言 + 百度文库",
        "id_slug": "legal-contract-wenxiaoyan",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "文小言",
            "百度文库"
        ],
        "steps": [
            "找公文/合同模板，生成正式文本"
        ],
        "outputs": [
            "行政法务"
        ],
        "summary": "国内 AI 工具组合：法律/合同：文小言 + 百度文库。适合行政法务，流程是：找公文/合同模板，生成正式文本。",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "找公文/合同模板，生成正式文本。",
        "audience": "行政法务"
    },
    {
        "num": "135",
        "scenario": "法律/合同",
        "title": "法律/合同：DeepSeek + WPS AI",
        "combo": "DeepSeek + WPS AI",
        "id_slug": "legal-contract-deepseek-wps-ai",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek",
            "WPS AI"
        ],
        "steps": [
            "DeepSeek 做条款对比，WPS AI 输出修改意见文档"
        ],
        "outputs": [
            "合同审查"
        ],
        "summary": "国内 AI 工具组合：法律/合同：DeepSeek + WPS AI。适合合同审查，流程是：DeepSeek 做条款对比，WPS AI 输出修改意见文档。",
        "tags": [
            "法律-合同",
            "docs",
            "legal"
        ],
        "importance": 76,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 做条款对比，WPS AI 输出修改意见文档。",
        "audience": "合同审查"
    },
    {
        "num": "136",
        "scenario": "法律/合同",
        "title": "法律/合同：ima + 企业制度库",
        "combo": "ima + 企业制度库",
        "id_slug": "legal-contract-ima",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ima",
            "企业制度库"
        ],
        "steps": [
            "制度、合同、SOP 入库，给员工做问答"
        ],
        "outputs": [
            "合规/HR"
        ],
        "summary": "国内 AI 工具组合：法律/合同：ima + 企业制度库。适合合规/HR，流程是：制度、合同、SOP 入库，给员工做问答。",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "制度、合同、SOP 入库，给员工做问答。",
        "audience": "合规/HR"
    },
    {
        "num": "137",
        "scenario": "财务/数据",
        "title": "财务/数据：DeepSeek + WPS 表格",
        "combo": "DeepSeek + WPS 表格",
        "id_slug": "finance-data-deepseek-wps",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek"
        ],
        "steps": [
            "批量分类、异常检测、公式解释和报表摘要"
        ],
        "outputs": [
            "财务运营"
        ],
        "summary": "国内 AI 工具组合：财务/数据：DeepSeek + WPS 表格。适合财务运营，流程是：批量分类、异常检测、公式解释和报表摘要。",
        "tags": [
            "财务-数据",
            "spreadsheet",
            "data"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "批量分类、异常检测、公式解释和报表摘要。",
        "audience": "财务运营"
    },
    {
        "num": "138",
        "scenario": "财务/数据",
        "title": "财务/数据：飞书多维表格 + AI 问数据",
        "combo": "飞书多维表格 + AI 问数据",
        "id_slug": "finance-data-feishu-base-ai-data",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书多维表格"
        ],
        "steps": [
            "自然语言查询经营数据并生成图表"
        ],
        "outputs": [
            "经营分析"
        ],
        "summary": "国内 AI 工具组合：财务/数据：飞书多维表格 + AI 问数据。适合经营分析，流程是：自然语言查询经营数据并生成图表。",
        "tags": [
            "财务-数据",
            "spreadsheet",
            "data"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "自然语言查询经营数据并生成图表。",
        "audience": "经营分析"
    },
    {
        "num": "139",
        "scenario": "财务/数据",
        "title": "财务/数据：钉钉多维表格 + 通义",
        "combo": "钉钉多维表格 + 通义",
        "id_slug": "finance-data-dingtalk-base-qwen",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "钉钉多维表格",
            "通义"
        ],
        "steps": [
            "销售、费用、回款数据自动分析和周报"
        ],
        "outputs": [
            "管理层"
        ],
        "summary": "国内 AI 工具组合：财务/数据：钉钉多维表格 + 通义。适合管理层，流程是：销售、费用、回款数据自动分析和周报。",
        "tags": [
            "财务-数据",
            "spreadsheet",
            "sales",
            "data",
            "automation"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "销售、费用、回款数据自动分析和周报。",
        "audience": "管理层"
    },
    {
        "num": "140",
        "scenario": "财务/数据",
        "title": "财务/数据：Kimi Sheets + CSV",
        "combo": "Kimi Sheets + CSV",
        "id_slug": "finance-data-kimi-sheets-csv",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi Sheets",
            "CSV"
        ],
        "steps": [
            "上传 CSV/Excel，做分析、可视化和结论"
        ],
        "outputs": [
            "数据分析"
        ],
        "summary": "国内 AI 工具组合：财务/数据：Kimi Sheets + CSV。适合数据分析，流程是：上传 CSV/Excel，做分析、可视化和结论。",
        "tags": [
            "财务-数据",
            "data"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "上传 CSV/Excel，做分析、可视化和结论。",
        "audience": "数据分析"
    },
    {
        "num": "141",
        "scenario": "财务/数据",
        "title": "财务/数据：天工表格 + WPS AI",
        "combo": "天工表格 + WPS AI",
        "id_slug": "finance-data-skywork-wps-ai",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "天工表格",
            "WPS AI"
        ],
        "steps": [
            "天工生成表格分析，WPS 美化交付"
        ],
        "outputs": [
            "财务汇报"
        ],
        "summary": "国内 AI 工具组合：财务/数据：天工表格 + WPS AI。适合财务汇报，流程是：天工生成表格分析，WPS 美化交付。",
        "tags": [
            "财务-数据",
            "spreadsheet",
            "data"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "天工生成表格分析，WPS 美化交付。",
        "audience": "财务汇报"
    },
    {
        "num": "142",
        "scenario": "财务/数据",
        "title": "财务/数据：扣子 + Python 节点 + LLM",
        "combo": "扣子 + Python 节点 + LLM",
        "id_slug": "finance-data-coze-cn-python-llm",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "扣子",
            "Python 节点",
            "LLM"
        ],
        "steps": [
            "PDF 提取数据，Python 计算指标，LLM 生成总结"
        ],
        "outputs": [
            "自动报表"
        ],
        "summary": "国内 AI 工具组合：财务/数据：扣子 + Python 节点 + LLM。适合自动报表，流程是：PDF 提取数据，Python 计算指标，LLM 生成总结。",
        "tags": [
            "财务-数据",
            "data"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "PDF 提取数据，Python 计算指标，LLM 生成总结。",
        "audience": "自动报表"
    },
    {
        "num": "143",
        "scenario": "财务/数据",
        "title": "财务/数据：ima + DeepSeek",
        "combo": "ima + DeepSeek",
        "id_slug": "finance-data-ima-deepseek",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ima",
            "DeepSeek"
        ],
        "steps": [
            "财务制度/历史报表入库，DeepSeek 做问答和摘要"
        ],
        "outputs": [
            "财务知识库"
        ],
        "summary": "国内 AI 工具组合：财务/数据：ima + DeepSeek。适合财务知识库，流程是：财务制度/历史报表入库，DeepSeek 做问答和摘要。",
        "tags": [
            "财务-数据",
            "data"
        ],
        "importance": 75,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "财务制度/历史报表入库，DeepSeek 做问答和摘要。",
        "audience": "财务知识库"
    },
    {
        "num": "144",
        "scenario": "财务/数据",
        "title": "财务/数据：通义 + 阿里云 BI",
        "combo": "通义 + 阿里云 BI",
        "id_slug": "finance-data-qwen-bi",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "通义",
            "阿里云 BI"
        ],
        "steps": [
            "通义解释指标，阿里云 BI 做数据看板"
        ],
        "outputs": [
            "云上 BI"
        ],
        "summary": "国内 AI 工具组合：财务/数据：通义 + 阿里云 BI。适合云上 BI，流程是：通义解释指标，阿里云 BI 做数据看板。",
        "tags": [
            "财务-数据",
            "data"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "通义解释指标，阿里云 BI 做数据看板。",
        "audience": "云上 BI"
    },
    {
        "num": "145",
        "scenario": "财务/数据",
        "title": "财务/数据：飞书 + Kimi",
        "combo": "飞书 + Kimi",
        "id_slug": "finance-data-feishu-kimi",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书",
            "Kimi"
        ],
        "steps": [
            "飞书沉淀业务数据，Kimi 写月度经营分析"
        ],
        "outputs": [
            "创业团队"
        ],
        "summary": "国内 AI 工具组合：财务/数据：飞书 + Kimi。适合创业团队，流程是：飞书沉淀业务数据，Kimi 写月度经营分析。",
        "tags": [
            "财务-数据",
            "data"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "飞书沉淀业务数据，Kimi 写月度经营分析。",
        "audience": "创业团队"
    },
    {
        "num": "146",
        "scenario": "财务/数据",
        "title": "财务/数据：DeepSeek API + n8n",
        "combo": "DeepSeek API + n8n",
        "id_slug": "finance-data-deepseek-api-n8n",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek API",
            "n8n"
        ],
        "steps": [
            "n8n 定时拉取数据，DeepSeek 分类总结，推送飞书/钉钉"
        ],
        "outputs": [
            "自动化报表"
        ],
        "summary": "国内 AI 工具组合：财务/数据：DeepSeek API + n8n。适合自动化报表，流程是：n8n 定时拉取数据，DeepSeek 分类总结，推送飞书/钉钉。",
        "tags": [
            "财务-数据",
            "data"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "n8n 定时拉取数据，DeepSeek 分类总结，推送飞书/钉钉。",
        "audience": "自动化报表"
    },
    {
        "num": "147",
        "scenario": "销售/CRM",
        "title": "销售/CRM：飞书 aily + 多维表格 CRM",
        "combo": "飞书 aily + 多维表格 CRM",
        "id_slug": "sales-crm-feishu-aily-base-crm",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书 aily",
            "多维表格 CRM"
        ],
        "steps": [
            "读取客户跟进、会议和任务，自动生成销售周报"
        ],
        "outputs": [
            "销售团队"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：飞书 aily + 多维表格 CRM。适合销售团队，流程是：读取客户跟进、会议和任务，自动生成销售周报。",
        "tags": [
            "销售-crm",
            "spreadsheet",
            "meeting",
            "sales",
            "automation"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "读取客户跟进、会议和任务，自动生成销售周报。",
        "audience": "销售团队"
    },
    {
        "num": "148",
        "scenario": "销售/CRM",
        "title": "销售/CRM：钉钉 AI 助理 + 销售表格",
        "combo": "钉钉 AI 助理 + 销售表格",
        "id_slug": "sales-crm-dingtalk-ai-sales",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "钉钉 AI 助理",
            "销售表格"
        ],
        "steps": [
            "定时生成销售周报并推送管理层"
        ],
        "outputs": [
            "钉钉销售"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：钉钉 AI 助理 + 销售表格。适合钉钉销售，流程是：定时生成销售周报并推送管理层。",
        "tags": [
            "销售-crm",
            "spreadsheet",
            "sales"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "定时生成销售周报并推送管理层。",
        "audience": "钉钉销售"
    },
    {
        "num": "149",
        "scenario": "销售/CRM",
        "title": "销售/CRM：豆包 + 企业微信",
        "combo": "豆包 + 企业微信",
        "id_slug": "sales-crm-doubao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "豆包",
            "企业微信"
        ],
        "steps": [
            "生成客户回复、邀约话术和售后 FAQ"
        ],
        "outputs": [
            "私域销售"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：豆包 + 企业微信。适合私域销售，流程是：生成客户回复、邀约话术和售后 FAQ。",
        "tags": [
            "销售-crm",
            "sales"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成客户回复、邀约话术和售后 FAQ。",
        "audience": "私域销售"
    },
    {
        "num": "150",
        "scenario": "销售/CRM",
        "title": "销售/CRM：腾讯元宝 + 微信资料",
        "combo": "腾讯元宝 + 微信资料",
        "id_slug": "sales-crm-yuanbao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "腾讯元宝",
            "微信资料"
        ],
        "steps": [
            "读取公开公众号/视频号线索，生成客户背景摘要"
        ],
        "outputs": [
            "BD"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：腾讯元宝 + 微信资料。适合BD，流程是：读取公开公众号/视频号线索，生成客户背景摘要。",
        "tags": [
            "销售-crm",
            "video",
            "sales"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "读取公开公众号/视频号线索，生成客户背景摘要。",
        "audience": "BD"
    },
    {
        "num": "151",
        "scenario": "销售/CRM",
        "title": "销售/CRM：Kimi + 客户访谈",
        "combo": "Kimi + 客户访谈",
        "id_slug": "sales-crm-kimi",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi",
            "客户访谈"
        ],
        "steps": [
            "分析访谈记录，提炼痛点、预算、决策链和方案"
        ],
        "outputs": [
            "售前"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：Kimi + 客户访谈。适合售前，流程是：分析访谈记录，提炼痛点、预算、决策链和方案。",
        "tags": [
            "销售-crm",
            "sales"
        ],
        "importance": 74,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "分析访谈记录，提炼痛点、预算、决策链和方案。",
        "audience": "售前"
    },
    {
        "num": "152",
        "scenario": "销售/CRM",
        "title": "销售/CRM：即梦 + 通义万相 + 豆包",
        "combo": "即梦 + 通义万相 + 豆包",
        "id_slug": "sales-crm-jimeng-qwen-doubao",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "即梦",
            "通义万相",
            "豆包"
        ],
        "steps": [
            "生成客户行业海报、提案封面和短视频素材"
        ],
        "outputs": [
            "营销销售"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：即梦 + 通义万相 + 豆包。适合营销销售，流程是：生成客户行业海报、提案封面和短视频素材。",
        "tags": [
            "销售-crm",
            "video",
            "sales"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "生成客户行业海报、提案封面和短视频素材。",
        "audience": "营销销售"
    },
    {
        "num": "153",
        "scenario": "销售/CRM",
        "title": "销售/CRM：扣子 + 微信客服",
        "combo": "扣子 + 微信客服",
        "id_slug": "sales-crm-coze-cn",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "扣子"
        ],
        "steps": [
            "构建售前问答、报价引导和线索收集 bot"
        ],
        "outputs": [
            "小微商家"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：扣子 + 微信客服。适合小微商家，流程是：构建售前问答、报价引导和线索收集 bot。",
        "tags": [
            "销售-crm",
            "support",
            "sales"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "构建售前问答、报价引导和线索收集 bot。",
        "audience": "小微商家"
    },
    {
        "num": "154",
        "scenario": "销售/CRM",
        "title": "销售/CRM：ima + 销售资料库",
        "combo": "ima + 销售资料库",
        "id_slug": "sales-crm-ima-sales",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ima",
            "销售资料库"
        ],
        "steps": [
            "沉淀案例、报价、FAQ，生成客户化回复"
        ],
        "outputs": [
            "客户成功"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：ima + 销售资料库。适合客户成功，流程是：沉淀案例、报价、FAQ，生成客户化回复。",
        "tags": [
            "销售-crm",
            "sales"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "沉淀案例、报价、FAQ，生成客户化回复。",
        "audience": "客户成功"
    },
    {
        "num": "155",
        "scenario": "销售/CRM",
        "title": "销售/CRM：DeepSeek + WPS 表格",
        "combo": "DeepSeek + WPS 表格",
        "id_slug": "sales-crm-deepseek-wps",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek"
        ],
        "steps": [
            "批量清洗线索、分类等级、生成跟进优先级"
        ],
        "outputs": [
            "销售运营"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：DeepSeek + WPS 表格。适合销售运营，流程是：批量清洗线索、分类等级、生成跟进优先级。",
        "tags": [
            "销售-crm",
            "spreadsheet",
            "sales"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "批量清洗线索、分类等级、生成跟进优先级。",
        "audience": "销售运营"
    },
    {
        "num": "156",
        "scenario": "销售/CRM",
        "title": "销售/CRM：飞书妙搭 + 报价工具",
        "combo": "飞书妙搭 + 报价工具",
        "id_slug": "sales-crm-feishu",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书妙搭",
            "报价工具"
        ],
        "steps": [
            "自然语言搭报价/合同生成工具，并接飞书审批"
        ],
        "outputs": [
            "商务团队"
        ],
        "summary": "国内 AI 工具组合：销售/CRM：飞书妙搭 + 报价工具。适合商务团队，流程是：自然语言搭报价/合同生成工具，并接飞书审批。",
        "tags": [
            "销售-crm",
            "sales",
            "legal"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "自然语言搭报价/合同生成工具，并接飞书审批。",
        "audience": "商务团队"
    },
    {
        "num": "157",
        "scenario": "产品/需求",
        "title": "产品/需求：Kimi + 飞书文档",
        "combo": "Kimi + 飞书文档",
        "id_slug": "product-requirements-kimi-feishu",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "Kimi",
            "飞书文档"
        ],
        "steps": [
            "Kimi 阅读用户反馈和竞品资料，输出 PRD，飞书协作评审"
        ],
        "outputs": [
            "产品经理"
        ],
        "summary": "国内 AI 工具组合：产品/需求：Kimi + 飞书文档。适合产品经理，流程是：Kimi 阅读用户反馈和竞品资料，输出 PRD，飞书协作评审。",
        "tags": [
            "产品-需求",
            "docs"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 阅读用户反馈和竞品资料，输出 PRD，飞书协作评审。",
        "audience": "产品经理"
    },
    {
        "num": "158",
        "scenario": "产品/需求",
        "title": "产品/需求：豆包 + 即梦",
        "combo": "豆包 + 即梦",
        "id_slug": "product-requirements-doubao-jimeng",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "豆包",
            "即梦"
        ],
        "steps": [
            "豆包写功能故事， 即梦生成产品概念图"
        ],
        "outputs": [
            "产品概念"
        ],
        "summary": "国内 AI 工具组合：产品/需求：豆包 + 即梦。适合产品概念，流程是：豆包写功能故事， 即梦生成产品概念图。",
        "tags": [
            "产品-需求"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "豆包写功能故事， 即梦生成产品概念图。",
        "audience": "产品概念"
    },
    {
        "num": "159",
        "scenario": "产品/需求",
        "title": "产品/需求：DeepSeek + Trae",
        "combo": "DeepSeek + Trae",
        "id_slug": "product-requirements-deepseek-trae",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "DeepSeek",
            "Trae"
        ],
        "steps": [
            "DeepSeek 拆技术方案，Trae 实现原型"
        ],
        "outputs": [
            "技术 PM"
        ],
        "summary": "国内 AI 工具组合：产品/需求：DeepSeek + Trae。适合技术 PM，流程是：DeepSeek 拆技术方案，Trae 实现原型。",
        "tags": [
            "产品-需求"
        ],
        "importance": 73,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "DeepSeek 拆技术方案，Trae 实现原型。",
        "audience": "技术 PM"
    },
    {
        "num": "160",
        "scenario": "产品/需求",
        "title": "产品/需求：飞书多维表格 + AI 问数据",
        "combo": "飞书多维表格 + AI 问数据",
        "id_slug": "product-requirements-feishu-base-ai-data",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "飞书多维表格"
        ],
        "steps": [
            "用户反馈入表，AI 分类、统计和生成需求优先级"
        ],
        "outputs": [
            "产品运营"
        ],
        "summary": "国内 AI 工具组合：产品/需求：飞书多维表格 + AI 问数据。适合产品运营，流程是：用户反馈入表，AI 分类、统计和生成需求优先级。",
        "tags": [
            "产品-需求",
            "spreadsheet",
            "data"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用户反馈入表，AI 分类、统计和生成需求优先级。",
        "audience": "产品运营"
    },
    {
        "num": "161",
        "scenario": "产品/需求",
        "title": "产品/需求：钉钉 + 宜搭 + 通义",
        "combo": "钉钉 + 宜搭 + 通义",
        "id_slug": "product-requirements-dingtalk-qwen",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "钉钉",
            "宜搭",
            "通义"
        ],
        "steps": [
            "用宜搭快速生成业务流程原型，通义补文案和逻辑"
        ],
        "outputs": [
            "内部产品"
        ],
        "summary": "国内 AI 工具组合：产品/需求：钉钉 + 宜搭 + 通义。适合内部产品，流程是：用宜搭快速生成业务流程原型，通义补文案和逻辑。",
        "tags": [
            "产品-需求"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用宜搭快速生成业务流程原型，通义补文案和逻辑。",
        "audience": "内部产品"
    },
    {
        "num": "162",
        "scenario": "产品/需求",
        "title": "产品/需求：ima + 竞品资料",
        "combo": "ima + 竞品资料",
        "id_slug": "product-requirements-ima",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "ima",
            "竞品资料"
        ],
        "steps": [
            "竞品文章、截图、报告入库，生成对比矩阵"
        ],
        "outputs": [
            "产品战略"
        ],
        "summary": "国内 AI 工具组合：产品/需求：ima + 竞品资料。适合产品战略，流程是：竞品文章、截图、报告入库，生成对比矩阵。",
        "tags": [
            "产品-需求"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "竞品文章、截图、报告入库，生成对比矩阵。",
        "audience": "产品战略"
    },
    {
        "num": "163",
        "scenario": "产品/需求",
        "title": "产品/需求：秘塔 + Kimi",
        "combo": "秘塔 + Kimi",
        "id_slug": "product-requirements-metaso-kimi",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "秘塔",
            "Kimi"
        ],
        "steps": [
            "搜索竞品和行业资料，Kimi 写产品方案"
        ],
        "outputs": [
            "新业务探索"
        ],
        "summary": "国内 AI 工具组合：产品/需求：秘塔 + Kimi。适合新业务探索，流程是：搜索竞品和行业资料，Kimi 写产品方案。",
        "tags": [
            "产品-需求"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "搜索竞品和行业资料，Kimi 写产品方案。",
        "audience": "新业务探索"
    },
    {
        "num": "164",
        "scenario": "产品/需求",
        "title": "产品/需求：扣子 + API",
        "combo": "扣子 + API",
        "id_slug": "product-requirements-coze-cn-api",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "扣子"
        ],
        "steps": [
            "把产品需求转成可交互的智能体 demo"
        ],
        "outputs": [
            "AI 产品"
        ],
        "summary": "国内 AI 工具组合：产品/需求：扣子 + API。适合AI 产品，流程是：把产品需求转成可交互的智能体 demo。",
        "tags": [
            "产品-需求"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "把产品需求转成可交互的智能体 demo。",
        "audience": "AI 产品"
    },
    {
        "num": "165",
        "scenario": "产品/需求",
        "title": "产品/需求：CodeBuddy + 飞书",
        "combo": "CodeBuddy + 飞书",
        "id_slug": "product-requirements-codebuddy-feishu",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "CodeBuddy",
            "飞书"
        ],
        "steps": [
            "研发任务从飞书进入 CodeBuddy，完成代码和审查"
        ],
        "outputs": [
            "研发协作"
        ],
        "summary": "国内 AI 工具组合：产品/需求：CodeBuddy + 飞书。适合研发协作，流程是：研发任务从飞书进入 CodeBuddy，完成代码和审查。",
        "tags": [
            "产品-需求",
            "coding"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "研发任务从飞书进入 CodeBuddy，完成代码和审查。",
        "audience": "研发协作"
    },
    {
        "num": "166",
        "scenario": "产品/需求",
        "title": "产品/需求：通义灵码 + 阿里云 DevOps",
        "combo": "通义灵码 + 阿里云 DevOps",
        "id_slug": "product-requirements-qwen-devops",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tools": [
            "通义灵码",
            "阿里云 DevOps"
        ],
        "steps": [
            "需求到代码、单测、部署联动"
        ],
        "outputs": [
            "企业研发"
        ],
        "summary": "国内 AI 工具组合：产品/需求：通义灵码 + 阿里云 DevOps。适合企业研发，流程是：需求到代码、单测、部署联动。",
        "tags": [
            "产品-需求",
            "coding"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "需求到代码、单测、部署联动。",
        "audience": "企业研发"
    },
    {
        "num": "167",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：ima + 微信收藏",
        "combo": "ima + 微信收藏",
        "id_slug": "knowledge-base-rag-ima",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "ima",
            "微信收藏"
        ],
        "steps": [
            "一键保存公众号/网页/报告到知识库，后续问答和写作"
        ],
        "outputs": [
            "个人第二大脑"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：ima + 微信收藏。适合个人第二大脑，流程是：一键保存公众号/网页/报告到知识库，后续问答和写作。",
        "tags": [
            "知识库-rag",
            "rag"
        ],
        "importance": 72,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "一键保存公众号/网页/报告到知识库，后续问答和写作。",
        "audience": "个人第二大脑"
    },
    {
        "num": "168",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：飞书知识库 + aily",
        "combo": "飞书知识库 + aily",
        "id_slug": "knowledge-base-rag-feishu-knowledge-base-aily",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书知识库",
            "aily"
        ],
        "steps": [
            "企业文档和会议沉淀，aily 作为内部问答入口"
        ],
        "outputs": [
            "企业知识库"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：飞书知识库 + aily。适合企业知识库，流程是：企业文档和会议沉淀，aily 作为内部问答入口。",
        "tags": [
            "知识库-rag",
            "docs",
            "meeting",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "企业文档和会议沉淀，aily 作为内部问答入口。",
        "audience": "企业知识库"
    },
    {
        "num": "169",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：钉钉知识库 + 通义",
        "combo": "钉钉知识库 + 通义",
        "id_slug": "knowledge-base-rag-dingtalk-knowledge-base-qwen",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉知识库",
            "通义"
        ],
        "steps": [
            "文档、群消息、会议纪要统一问答"
        ],
        "outputs": [
            "钉钉组织"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：钉钉知识库 + 通义。适合钉钉组织，流程是：文档、群消息、会议纪要统一问答。",
        "tags": [
            "知识库-rag",
            "docs",
            "meeting",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "文档、群消息、会议纪要统一问答。",
        "audience": "钉钉组织"
    },
    {
        "num": "170",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：FastGPT + DeepSeek",
        "combo": "FastGPT + DeepSeek",
        "id_slug": "knowledge-base-rag-fastgpt-deepseek",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "FastGPT",
            "DeepSeek"
        ],
        "steps": [
            "私有文档上传、检索、问答和 API 接入"
        ],
        "outputs": [
            "中小企业"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：FastGPT + DeepSeek。适合中小企业，流程是：私有文档上传、检索、问答和 API 接入。",
        "tags": [
            "知识库-rag",
            "docs",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "私有文档上传、检索、问答和 API 接入。",
        "audience": "中小企业"
    },
    {
        "num": "171",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：Dify + Qwen",
        "combo": "Dify + Qwen",
        "id_slug": "knowledge-base-rag-dify-qwen",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Dify",
            "Qwen"
        ],
        "steps": [
            "Dify 编排工作流，Qwen 做中文问答和生成"
        ],
        "outputs": [
            "开发者"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：Dify + Qwen。适合开发者，流程是：Dify 编排工作流，Qwen 做中文问答和生成。",
        "tags": [
            "知识库-rag",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Dify 编排工作流，Qwen 做中文问答和生成。",
        "audience": "开发者"
    },
    {
        "num": "172",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：RAGFlow + Kimi/DeepSeek",
        "combo": "RAGFlow + Kimi/DeepSeek",
        "id_slug": "knowledge-base-rag-rag-flow-kimi-deepseek",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "RAGFlow",
            "Kimi",
            "DeepSeek"
        ],
        "steps": [
            "RAGFlow 解析复杂 PDF，模型生成结构化回答"
        ],
        "outputs": [
            "文档密集团队"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：RAGFlow + Kimi/DeepSeek。适合文档密集团队，流程是：RAGFlow 解析复杂 PDF，模型生成结构化回答。",
        "tags": [
            "知识库-rag",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "RAGFlow 解析复杂 PDF，模型生成结构化回答。",
        "audience": "文档密集团队"
    },
    {
        "num": "173",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：MaxKB + 通义",
        "combo": "MaxKB + 通义",
        "id_slug": "knowledge-base-rag-maxkb-qwen",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "MaxKB",
            "通义"
        ],
        "steps": [
            "快速搭企业 FAQ、客服和内部知识库"
        ],
        "outputs": [
            "运维/客服"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：MaxKB + 通义。适合运维/客服，流程是：快速搭企业 FAQ、客服和内部知识库。",
        "tags": [
            "知识库-rag",
            "rag",
            "support"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "快速搭企业 FAQ、客服和内部知识库。",
        "audience": "运维/客服"
    },
    {
        "num": "174",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：Kimi + 本地文件夹",
        "combo": "Kimi + 本地文件夹",
        "id_slug": "knowledge-base-rag-kimi-local",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Kimi"
        ],
        "steps": [
            "Kimi 处理长文档和多文件，生成摘要和任务"
        ],
        "outputs": [
            "个人研究"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：Kimi + 本地文件夹。适合个人研究，流程是：Kimi 处理长文档和多文件，生成摘要和任务。",
        "tags": [
            "知识库-rag",
            "docs",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Kimi 处理长文档和多文件，生成摘要和任务。",
        "audience": "个人研究"
    },
    {
        "num": "175",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：纳米 + ima",
        "combo": "纳米 + ima",
        "id_slug": "knowledge-base-rag-nami-ima",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "纳米",
            "ima"
        ],
        "steps": [
            "纳米把资料变脑图，ima 做长期沉淀"
        ],
        "outputs": [
            "学习/研究"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：纳米 + ima。适合学习/研究，流程是：纳米把资料变脑图，ima 做长期沉淀。",
        "tags": [
            "知识库-rag",
            "rag"
        ],
        "importance": 71,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "纳米把资料变脑图，ima 做长期沉淀。",
        "audience": "学习/研究"
    },
    {
        "num": "176",
        "scenario": "知识库/RAG",
        "title": "知识库/RAG：秘塔 + 飞书文档",
        "combo": "秘塔 + 飞书文档",
        "id_slug": "knowledge-base-rag-metaso-feishu",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "秘塔",
            "飞书文档"
        ],
        "steps": [
            "秘塔查资料，飞书文档协作沉淀和任务化"
        ],
        "outputs": [
            "团队资料库"
        ],
        "summary": "国内 AI 工具组合：知识库/RAG：秘塔 + 飞书文档。适合团队资料库，流程是：秘塔查资料，飞书文档协作沉淀和任务化。",
        "tags": [
            "知识库-rag",
            "docs",
            "rag"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "秘塔查资料，飞书文档协作沉淀和任务化。",
        "audience": "团队资料库"
    },
    {
        "num": "177",
        "scenario": "自动化",
        "title": "自动化：n8n + DeepSeek API",
        "combo": "n8n + DeepSeek API",
        "id_slug": "automation-n8n-deepseek-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "n8n",
            "DeepSeek API"
        ],
        "steps": [
            "n8n 定时触发，DeepSeek 批量摘要/分类，推送飞书/钉钉"
        ],
        "outputs": [
            "低成本自动化"
        ],
        "summary": "国内 AI 工具组合：自动化：n8n + DeepSeek API。适合低成本自动化，流程是：n8n 定时触发，DeepSeek 批量摘要/分类，推送飞书/钉钉。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "n8n 定时触发，DeepSeek 批量摘要/分类，推送飞书/钉钉。",
        "audience": "低成本自动化"
    },
    {
        "num": "178",
        "scenario": "自动化",
        "title": "自动化：扣子 + n8n",
        "combo": "扣子 + n8n",
        "id_slug": "automation-coze-cn-n8n",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "扣子",
            "n8n"
        ],
        "steps": [
            "扣子处理 AI 判断和对话，n8n 处理外部系统连接"
        ],
        "outputs": [
            "复杂流程"
        ],
        "summary": "国内 AI 工具组合：自动化：扣子 + n8n。适合复杂流程，流程是：扣子处理 AI 判断和对话，n8n 处理外部系统连接。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "扣子处理 AI 判断和对话，n8n 处理外部系统连接。",
        "audience": "复杂流程"
    },
    {
        "num": "179",
        "scenario": "自动化",
        "title": "自动化：飞书多维表格 + 扣子",
        "combo": "飞书多维表格 + 扣子",
        "id_slug": "automation-feishu-base-coze-cn",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书多维表格",
            "扣子"
        ],
        "steps": [
            "表格新增记录触发扣子生成内容并回写字段"
        ],
        "outputs": [
            "内容工厂"
        ],
        "summary": "国内 AI 工具组合：自动化：飞书多维表格 + 扣子。适合内容工厂，流程是：表格新增记录触发扣子生成内容并回写字段。",
        "tags": [
            "自动化",
            "spreadsheet",
            "automation",
            "content"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "表格新增记录触发扣子生成内容并回写字段。",
        "audience": "内容工厂"
    },
    {
        "num": "180",
        "scenario": "自动化",
        "title": "自动化：钉钉机器人 + DeepSeek",
        "combo": "钉钉机器人 + DeepSeek",
        "id_slug": "automation-dingtalk-deepseek",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "钉钉机器人",
            "DeepSeek"
        ],
        "steps": [
            "收到工单后自动分类、摘要、派单"
        ],
        "outputs": [
            "IT/客服"
        ],
        "summary": "国内 AI 工具组合：自动化：钉钉机器人 + DeepSeek。适合IT/客服，流程是：收到工单后自动分类、摘要、派单。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "收到工单后自动分类、摘要、派单。",
        "audience": "IT/客服"
    },
    {
        "num": "181",
        "scenario": "自动化",
        "title": "自动化：企业微信机器人 + 豆包",
        "combo": "企业微信机器人 + 豆包",
        "id_slug": "automation-doubao",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "企业微信机器人",
            "豆包"
        ],
        "steps": [
            "群消息摘要、FAQ 回复、提醒和日报"
        ],
        "outputs": [
            "微信生态组织"
        ],
        "summary": "国内 AI 工具组合：自动化：企业微信机器人 + 豆包。适合微信生态组织，流程是：群消息摘要、FAQ 回复、提醒和日报。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "群消息摘要、FAQ 回复、提醒和日报。",
        "audience": "微信生态组织"
    },
    {
        "num": "182",
        "scenario": "自动化",
        "title": "自动化：Coze + Webhook + API",
        "combo": "Coze + Webhook + API",
        "id_slug": "automation-coze-webhook-api",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Coze",
            "Webhook"
        ],
        "steps": [
            "Coze 智能体通过 webhook 调业务系统，完成查询/下单/推送"
        ],
        "outputs": [
            "轻量应用"
        ],
        "summary": "国内 AI 工具组合：自动化：Coze + Webhook + API。适合轻量应用，流程是：Coze 智能体通过 webhook 调业务系统，完成查询/下单/推送。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "Coze 智能体通过 webhook 调业务系统，完成查询/下单/推送。",
        "audience": "轻量应用"
    },
    {
        "num": "183",
        "scenario": "自动化",
        "title": "自动化：飞书 aily + 定时任务",
        "combo": "飞书 aily + 定时任务",
        "id_slug": "automation-feishu-aily",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书 aily",
            "定时任务"
        ],
        "steps": [
            "每周固定生成周报、复盘、提醒和资料整理"
        ],
        "outputs": [
            "个人助理"
        ],
        "summary": "国内 AI 工具组合：自动化：飞书 aily + 定时任务。适合个人助理，流程是：每周固定生成周报、复盘、提醒和资料整理。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 70,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "每周固定生成周报、复盘、提醒和资料整理。",
        "audience": "个人助理"
    },
    {
        "num": "184",
        "scenario": "自动化",
        "title": "自动化：OpenClaw + 本地电脑",
        "combo": "OpenClaw + 本地电脑",
        "id_slug": "automation-openclaw-local",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "OpenClaw",
            "本地电脑"
        ],
        "steps": [
            "通过自然语言整理文件、发消息、安排日程和写脚本"
        ],
        "outputs": [
            "个人 agent"
        ],
        "summary": "国内 AI 工具组合：自动化：OpenClaw + 本地电脑。适合个人 agent，流程是：通过自然语言整理文件、发消息、安排日程和写脚本。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "通过自然语言整理文件、发消息、安排日程和写脚本。",
        "audience": "个人 agent"
    },
    {
        "num": "185",
        "scenario": "自动化",
        "title": "自动化：WorkBuddy + QQ/飞书/钉钉",
        "combo": "WorkBuddy + QQ/飞书/钉钉",
        "id_slug": "automation-workbuddy-qq-feishu-dingtalk",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "WorkBuddy",
            "QQ",
            "飞书",
            "钉钉"
        ],
        "steps": [
            "聊天入口下达任务，自动处理数据和文案"
        ],
        "outputs": [
            "办公自动化"
        ],
        "summary": "国内 AI 工具组合：自动化：WorkBuddy + QQ/飞书/钉钉。适合办公自动化，流程是：聊天入口下达任务，自动处理数据和文案。",
        "tags": [
            "自动化",
            "data",
            "automation"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "聊天入口下达任务，自动处理数据和文案。",
        "audience": "办公自动化"
    },
    {
        "num": "186",
        "scenario": "自动化",
        "title": "自动化：火山方舟 + 扣子",
        "combo": "火山方舟 + 扣子",
        "id_slug": "automation-coze-cn",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "火山方舟",
            "扣子"
        ],
        "steps": [
            "方舟提供模型/API，扣子负责应用编排和发布"
        ],
        "outputs": [
            "企业 AI"
        ],
        "summary": "国内 AI 工具组合：自动化：火山方舟 + 扣子。适合企业 AI，流程是：方舟提供模型/API，扣子负责应用编排和发布。",
        "tags": [
            "自动化",
            "automation"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "方舟提供模型/API，扣子负责应用编排和发布。",
        "audience": "企业 AI"
    },
    {
        "num": "187",
        "scenario": "本地/开源",
        "title": "本地/开源：DeepSeek 开源模型 + Ollama",
        "combo": "DeepSeek 开源模型 + Ollama",
        "id_slug": "local-open-source-deepseek-open-source-ollama",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "DeepSeek 开源模型",
            "Ollama"
        ],
        "steps": [
            "本地运行模型，处理隐私敏感摘要、分类和代码"
        ],
        "outputs": [
            "隐私优先"
        ],
        "summary": "国内 AI 工具组合：本地/开源：DeepSeek 开源模型 + Ollama。适合隐私优先，流程是：本地运行模型，处理隐私敏感摘要、分类和代码。",
        "tags": [
            "本地-开源",
            "coding"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "本地运行模型，处理隐私敏感摘要、分类和代码。",
        "audience": "隐私优先"
    },
    {
        "num": "188",
        "scenario": "本地/开源",
        "title": "本地/开源：Qwen 开源模型 + Dify",
        "combo": "Qwen 开源模型 + Dify",
        "id_slug": "local-open-source-qwen-open-source-dify",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "Qwen 开源模型",
            "Dify"
        ],
        "steps": [
            "用 Qwen 作为模型底座，Dify 搭应用和工作流"
        ],
        "outputs": [
            "私有部署"
        ],
        "summary": "国内 AI 工具组合：本地/开源：Qwen 开源模型 + Dify。适合私有部署，流程是：用 Qwen 作为模型底座，Dify 搭应用和工作流。",
        "tags": [
            "本地-开源"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "用 Qwen 作为模型底座，Dify 搭应用和工作流。",
        "audience": "私有部署"
    },
    {
        "num": "189",
        "scenario": "本地/开源",
        "title": "本地/开源：GLM 开源模型 + FastGPT",
        "combo": "GLM 开源模型 + FastGPT",
        "id_slug": "local-open-source-glm-open-source-fastgpt",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "GLM 开源模型",
            "FastGPT"
        ],
        "steps": [
            "GLM 做问答，FastGPT 管知识库和接口"
        ],
        "outputs": [
            "企业内网"
        ],
        "summary": "国内 AI 工具组合：本地/开源：GLM 开源模型 + FastGPT。适合企业内网，流程是：GLM 做问答，FastGPT 管知识库和接口。",
        "tags": [
            "本地-开源",
            "rag"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "GLM 做问答，FastGPT 管知识库和接口。",
        "audience": "企业内网"
    },
    {
        "num": "190",
        "scenario": "本地/开源",
        "title": "本地/开源：Kimi K2.6 开源权重 + Trae",
        "combo": "Kimi K2.6 开源权重 + Trae",
        "id_slug": "local-open-source-kimi-k2-6-open-source-trae",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "Kimi K2.6 开源权重",
            "Trae"
        ],
        "steps": [
            "本地/私有模型处理代码与长上下文，Trae 编辑"
        ],
        "outputs": [
            "高级开发"
        ],
        "summary": "国内 AI 工具组合：本地/开源：Kimi K2.6 开源权重 + Trae。适合高级开发，流程是：本地/私有模型处理代码与长上下文，Trae 编辑。",
        "tags": [
            "本地-开源",
            "coding"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "本地/私有模型处理代码与长上下文，Trae 编辑。",
        "audience": "高级开发"
    },
    {
        "num": "191",
        "scenario": "本地/开源",
        "title": "本地/开源：ComfyUI + 通义万相/即梦素材",
        "combo": "ComfyUI + 通义万相/即梦素材",
        "id_slug": "local-open-source-comfyui-qwen-jimeng",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "ComfyUI",
            "通义万相",
            "即梦素材"
        ],
        "steps": [
            "ComfyUI 做图像工作流，国产模型生成素材"
        ],
        "outputs": [
            "视觉工程"
        ],
        "summary": "国内 AI 工具组合：本地/开源：ComfyUI + 通义万相/即梦素材。适合视觉工程，流程是：ComfyUI 做图像工作流，国产模型生成素材。",
        "tags": [
            "本地-开源",
            "image"
        ],
        "importance": 69,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "ComfyUI 做图像工作流，国产模型生成素材。",
        "audience": "视觉工程"
    },
    {
        "num": "192",
        "scenario": "本地/开源",
        "title": "本地/开源：OpenClaw + 本地模型",
        "combo": "OpenClaw + 本地模型",
        "id_slug": "local-open-source-openclaw-local",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "OpenClaw",
            "本地模型"
        ],
        "steps": [
            "OpenClaw 编排行动，本地模型做敏感任务处理"
        ],
        "outputs": [
            "安全实验"
        ],
        "summary": "国内 AI 工具组合：本地/开源：OpenClaw + 本地模型。适合安全实验，流程是：OpenClaw 编排行动，本地模型做敏感任务处理。",
        "tags": [
            "本地-开源"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "OpenClaw 编排行动，本地模型做敏感任务处理。",
        "audience": "安全实验"
    },
    {
        "num": "193",
        "scenario": "本地/开源",
        "title": "本地/开源：RAGFlow + 本地 DeepSeek",
        "combo": "RAGFlow + 本地 DeepSeek",
        "id_slug": "local-open-source-rag-flow-local-deepseek",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "RAGFlow",
            "本地 DeepSeek"
        ],
        "steps": [
            "复杂文档解析和本地问答，不出内网"
        ],
        "outputs": [
            "政企文档"
        ],
        "summary": "国内 AI 工具组合：本地/开源：RAGFlow + 本地 DeepSeek。适合政企文档，流程是：复杂文档解析和本地问答，不出内网。",
        "tags": [
            "本地-开源",
            "docs"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "复杂文档解析和本地问答，不出内网。",
        "audience": "政企文档"
    },
    {
        "num": "194",
        "scenario": "本地/开源",
        "title": "本地/开源：MaxKB + Qwen + 内网文档",
        "combo": "MaxKB + Qwen + 内网文档",
        "id_slug": "local-open-source-maxkb-qwen",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "MaxKB",
            "Qwen"
        ],
        "steps": [
            "轻量知识库问答，适合部门自建"
        ],
        "outputs": [
            "部门知识库"
        ],
        "summary": "国内 AI 工具组合：本地/开源：MaxKB + Qwen + 内网文档。适合部门知识库，流程是：轻量知识库问答，适合部门自建。",
        "tags": [
            "本地-开源",
            "docs",
            "rag"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "轻量知识库问答，适合部门自建。",
        "audience": "部门知识库"
    },
    {
        "num": "195",
        "scenario": "本地/开源",
        "title": "本地/开源：CodeGeeX + 私有 Git",
        "combo": "CodeGeeX + 私有 Git",
        "id_slug": "local-open-source-codegeex-git",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "CodeGeeX"
        ],
        "steps": [
            "多语言代码补全配合私有代码仓库"
        ],
        "outputs": [
            "研发团队"
        ],
        "summary": "国内 AI 工具组合：本地/开源：CodeGeeX + 私有 Git。适合研发团队，流程是：多语言代码补全配合私有代码仓库。",
        "tags": [
            "本地-开源",
            "coding"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "多语言代码补全配合私有代码仓库。",
        "audience": "研发团队"
    },
    {
        "num": "196",
        "scenario": "本地/开源",
        "title": "本地/开源：DeepSeek + Python 脚本",
        "combo": "DeepSeek + Python 脚本",
        "id_slug": "local-open-source-deepseek-python",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tools": [
            "DeepSeek"
        ],
        "steps": [
            "模型做分类/摘要，Python 负责文件、表格和批处理"
        ],
        "outputs": [
            "个人自动化"
        ],
        "summary": "国内 AI 工具组合：本地/开源：DeepSeek + Python 脚本。适合个人自动化，流程是：模型做分类/摘要，Python 负责文件、表格和批处理。",
        "tags": [
            "本地-开源",
            "spreadsheet"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "模型做分类/摘要，Python 负责文件、表格和批处理。",
        "audience": "个人自动化"
    },
    {
        "num": "197",
        "scenario": "组合总栈",
        "title": "组合总栈：Kimi + 秘塔 + WPS AI",
        "combo": "Kimi + 秘塔 + WPS AI",
        "id_slug": "full-stack-kimi-metaso-wps-ai",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "Kimi",
            "秘塔",
            "WPS AI"
        ],
        "steps": [
            "搜索资料、长文整理、生成办公交付物"
        ],
        "outputs": [
            "研究办公"
        ],
        "summary": "国内 AI 工具组合：组合总栈：Kimi + 秘塔 + WPS AI。适合研究办公，流程是：搜索资料、长文整理、生成办公交付物。",
        "tags": [
            "组合总栈"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "搜索资料、长文整理、生成办公交付物。",
        "audience": "研究办公"
    },
    {
        "num": "198",
        "scenario": "组合总栈",
        "title": "组合总栈：豆包 + 即梦 + 剪映",
        "combo": "豆包 + 即梦 + 剪映",
        "id_slug": "full-stack-doubao-jimeng-jianying",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "豆包",
            "即梦",
            "剪映"
        ],
        "steps": [
            "脚本、视觉、视频、字幕和发布"
        ],
        "outputs": [
            "短视频"
        ],
        "summary": "国内 AI 工具组合：组合总栈：豆包 + 即梦 + 剪映。适合短视频，流程是：脚本、视觉、视频、字幕和发布。",
        "tags": [
            "组合总栈",
            "video"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "脚本、视觉、视频、字幕和发布。",
        "audience": "短视频"
    },
    {
        "num": "199",
        "scenario": "组合总栈",
        "title": "组合总栈：DeepSeek + Trae + CodeBuddy",
        "combo": "DeepSeek + Trae + CodeBuddy",
        "id_slug": "full-stack-deepseek-trae-codebuddy",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "DeepSeek",
            "Trae",
            "CodeBuddy"
        ],
        "steps": [
            "低成本推理、IDE 编码、代码审查和部署"
        ],
        "outputs": [
            "开发者"
        ],
        "summary": "国内 AI 工具组合：组合总栈：DeepSeek + Trae + CodeBuddy。适合开发者，流程是：低成本推理、IDE 编码、代码审查和部署。",
        "tags": [
            "组合总栈",
            "coding"
        ],
        "importance": 68,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "低成本推理、IDE 编码、代码审查和部署。",
        "audience": "开发者"
    },
    {
        "num": "200",
        "scenario": "组合总栈",
        "title": "组合总栈：飞书 aily + 多维表格 + 扣子 + Kimi",
        "combo": "飞书 aily + 多维表格 + 扣子 + Kimi",
        "id_slug": "full-stack-feishu-aily-base-coze-cn-kimi",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tools": [
            "飞书 aily",
            "扣子",
            "Kimi"
        ],
        "steps": [
            "企业资料/数据沉淀在飞书，多维表格分析，扣子编排执行，Kimi输出长报告"
        ],
        "outputs": [
            "企业 AI 工作流"
        ],
        "summary": "国内 AI 工具组合：组合总栈：飞书 aily + 多维表格 + 扣子 + Kimi。适合企业 AI 工作流，流程是：企业资料/数据沉淀在飞书，多维表格分析，扣子编排执行，Kimi输出长报告。",
        "tags": [
            "组合总栈",
            "spreadsheet",
            "data"
        ],
        "importance": 67,
        "source_section": "china_ai_tool_workflow_stacks_2026_recent_3_months.pdf",
        "workflow": "企业资料/数据沉淀在飞书，多维表格分析，扣子编排执行，Kimi输出长报告。",
        "audience": "企业 AI 工作流"
    }
]

CHINA_AI_TOOL_SKILLS = [
    {
        "tool": "豆包",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "legal"
        ],
        "example": "通用助手：豆包 + Kimi",
        "workflow": "豆包处理日常问答、短文案、语音/图片输入；Kimi 接长PDF、合同、报告和长文总结。"
    },
    {
        "tool": "Kimi",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "legal"
        ],
        "example": "通用助手：豆包 + Kimi",
        "workflow": "豆包处理日常问答、短文案、语音/图片输入；Kimi 接长PDF、合同、报告和长文总结。"
    },
    {
        "tool": "DeepSeek",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs",
            "coding"
        ],
        "example": "通用助手：DeepSeek + Kimi",
        "workflow": "DeepSeek 做低成本推理、代码和批量初稿；Kimi做长文档吸收和结构化报告。"
    },
    {
        "tool": "通义",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs",
            "spreadsheet"
        ],
        "example": "通用助手：通义 + WPS AI",
        "workflow": "通义做问答和多模态生成；WPS AI 落到文档、表格、PPT 成品。"
    },
    {
        "tool": "WPS AI",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs",
            "spreadsheet"
        ],
        "example": "通用助手：通义 + WPS AI",
        "workflow": "通义做问答和多模态生成；WPS AI 落到文档、表格、PPT 成品。"
    },
    {
        "tool": "腾讯元宝",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "rag"
        ],
        "example": "通用助手：腾讯元宝 + ima",
        "workflow": "元宝查微信生态和联网信息；ima 沉淀知识库并生成文章/纪要。"
    },
    {
        "tool": "ima",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "rag"
        ],
        "example": "通用助手：腾讯元宝 + ima",
        "workflow": "元宝查微信生态和联网信息；ima 沉淀知识库并生成文章/纪要。"
    },
    {
        "tool": "讯飞星火",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "meeting"
        ],
        "example": "通用助手：讯飞星火 + 通义听悟",
        "workflow": "星火做学习答疑和写作；听悟转写课程/会议并输出摘要。"
    },
    {
        "tool": "通义听悟",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "meeting"
        ],
        "example": "通用助手：讯飞星火 + 通义听悟",
        "workflow": "星火做学习答疑和写作；听悟转写课程/会议并输出摘要。"
    },
    {
        "tool": "文小言",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手"
        ],
        "example": "通用助手：文小言 + 百度文库 AI",
        "workflow": "文小言做公文/论文/策划；百度文库 AI 找模板和资料包。"
    },
    {
        "tool": "百度文库 AI",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手"
        ],
        "example": "通用助手：文小言 + 百度文库 AI",
        "workflow": "文小言做公文/论文/策划；百度文库 AI 找模板和资料包。"
    },
    {
        "tool": "GLM",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs"
        ],
        "example": "通用助手：GLM/智谱清言 + 飞书",
        "workflow": "GLM 做企业级问答和推理；飞书承载文档、审批、任务。"
    },
    {
        "tool": "智谱清言",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs"
        ],
        "example": "通用助手：GLM/智谱清言 + 飞书",
        "workflow": "GLM 做企业级问答和推理；飞书承载文档、审批、任务。"
    },
    {
        "tool": "飞书",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs"
        ],
        "example": "通用助手：GLM/智谱清言 + 飞书",
        "workflow": "GLM 做企业级问答和推理；飞书承载文档、审批、任务。"
    },
    {
        "tool": "天工 Skywork",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "docs",
            "spreadsheet"
        ],
        "example": "通用助手：天工 Skywork + Kimi",
        "workflow": "天工做 Deep Research、文档/PPT/表格；Kimi 对超长资料二次理解。"
    },
    {
        "tool": "纳米 AI 搜索",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手",
            "video"
        ],
        "example": "通用助手：纳米 AI 搜索 + 豆包",
        "workflow": "纳米解析网页/PDF/视频并生成脑图；豆包改写成短文案。"
    },
    {
        "tool": "秘塔 AI 搜索",
        "scenario": "通用助手",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "通用助手"
        ],
        "example": "通用助手：秘塔 AI 搜索 + DeepSeek",
        "workflow": "秘塔找资料和来源；DeepSeek 做推理、分类和提纲。"
    },
    {
        "tool": "通义千问",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "research"
        ],
        "example": "研究报告：DeepSeek + 通义千问",
        "workflow": "DeepSeek 做成本敏感的批量资料初筛；通义做多模态补充和成稿。"
    },
    {
        "tool": "Kimi Deep Research",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "research"
        ],
        "example": "研究报告：Kimi Deep Research + Kimi Slides",
        "workflow": "Kimi 先生成万字研究报告，再用 Slides 入口生成演示稿。"
    },
    {
        "tool": "Kimi Slides",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "research"
        ],
        "example": "研究报告：Kimi Deep Research + Kimi Slides",
        "workflow": "Kimi 先生成万字研究报告，再用 Slides 入口生成演示稿。"
    },
    {
        "tool": "飞书知识库",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "docs",
            "meeting",
            "rag",
            "automation",
            "research"
        ],
        "example": "研究报告：飞书知识库 + 飞书 aily",
        "workflow": "飞书 aily 读取文档、会议和消息，自动整理项目背景、风险和周报。"
    },
    {
        "tool": "飞书 aily",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "docs",
            "meeting",
            "rag",
            "automation",
            "research"
        ],
        "example": "研究报告：飞书知识库 + 飞书 aily",
        "workflow": "飞书 aily 读取文档、会议和消息，自动整理项目背景、风险和周报。"
    },
    {
        "tool": "通义 AI 助理",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "docs",
            "research"
        ],
        "example": "研究报告：钉钉文档 + 通义 AI 助理",
        "workflow": "钉钉 AI 助理从文档和消息提炼项目复盘、纪要和行动项。"
    },
    {
        "tool": "DeepSeek API",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "research"
        ],
        "example": "研究报告：ima + DeepSeek API",
        "workflow": "ima 建私域资料库；DeepSeek API 做批量问答、分类和摘要。"
    },
    {
        "tool": "秘塔",
        "scenario": "研究报告",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "研究报告",
            "research"
        ],
        "example": "研究报告：秘塔 + 文小言",
        "workflow": "秘塔查证；文小言写公文、策划案和论文式结构。"
    },
    {
        "tool": "AiPPT",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公"
        ],
        "example": "PPT/办公：通义 + AiPPT",
        "workflow": "通义生成大纲和讲稿；AiPPT 输出可编辑源文件。"
    },
    {
        "tool": "通义万相",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公"
        ],
        "example": "PPT/办公：Kimi Slides + 通义万相",
        "workflow": "Kimi 生成 slides；通义万相补图、海报和封面。"
    },
    {
        "tool": "即梦",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公"
        ],
        "example": "PPT/办公：豆包 + 即梦 + WPS AI",
        "workflow": "豆包写文案；即梦生成视觉素材；WPS AI 组装 PPT。"
    },
    {
        "tool": "飞书妙搭",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公",
            "docs",
            "automation",
            "legal"
        ],
        "example": "PPT/办公：飞书妙搭 + 飞书文档",
        "workflow": "用自然语言搭合同/表单工具，自动填字段并导出 Word。"
    },
    {
        "tool": "飞书文档",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公",
            "docs",
            "automation",
            "legal"
        ],
        "example": "PPT/办公：飞书妙搭 + 飞书文档",
        "workflow": "用自然语言搭合同/表单工具，自动填字段并导出 Word。"
    },
    {
        "tool": "飞书多维表格 Agent",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公",
            "docs",
            "spreadsheet",
            "data"
        ],
        "example": "PPT/办公：飞书多维表格 Agent + 飞书文档",
        "workflow": "表格数据一句话生成图表和洞察，再同步到飞书文档周报。"
    },
    {
        "tool": "钉钉 AI 助理",
        "scenario": "PPT/办公",
        "category_id": "ai-office",
        "category_label": "AI OFFICE",
        "tags": [
            "ppt-办公",
            "spreadsheet",
            "sales",
            "data"
        ],
        "example": "PPT/办公：钉钉 AI 助理 + 多维表格",
        "workflow": "导入销售数据，定时生成销售周报并推送管理层。"
    },
    {
        "tool": "SkillHub",
        "scenario": "飞书工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "飞书工作流",
            "docs",
            "data"
        ],
        "example": "飞书工作流：飞书 aily + SkillHub",
        "workflow": "安装网页抓取/数据分析/文档生成技能，变成部门专用助手。"
    },
    {
        "tool": "飞书多维表格",
        "scenario": "飞书工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "飞书工作流",
            "spreadsheet",
            "data",
            "automation"
        ],
        "example": "飞书工作流：飞书多维表格 + AI 问数据",
        "workflow": "自然语言问表格，自动统计、分析和给出业务洞察。"
    },
    {
        "tool": "飞书 CLI",
        "scenario": "飞书工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "飞书工作流",
            "automation"
        ],
        "example": "飞书工作流：飞书 CLI + OpenClaw 插件",
        "workflow": "开发 agent/插件自动读取项目资料、跑脚本和生成交付物。"
    },
    {
        "tool": "OpenClaw 插件",
        "scenario": "飞书工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "飞书工作流",
            "automation"
        ],
        "example": "飞书工作流：飞书 CLI + OpenClaw 插件",
        "workflow": "开发 agent/插件自动读取项目资料、跑脚本和生成交付物。"
    },
    {
        "tool": "扣子工作流",
        "scenario": "飞书工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "飞书工作流"
        ],
        "example": "飞书工作流：飞书 + 扣子工作流",
        "workflow": "扣子编排外部工具，飞书负责消息、审批和团队分发。"
    },
    {
        "tool": "钉钉多维表格",
        "scenario": "钉钉工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "钉钉工作流",
            "spreadsheet",
            "data"
        ],
        "example": "钉钉工作流：钉钉多维表格 + 通义",
        "workflow": "多维表格沉淀数据；通义生成分析结论和周报。"
    },
    {
        "tool": "宜搭",
        "scenario": "钉钉工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "钉钉工作流"
        ],
        "example": "钉钉工作流：宜搭 + 通义 AI",
        "workflow": "自然语言生成内部应用、审批表单和业务流程。"
    },
    {
        "tool": "通义 AI",
        "scenario": "钉钉工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "钉钉工作流"
        ],
        "example": "钉钉工作流：宜搭 + 通义 AI",
        "workflow": "自然语言生成内部应用、审批表单和业务流程。"
    },
    {
        "tool": "钉钉酷应用",
        "scenario": "钉钉工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "钉钉工作流"
        ],
        "example": "钉钉工作流：钉钉酷应用 + AI 助理",
        "workflow": "把轻应用嵌入聊天窗口，减少系统切换。"
    },
    {
        "tool": "钉钉",
        "scenario": "钉钉工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "钉钉工作流",
            "docs",
            "meeting"
        ],
        "example": "钉钉工作流：钉钉 + WPS AI",
        "workflow": "钉钉沉淀任务和会议；WPS AI 输出正式文档/PPT。"
    },
    {
        "tool": "扣子",
        "scenario": "钉钉工作流",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "钉钉工作流"
        ],
        "example": "钉钉工作流：钉钉 + 扣子",
        "workflow": "扣子做智能体和外部 API，钉钉做入口和通知。"
    },
    {
        "tool": "豆包 Pro",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent",
            "rag",
            "support"
        ],
        "example": "扣子/Agent：扣子 + 豆包 Pro",
        "workflow": "用豆包 Pro 作为智能体大脑，结合知识库和插件做客服/咨询机器人。"
    },
    {
        "tool": "微信公众号",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent"
        ],
        "example": "扣子/Agent：扣子 + 微信公众号",
        "workflow": "构建问答/资料查询 bot，发布到公众号接收用户咨询。"
    },
    {
        "tool": "抖音",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent",
            "video"
        ],
        "example": "扣子/Agent：扣子 + 抖音",
        "workflow": "把短视频脚本、评论回复、私信问答做成可复用 bot。"
    },
    {
        "tool": "扣子 Agent Skills",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent"
        ],
        "example": "扣子/Agent：扣子 Agent Skills + 法律检索",
        "workflow": "把法规检索、案例摘要、风险提示封成技能包。"
    },
    {
        "tool": "扣子 Agent Plan",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent"
        ],
        "example": "扣子/Agent：扣子 Agent Plan + 增长运营",
        "workflow": "设定 30 天涨粉目标，AI 拆成选题、发布、复盘任务。"
    },
    {
        "tool": "扣子 Agent Coding",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent"
        ],
        "example": "扣子/Agent：扣子 Agent Coding + 业务流程",
        "workflow": "自然语言描述需求，生成完整工作流并部署。"
    },
    {
        "tool": "扣子视频 Agent",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent",
            "video"
        ],
        "example": "扣子/Agent：扣子视频 Agent + 即梦/Seedance",
        "workflow": "生成分镜、图生视频、配音和口型匹配，输出长视频雏形。"
    },
    {
        "tool": "Seedance",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent",
            "video"
        ],
        "example": "扣子/Agent：扣子视频 Agent + 即梦/Seedance",
        "workflow": "生成分镜、图生视频、配音和口型匹配，输出长视频雏形。"
    },
    {
        "tool": "火山引擎",
        "scenario": "扣子/Agent",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "扣子-agent"
        ],
        "example": "扣子/Agent：扣子 + 火山引擎",
        "workflow": "扣子做编排，火山引擎提供模型/API/部署能力。"
    },
    {
        "tool": "小红书",
        "scenario": "内容写作",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "内容写作",
            "content"
        ],
        "example": "内容写作：豆包 + 小红书",
        "workflow": "豆包生成标题、正文、评论回复和选题方向。"
    },
    {
        "tool": "讯飞听见",
        "scenario": "内容写作",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "内容写作",
            "content"
        ],
        "example": "内容写作：讯飞星火 + 讯飞听见",
        "workflow": "听见转写采访，星火整理成稿件。"
    },
    {
        "tool": "天工",
        "scenario": "内容写作",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "内容写作",
            "research",
            "content"
        ],
        "example": "内容写作：天工 + AiPPT",
        "workflow": "天工做研究和长文，AiPPT 做公开课/直播课件。"
    },
    {
        "tool": "剪映",
        "scenario": "内容写作",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "内容写作",
            "content"
        ],
        "example": "内容写作：Kimi + 剪映",
        "workflow": "Kimi 写脚本和分镜，剪映做剪辑和字幕。"
    },
    {
        "tool": "可灵 AI",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：豆包 + 可灵 AI",
        "workflow": "豆包写剧情、镜头、旁白；可灵生成视频片段。"
    },
    {
        "tool": "海螺 AI",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：豆包 + 海螺 AI",
        "workflow": "豆包写口播脚本；海螺生成镜头或人物视频。"
    },
    {
        "tool": "Seedance 2.0",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：即梦 + Seedance 2.0",
        "workflow": "即梦使用 Seedance 生成文生视频/图生视频，再人工剪辑。"
    },
    {
        "tool": "小云雀",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：剪映 + 小云雀/Seedance",
        "workflow": "剪映入口生成 AI 视频素材，接字幕、配乐和发布。"
    },
    {
        "tool": "Vidu",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：Vidu + Kimi",
        "workflow": "Kimi 写动画剧集大纲和分镜，Vidu 生成动画片段。"
    },
    {
        "tool": "SkyReels",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：SkyReels + 豆包",
        "workflow": "豆包写连续剧情，SkyReels 生成连续镜头。"
    },
    {
        "tool": "可灵",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：可灵 + 通义万相",
        "workflow": "万相先生成角色/场景图，可灵图生视频。"
    },
    {
        "tool": "豆包语音",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：即梦 + 剪映 + 豆包语音",
        "workflow": "即梦生成画面，豆包语音配音，剪映合成和调节节奏。"
    },
    {
        "tool": "Seedance API",
        "scenario": "视频生成",
        "category_id": "ai-media",
        "category_label": "AI MEDIA",
        "tags": [
            "视频生成",
            "video"
        ],
        "example": "视频生成：Seedance API + 扣子",
        "workflow": "扣子工作流调用 Seedance API 批量生成视频素材。"
    },
    {
        "tool": "百度 AI 修图",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image"
        ],
        "example": "图像设计：文小言 + 百度 AI 修图",
        "workflow": "文小言策划文案，百度系工具做对话式修图。"
    },
    {
        "tool": "美图设计室",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image"
        ],
        "example": "图像设计：美图设计室 + Kimi",
        "workflow": "Kimi 写营销文案，美图设计室批量生成海报。"
    },
    {
        "tool": "稿定 AI",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image"
        ],
        "example": "图像设计：稿定 AI + 豆包",
        "workflow": "豆包生成活动文案和尺寸要求，稿定套模板输出。"
    },
    {
        "tool": "可画",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image"
        ],
        "example": "图像设计：可画/创客贴 + DeepSeek",
        "workflow": "DeepSeek 写信息架构，可画/创客贴设计成图文海报。"
    },
    {
        "tool": "创客贴",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image"
        ],
        "example": "图像设计：可画/创客贴 + DeepSeek",
        "workflow": "DeepSeek 写信息架构，可画/创客贴设计成图文海报。"
    },
    {
        "tool": "豆包图片",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "video",
            "image"
        ],
        "example": "图像设计：豆包图片 + 剪映",
        "workflow": "豆包生成图片素材，剪映做图文视频。"
    },
    {
        "tool": "1688",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image",
            "ecommerce"
        ],
        "example": "图像设计：通义万相 + 1688/淘宝素材",
        "workflow": "万相生成场景图，结合电商素材做主图和详情页。"
    },
    {
        "tool": "淘宝素材",
        "scenario": "图像设计",
        "category_id": "ai-visual",
        "category_label": "AI VISUAL",
        "tags": [
            "图像设计",
            "image",
            "ecommerce"
        ],
        "example": "图像设计：通义万相 + 1688/淘宝素材",
        "workflow": "万相生成场景图，结合电商素材做主图和详情页。"
    },
    {
        "tool": "Trae",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：Trae + DeepSeek",
        "workflow": "Trae 管工程上下文，DeepSeek 做推理、代码和错误解释。"
    },
    {
        "tool": "豆包模型",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：Trae + 豆包模型",
        "workflow": "国内版 Trae 用豆包模型做 IDE 对话、补全和多文件修改。"
    },
    {
        "tool": "通义灵码",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：通义灵码 + 阿里云",
        "workflow": "灵码写代码/单测/审查，阿里云部署和云服务联动。"
    },
    {
        "tool": "阿里云",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：通义灵码 + 阿里云",
        "workflow": "灵码写代码/单测/审查，阿里云部署和云服务联动。"
    },
    {
        "tool": "CodeBuddy",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：CodeBuddy + 微信开发者工具",
        "workflow": "CodeBuddy 插件接微信开发者工具，做小程序补全和审查。"
    },
    {
        "tool": "微信开发者工具",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：CodeBuddy + 微信开发者工具",
        "workflow": "CodeBuddy 插件接微信开发者工具，做小程序补全和审查。"
    },
    {
        "tool": "CodeBuddy IDE",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding",
            "automation"
        ],
        "example": "AI 编程：CodeBuddy IDE + CLI",
        "workflow": "IDE 做多文件开发，CLI 做终端任务和自动化。"
    },
    {
        "tool": "CLI",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding",
            "automation"
        ],
        "example": "AI 编程：CodeBuddy IDE + CLI",
        "workflow": "IDE 做多文件开发，CLI 做终端任务和自动化。"
    },
    {
        "tool": "WorkBuddy",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding",
            "data",
            "automation"
        ],
        "example": "AI 编程：WorkBuddy + 飞书/钉钉",
        "workflow": "用自然语言让 WorkBuddy 处理数据、文案和自动化办公。"
    },
    {
        "tool": "文心快码",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：文心快码 + 百度智能云",
        "workflow": "快码理解项目并生成/修复代码，百度云承接部署。"
    },
    {
        "tool": "百度智能云",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：文心快码 + 百度智能云",
        "workflow": "快码理解项目并生成/修复代码，百度云承接部署。"
    },
    {
        "tool": "MarsCode",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "example": "AI 编程：MarsCode + 豆包",
        "workflow": "MarsCode 做 IDE 开发和 bug fix，豆包补充文档和解释。"
    },
    {
        "tool": "CodeGeeX",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "example": "AI 编程：CodeGeeX + GLM",
        "workflow": "CodeGeeX 多 IDE 补全，GLM 做复杂问答和文档。"
    },
    {
        "tool": "iFlyCode",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：iFlyCode + 星火",
        "workflow": "iFlyCode 处理代码，星火做中文解释、学习和问答。"
    },
    {
        "tool": "星火",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：iFlyCode + 星火",
        "workflow": "iFlyCode 处理代码，星火做中文解释、学习和问答。"
    },
    {
        "tool": "Dify",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：DeepSeek API + Dify",
        "workflow": "Dify 编排应用，DeepSeek API 负责低成本推理和代码分析。"
    },
    {
        "tool": "FastGPT",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "rag",
            "coding"
        ],
        "example": "AI 编程：FastGPT + DeepSeek",
        "workflow": "FastGPT 建企业知识库问答，DeepSeek 做模型底座。"
    },
    {
        "tool": "RAGFlow",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "example": "AI 编程：RAGFlow + Qwen/DeepSeek",
        "workflow": "RAGFlow 做文档解析和检索增强，Qwen/DeepSeek 生成回答。"
    },
    {
        "tool": "Qwen",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "docs",
            "coding"
        ],
        "example": "AI 编程：RAGFlow + Qwen/DeepSeek",
        "workflow": "RAGFlow 做文档解析和检索增强，Qwen/DeepSeek 生成回答。"
    },
    {
        "tool": "MaxKB",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "rag",
            "coding"
        ],
        "example": "AI 编程：MaxKB + 通义/DeepSeek",
        "workflow": "MaxKB 快速搭知识库应用，通义/DeepSeek 做问答。"
    },
    {
        "tool": "OpenClaw",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：OpenClaw + 国内云",
        "workflow": "云端部署 OpenClaw，连接日程、消息、文件和代码任务。"
    },
    {
        "tool": "Confucius Code Agent",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：Confucius Code Agent + Git",
        "workflow": "开源软件工程 agent 处理 issue、代码修改和提交。"
    },
    {
        "tool": "Git",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：Confucius Code Agent + Git",
        "workflow": "开源软件工程 agent 处理 issue、代码修改和提交。"
    },
    {
        "tool": "Kimi K2.6",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：Kimi K2.6 + Trae",
        "workflow": "Kimi 长上下文理解代码库，Trae 负责 IDE 编辑。"
    },
    {
        "tool": "DeepSeek V4",
        "scenario": "AI 编程",
        "category_id": "ai-coding",
        "category_label": "AI CODING",
        "tags": [
            "ai 编程",
            "coding"
        ],
        "example": "AI 编程：DeepSeek V4 + 通义灵码",
        "workflow": "DeepSeek 做低成本复杂推理，灵码在工程内落地修改。"
    },
    {
        "tool": "巨量引擎",
        "scenario": "电商",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "电商",
            "ecommerce"
        ],
        "example": "电商：豆包 + 巨量引擎",
        "workflow": "豆包生成广告卖点、脚本和投放文案，巨量引擎测试素材。"
    },
    {
        "tool": "AI 图表",
        "scenario": "电商",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "电商",
            "spreadsheet",
            "ecommerce",
            "data",
            "automation"
        ],
        "example": "电商：飞书多维表格 + AI 图表",
        "workflow": "沉淀商品/投放数据，自动生成战报和洞察。"
    },
    {
        "tool": "小红书资料",
        "scenario": "电商",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "电商",
            "ecommerce"
        ],
        "example": "电商：Kimi + 1688/小红书资料",
        "workflow": "整理竞品卖点和用户评价，生成商品文案。"
    },
    {
        "tool": "豆包爱学",
        "scenario": "教育",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "教育",
            "education"
        ],
        "example": "教育：豆包爱学 + 豆包",
        "workflow": "学生问答、作文修改、知识点讲解和学习计划。"
    },
    {
        "tool": "AI 问卷",
        "scenario": "教育",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "教育",
            "spreadsheet",
            "data",
            "education"
        ],
        "example": "教育：飞书多维表格 + AI 问卷",
        "workflow": "生成报名表、反馈表和数据分析。"
    },
    {
        "tool": "钉钉会议",
        "scenario": "教育",
        "category_id": "ai-research",
        "category_label": "AI RESEARCH",
        "tags": [
            "教育",
            "meeting",
            "automation",
            "education"
        ],
        "example": "教育：钉钉会议 + AI 助理",
        "workflow": "课堂/教研会议自动纪要和行动项。"
    },
    {
        "tool": "合同 PDF",
        "scenario": "法律/合同",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "example": "法律/合同：Kimi + 合同 PDF",
        "workflow": "批量阅读合同，列出关键条款、风险和待确认项。"
    },
    {
        "tool": "合同助手",
        "scenario": "法律/合同",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "法律-合同",
            "automation",
            "legal"
        ],
        "example": "法律/合同：飞书妙搭 + 合同助手",
        "workflow": "生成合同字段表单，自动填充、预览、导出 Word。"
    },
    {
        "tool": "法律检索技能",
        "scenario": "法律/合同",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "example": "法律/合同：扣子 + 法律检索技能",
        "workflow": "封装法规检索、案例摘要、风险问答。"
    },
    {
        "tool": "百度文库",
        "scenario": "法律/合同",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "example": "法律/合同：文小言 + 百度文库",
        "workflow": "找公文/合同模板，生成正式文本。"
    },
    {
        "tool": "企业制度库",
        "scenario": "法律/合同",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "法律-合同",
            "legal"
        ],
        "example": "法律/合同：ima + 企业制度库",
        "workflow": "制度、合同、SOP 入库，给员工做问答。"
    },
    {
        "tool": "Kimi Sheets",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "data"
        ],
        "example": "财务/数据：Kimi Sheets + CSV",
        "workflow": "上传 CSV/Excel，做分析、可视化和结论。"
    },
    {
        "tool": "CSV",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "data"
        ],
        "example": "财务/数据：Kimi Sheets + CSV",
        "workflow": "上传 CSV/Excel，做分析、可视化和结论。"
    },
    {
        "tool": "天工表格",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "spreadsheet",
            "data"
        ],
        "example": "财务/数据：天工表格 + WPS AI",
        "workflow": "天工生成表格分析，WPS 美化交付。"
    },
    {
        "tool": "Python 节点",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "data"
        ],
        "example": "财务/数据：扣子 + Python 节点 + LLM",
        "workflow": "PDF 提取数据，Python 计算指标，LLM 生成总结。"
    },
    {
        "tool": "LLM",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "data"
        ],
        "example": "财务/数据：扣子 + Python 节点 + LLM",
        "workflow": "PDF 提取数据，Python 计算指标，LLM 生成总结。"
    },
    {
        "tool": "阿里云 BI",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "data"
        ],
        "example": "财务/数据：通义 + 阿里云 BI",
        "workflow": "通义解释指标，阿里云 BI 做数据看板。"
    },
    {
        "tool": "n8n",
        "scenario": "财务/数据",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "财务-数据",
            "data"
        ],
        "example": "财务/数据：DeepSeek API + n8n",
        "workflow": "n8n 定时拉取数据，DeepSeek 分类总结，推送飞书/钉钉。"
    },
    {
        "tool": "多维表格 CRM",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "spreadsheet",
            "meeting",
            "sales",
            "automation"
        ],
        "example": "销售/CRM：飞书 aily + 多维表格 CRM",
        "workflow": "读取客户跟进、会议和任务，自动生成销售周报。"
    },
    {
        "tool": "销售表格",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "spreadsheet",
            "sales"
        ],
        "example": "销售/CRM：钉钉 AI 助理 + 销售表格",
        "workflow": "定时生成销售周报并推送管理层。"
    },
    {
        "tool": "企业微信",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "sales"
        ],
        "example": "销售/CRM：豆包 + 企业微信",
        "workflow": "生成客户回复、邀约话术和售后 FAQ。"
    },
    {
        "tool": "微信资料",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "video",
            "sales"
        ],
        "example": "销售/CRM：腾讯元宝 + 微信资料",
        "workflow": "读取公开公众号/视频号线索，生成客户背景摘要。"
    },
    {
        "tool": "客户访谈",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "sales"
        ],
        "example": "销售/CRM：Kimi + 客户访谈",
        "workflow": "分析访谈记录，提炼痛点、预算、决策链和方案。"
    },
    {
        "tool": "销售资料库",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "sales"
        ],
        "example": "销售/CRM：ima + 销售资料库",
        "workflow": "沉淀案例、报价、FAQ，生成客户化回复。"
    },
    {
        "tool": "报价工具",
        "scenario": "销售/CRM",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "销售-crm",
            "sales",
            "legal"
        ],
        "example": "销售/CRM：飞书妙搭 + 报价工具",
        "workflow": "自然语言搭报价/合同生成工具，并接飞书审批。"
    },
    {
        "tool": "竞品资料",
        "scenario": "产品/需求",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "产品-需求"
        ],
        "example": "产品/需求：ima + 竞品资料",
        "workflow": "竞品文章、截图、报告入库，生成对比矩阵。"
    },
    {
        "tool": "阿里云 DevOps",
        "scenario": "产品/需求",
        "category_id": "ai-business",
        "category_label": "AI BUSINESS",
        "tags": [
            "产品-需求",
            "coding"
        ],
        "example": "产品/需求：通义灵码 + 阿里云 DevOps",
        "workflow": "需求到代码、单测、部署联动。"
    },
    {
        "tool": "微信收藏",
        "scenario": "知识库/RAG",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "知识库-rag",
            "rag"
        ],
        "example": "知识库/RAG：ima + 微信收藏",
        "workflow": "一键保存公众号/网页/报告到知识库，后续问答和写作。"
    },
    {
        "tool": "aily",
        "scenario": "知识库/RAG",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "知识库-rag",
            "docs",
            "meeting",
            "rag"
        ],
        "example": "知识库/RAG：飞书知识库 + aily",
        "workflow": "企业文档和会议沉淀，aily 作为内部问答入口。"
    },
    {
        "tool": "钉钉知识库",
        "scenario": "知识库/RAG",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "知识库-rag",
            "docs",
            "meeting",
            "rag"
        ],
        "example": "知识库/RAG：钉钉知识库 + 通义",
        "workflow": "文档、群消息、会议纪要统一问答。"
    },
    {
        "tool": "纳米",
        "scenario": "知识库/RAG",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "知识库-rag",
            "rag"
        ],
        "example": "知识库/RAG：纳米 + ima",
        "workflow": "纳米把资料变脑图，ima 做长期沉淀。"
    },
    {
        "tool": "钉钉机器人",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：钉钉机器人 + DeepSeek",
        "workflow": "收到工单后自动分类、摘要、派单。"
    },
    {
        "tool": "企业微信机器人",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：企业微信机器人 + 豆包",
        "workflow": "群消息摘要、FAQ 回复、提醒和日报。"
    },
    {
        "tool": "Coze",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：Coze + Webhook + API",
        "workflow": "Coze 智能体通过 webhook 调业务系统，完成查询/下单/推送。"
    },
    {
        "tool": "Webhook",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：Coze + Webhook + API",
        "workflow": "Coze 智能体通过 webhook 调业务系统，完成查询/下单/推送。"
    },
    {
        "tool": "定时任务",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：飞书 aily + 定时任务",
        "workflow": "每周固定生成周报、复盘、提醒和资料整理。"
    },
    {
        "tool": "本地电脑",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：OpenClaw + 本地电脑",
        "workflow": "通过自然语言整理文件、发消息、安排日程和写脚本。"
    },
    {
        "tool": "QQ",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "data",
            "automation"
        ],
        "example": "自动化：WorkBuddy + QQ/飞书/钉钉",
        "workflow": "聊天入口下达任务，自动处理数据和文案。"
    },
    {
        "tool": "火山方舟",
        "scenario": "自动化",
        "category_id": "ai-agent",
        "category_label": "AI AGENT",
        "tags": [
            "自动化",
            "automation"
        ],
        "example": "自动化：火山方舟 + 扣子",
        "workflow": "方舟提供模型/API，扣子负责应用编排和发布。"
    },
    {
        "tool": "DeepSeek 开源模型",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "coding"
        ],
        "example": "本地/开源：DeepSeek 开源模型 + Ollama",
        "workflow": "本地运行模型，处理隐私敏感摘要、分类和代码。"
    },
    {
        "tool": "Ollama",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "coding"
        ],
        "example": "本地/开源：DeepSeek 开源模型 + Ollama",
        "workflow": "本地运行模型，处理隐私敏感摘要、分类和代码。"
    },
    {
        "tool": "Qwen 开源模型",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源"
        ],
        "example": "本地/开源：Qwen 开源模型 + Dify",
        "workflow": "用 Qwen 作为模型底座，Dify 搭应用和工作流。"
    },
    {
        "tool": "GLM 开源模型",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "rag"
        ],
        "example": "本地/开源：GLM 开源模型 + FastGPT",
        "workflow": "GLM 做问答，FastGPT 管知识库和接口。"
    },
    {
        "tool": "Kimi K2.6 开源权重",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "coding"
        ],
        "example": "本地/开源：Kimi K2.6 开源权重 + Trae",
        "workflow": "本地/私有模型处理代码与长上下文，Trae 编辑。"
    },
    {
        "tool": "ComfyUI",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "image"
        ],
        "example": "本地/开源：ComfyUI + 通义万相/即梦素材",
        "workflow": "ComfyUI 做图像工作流，国产模型生成素材。"
    },
    {
        "tool": "即梦素材",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "image"
        ],
        "example": "本地/开源：ComfyUI + 通义万相/即梦素材",
        "workflow": "ComfyUI 做图像工作流，国产模型生成素材。"
    },
    {
        "tool": "本地模型",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源"
        ],
        "example": "本地/开源：OpenClaw + 本地模型",
        "workflow": "OpenClaw 编排行动，本地模型做敏感任务处理。"
    },
    {
        "tool": "本地 DeepSeek",
        "scenario": "本地/开源",
        "category_id": "ai-models",
        "category_label": "AI MODELS",
        "tags": [
            "本地-开源",
            "docs"
        ],
        "example": "本地/开源：RAGFlow + 本地 DeepSeek",
        "workflow": "复杂文档解析和本地问答，不出内网。"
    }
]

TOOL_SLUG_MAP = {
    "豆包": "doubao", "通义": "qwen", "通义千问": "qwen", "通义万相": "tongyi-wanxiang",
    "腾讯元宝": "tencent-yuanbao", "讯飞星火": "iflytek-spark", "通义听悟": "tingwu",
    "文小言": "wenxiaoyan", "百度文库 AI": "baidu-wenku-ai", "智谱清言": "zhipu-qingyan",
    "飞书": "feishu", "飞书 aily": "feishu-aily", "飞书知识库": "feishu-knowledge-base",
    "天工 Skywork": "skywork", "天工": "skywork", "纳米 AI 搜索": "nami-ai-search",
    "秘塔 AI 搜索": "metaso-ai-search", "秘塔": "metaso", "即梦": "jimeng", "可灵 AI": "kling-ai",
    "海螺 AI": "hailuo-ai", "剪映": "jianying", "扣子": "coze-cn", "扣子工作流": "coze-workflow-cn",
    "钉钉": "dingtalk", "钉钉 AI 助理": "dingtalk-ai-assistant", "宜搭": "yida",
    "飞书多维表格": "feishu-base", "飞书多维表格 Agent": "feishu-base-agent",
}


def _slugify(value: str) -> str:
    if value in TOOL_SLUG_MAP:
        return TOOL_SLUG_MAP[value]
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if slug:
        return slug[:60]
    digest = hashlib.md5(value.encode("utf-8")).hexdigest()[:10]
    return f"cn-tool-{digest}"


def _unique_item_id(prefix: str, slug: str, used: set[str]) -> str:
    base = f"{prefix}-{slug}"
    candidate = base
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def _tool_profile(tool: str, scenario: str, category_id: str) -> tuple[str, str, str]:
    value = tool.lower()
    rules = [
        (("豆包", "kimi", "deepseek", "通义", "glm", "智谱", "腾讯元宝", "讯飞星火", "文小言"), "做中文问答、写作和多模态处理", "中文大模型助手", "用于日常问答、资料理解、写作、推理或多模态输入，是中文工作流的模型底座。"),
        (("秘塔", "纳米", "skywork", "天工", "deep research"), "检索资料并生成研究内容", "AI 搜索和研究", "负责联网检索、多源资料整理、脑图、报告初稿或引用线索，适合研究报告和内容选题。"),
        (("wps", "aippt", "slides", "百度文库"), "生成办公文档和演示稿", "办公交付", "把资料、提纲或模板转成 Word、PPT、表格、汇报稿等可交付文件。"),
        (("飞书", "lark", "aily", "skillhub"), "沉淀企业知识和协作流程", "企业协作和知识库", "连接消息、文档、会议、任务和多维表格，让团队知识可以被整理、分析和复用。"),
        (("钉钉", "宜搭"), "搭建企业流程和自动化办公", "企业办公自动化", "把消息、文档、审批、表格和业务应用连接起来，适合组织内部流程和报表自动化。"),
        (("扣子", "coze", "agent"), "编排智能体和业务自动化", "Agent 编排", "通过可视化节点、插件、知识库和模型调用构建客服、运营、问答或内部助手。"),
        (("即梦", "可灵", "海螺", "seedance", "vidu", "skyreels", "剪映"), "生成和剪辑短视频内容", "视频生成和剪辑", "覆盖脚本、分镜、图生视频、字幕、口播和成片包装，适合短视频和直播素材生产。"),
        (("万相", "美图", "稿定", "canva", "创客贴"), "生成视觉素材和营销设计", "图像设计", "用于商品图、海报、封面、配图、品牌视觉和营销素材制作。"),
        (("trae", "codebuddy", "marscode", "灵码", "codegeex", "文心快码", "openclaw", "confucius"), "完成代码生成、审查和研发自动化", "AI 编程", "用于 IDE 编码、代码理解、任务调度、审查、部署或私有仓库开发。"),
        (("fastgpt", "ragflow", "maxkb", "dify", "qwen"), "搭建知识库和 RAG 问答", "知识库和 RAG", "负责文档解析、检索问答、工作流编排和 API 接入，适合企业 FAQ、客服和内部知识库。"),
        (("n8n", "api", "飞书机器人", "钉钉机器人"), "连接系统并自动执行任务", "自动化集成", "用于定时触发、跨系统连接、消息推送和批量处理，把 AI 判断接到真实业务流程。"),
        (("excel", "power bi", "金山表单", "多维表格"), "分析表格和业务数据", "数据分析", "用于清洗表格、生成图表、汇总销售/财务/运营数据并输出洞察。"),
        (("法大大", "e签宝", "合同", "法务"), "处理合同审查和签署", "法律合同", "用于合同模板、条款检查、签署、归档和风险提示。"),
    ]
    for keywords, action, label, detail in rules:
        if any(keyword in tool or keyword in value for keyword in keywords):
            return action, label, detail
    fallback = {
        "通用助手": ("做中文 AI 助手任务", "中文 AI 助手", "用于问答、写作、总结、资料处理或多模态输入。"),
        "研究报告": ("整理资料并生成研究报告", "研究分析", "用于资料检索、长文阅读、结构化摘要和报告成稿。"),
        "PPT/办公": ("生成办公交付物", "办公自动化", "用于文档、表格、PPT、会议纪要或模板化材料。"),
        "内容写作": ("生成内容和运营素材", "内容创作", "用于选题、文案、文章、脚本、封面或发布素材。"),
        "视频生成": ("生成视频素材", "视频生成", "用于脚本、分镜、图生视频、字幕或短视频成片。"),
        "图像设计": ("制作图像和视觉设计", "图像设计", "用于海报、商品图、封面、配图和品牌视觉。"),
        "AI 编程": ("完成代码和研发任务", "AI 编程", "用于代码生成、理解、修改、审查或部署。"),
        "知识库/RAG": ("搭建知识库问答", "知识库和 RAG", "用于文档解析、检索、问答和内部知识沉淀。"),
        "自动化": ("编排自动化流程", "自动化工作流", "用于定时任务、跨系统连接、批处理和消息推送。"),
    }
    return fallback.get(scenario, ("完成具体业务任务", "AI 工作流", "用于把资料、模型和业务系统连接成可交付结果。"))


def _skill_description(tool: str, scenario: str, workflow: str) -> str:
    action, label, detail = _tool_profile(tool, scenario, "")
    return f"{tool} 主要用于{label}。{detail}在这个组合里，它的作用是{action}；对应流程是：{workflow}"


def china_tool_skill_items() -> list[dict]:
    items: list[dict] = []
    seen: set[tuple[str, str]] = set()
    used_ids: set[str] = set()
    for item in CHINA_AI_TOOL_SKILLS:
        tool = item["tool"]
        action, _, _ = _tool_profile(tool, item["scenario"], item["category_id"])
        name = f"用 {tool} {action}"
        key = (tool.lower(), item["category_id"])
        if key in seen:
            continue
        seen.add(key)
        tags = list(dict.fromkeys([_slugify(tool), "china-ai", *item.get("tags", [])]))[:8]
        skill_id = _unique_item_id("china-tool", _slugify(tool), used_ids)
        items.append({
            "id": skill_id,
            "name": name,
            "category_id": item["category_id"],
            "category_label": item["category_label"],
            "tool": tool,
            "stage": "workflow",
            "description": _skill_description(tool, item["scenario"], item.get("workflow", "")),
            "tags": tags,
            "examples": [item.get("example", "中国 AI 工具组合")],
            "input_types": ["text", "file", "prompt"],
            "output_types": ["workflow", "draft", "asset"],
            "difficulty": 2,
            "importance": 64,
            "is_core": False,
            "is_active": True,
        })
    return items


def china_library_items() -> list[dict]:
    items: list[dict] = []
    used_ids: set[str] = set()
    for item in CHINA_AI_WORKFLOWS:
        workflow_id = _unique_item_id("workflow-china", item["id_slug"], used_ids)
        combo_id = _unique_item_id("combo-china", item["id_slug"], used_ids)
        common = {
            "category_id": item["category_id"],
            "category_label": item["category_label"],
            "tools": item["tools"],
            "tags": item["tags"],
            "source_section": CHINA_AI_SOURCE,
            "importance": item["importance"],
            "is_active": True,
        }
        combo_summary = f"中国 AI 工具组合：{item['title']}。适合{item['audience']}，工具链：{' + '.join(item['tools'])}。"
        items.append({
            "id": combo_id,
            "item_type": "combination",
            "title": item["title"],
            "summary": combo_summary,
            "steps": [],
            "outputs": [item["audience"]],
            **common,
        })
        items.append({
            "id": workflow_id,
            "item_type": "workflow",
            "title": item["title"],
            "summary": item["summary"],
            "steps": item["steps"],
            "outputs": item["outputs"],
            **common,
        })
    return items
