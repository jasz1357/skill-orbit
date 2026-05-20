import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// ---------------- theme system ----------------
// Two distinct visual worlds, each with isolated data:
//   ORBIT  — cosmic night, dark Earth + city lights, satellite-tracking aesthetic
//   BLOOM  — warm dawn, pastel garden moon, drifting pollen, watercolor aesthetic
const THEMES = {
  orbit: {
    label: 'ORBIT',
    cnLabel: '工作',
    brandName: 'AI Skill & Orbit',
    tagline: 'A LIVING MAP OF AI CAPABILITIES',
    defaultRings: [
      { id:'models-general-assistants',      mainId:'ai-models',   label:'GENERAL AI',       labelCn:'通用助手',       color:'#ffb066', r:1.32, tilt:[ 0.24, 0.10, 0.04], speed:0.064 },
      { id:'models-reasoning-long-context',  mainId:'ai-models',   label:'REASONING',        labelCn:'长文推理',       color:'#ffc47d', r:1.42, tilt:[ 0.32, 0.03, 0.12], speed:0.057 },
      { id:'models-chinese-ecosystem',       mainId:'ai-models',   label:'CHINESE MODELS',   labelCn:'中文模型',       color:'#ffd28f', r:1.52, tilt:[ 0.18, 0.18,-0.06], speed:0.051 },
      { id:'models-local-open-source',       mainId:'ai-models',   label:'LOCAL MODELS',     labelCn:'本地模型',       color:'#ffdfaa', r:1.62, tilt:[ 0.38,-0.05, 0.09], speed:0.046 },

      { id:'coding-app-prototype',           mainId:'ai-coding',   label:'APP PROTOTYPE',    labelCn:'应用原型',       color:'#7ed6e6', r:1.76, tilt:[-0.38, 0.34, 0.12], speed:0.041 },
      { id:'coding-code-edit-review',        mainId:'ai-coding',   label:'CODE REVIEW',      labelCn:'代码生成审查',   color:'#8ce2f0', r:1.86, tilt:[-0.46, 0.24, 0.22], speed:0.038 },
      { id:'coding-devops-testing',          mainId:'ai-coding',   label:'DEVOPS QA',        labelCn:'部署测试',       color:'#a2e8f4', r:1.96, tilt:[-0.26, 0.42,-0.02], speed:0.035 },
      { id:'coding-data-backend',            mainId:'ai-coding',   label:'BACKEND API',      labelCn:'后端数据',       color:'#b8eef7', r:2.06, tilt:[-0.54, 0.16,-0.12], speed:0.032 },

      { id:'visual-image-generation',        mainId:'ai-visual',   label:'IMAGE EDIT',       labelCn:'图像生成修图',   color:'#e69aa3', r:2.20, tilt:[ 0.62,-0.22, 0.10], speed:0.030 },
      { id:'visual-brand-design',            mainId:'ai-visual',   label:'BRAND DESIGN',     labelCn:'品牌设计',       color:'#eda8b1', r:2.30, tilt:[ 0.52,-0.34, 0.18], speed:0.028 },
      { id:'visual-ui-prototype',            mainId:'ai-visual',   label:'UI MOCKUP',        labelCn:'UI 产品稿',      color:'#f0b5bd', r:2.40, tilt:[ 0.74,-0.12,-0.04], speed:0.026 },
      { id:'visual-3d-assets',               mainId:'ai-visual',   label:'3D ASSETS',        labelCn:'3D 资产',        color:'#f5c2c9', r:2.50, tilt:[ 0.44,-0.42, 0.04], speed:0.024 },

      { id:'media-video-editing',            mainId:'ai-media',    label:'VIDEO EDIT',       labelCn:'视频生成剪辑',   color:'#b99cff', r:2.64, tilt:[-0.70,-0.10,-0.15], speed:0.023 },
      { id:'media-audio-voice-music',        mainId:'ai-media',    label:'AUDIO VOICE',      labelCn:'音频语音',       color:'#c5aaff', r:2.74, tilt:[-0.58,-0.24,-0.04], speed:0.021 },
      { id:'media-avatar-livestream',        mainId:'ai-media',    label:'AVATAR LIVE',      labelCn:'数字人直播',     color:'#d1b8ff', r:2.84, tilt:[-0.78, 0.02,-0.22], speed:0.020 },
      { id:'media-social-publishing',        mainId:'ai-media',    label:'SOCIAL PUBLISH',   labelCn:'社媒发布',       color:'#dcc8ff', r:2.94, tilt:[-0.50,-0.36, 0.10], speed:0.019 },

      { id:'office-ppt-decks',               mainId:'ai-office',   label:'PPT DECKS',        labelCn:'PPT 汇报',       color:'#ffe27a', r:3.08, tilt:[ 0.14, 0.52,-0.08], speed:0.018 },
      { id:'office-doc-writing',             mainId:'ai-office',   label:'DOC WRITING',      labelCn:'文档写作',       color:'#ffea96', r:3.18, tilt:[ 0.26, 0.42, 0.08], speed:0.017 },
      { id:'office-sheets-data',             mainId:'ai-office',   label:'SHEETS DATA',      labelCn:'表格数据',       color:'#fff0ad', r:3.28, tilt:[ 0.02, 0.62,-0.16], speed:0.016 },
      { id:'office-meetings-knowledge',      mainId:'ai-office',   label:'MEETING NOTES',    labelCn:'会议知识',       color:'#fff5c2', r:3.38, tilt:[ 0.34, 0.30, 0.14], speed:0.015 },

      { id:'research-web-search',            mainId:'ai-research', label:'SOURCE SEARCH',    labelCn:'来源核查',       color:'#91e6a7', r:3.52, tilt:[-0.18,-0.46, 0.18], speed:0.014 },
      { id:'research-academic-literature',   mainId:'ai-research', label:'PAPERS',           labelCn:'论文文献',       color:'#a3ebb5', r:3.62, tilt:[-0.30,-0.36, 0.04], speed:0.013 },
      { id:'research-market-competitive',    mainId:'ai-research', label:'MARKET INTEL',     labelCn:'市场竞品',       color:'#b6f0c4', r:3.72, tilt:[-0.06,-0.56, 0.26], speed:0.012 },
      { id:'research-data-reports',          mainId:'ai-research', label:'DATA REPORTS',     labelCn:'数据报告',       color:'#c8f5d2', r:3.82, tilt:[-0.36,-0.24, 0.16], speed:0.011 },

      { id:'agent-workflow-automation',      mainId:'ai-agent',    label:'WORKFLOW AUTO',    labelCn:'工作流自动化',   color:'#ff8ed1', r:3.96, tilt:[ 0.78, 0.22,-0.18], speed:0.0105 },
      { id:'agent-browser-task',             mainId:'ai-agent',    label:'BROWSER AGENT',    labelCn:'浏览器任务',     color:'#ff9ed9', r:4.06, tilt:[ 0.66, 0.34,-0.06], speed:0.0100 },
      { id:'agent-bots-rag',                 mainId:'ai-agent',    label:'BOT RAG',          labelCn:'Bot 与 RAG',     color:'#ffafe1', r:4.16, tilt:[ 0.88, 0.08,-0.26], speed:0.0095 },
      { id:'agent-api-mcp-integrations',     mainId:'ai-agent',    label:'API MCP',          labelCn:'API 与 MCP',     color:'#ffc0e8', r:4.26, tilt:[ 0.58, 0.44, 0.02], speed:0.0090 },

      { id:'business-marketing-growth',      mainId:'ai-business', label:'MARKETING SEO',    labelCn:'营销增长',       color:'#9fb7ff', r:4.40, tilt:[-0.58, 0.58, 0.22], speed:0.0086 },
      { id:'business-sales-crm',             mainId:'ai-business', label:'SALES CRM',        labelCn:'销售 CRM',       color:'#aec3ff', r:4.50, tilt:[-0.70, 0.44, 0.10], speed:0.0082 },
      { id:'business-support-community',     mainId:'ai-business', label:'SUPPORT',          labelCn:'客服社群',       color:'#bdceff', r:4.60, tilt:[-0.46, 0.68, 0.30], speed:0.0078 },
      { id:'business-ops-finance-legal',     mainId:'ai-business', label:'OPS LEGAL',        labelCn:'运营法务',       color:'#ccd9ff', r:4.70, tilt:[-0.76, 0.34, 0.24], speed:0.0074 },
      { id:'business-ecommerce-product',     mainId:'ai-business', label:'ECOM PRODUCT',     labelCn:'电商产品',       color:'#dbe4ff', r:4.80, tilt:[-0.50, 0.76, 0.12], speed:0.0070 },
    ],
  },
  bloom: {
    label: 'BLOOM',
    cnLabel: '生活',
    brandName: 'Ember & Forge',
    tagline: 'A LOG OF LIFE OFF THE GRID',
    defaultRings: [
      { id:'forge', label:'FORGE', labelCn:'创造', color:'#ff7a30', r:1.55, tilt:[ 0.20, 0.08, 0.06], speed:0.055 },
      { id:'rest',  label:'REST',  labelCn:'休息', color:'#7ed6e6', r:1.95, tilt:[-0.45, 0.30, 0.18], speed:0.038 },
      { id:'kin',   label:'KIN',   labelCn:'关系', color:'#e88a96', r:2.40, tilt:[ 0.70,-0.25, 0.08], speed:0.026 },
    ],
  },
};

const AI_MAIN_CATEGORIES = [
  { id:'ai-models', label:'AI MODELS', labelCn:'AI 模型', color:'#ffb066' },
  { id:'ai-coding', label:'AI CODING', labelCn:'AI 编程', color:'#7ed6e6' },
  { id:'ai-visual', label:'AI VISUAL', labelCn:'AI 视觉', color:'#e69aa3' },
  { id:'ai-media', label:'AI MEDIA', labelCn:'AI 媒体', color:'#b99cff' },
  { id:'ai-office', label:'AI OFFICE', labelCn:'AI 办公', color:'#ffe27a' },
  { id:'ai-research', label:'AI RESEARCH', labelCn:'AI 研究', color:'#91e6a7' },
  { id:'ai-agent', label:'AI AGENT', labelCn:'AI 智能体', color:'#ff8ed1' },
  { id:'ai-business', label:'AI BUSINESS', labelCn:'AI 商业', color:'#9fb7ff' },
];

let currentTheme = (() => {
  try{ return localStorage.getItem('skill-current-theme') || 'orbit'; }
  catch(e){ return 'orbit'; }
})();

let currentLang = (() => {
  try{ return localStorage.getItem('skill-orbit-lang') || 'en'; }
  catch(e){ return 'en'; }
})();

const I18N = {
  en: {
    brand: 'Skill & Orbit',
    tagline: 'A PERSONAL UNIVERSE OF SKILLS',
    orbit: 'ORBIT',
    bloom: 'BLOOM',
    work: 'Work',
    life: 'Life',
    langToggle: '中文',
    lat: 'LAT',
    lon: 'LON',
    scrollHelp: 'SCROLL · DRAG · HOVER',
    spaceHelpPrefix: 'SPACE ',
    pause: 'PAUSE',
    clickCategory: ' · CLICK CATEGORY ',
    solo: 'SOLO',
    paused: 'PAUSED',
    spaceToResume: 'SPACE TO RESUME',
    memoryArchive: 'MEMORY ARCHIVE',
    total: 'TOTAL',
    newCategory: '+ NEW CATEGORY',
    categoryPlaceholder: 'Category name (e.g. ART)',
    knowledgeBase: 'KNOWLEDGE BASE',
    dbEntryTitle: 'AI SKILL DATABASE',
    dbEntryDesc: 'Full library for search, future updates, and AI combinations.',
    recentNodes: 'RECENT NODES',
    searchNodes: 'Search nodes...',
    noMatchingNodes: 'No matching nodes',
    dbTitle: 'AI SKILL DATABASE',
    dbSub: 'Complete AI skill library and workflow stacks from the guide. Core skills appear as orbit nodes.',
    skills: 'SKILLS',
    skill: 'SKILL',
    stacks: 'WORKFLOW STACKS',
    integration: 'INTEGRATION',
    combo: 'INTEGRATION',
    workflow: 'WORKFLOW',
    searchSkills: 'Search all AI skills...',
    searchStacks: 'Search workflow stacks...',
    searchCombos: 'Search workflow stacks...',
    searchWorkflows: 'Search workflow stacks...',
    loadingDatabase: 'LOADING DATABASE',
    noMatchingSkills: 'NO MATCHING AI SKILLS',
    core: 'CORE',
    tool: 'TOOL',
    stage: 'STAGE',
    aiLibrary: 'AI LIBRARY',
    noMatchingType: type => type === 'stacks' ? 'NO MATCHING WORKFLOW STACKS' : `NO MATCHING ${type.toUpperCase()} ITEMS`,
    startBackend: 'START BACKEND TO LOAD DATABASE',
    login: 'LOG IN',
    register: 'REGISTER',
    logout: 'LOG OUT',
    username: 'USERNAME',
    email: 'EMAIL',
    password: 'PASSWORD',
    authRegisterHint: 'Create an account to save personal archive and node changes.',
    authLoginHint: 'Use admin / admin123, or your registered account.',
    authFullService: 'Please log in to enjoy full service.',
    authDbRequired: 'Please login or register new account.',
    creatingAccount: 'Creating account...',
    loggingIn: 'Logging in...',
    memoryNode: 'MEMORY · NODE',
    howUse: 'HOW I USE IT',
    notePlaceholder: "How you understand this skill, where you've used it, what tripped you up, where to go next...",
    autosaved: 'Auto-saved',
    escToClose: 'to close',
    deleteNode: 'DELETE NODE',
    confirmDeleteNode: 'Are you sure you want to delete? This cannot be recovered.',
    confirmDeleteArchive: 'Are you sure you want to delete? All nodes in this category will also be deleted.',
    confirmCancel: 'CANCEL',
    confirmDelete: 'DELETE',
    keepOneCategory: 'Keep at least one archive.',
    assistant: 'ORBITAL · ASSISTANT',
    system: 'SYSTEM',
    chatIntro: 'Ask for an AI task and I will search the skill database.',
    bloomChatIntro: 'Tell me what you learned or did today, and I will sort it into your life archive.',
    chatPlaceholder: 'I want to make a PPT today...',
    bloomChatPlaceholder: 'I learned how to cook braised ribs...',
    memoryNodeHead: 'MEMORY NODE',
    parsing: 'parsing',
    foundSkills: count => `I found ${count} AI skill${count > 1 ? 's' : ''} in the database.`,
    foundRecommendations: count => `You need these ${count} related AI workflow stack${count > 1 ? 's' : ''}:`,
    foundPlans: count => `I recommend these ${count} plan${count > 1 ? 's' : ''}:`,
    bestFor: 'Best for',
    needs: 'Needs',
    outputs: 'Outputs',
    noDirectMatch: 'No direct database match yet. Try a broader tool or task keyword.',
    loggedOrbit: 'Logged to the orbit.',
    loggedMemoryOrbit: 'Logged to the memory orbit.',
    addNodeLabel: '+1 NODE',
  },
  zh: {
    brand: '技能星球',
    tagline: '你的 AI 技能宇宙',
    orbit: '星轨',
    bloom: '绽放',
    work: '工作',
    life: '生活',
    langToggle: 'EN',
    lat: '纬度',
    lon: '经度',
    scrollHelp: '滚动 · 拖拽 · 悬停',
    spaceHelpPrefix: '空格 ',
    pause: '暂停',
    clickCategory: ' · 点击分类 ',
    solo: '聚焦',
    paused: '已暂停',
    spaceToResume: '按空格继续',
    memoryArchive: '技能档案',
    total: '总数',
    newCategory: '+ 新建分类',
    categoryPlaceholder: '分类名称，例如：AI 办公',
    knowledgeBase: '知识库',
    dbEntryTitle: 'AI 技能数据库',
    dbEntryDesc: '用于搜索、后续更新和 AI 技能组合的完整资料库。',
    recentNodes: '最近节点',
    searchNodes: '搜索节点...',
    noMatchingNodes: '没有匹配节点',
    dbTitle: 'AI 技能数据库',
    dbSub: '来自指南的完整 AI 技能库和工作流栈。核心技能会显示在星球轨道上。',
    skills: '技能',
    skill: '技能',
    stacks: '工作流栈',
    integration: '工具组合',
    combo: '工具组合',
    workflow: '工作流',
    searchSkills: '搜索所有 AI 技能...',
    searchStacks: '搜索工作流栈...',
    searchCombos: '搜索工作流栈...',
    searchWorkflows: '搜索工作流栈...',
    loadingDatabase: '正在加载数据库',
    noMatchingSkills: '没有匹配的 AI 技能',
    core: '核心',
    tool: '工具',
    stage: '阶段',
    aiLibrary: 'AI 资料库',
    noMatchingType: type => type === 'stacks' ? '没有匹配的工作流栈' : '没有匹配项目',
    startBackend: '请先启动后端以加载数据库',
    login: '登录',
    register: '注册',
    logout: '退出',
    username: '用户名',
    email: '邮箱',
    password: '密码',
    authRegisterHint: '创建账户后可以保存个人档案和节点修改。',
    authLoginHint: '可使用 admin / admin123，或你注册的账户。',
    authFullService: 'Please log in to enjoy full service.',
    authDbRequired: 'Please login or register new account.',
    creatingAccount: '正在创建账户...',
    loggingIn: '正在登录...',
    memoryNode: '记忆 · 节点',
    howUse: '我如何使用它',
    notePlaceholder: '你如何理解这个技能、在哪里用过、遇到什么问题、下一步想怎么做...',
    autosaved: '自动保存',
    escToClose: '关闭',
    deleteNode: '删除节点',
    confirmDeleteNode: '是否确定删除？删除后无法恢复。',
    confirmDeleteArchive: '是否确定删除？删除后本分类中的所有 node 都会一起删除。',
    confirmCancel: '取消',
    confirmDelete: '删除',
    keepOneCategory: '至少保留一个分类。',
    assistant: '轨道 · 助手',
    system: '系统',
    chatIntro: '告诉我你想完成的 AI 任务，我会搜索技能数据库。',
    bloomChatIntro: '告诉我你今天学会了什么或完成了什么，我会自动分类成生活 note。',
    chatPlaceholder: '我今天想做一个 PPT...',
    bloomChatPlaceholder: '我学会了做红烧排骨...',
    memoryNodeHead: '技能节点',
    parsing: '解析中',
    foundSkills: count => `我在数据库里找到了 ${count} 个相关 AI 技能。`,
    foundRecommendations: count => `你需要这些 ${count} 个相关 AI 工作流组合：`,
    foundPlans: count => `我推荐这 ${count} 个方案：`,
    bestFor: '适合',
    needs: '需要',
    outputs: '产出',
    noDirectMatch: '暂时没有直接匹配。可以试试更宽泛的工具或任务关键词。',
    loggedOrbit: '已记录到技能星轨。',
    loggedMemoryOrbit: '已记录到技能星轨。',
    addNodeLabel: '+1 节点',
  }
};

function t(key, ...args){
  const value = I18N[currentLang]?.[key] ?? I18N.en[key] ?? key;
  return typeof value === 'function' ? value(...args) : value;
}

const CATEGORY_LABEL_ZH = {
  'AI MODELS': 'AI 模型',
  'AI CODING': 'AI 编程',
  'AI VISUAL': 'AI 视觉',
  'AI MEDIA': 'AI 媒体',
  'AI OFFICE': 'AI 办公',
  'AI RESEARCH': 'AI 研究',
  'AI AGENT': 'AI 智能体',
  'AI BUSINESS': 'AI 商业',
  'AI-MODELS': 'AI 模型',
  'AI-CODING': 'AI 编程',
  'AI-VISUAL': 'AI 视觉',
  'AI-MEDIA': 'AI 媒体',
  'AI-OFFICE': 'AI 办公',
  'AI-RESEARCH': 'AI 研究',
  'AI-AGENT': 'AI 智能体',
  'AI-BUSINESS': 'AI 商业',
  FORGE: '创造',
  REST: '休息',
  KIN: '关系',
};

const SKILL_ZH = {
  '用 Claude 做复杂推理与长文写作': '用 Claude 做复杂推理与长文写作',
  '用 ChatGPT 做通用问答与任务规划': '用 ChatGPT 做通用问答与任务规划',
  '用 Gemini 处理长上下文和 Google Workspace': '用 Gemini 处理长上下文和 Google Workspace',
};

const TERM_ZH = {
  TOOL: '工具',
  STAGE: '阶段',
  CORE: '核心',
  PDF: 'PDF',
  combination: '组合',
  workflow: '工作流',
  skills: '技能',
  'AI LIBRARY': 'AI 资料库',
  '2026_AI_工具实战指南 · Combination': '2026 AI 工具实战指南 · 技能组合',
  '2026_AI_工具实战指南 · 项目工作流': '2026 AI 工具实战指南 · 项目工作流',
  'Project workflow from the PDF guide. Use it as a reusable plan for AI skill combinations.': '来自 PDF 指南的项目工作流，可作为 AI 技能组合的可复用执行方案。',
  'Analyze data, generate narrative insight, and present it as a deck.': '分析数据，生成叙事洞察，并整理成演示文稿。',
  'Package SOPs as skills and connect them to tools through MCP.': '把 SOP 封装成技能，并通过 MCP 连接外部工具。',
  'Use hooks and subagents for more controlled software development workflows.': '使用 hooks 和 subagents，让软件开发工作流更可控。',
  'Create an IM bot that summarizes, extracts, OCRs, and routes tasks.': '创建一个能总结、提取、OCR 并分发任务的即时通讯 Bot。',
  'Build a bot and connect it to team knowledge bases.': '搭建 Bot，并连接团队知识库。',
  'Build a product and add analytics plus error monitoring.': '构建产品，并加入数据分析与错误监控。',
  'Generate polished React UI components with a consistent design system.': '生成风格统一、完成度更高的 React UI 组件。',
  'Research keywords, build SEO briefs, and draft optimized content.': '研究关键词，生成 SEO brief，并撰写优化内容。',
  'Find papers, compare claims, and inspect citation reliability.': '查找论文、比较观点，并检查引用可靠性。',
  'Organize references and generate grounded literature review notes.': '整理文献，并生成有来源依据的综述笔记。',
};

function displayCategoryLabel(labelOrId){
  if(currentLang !== 'zh') return labelOrId || '';
  return CATEGORY_LABEL_ZH[labelOrId] || CATEGORY_LABEL_ZH[String(labelOrId || '').toUpperCase()] || labelOrId || '';
}

function translateText(value){
  if(currentLang !== 'zh') return value || '';
  if(!value) return '';
  return TERM_ZH[value] || SKILL_ZH[value] || value;
}

function hasCjk(value){
  return /[\u3400-\u9fff]/.test(String(value || ''));
}

function titleCaseToken(token){
  const keep = {
    ai: 'AI', api: 'API', ui: 'UI', ide: 'IDE', pdf: 'PDF', ppt: 'PPT', crm: 'CRM',
    seo: 'SEO', bgm: 'BGM', pr: 'PR', rag: 'RAG', mcp: 'MCP', saas: 'SaaS',
    gpt: 'GPT', glm: 'GLM', qwen: 'Qwen', kimi: 'Kimi',
  };
  const key = token.toLowerCase();
  if(keep[key]) return keep[key];
  return token.charAt(0).toUpperCase() + token.slice(1);
}

function titleFromSlug(slug){
  return String(slug || '')
    .replace(/^(combo|workflow)-aiw100-/, '')
    .replace(/^combo-|^workflow-/, '')
    .replace(/^aiw100-/, '')
    .replace(/^\d{3}-/, '')
    .split('-')
    .filter(Boolean)
    .map(titleCaseToken)
    .join(' ');
}

const CHINA_TOOL_NAMES_EN = {
  '豆包': 'Doubao',
  '豆包 Pro': 'Doubao Pro',
  '豆包语音': 'Doubao Voice',
  '豆包图片': 'Doubao Image',
  '豆包模型': 'Doubao model',
  '腾讯元宝': 'Tencent Yuanbao',
  '讯飞星火': 'iFlytek Spark',
  '星火': 'iFlytek Spark',
  '通义': 'Qwen',
  '通义千问': 'Qwen',
  '通义万相': 'Tongyi Wanxiang',
  '通义听悟': 'Tingwu',
  '通义灵码': 'Tongyi Lingma',
  '通义 AI': 'Qwen AI',
  '通义 AI 助理': 'Qwen AI Assistant',
  '文小言': 'Wenxiaoyan',
  '百度文库 AI': 'Baidu Wenku AI',
  '百度文库': 'Baidu Wenku',
  '智谱清言': 'Zhipu Qingyan',
  '飞书': 'Feishu',
  '飞书 aily': 'Feishu aily',
  '飞书知识库': 'Feishu Knowledge Base',
  '飞书多维表格': 'Feishu Base',
  '飞书多维表格 Agent': 'Feishu Base Agent',
  '飞书妙搭': 'Feishu App Builder',
  '飞书文档': 'Feishu Docs',
  '飞书 CLI': 'Feishu CLI',
  'OpenClaw 插件': 'OpenClaw plugin',
  '钉钉': 'DingTalk',
  '钉钉 AI 助理': 'DingTalk AI Assistant',
  '钉钉多维表格': 'DingTalk Base',
  '钉钉知识库': 'DingTalk Knowledge Base',
  '钉钉酷应用': 'DingTalk Cool App',
  '钉钉会议': 'DingTalk Meetings',
  '宜搭': 'Yida',
  '秘塔': 'Metaso',
  '秘塔 AI 搜索': 'Metaso AI Search',
  '纳米': 'Nami',
  '纳米 AI 搜索': 'Nami AI Search',
  '天工': 'Skywork',
  '天工 Skywork': 'Skywork',
  '天工表格': 'Skywork Sheets',
  '即梦': 'Jimeng',
  '即梦素材': 'Jimeng assets',
  '可灵': 'Kling',
  '可灵 AI': 'Kling AI',
  '海螺 AI': 'Hailuo AI',
  '小云雀': 'Xiaoyunque',
  '剪映': 'Jianying',
  '扣子': 'Coze CN',
  '扣子工作流': 'Coze Workflow',
  '扣子 Agent Skills': 'Coze Agent Skills',
  '扣子 Agent Plan': 'Coze Agent Plan',
  '扣子 Agent Coding': 'Coze Agent Coding',
  '扣子视频 Agent': 'Coze Video Agent',
  '小红书': 'Xiaohongshu',
  '微信公众号': 'WeChat Official Account',
  '公众号素材': 'WeChat article assets',
  '抖音': 'Douyin',
  '火山引擎': 'Volcengine',
  '火山方舟': 'Volcengine Ark',
  '美图设计室': 'Meitu Design Studio',
  '创客贴': 'Chuangkit',
  '可画': 'Canva China',
  '稿定 AI': 'Gaoding AI',
  '百度 AI 修图': 'Baidu AI Retouch',
  '文心快码': 'Baidu Comate',
  '阿里云': 'Alibaba Cloud',
  '百度智能云': 'Baidu AI Cloud',
  '巨量引擎': 'Ocean Engine',
  '企业微信': 'WeCom',
  '企业微信机器人': 'WeCom Bot',
  '微信收藏': 'WeChat Favorites',
  '微信资料': 'WeChat materials',
  '微信私域': 'WeChat private traffic',
  '企业制度库': 'company policy library',
  '销售表格': 'sales spreadsheet',
  '销售资料库': 'sales knowledge base',
  '报价工具': 'quotation tool',
  '竞品资料': 'competitor materials',
  '客户访谈': 'customer interviews',
  '淘宝素材': 'Taobao assets',
  '小红书资料': 'Xiaohongshu research',
  '本地模型': 'local models',
  '本地电脑': 'local computer',
  '法律检索技能': 'legal search skill',
  '合同助手': 'contract assistant',
  '定时任务': 'scheduled tasks',
  '飞书机器人': 'Feishu bot',
  '钉钉机器人': 'DingTalk bot',
};

const CHINA_SCENARIO_EN = {
  'PPT/提案': 'Proposal deck',
  '通用助手': 'General assistant',
  '研究报告': 'Research report',
  '研究': 'Research',
  '写作': 'Writing',
  '社媒': 'Social media',
  '编程': 'Coding',
  '数据': 'Data',
  '会议': 'Meetings',
  '设计': 'Design',
  '音视频': 'Audio and video',
  '商务': 'Business',
  '个人效率': 'Personal productivity',
  'PPT/办公': 'Presentations and office work',
  '飞书工作流': 'Feishu workflow',
  '钉钉工作流': 'DingTalk workflow',
  '扣子/Agent': 'Coze and agent workflow',
  '内容写作': 'Content writing',
  '视频生成': 'Video generation',
  '图像设计': 'Image design',
  'AI 编程': 'AI coding',
  '电商': 'E-commerce',
  '教育': 'Education',
  '财务/数据': 'Finance and data',
  '销售/CRM': 'Sales and CRM',
  '产品/需求': 'Product and requirements',
  '知识库/RAG': 'Knowledge base and RAG',
  '自动化': 'Automation',
  '本地/开源': 'Local and open-source stack',
  '法律/合同': 'Legal and contracts',
  '组合总栈': 'Full workflow stack',
};

const GUIDE_WORKFLOW_TITLES_EN = {
  '两周做一本可发布电子书': 'Publishable ebook in two weeks',
  '72 小时做一个 SaaS': 'Build a SaaS in 72 hours',
  '两周做原创歌曲 + MV': 'Original song and music video in two weeks',
  '新品全平台上线': 'Cross-platform product launch',
  '三个月做研究论文': 'Research paper in three months',
  'B2B SDR 外呼流水线': 'B2B SDR outbound pipeline',
  '每周 AI Newsletter': 'Weekly AI newsletter',
  '房产研究与谈判策略': 'Real-estate research and negotiation strategy',
  '四周拿到 3+ offer': 'Get three or more offers in four weeks',
  '公开数据到生物研究投稿': 'Public data to biology research submission',
  '合同从收件箱到签字归档': 'Contract intake, signing, and archive workflow',
  '五天做 Brand Identity': 'Brand identity in five days',
  '两周做可玩游戏 demo': 'Playable game demo in two weeks',
  '三周做公司深度研报': 'Company deep-dive report in three weeks',
  '客服 80% 工单 AI 自助解决': 'AI self-service for 80% of support tickets',
};

const CHINA_AUDIENCE_EN = {
  '咨询、销售、课程、融资路演': 'consulting, sales, course creation, and fundraising roadshows',
  '市场研究、行业报告转 PPT': 'market research and industry-report-to-PPT work',
  '内容团队、轻量品牌提案': 'content teams and lightweight brand proposals',
  '小团队快速出图出 deck': 'small teams that need quick visuals and decks',
  '产品概念、设计汇报': 'product concepts and design reviews',
  '学习型组织、课程制作': 'learning organizations and course production',
  '企业内部周报/月报': 'internal weekly and monthly reports',
  '客户成功、项目经理': 'customer success and project managers',
  '研究员、创作者、顾问': 'researchers, creators, and consultants',
  '深度报告、白皮书': 'deep reports and white papers',
  '个人知识管理': 'personal knowledge management',
  '团队研究沉淀': 'team research archives',
  '学术/培训资料整理': 'academic and training-material organization',
  '大公司知识检索': 'enterprise knowledge search',
  '法务、运营、项目 PM': 'legal, operations, and project-management teams',
  '科研、医学/政策研究': 'scientific, medical, and policy research',
  '论文写作、证据型内容': 'paper writing and evidence-based content',
  '趋势研究、社媒分析': 'trend research and social-media analysis',
  '全栈开发者': 'full-stack developers',
  '工程团队': 'engineering teams',
  '产品工程': 'product engineering',
  '复杂代码库': 'complex codebases',
  '供应链安全': 'supply-chain security',
  '产品研发闭环': 'product-development loops',
  '数据工程': 'data engineering',
  'SRE/DevOps': 'SRE and DevOps teams',
  '生产自动化': 'production automation',
  '产品/工程会议': 'product and engineering meetings',
  '销售团队': 'sales teams',
  '语音 agent 团队': 'voice-agent teams',
  '业务自动化': 'business automation',
  '企业 IT': 'enterprise IT',
  'AI 治理团队': 'AI governance teams',
  '创意工作室': 'creative studios',
  '短视频': 'short-video teams',
  '小企业财务': 'small-business finance',
  '单人创业者': 'one-person founders',
  '个人日常、学生、职场': 'individuals, students, and office workers',
  '技术用户、研究用户': 'technical and research users',
  '办公室用户': 'office users',
  '公众号、微信生态团队': 'WeChat content and ecosystem teams',
  '教育、培训': 'education and training teams',
  '行政、学生': 'administrative staff and students',
  '企业团队': 'enterprise teams',
  '报告型用户': 'report-heavy users',
  '内容运营': 'content operators',
  '研究、写作': 'research and writing work',
  '行业研究': 'industry research',
  '知识整理': 'knowledge organization',
  '咨询、学生': 'consultants and students',
  '微信生态研究': 'WeChat ecosystem research',
  '企业资料处理': 'enterprise document processing',
  '报告到 PPT': 'report-to-presentation workflows',
  '企业内部研究': 'internal enterprise research',
  '钉钉团队': 'DingTalk teams',
  '知识库运营': 'knowledge-base operations',
  '工作汇报': 'work reporting',
  '快速提案': 'fast proposals',
  '综合办公': 'general office workflows',
  '培训/路演': 'training and roadshows',
  '市场活动': 'marketing campaigns',
  '商务合同': 'business contracts',
  '运营周报': 'operations weekly reports',
  '销售管理': 'sales management',
  '会议复盘': 'meeting reviews',
  '行政材料': 'administrative materials',
  '团队管理': 'team management',
  '企业助手': 'enterprise assistants',
  '运营/数据': 'operations and data teams',
  '客服/咨询': 'customer support and consulting',
  '私域运营': 'private traffic operations',
  '抖音运营': 'Douyin operations',
  '轻 SaaS': 'lightweight SaaS projects',
  '法务助手': 'legal assistants',
  '自媒体增长': 'creator growth',
  '视频创作': 'video creators',
  '博客/内容站': 'blogs and content sites',
  '小红书运营': 'Xiaohongshu operations',
  '公众号作者': 'WeChat writers',
  '知识博主': 'knowledge creators',
  '企业文案': 'enterprise copywriting',
  '营销内容': 'marketing content',
  '媒体/访谈': 'media and interview workflows',
  '课程/培训': 'courses and training',
  '短视频': 'short-video workflows',
  '抖音/视频号': 'Douyin and Channels accounts',
  '产品经理': 'product managers',
  '企业知识库': 'enterprise knowledge bases',
  '开发者': 'developers',
  '中小企业': 'SMBs',
  '个人研究': 'personal research',
  '低成本自动化': 'low-cost automation',
  '企业 AI 工作流': 'enterprise AI workflows',
};

function englishToolName(value){
  const raw = String(value || '').trim();
  if(!raw) return '';
  const direct = CHINA_TOOL_NAMES_EN[raw];
  if(direct) return direct;
  if(raw.includes('+') || raw.includes('、') || raw.includes('，')){
    return raw
      .split(/\s*(?:\+|、|，|,)\s*/)
      .filter(Boolean)
      .map(englishToolName)
      .join(' + ');
  }
  if(!hasCjk(raw)) return raw;
  return titleFromSlug(raw.replace(/[^\w]+/g, '-')) || 'Chinese AI tool';
}

const CHINA_SCENARIO_PURPOSE_EN = {
  'PPT/提案': 'turn research, interviews, documents, and positioning into proposal decks or presentation materials',
  '通用助手': 'answer daily questions, draft short content, read long documents, and handle multimodal inputs',
  '研究报告': 'collect sources, read long material, structure findings, and turn research into usable reports',
  '研究': 'collect sources, verify evidence, structure findings, and turn them into reusable knowledge or reports',
  '写作': 'turn ideas and source material into drafts, polished copy, newsletters, scripts, or long-form writing',
  '社媒': 'monitor trends, create social posts or clips, schedule publishing, and review performance',
  '编程': 'plan, implement, review, test, and maintain software with AI coding tools',
  '数据': 'connect data systems, analyze incidents or metrics, and turn signals into decisions or actions',
  '会议': 'capture conversations, summarize decisions, and turn meeting notes into follow-up work',
  '设计': 'turn briefs into visual concepts, branded assets, designs, or creative production files',
  '音视频': 'turn scripts, updates, images, or voice inputs into audio and video deliverables',
  '商务': 'support sales, marketing, finance, support, and customer-facing business operations',
  '个人效率': 'capture personal context, organize tasks, preserve project memory, and automate solo work',
  'PPT/办公': 'convert documents, meetings, and business material into polished office deliverables',
  '飞书工作流': 'connect Feishu documents, knowledge bases, tables, and bots into team workflows',
  '钉钉工作流': 'connect DingTalk documents, meetings, knowledge bases, and internal apps into team workflows',
  '扣子/Agent': 'build agents that collect information, call tools, execute steps, and return structured results',
  '内容写作': 'plan topics, draft articles, refine copy, and adapt content for publishing channels',
  '视频生成': 'turn scripts, images, voice, and briefs into short videos or presentation-ready clips',
  '图像设计': 'create, retouch, and package visual assets for posts, ads, posters, and product pages',
  'AI 编程': 'move from requirements to code, review, debugging, deployment, and technical documentation',
  '电商': 'produce product copy, visual assets, customer replies, and operating reports for commerce teams',
  '教育': 'prepare lesson plans, course materials, tutoring content, and assessment support',
  '财务/数据': 'clean data, analyze tables, explain financial signals, and produce charts or reports',
  '销售/CRM': 'organize leads, prepare outreach, summarize customer needs, and support sales follow-up',
  '产品/需求': 'turn user feedback and business goals into requirements, prototypes, and delivery plans',
  '知识库/RAG': 'ingest internal documents, organize knowledge, and answer questions from trusted sources',
  '自动化': 'connect repetitive tasks, scheduled jobs, bots, and notifications into repeatable workflows',
  '本地/开源': 'run lower-cost or private AI workflows on local and open-source models',
  '法律/合同': 'search legal material, review clauses, compare contracts, and produce risk notes',
  '组合总栈': 'combine multiple Chinese AI tools into an end-to-end stack for a complete business scenario',
};

function chinaScenarioFromTitle(title){
  return String(title || '').split(/[：:]/)[0].trim();
}

function englishAudienceName(value){
  const raw = String(value || '').trim();
  if(!raw) return '';
  if(CHINA_AUDIENCE_EN[raw]) return CHINA_AUDIENCE_EN[raw];
  if(!hasCjk(raw)) return raw;
  return displayCategoryLabel(raw).toLowerCase();
}

function cleanGuideTitle(title){
  return String(title || '').replace(/^项目工作流\s*\d+\s*[：:]\s*/, '').trim();
}

function englishGuideTitle(title, fallbackId){
  const clean = cleanGuideTitle(title);
  if(GUIDE_WORKFLOW_TITLES_EN[clean]) return GUIDE_WORKFLOW_TITLES_EN[clean];
  return titleFromSlug(fallbackId || clean);
}

function englishExpandedTitle(title, fallbackId){
  const raw = String(title || '').trim();
  const parts = raw.split(/[：:]/);
  if(parts.length >= 2){
    const scenario = parts.shift().trim();
    const combo = parts.join(':').trim();
    const scenarioEn = CHINA_SCENARIO_EN[scenario] || titleFromSlug(scenario);
    return combo ? `${scenarioEn}: ${combo}` : scenarioEn;
  }
  return titleFromSlug(fallbackId || raw);
}

function englishChinaTitle(title, fallbackId){
  const raw = String(title || '').trim();
  const parts = raw.split(/[：:]/);
  if(parts.length >= 2){
    const scenario = parts.shift().trim();
    const toolText = parts.join(':').trim();
    const scenarioEn = CHINA_SCENARIO_EN[scenario] || titleFromSlug(scenario);
    const toolsEn = toolText
      .split(/\s*(?:\+|、|，|,|和|与)\s*/)
      .filter(Boolean)
      .map(englishToolName)
      .filter(Boolean)
      .join(' + ');
    return toolsEn ? `${scenarioEn}: ${toolsEn}` : scenarioEn;
  }
  return titleFromSlug(fallbackId || raw);
}

function englishDeliverableName(value){
  const raw = String(value || '').trim();
  if(!raw) return '';
  if(!hasCjk(raw)) return raw;
  if(/PPT|汇报|演示|deck/i.test(raw)) return 'presentation materials';
  if(/封面|海报|视觉|素材|产品图|配图|Logo/i.test(raw)) return 'visual assets';
  if(/短视频|MV|视频|宣传/i.test(raw)) return 'video assets';
  if(/论文|研报|报告|研究/i.test(raw)) return 'research report';
  if(/合同|签字|风险/i.test(raw)) return 'contract review and signing records';
  if(/客服|工单|Bot|知识库/i.test(raw)) return 'support knowledge base and bot workflow';
  if(/简历|offer|面试|薪资/i.test(raw)) return 'career application materials';
  if(/EPUB|电子书|有声/i.test(raw)) return 'ebook and publishing package';
  if(/数据库|登录|全栈|应用|SaaS/i.test(raw)) return 'full-stack application deliverable';
  if(/CRM|账户|外联|销售/i.test(raw)) return 'sales and CRM assets';
  return 'deliverable package';
}

function englishChinaStepAction(step, tool){
  const text = String(step || '');
  const actor = englishToolName(tool) || 'AI';
  if(/搜索|检索|资料|来源|联网/.test(text)) return `${actor} searches for sources, gathers references, and turns raw material into structured inputs`;
  if(/长PDF|合同|报告|长文|总结|阅读|读取/.test(text)) return `${actor} reads long documents and extracts the decisions, risks, or key points`;
  if(/PPT|幻灯|演示|路演|提案/.test(text)) return `${actor} converts the material into presentation-ready slides or proposal content`;
  if(/会议|转写|纪要|复盘/.test(text)) return `${actor} transcribes meetings and turns discussion into notes, summaries, and follow-up actions`;
  if(/知识库|RAG|问答|企业资料|制度库/.test(text)) return `${actor} organizes knowledge into a searchable base and answers questions against those materials`;
  if(/代码|编程|审查|部署|调试|接口/.test(text)) return `${actor} supports coding, review, debugging, integration, or deployment work`;
  if(/视频|剪辑|字幕|分镜|脚本/.test(text)) return `${actor} helps shape scripts, scenes, subtitles, and short-video production assets`;
  if(/图像|海报|视觉|素材|修图|封面|配图/.test(text)) return `${actor} creates or refines visual assets for publishing, marketing, or product pages`;
  if(/数据|表格|财务|图表|统计|周报/.test(text)) return `${actor} cleans tables, analyzes metrics, and turns data into reports or charts`;
  if(/客服|FAQ|回复|咨询|客户/.test(text)) return `${actor} drafts customer-facing answers, FAQs, and follow-up messages`;
  if(/文案|标题|文章|公众号|小红书|内容/.test(text)) return `${actor} plans, drafts, and adapts content for the target publishing channel`;
  if(/自动|机器人|定时|推送|同步/.test(text)) return `${actor} automates the repetitive handoff, notification, or synchronization step`;
  return `${actor} handles one concrete step in the workflow and passes structured output to the next tool`;
}

function stripCjk(value){
  return String(value || '')
    .replace(/[\u3400-\u9fff]+/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function englishAiw100StepAction(step){
  const raw = String(step || '').trim();
  if(!raw) return '';
  let text = raw;
  const replacements = [
    [/先把访谈\/资料整理成叙事大纲、页标题、每页要点/g, 'turns interviews and source material into a narrative outline, page titles, and slide-level points'],
    [/再做逻辑审稿和演讲稿/g, 'then reviews the logic and writes the speaker script'],
    [/深研收集市场\/竞品\/引用/g, 'runs deep research on the market, competitors, and citations'],
    [/输出结构化简报/g, 'outputs a structured brief'],
    [/变成演示文稿/g, 'turns it into a presentation'],
    [/人工补品牌视觉/g, 'adds brand visuals manually'],
    [/找带来源的信息/g, 'finds sourced information'],
    [/压成故事线/g, 'compresses it into a storyline'],
    [/套品牌模板生成图文页/g, 'applies brand templates to create visual pages'],
    [/沉淀定位、标语、页面结构/g, 'develops positioning, taglines, and page structure'],
    [/调用 Canva app/g, 'calls the Canva app'],
    [/直接生成宣传页或简报/g, 'directly generates a promo page or brief'],
    [/快速探索界面\/产品概念/g, 'quickly explores interface and product concepts'],
    [/导出到 Canva/g, 'exports to Canva'],
    [/再做视觉统一和版式整理/g, 'then standardizes visuals and layout'],
    [/汇总长资料和音视频/g, 'summarizes long documents and audio/video material'],
    [/提炼核心观点/g, 'extracts the core arguments'],
    [/生成培训\/分享 PPT/g, 'generates training or sharing slides'],
    [/读取 Drive 内文档/g, 'reads documents from Drive'],
    [/生成会议汇报结构/g, 'generates the meeting-report structure'],
    [/再用 Slides 或 Canva 做版式/g, 'then lays it out in Slides or Canva'],
    [/搜 Notion 项目资料/g, 'searches Notion project material'],
    [/生成客户化方案/g, 'generates a customized client proposal'],
    [/回写版本记录/g, 'writes version records back to Notion'],
    [/让代理先做网页调研和资料收集/g, 'lets agents perform web research and source collection first'],
    [/做去噪和观点排序/g, 'removes noise and ranks the arguments'],
    [/出简报/g, 'creates the brief'],
    [/从 Docs\/Sheets 摘要数据/g, 'summarizes data from Docs and Sheets'],
    [/生成视觉稿/g, 'generates visual drafts'],
    [/做文案润色/g, 'polishes the copy'],
    [/搜索并给来源/g, 'searches and provides sources'],
    [/长上下文吸收资料/g, 'absorbs source material with long-context reading'],
    [/输出框架、洞察、反方观点和结论/g, 'outputs the framework, insights, counterarguments, and conclusions'],
    [/先做广域多源研究/g, 'first performs broad multi-source research'],
    [/负责压缩、重排、写成更有人味的报告/g, 'compresses, restructures, and rewrites it into a more human report'],
    [/建引用清单/g, 'builds the citation list'],
    [/做问答\/表格/g, 'handles Q&A and tables'],
    [/保存知识库与复用模板/g, 'stores the knowledge base and reusable templates'],
    [/做长文档理解和推理/g, 'handles long-document understanding and reasoning'],
    [/把结果嵌入项目页、任务页、数据库/g, 'embeds the results into project pages, task pages, and databases'],
    [/处理私有资料/g, 'processes private source material'],
    [/补 Google 生态检索/g, 'adds Google-ecosystem search'],
    [/输出最终观点/g, 'outputs the final point of view'],
    [/从 SharePoint 找内部制度、历史报告、模板/g, 'finds internal policies, historical reports, and templates in SharePoint'],
    [/生成带出处的内部问答/g, 'generates internal Q&A with citations'],
    [/搜合同\/文档\/会议纪要/g, 'searches contracts, documents, and meeting notes'],
    [/比较版本差异并生成行动项/g, 'compares version differences and creates action items'],
    [/找现实资料/g, 'finds real-world sources'],
    [/找论文/g, 'finds papers'],
    [/做文献综述和研究假设/g, 'writes the literature review and research hypotheses'],
    [/生成问题树/g, 'creates the question tree'],
    [/查论文证据/g, 'checks paper evidence'],
    [/管引用/g, 'manages citations'],
    [/抓 X 实时舆情/g, 'captures real-time X sentiment'],
    [/验证外部来源/g, 'verifies external sources'],
    [/写洞察摘要/g, 'writes the insight summary'],
    [/起草长文和结构/g, 'drafts long-form content and structure'],
    [/做语法、语气、清晰度 QA/g, 'checks grammar, tone, and clarity'],
    [/发散选题和角度/g, 'brainstorms topics and angles'],
    [/统一成稳定语气、长文结构和精修稿/g, 'turns them into a consistent voice, long-form structure, and polished draft'],
    [/找素材/g, 'finds source material'],
    [/写 newsletter/g, 'writes the newsletter'],
    [/发布并复盘数据/g, 'publishes and reviews performance data'],
    [/学习个人写作样本/g, 'learns the personal writing samples'],
    [/管选题库、草稿和发布状态/g, 'manages the topic library, drafts, and publishing status'],
    [/快速起草/g, 'drafts quickly'],
    [/控制可读性和错误/g, 'controls readability and errors'],
    [/收集高亮信息/g, 'collects highlights'],
    [/建本地知识库/g, 'builds the local knowledge base'],
    [/生成文章\/脚本/g, 'generates articles or scripts'],
    [/做定位和产品卖点/g, 'develops positioning and product selling points'],
    [/批量生成广告版本/g, 'generates ad variants in bulk'],
    [/负责结构和改写/g, 'handles structure and rewriting'],
    [/负责协作评论、版本控制和交付/g, 'handles collaboration comments, version control, and delivery'],
    [/语音记录想法/g, 'records ideas by voice'],
    [/把口述内容重构成文章\/方案/g, 'restructures dictated ideas into articles or plans'],
    [/做信息页雏形/g, 'creates the first information-page draft'],
    [/改成观点型长文/g, 'turns it into opinionated long-form content'],
    [/下载源视频/g, 'downloads the source video'],
    [/下载/g, 'downloads'],
    [/转写/g, 'transcribes'],
    [/提炼/g, 'extracts'],
    [/高光点/g, 'highlight moments'],
    [/自动切片/g, 'automatically cuts clips'],
    [/排序/g, 'ranks'],
    [/加爆款字幕特效/g, 'adds viral subtitle effects'],
    [/多语种配音/g, 'creates multilingual voiceovers'],
    [/对口型/g, 'syncs lip movement'],
    [/一键分发/g, 'distributes in one click to'],
    [/写 PRD\+用户故事/g, 'writes the PRD and user stories'],
    [/写 PRD 和功能规格/g, 'writes the PRD and feature specifications'],
    [/生成 React\+Tailwind UI/g, 'generates the React and Tailwind UI'],
    [/生成 React \+ Supabase 原型/g, 'generates the React and Supabase prototype'],
    [/截图导入/g, 'imports screenshots into'],
    [/接 Supabase 后端/g, 'connects the Supabase backend'],
    [/写测试/g, 'writes tests'],
    [/接支付/g, 'connects payments'],
    [/部署/g, 'deploys'],
    [/埋点/g, 'adds analytics tracking'],
    [/修代码和补后端/g, 'fixes code and completes backend logic'],
    [/生成组件/g, 'generates UI components'],
    [/做增长和追踪/g, 'handles growth tracking and analytics'],
    [/文档导出/g, 'exports documents'],
    [/解析/g, 'parses'],
    [/切块嵌入/g, 'chunks and embeds documents'],
    [/向量库/g, 'stores vectors in the vector database'],
    [/编排 RAG 工作流/g, 'orchestrates the RAG workflow'],
    [/做检索答复/g, 'answers with retrieved context'],
    [/出口/g, 'serves as the output channel'],
    [/监控/g, 'monitors quality and traces'],
    [/拉 ICP 名单/g, 'pulls the ICP lead list'],
    [/做 enrichment/g, 'enriches lead data'],
    [/按公司新闻写个性化首句/g, 'writes personalized opening lines from company news'],
    [/实时打分优化/g, 'scores and optimizes messages in real time'],
    [/多账号轮发/g, 'rotates sending across multiple accounts'],
    [/自动入 CRM/g, 'syncs records into the CRM'],
    [/录跟进电话/g, 'records follow-up calls'],
    [/抓图/g, 'collects product images'],
    [/放大/g, 'upscales images'],
    [/去水印/g, 'removes watermarks'],
    [/重绘场景/g, 'redraws product scenes'],
    [/生成多语 slogan 海报/g, 'generates multilingual slogan posters'],
    [/写 SEO 标题描述/g, 'writes SEO titles and descriptions'],
    [/翻译 7 国语/g, 'translates into seven languages'],
    [/批量上架/g, 'publishes listings in bulk'],
    [/跑初轮/g, 'runs the first research pass'],
    [/补多源/g, 'adds multi-source evidence'],
    [/生成综述大纲/g, 'generates the review outline'],
    [/上传 30 篇 PDF 抽要点/g, 'extracts key points from 30 uploaded PDFs'],
    [/整合写正稿/g, 'integrates the material into the main draft'],
    [/出 PPT 版/g, 'creates the slide version'],
    [/录播客版/g, 'records the podcast version'],
    [/找蓝海关键词/g, 'finds low-competition keywords'],
    [/写脚本\+缩略图 prompt/g, 'writes the script and thumbnail prompt'],
    [/出缩略图/g, 'creates thumbnails'],
    [/做开场转场/g, 'creates openings and transitions'],
    [/录制\+去停顿/g, 'records and removes pauses'],
    [/加字幕/g, 'adds subtitles'],
    [/优化标题/g, 'optimizes titles'],
    [/市场调研/g, 'researches the market'],
    [/找 KOL 和潜在合作/g, 'finds KOLs and potential partners'],
    [/做商品图/g, 'creates product images'],
    [/提升视觉和文字图/g, 'improves visuals and text images'],
    [/做视频素材/g, 'creates video assets'],
    [/写 landing page 和邮件/g, 'writes landing-page copy and emails'],
    [/做自动化和 SEO/g, 'handles automation and SEO'],
    [/找论文/g, 'finds papers'],
    [/检查引用/g, 'checks citations'],
    [/整理资料/g, 'organizes source material'],
    [/管理文献/g, 'manages references'],
    [/分析数据/g, 'analyzes data'],
    [/写论文/g, 'writes the paper'],
    [/校对/g, 'proofreads'],
    [/排版/g, 'typesets'],
    [/做答辩 PPT/g, 'creates the defense slides'],
    [/定义 ICP/g, 'defines the ICP'],
    [/拉取线索/g, 'pulls leads'],
    [/做意图信号/g, 'detects intent signals'],
    [/发送 A\/B 邮件/g, 'sends A/B outreach emails'],
    [/回写 CRM/g, 'writes updates back to the CRM'],
    [/生成 call prep/g, 'generates call-prep briefs'],
    [/收集 50 条素材/g, 'collects 50 source items'],
    [/做主题筛选和结构/g, 'selects topics and builds the structure'],
    [/生成 brief/g, 'generates the brief'],
    [/起草和改写/g, 'drafts and rewrites'],
    [/做头图/g, 'creates the header image'],
    [/发布/g, 'publishes'],
    [/整理访谈材料/g, 'organizes interview material'],
    [/搜集房源和区域信息/g, 'collects property and neighborhood data'],
    [/整理对比表/g, 'builds the comparison table'],
    [/做财务测算/g, 'runs financial calculations'],
    [/做区域和政策研究/g, 'researches local area and policy context'],
    [/生成谈判策略/g, 'generates negotiation strategy'],
    [/处理合同/g, 'handles contracts'],
    [/优化简历和定位/g, 'optimizes the resume and positioning'],
    [/搜集公司和岗位/g, 'collects company and role information'],
    [/定制 cover letter/g, 'customizes cover letters'],
    [/找 hiring manager/g, 'finds hiring managers'],
    [/做面试题和 STAR 框架/g, 'prepares interview questions and STAR stories'],
    [/做口语模拟/g, 'runs spoken interview practice'],
    [/做薪资谈判/g, 'prepares salary negotiation'],
    [/科学问题选择/g, 'selects the research question'],
    [/做文献检索/g, 'searches the literature'],
    [/开发 Nextflow pipeline/g, 'develops the Nextflow pipeline'],
    [/做单细胞 QC/g, 'runs single-cell QC'],
    [/画图/g, 'creates figures'],
    [/读取合同邮件/g, 'reads contract emails'],
    [/检查条款/g, 'checks contract clauses'],
    [/输出风险评估/g, 'outputs a risk assessment'],
    [/发起签字/g, 'starts the signing flow'],
    [/归档/g, 'archives files'],
    [/记录元数据/g, 'records metadata'],
    [/定义品牌策略/g, 'defines brand strategy'],
    [/做方向探索/g, 'explores visual directions'],
    [/做 logo\/vector/g, 'creates logos and vectors'],
    [/做模板/g, 'builds templates'],
    [/做延展素材/g, 'creates derivative brand assets'],
    [/写 design doc 和关卡机制/g, 'writes the design doc and level mechanics'],
    [/生成 3D 资产/g, 'generates 3D assets'],
    [/做整理/g, 'organizes and cleans up assets'],
    [/生成音频/g, 'generates audio'],
    [/写 Unity\/Unreal 逻辑/g, 'writes Unity or Unreal logic'],
    [/做预告片/g, 'creates the trailer'],
    [/做商店视觉/g, 'creates store-page visuals'],
    [/做行业资料/g, 'collects industry material'],
    [/汇总数据/g, 'summarizes data'],
    [/做 DCF 和敏感性分析/g, 'builds the DCF and sensitivity analysis'],
    [/整理访谈/g, 'organizes interview notes'],
    [/消化 PDF/g, 'digests PDFs'],
    [/做图表和写作/g, 'creates charts and writes the report'],
    [/生成汇报 PPT/g, 'creates the presentation deck'],
    [/搭建客服 RAG Bot/g, 'builds the support RAG bot'],
    [/整理 FAQ 和知识库/g, 'organizes the FAQ and knowledge base'],
    [/接入对话/g, 'connects the chat channel'],
    [/做复杂回复和总结/g, 'handles complex replies and summaries'],
    [/回流产品缺陷/g, 'routes product defects back to engineering'],
    [/持续优化召回和回答质量/g, 'continuously improves retrieval and answer quality'],
    [/负责多文件编辑和 diff/g, 'handles multi-file edits and diffs'],
    [/负责架构推理、复杂 bug、重构计划/g, 'handles architecture reasoning, complex bugs, and refactor plans'],
    [/读 repo、改代码、跑测试/g, 'reads the repository, edits code, and runs tests'],
    [/承载审查和合并/g, 'carries review and merge workflow'],
    [/处理 issue 到 PR 的实现/g, 'implements issues through pull requests'],
    [/帮忙解释方案、生成测试和文档/g, 'explains the plan and generates tests and documentation'],
    [/在 IDE 补全和小改/g, 'handles IDE completion and small edits'],
    [/处理大上下文设计和代码审稿/g, 'handles large-context design and code review'],
    [/负责上下文编辑/g, 'handles context-aware edits'],
    [/做困难算法、调试思路、单测用例/g, 'works through hard algorithms, debugging strategy, and unit-test cases'],
    [/约束项目规则/g, 'constrains project rules'],
    [/监控成本/g, 'monitors cost'],
    [/执行任务/g, 'executes tasks'],
    [/分解任务/g, 'breaks down tasks'],
    [/并行查找\/实现\/审查/g, 'searches, implements, and reviews in parallel'],
    [/做安全和质量门禁/g, 'acts as a safety and quality gate'],
    [/做 OpenAI 生态\/桌面任务/g, 'handles OpenAI ecosystem and desktop tasks'],
    [/处理长上下文和重构/g, 'handles long context and refactoring'],
    [/互相审稿/g, 'cross-reviews the work'],
    [/快速搭云端原型/g, 'quickly builds a cloud prototype'],
    [/生成需求、调试和部署说明/g, 'generates requirements, debugging notes, and deployment instructions'],
    [/生成前端原型/g, 'generates the frontend prototype'],
    [/审查业务逻辑、状态和安全风险/g, 'reviews business logic, state, and security risks'],
    [/出 UI/g, 'creates the UI'],
    [/接入项目并改文件/g, 'connects it to the project and edits files'],
    [/做产品逻辑和代码审查/g, 'handles product logic and code review'],
    [/做 agentic IDE 流程/g, 'runs the agentic IDE workflow'],
    [/负责解释、规划、复杂改造/g, 'handles explanation, planning, and complex changes'],
    [/跑开源\/低成本模型/g, 'runs open-source or low-cost models'],
    [/处理关键难题/g, 'handles critical hard problems'],
    [/保留隐私和成本弹性/g, 'keeps privacy and cost flexibility'],
    [/用容器和 git worktree 隔离多 agent/g, 'isolates multiple agents with containers and git worktrees'],
    [/不同模型并行做功能/g, 'lets different models build features in parallel'],
    [/统一管理多个 coding agent/g, 'manages multiple coding agents in one place'],
    [/减少复制粘贴和上下文断裂/g, 'reduces copy-paste and context breaks'],
    [/本地扫描 prompt\/tool\/secret 风险/g, 'locally scans prompt, tool, and secret risks'],
    [/查漏洞、恶意包和许可证/g, 'checks vulnerabilities, malicious packages, and licenses'],
    [/自动生成实现计划/g, 'automatically generates the implementation plan'],
    [/生成验收标准/g, 'generates acceptance criteria'],
    [/自然语言生成\/调试 Spark pipelines/g, 'generates and debugs Spark pipelines from natural language'],
    [/写业务解释和数据质量报告/g, 'writes business explanations and data-quality reports'],
    [/连接 60\\+ 工具做 incident 测试和诊断/g, 'connects 60+ tools for incident testing and diagnosis'],
    [/分发修复建议/g, 'distributes remediation suggestions'],
    [/统一 iMessage\/WhatsApp\/Telegram\/Slack\/SMS 入口/g, 'unifies iMessage, WhatsApp, Telegram, Slack, and SMS'],
    [/分类、回复和路由/g, 'classifies, replies, and routes messages'],
    [/本地私有 AI stack/g, 'runs a private local AI stack'],
    [/避免云锁定/g, 'avoids cloud lock-in'],
    [/用于摘要、分类、提取和内部问答/g, 'supports summarization, classification, extraction, and internal Q&A'],
    [/做模型路由和成本控制/g, 'handles model routing and cost control'],
    [/管 agent 状态/g, 'manages agent state'],
    [/接业务系统/g, 'connects business systems'],
    [/做轻量会议笔记/g, 'creates lightweight meeting notes'],
    [/提炼需求/g, 'extracts requirements'],
    [/建 issue/g, 'creates issues'],
    [/转写销售电话/g, 'transcribes sales calls'],
    [/生成摘要和风险/g, 'generates summaries and risk notes'],
    [/更新字段/g, 'updates fields'],
    [/把邮件\/更新转成视频或语音/g, 'turns emails or updates into video or voice'],
    [/构建实时语音 agent/g, 'builds real-time voice agents'],
    [/调试延迟、工具调用和流水线/g, 'debugs latency, tool calls, and pipelines'],
    [/语音转文本/g, 'transcribes speech to text'],
    [/跑模型/g, 'runs the model'],
    [/做纪要\/行动项/g, 'creates minutes and action items'],
    [/生成流程草稿和 JS\/JSON/g, 'generates workflow drafts and JS/JSON'],
    [/负责 webhook、重试、鉴权、日志和人工调试/g, 'handles webhooks, retries, authentication, logs, and human debugging'],
    [/解释数据结构并给修复表达式/g, 'explains the data structure and provides fixed expressions'],
    [/处理简单跨 app 触发/g, 'handles simple cross-app triggers'],
    [/复杂状态、循环、错误处理放 n8n/g, 'keeps complex state, loops, and error handling in n8n'],
    [/管复杂自动化版图/g, 'maps complex automation systems'],
    [/写节点逻辑、文档和异常处理说明/g, 'writes node logic, documentation, and exception-handling notes'],
    [/写轻量 serverless workflow/g, 'writes lightweight serverless workflows'],
    [/负责摘要、分类、回复/g, 'handles summarization, classification, and replies'],
    [/触发多步骤链路/g, 'triggers a multi-step chain'],
    [/生成每步文案和条件判断/g, 'generates copy and conditions for each step'],
    [/搭多步骤 AI workflow/g, 'builds multi-step AI workflows'],
    [/分别处理推理和通用输出/g, 'separately handle reasoning and general output'],
    [/用自然语言构建企业 app\/workflow/g, 'builds enterprise apps and workflows in natural language'],
    [/作为复杂推理和代码生成核心/g, 'acts as the core for complex reasoning and code generation'],
    [/直接触发 ServiceNow onboarding、审批、工单等系统动作/g, 'directly triggers ServiceNow onboarding, approvals, tickets, and other system actions'],
    [/由平台治理/g, 'is governed by the platform'],
    [/统一发现、观测、治理和必要时关闭越权 agent/g, 'discovers, observes, governs, and can shut down overreaching agents'],
    [/生成故事线和视觉 brief/g, 'generates the storyline and visual brief'],
    [/生成图形和 deck/g, 'generates graphics and decks'],
    [/做社媒和 deck/g, 'creates social posts and decks'],
    [/做轻量图形补充/g, 'adds lightweight graphics'],
    [/写文案/g, 'writes copy'],
    [/在 Adobe 做素材\/视频批处理/g, 'batch-processes assets and video in Adobe'],
    [/在 Blender 做 3D 场景脚本/g, 'scripts 3D scenes in Blender'],
    [/连接跨媒体资产/g, 'connects cross-media assets'],
    [/生成式设计后用物理仿真校验/g, 'validates generative design with physics simulation'],
    [/解释约束和优化方向/g, 'explains constraints and optimization directions'],
    [/出概念图/g, 'creates concept images'],
    [/放大\/增强/g, 'upscales and enhances'],
    [/写视觉规范/g, 'writes visual guidelines'],
    [/写 HTML\/场景/g, 'writes HTML and scenes'],
    [/渲染 MP4/g, 'renders MP4'],
    [/把邮件更新、销售跟进、内部通知转成个性化视频\/语音/g, 'turns email updates, sales follow-ups, and internal notices into personalized video or voice'],
    [/快速克隆并部署多语言语音/g, 'quickly clones and deploys multilingual voices'],
    [/写脚本和对话流/g, 'writes scripts and conversation flows'],
    [/生成基础图片/g, 'generates base images'],
    [/写脚本\/标题/g, 'writes scripts and titles'],
    [/剪辑发布/g, 'edits and publishes'],
    [/监控社媒社区线索/g, 'monitors social and community leads'],
    [/生成个性化触达和跟进策略/g, 'generates personalized outreach and follow-up strategy'],
    [/做财务 admin/g, 'handles finance administration'],
    [/解释现金流、异常和待办/g, 'explains cash flow, anomalies, and to-dos'],
    [/追踪机会/g, 'tracks opportunities'],
    [/写邮件和提案/g, 'writes emails and proposals'],
    [/生成客户 deck/g, 'generates client decks'],
    [/处理客服自动回复/g, 'handles automated support replies'],
    [/管工单/g, 'manages tickets'],
    [/做升级问题摘要/g, 'summarizes escalated issues'],
    [/管多账号 LinkedIn 外联/g, 'manages multi-account LinkedIn outreach'],
    [/写不同 persona 的跟进文案/g, 'writes follow-up copy for different personas'],
    [/做邮件营销自动化/g, 'handles email marketing automation'],
    [/写内容计划/g, 'writes the content plan'],
    [/管 campaign/g, 'manages the campaign'],
    [/语音输入想法/g, 'captures ideas by voice'],
    [/整理为任务、邮件、文章或计划/g, 'organizes them into tasks, emails, articles, or plans'],
    [/减少在浏览器工具间复制粘贴/g, 'reduces copying and pasting between browser tools'],
    [/保持上下文/g, 'keeps context'],
    [/做持久项目记忆/g, 'stores persistent project memory'],
    [/读取上下文后执行任务/g, 'reads context and then executes tasks'],
    [/把目标拆成任务和日程/g, 'breaks goals into tasks and calendar events'],
    [/负责执行提醒/g, 'handles execution reminders'],
    [/研究，/g, 'researches, '],
    [/决策\/写作/g, 'handles decisions and writing'],
    [/实现/g, 'implements'],
    [/表达/g, 'presents the work'],
    [/自动化/g, 'automates'],
  ];
  replacements.forEach(([pattern, replacement]) => {
    text = text.replace(pattern, replacement);
  });
  text = text
    .replace(/；/g, '; ')
    .replace(/，/g, ', ')
    .replace(/。/g, '.')
    .replace(/做/g, 'handles ')
    .replace(/写/g, 'writes ')
    .replace(/生成/g, 'generates ')
    .replace(/整理/g, 'organizes ')
    .replace(/输出/g, 'outputs ')
    .replace(/接/g, 'connects ')
    .replace(/找/g, 'finds ')
    .replace(/和/g, ' and ')
    .replace(/资料/g, 'source material')
    .replace(/文章/g, 'articles')
    .replace(/报告/g, 'reports')
    .replace(/文档/g, 'documents')
    .replace(/表格/g, 'spreadsheets')
    .replace(/图片/g, 'images')
    .replace(/视频/g, 'videos')
    .replace(/代码/g, 'code')
    .replace(/\s+/g, ' ')
    .trim();
  if(hasCjk(text)){
    const toolMatch = raw.match(/^([A-Za-z0-9._/+\-\s]+|[\u3400-\u9fffA-Za-z0-9._/+\-\s]+?)(?:\s|做|写|生成|接|找|转写|下载|整理|输出)/);
    const actor = englishToolName(toolMatch?.[1]?.trim() || '') || 'This tool';
    return englishChinaStepAction(raw, actor);
  }
  return text;
}

function englishAiw100WorkflowOutline(item){
  const steps = item?.steps || [];
  if(!steps.length) return 'The source PDF only lists the tool combination for this item.';
  return steps.slice(0, 8).map(englishAiw100StepAction).filter(Boolean).join('; ');
}

function englishChinaWorkflowOutline(item){
  const tools = item?.tools || [];
  const steps = item?.steps || [];
  const pickedSteps = steps.length ? steps.slice(0, 4) : tools.slice(0, 4);
  if(!pickedSteps.length) return 'The tools are arranged as a practical sequence from input, processing, review, and final delivery.';
  return pickedSteps.map((step, idx) => englishChinaStepAction(step, tools[idx] || tools[0])).join('; ');
}

function englishChinaLibrarySummary(item){
  const scenario = chinaScenarioFromTitle(item?.title);
  const scenarioEn = CHINA_SCENARIO_EN[scenario] || displayCategoryLabel(item?.category_label || 'AI workflow');
  const purpose = CHINA_SCENARIO_PURPOSE_EN[scenario] || `support ${scenarioEn.toLowerCase()} work with a repeatable AI process`;
  const tools = (item?.tools || []).slice(0, 6).map(englishToolName).filter(Boolean);
  const audience = (item?.outputs || []).slice(0, 3).map(englishAudienceName).filter(Boolean).join(', ');
  const toolText = tools.length ? tools.join(' + ') : 'a focused AI tool stack';
  const audienceText = audience || 'the target work scenario';
  const outline = englishChinaWorkflowOutline(item);
  if(item?.item_type === 'workflow'){
    return `${scenarioEn} workflow for ${audienceText}. It combines ${toolText} to ${purpose}. Process: ${outline}.`;
  }
  return `${scenarioEn} combination for ${audienceText}. It is made of ${toolText} and is used to ${purpose}. Role split: ${outline}.`;
}

function englishGuideLibrarySummary(item){
  const title = englishGuideTitle(item?.title, item?.id).toLowerCase();
  const outputs = (item?.outputs || []).slice(0, 4).map(englishDeliverableName).filter(Boolean);
  const outputText = outputs.length ? outputs.join(', ') : 'a usable project deliverable';
  const outline = englishAiw100WorkflowOutline(item);
  if(item?.item_type === 'combination'){
    return `Tool combination for ${title}. Role split from the source workflow: ${outline}.`;
  }
  return `Workflow for ${title}. It produces ${outputText}. Process from the source workflow: ${outline}.`;
}

function englishExpandedLibrarySummary(item){
  const title = englishExpandedTitle(item?.title, item?.id).toLowerCase();
  const audience = (item?.outputs || []).slice(0, 3).map(englishAudienceName).filter(Boolean).join(', ');
  const outline = englishAiw100WorkflowOutline(item);
  const target = audience ? ` for ${audience}` : '';
  if(item?.item_type === 'workflow'){
    return `Workflow${target}: ${title}. Source workflow: ${outline}.`;
  }
  return `Integration${target}: ${title}. Tool roles from the source workflow: ${outline}.`;
}

function englishSkillName(skill){
  if(!hasCjk(skill?.name)) return skill?.name || '';
  if(String(skill?.id || '').startsWith('expanded-tool-')){
    return `Use ${englishToolName(skill.tool) || titleFromSlug(skill.id)} in AI workflow integrations`;
  }
  if(String(skill?.id || '').startsWith('china-tool-')){
    const phraseByCategory = {
      'ai-coding': 'AI coding and development',
      'ai-media': 'video and media production',
      'ai-visual': 'visual design',
      'ai-office': 'office deliverables',
      'ai-research': 'research and knowledge work',
      'ai-agent': 'agentic workflow automation',
      'ai-business': 'business operations',
      'ai-models': 'Chinese AI assistance',
    };
    return `Use ${englishToolName(skill.tool) || titleFromSlug(skill.id)} for ${phraseByCategory[skill.category_id] || 'AI workflows'}`;
  }
  if(String(skill?.id || '').startsWith('aiw100-tool-')){
    const phraseByCategory = {
      'ai-coding': 'engineering delivery',
      'ai-media': 'media production',
      'ai-visual': 'visual asset creation',
      'ai-office': 'office and knowledge work',
      'ai-research': 'research and analysis',
      'ai-agent': 'workflow automation',
      'ai-business': 'business operations',
      'ai-models': 'model workflows',
    };
    return `Use ${skill.tool || titleFromSlug(skill.id)} for ${phraseByCategory[skill.category_id] || 'AI tasks'}`;
  }
  const tool = skill.tool || titleFromSlug(skill.id).split(' ')[0] || 'AI';
  const task = titleFromSlug(String(skill.id || '').replace(String(tool).toLowerCase().replace(/[^a-z0-9]+/g, '-'), ''))
    .replace(/^Ai /, '')
    .trim();
  const fallback = titleFromSlug(skill.id);
  return `Use ${tool} for ${task || fallback}`;
}

function englishSkillDescription(skill){
  if(!hasCjk(skill?.description)) return skill?.description || '';
  if(String(skill?.id || '').startsWith('expanded-tool-')){
    const tool = englishToolName(skill.tool) || englishSkillName(skill);
    const examples = (skill.examples || []).slice(0, 1).map(englishAiw100StepAction).filter(Boolean);
    const sourceUse = examples.length ? examples[0] : 'supports one source-defined workflow step';
    return `${tool} appears in the expanded 2026 AI workflow stack. Source-defined use: ${sourceUse}.`;
  }
  if(String(skill?.id || '').startsWith('china-tool-')){
    const scenario = displayCategoryLabel(skill.category_label || 'AI workflow').toLowerCase();
    const tool = englishToolName(skill.tool) || englishSkillName(skill);
    const examples = (skill.examples || []).slice(0, 2).map(x => englishChinaStepAction(x, skill.tool));
    const exampleText = examples.length ? ` Typical use: ${examples.join('; ')}.` : '';
    return `${tool} is used in ${scenario} workflows to handle a specific production, analysis, communication, or automation step.${exampleText}`;
  }
  const examples = (skill.examples || []).filter(Boolean).slice(0, 2).map(x => englishChinaStepAction(x, skill.tool));
  if(examples.length){
    return `${englishSkillName(skill)} helps turn a task brief into concrete AI-assisted output. Typical use: ${examples.join('; ')}.`;
  }
  const tags = (skill.tags || []).filter(Boolean).filter(x => !hasCjk(x)).slice(0, 4);
  if(tags.length){
    return `Best for ${tags.join(', ')} workflows.`;
  }
  return `Best for ${displayCategoryLabel(skill.category_label || 'AI skill').toLowerCase()} tasks.`;
}

function displaySkillName(skill){
  return currentLang === 'en' ? englishSkillName(skill) : translateText(skill?.name || '');
}

function displaySkillDescription(skill){
  return currentLang === 'en' ? englishSkillDescription(skill) : translateText(skill?.description || '');
}

function displayNodeName(node){
  if(currentTheme === 'bloom' || ['forge', 'rest', 'kin'].includes(node?.cat)) return node?.name || '';
  if(currentLang !== 'en') return node?.name || '';
  const skillLike = {
    id: node?.id || '',
    name: node?.name || '',
    tool: '',
    category_label: node?.cat || '',
    tags: [],
  };
  return hasCjk(skillLike.name) ? englishSkillName(skillLike) : skillLike.name;
}

function displayLibraryTitle(item){
  if(currentLang === 'en' && hasCjk(item?.title)){
    const source = String(item?.source_section || '');
    if(source.includes('ai_tool_workflow_stacks_2026_recent_3_months_expanded')) return englishExpandedTitle(item.title, item.id);
    if(source.includes('2026_AI_工具实战指南') || source.includes('AI工作流100条')) return englishGuideTitle(item.title, item.id);
    return englishChinaTitle(item.title, item.id);
  }
  return currentLang === 'zh' ? translateText(item?.title || '') : (item?.title || '');
}

function displayLibrarySummary(item){
  if(currentLang === 'en' && hasCjk(item?.summary)){
    const source = String(item?.source_section || '');
    if(source.includes('ai_tool_workflow_stacks_2026_recent_3_months_expanded')) return englishExpandedLibrarySummary(item);
    if(source.includes('2026_AI_工具实战指南') || source.includes('AI工作流100条')) return englishGuideLibrarySummary(item);
    return englishChinaLibrarySummary(item);
  }
  return currentLang === 'zh' ? translateText(item?.summary || '') : (item?.summary || '');
}

function displayLibraryChip(value){
  if(currentLang !== 'en') return translateText(value);
  return CHINA_AUDIENCE_EN[value] || englishToolName(value);
}

function displaySourceSection(value){
  const raw = String(value || 'PDF');
  if(currentLang !== 'en') return translateText(raw);
  if(raw.includes('ai_tool_workflow_stacks_2026_recent_3_months_expanded')) return 'Expanded AI tool workflow stacks';
  if(raw.includes('AI工作流100条')) return 'AI Workflow 100';
  if(raw.includes('china_ai_tool_workflow')) return 'China AI tool workflow stacks';
  if(hasCjk(raw)) return titleFromSlug(raw.replace(/[^\w]+/g, '-')) || 'PDF source';
  return raw;
}

// ---------------- scene ----------------
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

const camera = new THREE.PerspectiveCamera(38, innerWidth/innerHeight, 0.1, 2000);
camera.position.set(0, 1.4, 6.2);

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.35;
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.06;
controls.rotateSpeed = 0.4;
controls.minDistance = 3.4;
controls.maxDistance = 11;
controls.enablePan = false;

// ---------------- background fields (per-theme) ----------------
// ORBIT: starfield — sharp distant suns
// BLOOM: pollen field — soft warm motes drifting slowly upward
function makeStars(count, radius){
  const g = new THREE.BufferGeometry();
  const pos = new Float32Array(count*3);
  const col = new Float32Array(count*3);
  const sz  = new Float32Array(count);
  for(let i=0;i<count;i++){
    const u = Math.random(), v = Math.random();
    const theta = 2*Math.PI*u;
    const phi = Math.acos(2*v - 1);
    const r = radius * (0.7 + Math.random()*0.6);
    pos[i*3+0] = r*Math.sin(phi)*Math.cos(theta);
    pos[i*3+1] = r*Math.sin(phi)*Math.sin(theta);
    pos[i*3+2] = r*Math.cos(phi);
    const c = new THREE.Color().setHSL(0.55 + (Math.random()-0.5)*0.2, 0.15, 0.6 + Math.random()*0.4);
    col[i*3+0]=c.r; col[i*3+1]=c.g; col[i*3+2]=c.b;
    sz[i] = Math.random() < 0.02 ? 2.4 : 0.6 + Math.random()*0.9;
  }
  g.setAttribute('position', new THREE.BufferAttribute(pos,3));
  g.setAttribute('color', new THREE.BufferAttribute(col,3));
  g.setAttribute('size', new THREE.BufferAttribute(sz,1));
  const m = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false,
    vertexShader: `
      attribute float size; varying vec3 vColor;
      void main(){
        vColor = color;
        vec4 mv = modelViewMatrix * vec4(position,1.0);
        gl_PointSize = size * (300.0 / -mv.z);
        gl_Position = projectionMatrix * mv;
      }`,
    fragmentShader: `
      varying vec3 vColor;
      void main(){
        vec2 c = gl_PointCoord - 0.5;
        float d = length(c);
        float a = smoothstep(0.5, 0.0, d);
        a *= smoothstep(0.5, 0.42, d) + 0.5;
        gl_FragColor = vec4(vColor, a);
      }`,
    vertexColors: true,
  });
  return new THREE.Points(g, m);
}

// Pollen / drifting motes — soft warm specks for BLOOM
function makePollen(count, radius){
  const g = new THREE.BufferGeometry();
  const pos = new Float32Array(count*3);
  const col = new Float32Array(count*3);
  const sz  = new Float32Array(count);
  const ph  = new Float32Array(count);
  for(let i=0;i<count;i++){
    const u = Math.random(), v = Math.random();
    const theta = 2*Math.PI*u;
    const phi = Math.acos(2*v - 1);
    const r = radius * (0.55 + Math.random()*0.5);
    pos[i*3+0] = r*Math.sin(phi)*Math.cos(theta);
    pos[i*3+1] = r*Math.sin(phi)*Math.sin(theta);
    pos[i*3+2] = r*Math.cos(phi);
    // warm cream / peach / dusty rose
    const c = new THREE.Color().setHSL(0.07 + Math.random()*0.06, 0.35 + Math.random()*0.2, 0.78 + Math.random()*0.15);
    col[i*3]=c.r; col[i*3+1]=c.g; col[i*3+2]=c.b;
    sz[i] = 1.4 + Math.random()*2.2;
    ph[i] = Math.random()*Math.PI*2;
  }
  g.setAttribute('position', new THREE.BufferAttribute(pos,3));
  g.setAttribute('color', new THREE.BufferAttribute(col,3));
  g.setAttribute('size', new THREE.BufferAttribute(sz,1));
  g.setAttribute('phase', new THREE.BufferAttribute(ph,1));
  const m = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false,
    uniforms: { uTime:{ value:0 } },
    vertexShader: `
      attribute float size; attribute float phase;
      varying vec3 vColor; varying float vAlpha;
      uniform float uTime;
      void main(){
        vColor = color;
        vec3 p = position;
        // gentle drift — soft vertical sway
        p.y += sin(uTime*0.18 + phase)*0.6;
        p.x += cos(uTime*0.13 + phase*1.3)*0.4;
        // breathing alpha
        vAlpha = 0.45 + 0.35*sin(uTime*0.6 + phase*2.0);
        vec4 mv = modelViewMatrix * vec4(p,1.0);
        gl_PointSize = size * (260.0 / -mv.z);
        gl_Position = projectionMatrix * mv;
      }`,
    fragmentShader: `
      varying vec3 vColor; varying float vAlpha;
      void main(){
        vec2 c = gl_PointCoord - 0.5;
        float d = length(c);
        float a = smoothstep(0.5, 0.0, d);
        a = pow(a, 2.0);
        gl_FragColor = vec4(vColor, a*vAlpha);
      }`,
    vertexColors: true,
  });
  return { points: new THREE.Points(g, m), material: m };
}

const starfield = makeStars(2200, 90);
scene.add(starfield);
const pollen = makePollen(1400, 70);
scene.add(pollen.points);
pollen.points.visible = false;  // legacy: BLOOM no longer uses pollen — kept to avoid uniform lookups changing

// far nebulae as faint colored gradient sphere
const nebulaeORBIT = (() => {
  const g = new THREE.SphereGeometry(120, 32, 32);
  const m = new THREE.ShaderMaterial({
    side: THREE.BackSide,
    uniforms: { t: { value: 0 } },
    vertexShader: `varying vec3 vN; void main(){ vN = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
    fragmentShader: `
      varying vec3 vN;
      void main(){
        float y = vN.y * 0.5 + 0.5;
        vec3 deep = vec3(0.0,0.0,0.0);
        vec3 warm = vec3(0.10,0.06,0.02);
        vec3 cool = vec3(0.02,0.04,0.08);
        vec3 c = mix(deep, mix(cool, warm, y), 0.45);
        gl_FragColor = vec4(c, 1.0);
      }`
  });
  const mesh = new THREE.Mesh(g, m);
  scene.add(mesh);
  return mesh;
})();

// BLOOM nebula: warm dawn gradient — cream top, peach mid, dusty rose bottom
const nebulaeBLOOM = (() => {
  const g = new THREE.SphereGeometry(120, 32, 32);
  const m = new THREE.ShaderMaterial({
    side: THREE.BackSide,
    vertexShader: `varying vec3 vN; void main(){ vN = normalize(position); gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
    fragmentShader: `
      varying vec3 vN;
      void main(){
        float y = vN.y * 0.5 + 0.5;
        // top: cream, middle: peach, bottom: dusty rose
        vec3 cream = vec3(0.96, 0.90, 0.80);
        vec3 peach = vec3(0.92, 0.78, 0.66);
        vec3 rose  = vec3(0.78, 0.62, 0.60);
        vec3 c = mix(rose, peach, smoothstep(0.0, 0.55, y));
        c = mix(c, cream, smoothstep(0.55, 1.0, y));
        // soft warm vignette darkening at horizon
        float vign = 1.0 - pow(abs(vN.y), 1.4);
        c = mix(c, c*0.92, vign*0.25);
        gl_FragColor = vec4(c, 1.0);
      }`
  });
  const mesh = new THREE.Mesh(g, m);
  scene.add(mesh);
  return mesh;
})();
nebulaeBLOOM.visible = false;  // legacy: BLOOM now shares the cosmic background

// ---------------- earth (procedural, no textures) ----------------
const EARTH_R = 1.0;

// Night-side earth — city lights, clouds, dark ocean, subtle warm rim
const earthMat = new THREE.ShaderMaterial({
  uniforms: {
    uTime:      { value: 0 },
    uSunDir:    { value: new THREE.Vector3(0.6, 0.25, 0.75).normalize() },
    uAmber:     { value: new THREE.Color('#ffb87a') },
    uOcean:     { value: new THREE.Color('#06143a') },
    uLand:      { value: new THREE.Color('#0a0e16') },
    uCamPos:    { value: new THREE.Vector3() },
  },
  vertexShader: `
    varying vec3 vWorldPos;
    varying vec3 vNormal;
    varying vec3 vObjPos;
    void main(){
      vObjPos = normalize(position);
      vNormal = normalize(normalMatrix * normal);
      vec4 wp = modelMatrix * vec4(position,1.0);
      vWorldPos = wp.xyz;
      gl_Position = projectionMatrix * viewMatrix * wp;
    }
  `,
  fragmentShader: `
    precision highp float;
    varying vec3 vWorldPos;
    varying vec3 vNormal;
    varying vec3 vObjPos;
    uniform float uTime;
    uniform vec3 uSunDir;
    uniform vec3 uAmber;
    uniform vec3 uOcean;
    uniform vec3 uLand;
    uniform vec3 uCamPos;

    float hash(vec3 p){ return fract(sin(dot(p, vec3(127.1,311.7,74.7)))*43758.5453); }
    float noise(vec3 p){
      vec3 i=floor(p), f=fract(p);
      f = f*f*(3.0-2.0*f);
      float n = mix(
        mix(mix(hash(i+vec3(0,0,0)),hash(i+vec3(1,0,0)),f.x),
            mix(hash(i+vec3(0,1,0)),hash(i+vec3(1,1,0)),f.x),f.y),
        mix(mix(hash(i+vec3(0,0,1)),hash(i+vec3(1,0,1)),f.x),
            mix(hash(i+vec3(0,1,1)),hash(i+vec3(1,1,1)),f.x),f.y), f.z);
      return n;
    }
    float fbm(vec3 p){
      float v=0.0, a=0.5;
      for(int i=0;i<6;i++){ v+=a*noise(p); p*=2.07; a*=0.5; }
      return v;
    }
    float fbmWarp(vec3 p){
      vec3 q = vec3(fbm(p), fbm(p+vec3(5.2,1.3,2.8)), fbm(p+vec3(1.7,9.2,4.4)));
      return fbm(p + 1.6*q);
    }

    void main(){
      vec3 N = normalize(vObjPos);
      // continent mask via fbm in spherical coords
      float continents = fbm(N*1.8 + 3.1);
      float detail = fbm(N*5.0);
      float landMask = smoothstep(0.50, 0.58, continents + detail*0.15);

      // city lights — concentrate on coasts
      vec3 cellP = N*26.0;
      float city = 0.0;
      float coast = 1.0 - smoothstep(0.0, 0.06, abs(continents - 0.55));
      float density = landMask * (0.45 + 0.55*coast);
      for(int i=0;i<4;i++){
        float k = float(i+1);
        float v = noise(cellP*k + float(i)*7.3);
        city += pow(smoothstep(0.84, 0.99, v), 5.0) * (0.7/k);
      }
      float spark = pow(noise(cellP*3.0 + 13.0), 18.0) * 4.0;
      city += spark * landMask;
      city *= density;
      float lat = abs(N.y);
      city *= smoothstep(0.95, 0.35, lat);

      // ocean shimmer — deep cosmic blue
      float oceanFlow = fbm(N*6.0 + vec3(uTime*0.025, 0.0, -uTime*0.02));
      vec3 oceanDeep = uOcean * 0.55;
      vec3 oceanBright = uOcean * 1.25 + vec3(0.0, 0.03, 0.08);
      vec3 oceanCol = mix(oceanDeep, oceanBright, oceanFlow);
      vec3 base = mix(oceanCol, uLand, landMask);

      float diff = max(dot(N, normalize(uSunDir)), 0.0);
      float nightFactor = smoothstep(0.25, -0.05, dot(N, normalize(uSunDir)));

      // ocean blue ambient, land near-black
      vec3 ambient = mix(vec3(0.04,0.07,0.18), vec3(0.02,0.025,0.035), landMask);
      vec3 col = ambient + base * (0.45 + 1.0*diff);
      col += uAmber * city * (0.8 + 1.8*nightFactor) * 3.2;
      vec3 V = normalize(uCamPos - vWorldPos);

      // flowing clouds
      vec3 cloudP = N*2.4 + vec3(uTime*0.012, uTime*0.004, 0.0);
      float clouds = fbmWarp(cloudP);
      float cloudMask = smoothstep(0.50, 0.78, clouds);
      float wisps = smoothstep(0.62, 0.85, fbm(N*4.5 + vec3(-uTime*0.02, 0.0, uTime*0.01)));
      col += vec3(0.10, 0.10, 0.12) * cloudMask * (0.18 + 0.7*diff);
      col += vec3(0.08, 0.08, 0.10) * wisps * (0.10 + 0.6*diff) * 0.5;
      col -= uAmber * city * cloudMask * 0.35 * nightFactor;

      // (terminator removed for cleaner deep look)
      float term = 0.0;

      // subtle deep-blue rim
      float fres = pow(1.0 - max(dot(normalize(vNormal), V), 0.0), 3.5);
      col += vec3(0.18, 0.28, 0.55) * fres * 0.22;

      gl_FragColor = vec4(col, 1.0);
    }
  `,
});

const earthGeo = new THREE.SphereGeometry(EARTH_R, 96, 96);
const earth = new THREE.Mesh(earthGeo, earthMat);
const groupOrbit = new THREE.Group();
groupOrbit.add(earth);
scene.add(groupOrbit);

// ---------------- BLOOM planet — Verdania, a living green world ----------------
// Earth-sibling life world: teal-green oceans, dark olive forest continents,
// warm golden city networks on the night side, drifting white cloud bands.
// Shader mirrors the ORBIT earth (continents + cities + clouds + rim) but
// re-keyed to a moss/teal/gold palette so it reads as the "living" twin.
const earthBloomMat = new THREE.ShaderMaterial({
  uniforms: {
    uTime:   { value: 0 },
    uSunDir: { value: new THREE.Vector3(0.55, 0.30, 0.65).normalize() },
    uCamPos: { value: new THREE.Vector3() },
    uOcean:  { value: new THREE.Color('#0e3a3a') },
    uShallow:{ value: new THREE.Color('#3aa884') },
    uLand:   { value: new THREE.Color('#1f3320') },
    uHigh:   { value: new THREE.Color('#7a8a55') },
    uGold:   { value: new THREE.Color('#ffc060') },
  },
  vertexShader: `
    varying vec3 vWorldPos; varying vec3 vNormal; varying vec3 vObjPos;
    void main(){
      vObjPos = normalize(position);
      vNormal = normalize(normalMatrix * normal);
      vec4 wp = modelMatrix * vec4(position,1.0);
      vWorldPos = wp.xyz;
      gl_Position = projectionMatrix * viewMatrix * wp;
    }`,
  fragmentShader: `
    precision highp float;
    varying vec3 vWorldPos; varying vec3 vNormal; varying vec3 vObjPos;
    uniform float uTime;
    uniform vec3 uSunDir, uCamPos, uOcean, uShallow, uLand, uHigh, uGold;

    float hash(vec3 p){ return fract(sin(dot(p, vec3(127.1,311.7,74.7)))*43758.5453); }
    float noise(vec3 p){
      vec3 i=floor(p), f=fract(p); f = f*f*(3.0-2.0*f);
      float n = mix(
        mix(mix(hash(i),hash(i+vec3(1,0,0)),f.x), mix(hash(i+vec3(0,1,0)),hash(i+vec3(1,1,0)),f.x),f.y),
        mix(mix(hash(i+vec3(0,0,1)),hash(i+vec3(1,0,1)),f.x), mix(hash(i+vec3(0,1,1)),hash(i+vec3(1,1,1)),f.x),f.y), f.z);
      return n;
    }
    float fbm(vec3 p){
      float v=0.0, a=0.5;
      for(int i=0;i<6;i++){ v+=a*noise(p); p*=2.07; a*=0.5; }
      return v;
    }
    float fbmWarp(vec3 p){
      vec3 q = vec3(fbm(p), fbm(p+vec3(5.2,1.3,2.8)), fbm(p+vec3(1.7,9.2,4.4)));
      return fbm(p + 1.6*q);
    }

    void main(){
      vec3 N = normalize(vObjPos);

      float continents = fbm(N*1.8 + 3.1);
      float detail = fbm(N*5.0);
      float c = continents + detail*0.15;
      float landMask = smoothstep(0.50, 0.58, c);

      float landVar = fbm(N*3.4 + 11.0);
      vec3 landCol = mix(uLand, uHigh, smoothstep(0.45, 0.75, landVar));

      float oceanShallow = smoothstep(0.42, 0.52, c);
      float oceanFlow = fbm(N*6.0 + vec3(uTime*0.020, 0.0, -uTime*0.018));
      vec3 oceanCol = mix(uOcean, uOcean*1.4 + vec3(0.0, 0.04, 0.04), oceanFlow*0.5);
      oceanCol = mix(oceanCol, uShallow, oceanShallow * 0.55);

      vec3 base = mix(oceanCol, landCol, landMask);

      float diff = max(dot(N, normalize(uSunDir)), 0.0);
      float nightFactor = smoothstep(0.25, -0.05, dot(N, normalize(uSunDir)));
      vec3 ambient = mix(vec3(0.04, 0.10, 0.10), vec3(0.025, 0.035, 0.025), landMask);
      vec3 col = ambient + base * (0.45 + 1.05*diff);

      vec3 cellP = N*26.0;
      float coast = 1.0 - smoothstep(0.0, 0.06, abs(continents - 0.55));
      float density = landMask * (0.45 + 0.55*coast);
      float city = 0.0;
      for(int i=0;i<4;i++){
        float k = float(i+1);
        float v = noise(cellP*k + float(i)*7.3);
        city += pow(smoothstep(0.84, 0.99, v), 5.0) * (0.7/k);
      }
      float spark = pow(noise(cellP*3.0 + 13.0), 18.0) * 4.0;
      city += spark * landMask;
      city *= density;
      city *= smoothstep(0.95, 0.35, abs(N.y));
      col += uGold * city * (0.8 + 1.8*nightFactor) * 3.0;

      vec3 cloudP = N*2.3 + vec3(uTime*0.014, uTime*0.004, 0.0);
      float clouds = fbmWarp(cloudP);
      float cloudMask = smoothstep(0.52, 0.80, clouds);
      float wisps = smoothstep(0.62, 0.85, fbm(N*4.5 + vec3(-uTime*0.02, 0.0, uTime*0.01)));
      col += vec3(0.85, 0.92, 0.85) * cloudMask * (0.20 + 0.65*diff);
      col += vec3(0.65, 0.72, 0.65) * wisps   * (0.10 + 0.55*diff) * 0.5;
      col -= uGold * city * cloudMask * 0.4 * nightFactor;

      vec3 V = normalize(uCamPos - vWorldPos);
      float fres = pow(1.0 - max(dot(normalize(vNormal), V), 0.0), 3.0);
      col += vec3(0.22, 0.55, 0.40) * fres * 0.35;
      col += vec3(0.50, 0.85, 0.65) * pow(fres, 2.0) * 0.20;

      gl_FragColor = vec4(col, 1.0);
    }`,
});
const earthBloom = new THREE.Mesh(earthGeo, earthBloomMat);
const groupBloom = new THREE.Group();
groupBloom.add(earthBloom);
scene.add(groupBloom);
groupBloom.visible = false;

// soft atmosphere shell — warm, very subtle (no thick blue ring)
const atmoMat = new THREE.ShaderMaterial({
  transparent: true, side: THREE.BackSide, depthWrite: false, blending: THREE.AdditiveBlending,
  uniforms: { uColor:{ value: new THREE.Color('#3a2a1a') } },
  vertexShader: `varying vec3 vN; varying vec3 vP; void main(){ vN=normalize(normalMatrix*normal); vec4 mv=modelViewMatrix*vec4(position,1.0); vP=-mv.xyz; gl_Position=projectionMatrix*mv; }`,
  fragmentShader: `
    varying vec3 vN; varying vec3 vP; uniform vec3 uColor;
    void main(){
      float i = pow(1.0 - max(dot(normalize(vN), normalize(vP)),0.0), 5.0);
      gl_FragColor = vec4(uColor*i, i*0.5);
    }`
});
const atmo = new THREE.Mesh(new THREE.SphereGeometry(EARTH_R*1.04, 64, 64), atmoMat);
groupOrbit.add(atmo);

// Landing-only main category rings: a curated Saturn-like rainbow system.
// These are visual signposts for exploration; sub-skill orbits stay hidden
// until a main category is focused.
const landingMainRingGroup = new THREE.Group();
landingMainRingGroup.rotation.set(0.62, 0.04, -0.02);
groupOrbit.add(landingMainRingGroup);
const landingMainRings = [];
const LANDING_RING_PALETTE = [
  { core:'#00f6ff', halo:'#95ffff', inner:'#f4ffff', outer:'#2f6bff' },
  { core:'#2f6bff', halo:'#7ff4ff', inner:'#cfe8ff', outer:'#745cff' },
  { core:'#745cff', halo:'#89f7ff', inner:'#e5dcff', outer:'#c84dff' },
  { core:'#d94dff', halo:'#9cffff', inner:'#ffd7ff', outer:'#ff3fae' },
  { core:'#ff3fae', halo:'#8dfff4', inner:'#ffe1f5', outer:'#ff7a45' },
  { core:'#ffb238', halo:'#50ffe0', inner:'#fff4bd', outer:'#c7ff48' },
  { core:'#39ffb6', halo:'#b5fff1', inner:'#e2fff6', outer:'#00b8ff' },
  { core:'#6ae6ff', halo:'#d7fff9', inner:'#f2ffff', outer:'#5a8cff' },
];
const landingRingHitMeshes = [];

function makeLandingSilkMaterial(palette, phase){
  return new THREE.ShaderMaterial({
    transparent: true,
    side: THREE.DoubleSide,
    depthTest: true,
    depthWrite: false,
    blending: THREE.NormalBlending,
    uniforms: {
      uCore: { value: new THREE.Color(palette.core) },
      uHalo: { value: new THREE.Color(palette.halo) },
      uInner: { value: new THREE.Color(palette.inner) },
      uOuter: { value: new THREE.Color(palette.outer) },
      uOpacity: { value: 0 },
      uTime: { value: 0 },
      uPhase: { value: phase },
    },
    vertexShader: `
      varying vec2 vUv;
      void main(){
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
      }
    `,
    fragmentShader: `
      varying vec2 vUv;
      uniform vec3 uCore;
      uniform vec3 uHalo;
      uniform vec3 uInner;
      uniform vec3 uOuter;
      uniform float uOpacity;
      uniform float uTime;
      uniform float uPhase;
      void main(){
        vec2 p = vUv - 0.5;
        float a = atan(p.y, p.x);
        float r = length(p) * 2.0;
        float radial = smoothstep(0.70, 1.0, r);
        float silk = 0.5 + 0.5 * sin(a * 10.0 + uTime * 0.58 + uPhase);
        float fine = 0.5 + 0.5 * sin(a * 28.0 - uTime * 0.34 + uPhase * 1.7);
        float thread = 0.5 + 0.5 * sin(a * 72.0 + r * 18.0 + uTime * 0.18 + uPhase);
        float sheen = pow(silk, 5.0) * 0.18 + fine * 0.055 + thread * 0.035;
        vec3 silver = vec3(0.76, 0.84, 0.88);
        vec3 cool = mix(mix(uCore, silver, 0.42), uHalo, 0.18 + sheen);
        vec3 warmEdge = mix(uInner, uOuter, radial);
        vec3 color = mix(cool, warmEdge, radial * 0.20);
        float alpha = uOpacity * (0.36 + sheen);
        gl_FragColor = vec4(color, alpha);
      }
    `,
  });
}

function setLandingOpacity(mat, value){
  if(mat.uniforms?.uOpacity) mat.uniforms.uOpacity.value = value;
  else mat.opacity = value;
}

function buildLandingMainRings(){
  landingMainRingGroup.clear();
  landingMainRings.length = 0;
  landingRingHitMeshes.length = 0;
}
buildLandingMainRings();

// BLOOM atmosphere — thin, subtle moss halo (matches ORBIT's quiet rim)
const atmoBloomMat = new THREE.ShaderMaterial({
  transparent: true, side: THREE.BackSide, depthWrite: false, blending: THREE.AdditiveBlending,
  uniforms: { uColor:{ value: new THREE.Color('#1f4a30') } },
  vertexShader: `varying vec3 vN; varying vec3 vP; void main(){ vN=normalize(normalMatrix*normal); vec4 mv=modelViewMatrix*vec4(position,1.0); vP=-mv.xyz; gl_Position=projectionMatrix*mv; }`,
  fragmentShader: `
    varying vec3 vN; varying vec3 vP; uniform vec3 uColor;
    void main(){
      float i = pow(1.0 - max(dot(normalize(vN), normalize(vP)),0.0), 5.0);
      gl_FragColor = vec4(uColor*i, i*0.5);
    }`
});
const atmoBloom = new THREE.Mesh(new THREE.SphereGeometry(EARTH_R*1.04, 64, 64), atmoBloomMat);
groupBloom.add(atmoBloom);

// ---------------- orbit rings (dynamic) ----------------
// Cosmic-logic helpers for procedurally generating new rings.
// - Radius increases asteroid-belt-like (~0.42 step + slight scatter)
// - Speed follows Kepler's third law (T² ∝ r³ ⇒ ω ∝ r^(-3/2))
// - Tilt is hashed from the category id so a renamed cat keeps its plane
// - Colors cycle in OKLCH space at constant L/C, hue stepping by 47° (golden-ish)
const RING_BASE_R = 1.55;
const RING_BASE_SPEED = 0.06;
const RING_STEP = 0.42;

// Stable string hash → [0,1)
function strHash01(s){
  let h = 2166136261 >>> 0;
  for(let i=0;i<s.length;i++){ h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
  return (h >>> 0) / 0xffffffff;
}
function tiltFromId(id){
  const a = strHash01(id+'#x') * 2 - 1;
  const b = strHash01(id+'#y') * 2 - 1;
  const c = strHash01(id+'#z') * 2 - 1;
  // ~ ±0.85 rad on x, ±0.6 on y, ±0.25 on z (real planets are mostly low-incl)
  return [ a*0.85, b*0.6, c*0.25 ];
}
function oklchToHex(L, C, hDeg){
  // OKLCH → linear sRGB → sRGB hex (Björn Ottosson formulae)
  const h = hDeg * Math.PI / 180;
  const a_ = Math.cos(h) * C;
  const b_ = Math.sin(h) * C;
  const l_ = L + 0.3963377774 * a_ + 0.2158037573 * b_;
  const m_ = L - 0.1055613458 * a_ - 0.0638541728 * b_;
  const s_ = L - 0.0894841775 * a_ - 1.2914855480 * b_;
  const l = l_*l_*l_, m = m_*m_*m_, s = s_*s_*s_;
  let r =  4.0767416621*l - 3.3077115913*m + 0.2309699292*s;
  let g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s;
  let bl=  -0.0041960863*l - 0.7034186147*m + 1.7076147010*s;
  const lin2srgb = v => {
    v = Math.max(0, Math.min(1, v));
    return v <= 0.0031308 ? 12.92*v : 1.055*Math.pow(v, 1/2.4) - 0.055;
  };
  r = Math.round(lin2srgb(r)*255);
  g = Math.round(lin2srgb(g)*255);
  bl= Math.round(lin2srgb(bl)*255);
  const h2 = n => n.toString(16).padStart(2,'0');
  return '#' + h2(r) + h2(g) + h2(bl);
}
// Default rings come from the active theme
const DEFAULT_RING_DEFS = THEMES[currentTheme].defaultRings;

const RINGS_KEY_BASE = 'skill-orbit-rings-v14';
const ringsKey = () => `${RINGS_KEY_BASE}:${currentTheme}`;
// one-time cleanup of legacy keys (Chinese labels & seeds, pre-theme storage)
try{
  if(localStorage.getItem('skill-orbit-rings-v1') || localStorage.getItem('skill-orbit-cat-labels-v1')){
    localStorage.removeItem('skill-orbit-rings-v1');
    localStorage.removeItem('skill-orbit-cat-labels-v1');
    localStorage.removeItem('skill-orbit-v1');
  }
  // migrate non-namespaced v2 → orbit theme namespace (one-time)
  const oldR = localStorage.getItem('skill-orbit-rings-v2');
  if(oldR && !localStorage.getItem('skill-orbit-rings-v2:orbit')){
    localStorage.setItem('skill-orbit-rings-v2:orbit', oldR);
    localStorage.removeItem('skill-orbit-rings-v2');
  }
  const oldS = localStorage.getItem('skill-orbit-v2');
  if(oldS && !localStorage.getItem('skill-orbit-v2:orbit')){
    localStorage.setItem('skill-orbit-v2:orbit', oldS);
    localStorage.removeItem('skill-orbit-v2');
  }
  if(!localStorage.getItem('skill-orbit-bloom-empty-v1')){
    localStorage.removeItem('skill-orbit-rings-v3:bloom');
    localStorage.removeItem('skill-orbit-v3:bloom');
    localStorage.setItem('skill-orbit-bloom-empty-v1', '1');
  }
}catch(e){}
function loadRingDefs(){
  try{
    const raw = localStorage.getItem(ringsKey());
    if(raw){
      const arr = JSON.parse(raw);
      if(Array.isArray(arr) && arr.length >= 1) return arr;
    }
  }catch(e){}
  const defs = THEMES[currentTheme].defaultRings.map(d => ({ ...d }));
  return currentTheme === 'orbit' ? layoutOrbitRingDefs(defs) : defs;
}
function saveRingDefs(){
  try{
    const data = RINGS.map(r => ({
      id: r.id, mainId: r.mainId || r.id, label: r.label, labelCn: r.labelCn,
      color: '#' + new THREE.Color(r.color).getHexString(),
      r: r.r, tilt: [r.tilt.x, r.tilt.y, r.tilt.z],
      defaultR: r.defaultR || r.r,
      defaultTilt: r.defaultTilt ? [r.defaultTilt.x, r.defaultTilt.y, r.defaultTilt.z] : [r.tilt.x, r.tilt.y, r.tilt.z],
      defaultCenter: r.defaultCenter ? [r.defaultCenter.x, r.defaultCenter.y, r.defaultCenter.z] : [0, 0, 0],
      defaultPresence: r.defaultPresence ?? 1,
      speed: r.speed,
    }));
    localStorage.setItem(ringsKey(), JSON.stringify(data));
  }catch(e){}
}

const RINGS = [];
const ringGroups = {};

function layoutOrbitRingDefs(defs){
  const byMain = new Map(AI_MAIN_CATEGORIES.map(cat => [cat.id, []]));
  defs.forEach(def => {
    const bucket = byMain.get(def.mainId) || byMain.get(AI_MAIN_CATEGORIES[0].id);
    bucket.push(def);
  });

  const focusLayout = { r:1.46, base:[ 0.54, 1.02,-0.46], fan:[ 0.34,-0.24, 0.30] };

  const laidOut = [];
  const saturnBaseTilt = [0.62, 0.04, -0.02];
  AI_MAIN_CATEGORIES.forEach((main, mainIndex) => {
    const subs = byMain.get(main.id) || [];
    const centeredOffset = (subs.length - 1) / 2;
    const mainOffset = mainIndex - (AI_MAIN_CATEGORIES.length - 1) / 2;
    subs.forEach((def, subIndex) => {
      const subOffset = subIndex - centeredOffset;
      const focusRadius = focusLayout.r + subIndex * 0.09 + Math.abs(subOffset) * 0.012;
      const defaultRadius = 1.74 + mainIndex * 0.075;
      const focusTilt = [
        focusLayout.base[0] + focusLayout.fan[0] * subOffset,
        focusLayout.base[1] + focusLayout.fan[1] * subOffset,
        focusLayout.base[2] + focusLayout.fan[2] * subOffset,
      ];
      const defaultTilt = [
        saturnBaseTilt[0] + mainOffset * 0.010,
        saturnBaseTilt[1] + mainOffset * 0.004,
        saturnBaseTilt[2] + mainOffset * 0.003,
      ];
      laidOut.push({
        ...def,
        r: focusRadius,
        tilt: focusTilt,
        defaultR: defaultRadius,
        defaultTilt,
        defaultCenter: [
          0,
          mainOffset * 0.003,
          0,
        ],
        defaultPresence: 0,
        speed: RING_BASE_SPEED * Math.pow(RING_BASE_R / focusRadius, 1.38),
      });
    });
  });
  return laidOut;
}

function makeArcLine(radius, start, end, segments, color, opacity){
  const pts = [];
  for(let i=0;i<=segments;i++){
    const a = start + (end - start) * (i / segments);
    pts.push(new THREE.Vector3(Math.cos(a)*radius, 0, Math.sin(a)*radius));
  }
  const geo = new THREE.BufferGeometry().setFromPoints(pts);
  const mat = new THREE.LineBasicMaterial({
    color,
    transparent: true,
    opacity,
    blending: THREE.AdditiveBlending,
    depthTest: true,
    depthWrite: false,
  });
  return { line: new THREE.Line(geo, mat), mat };
}

function buildRing(def){
  const cfg = {
    id: def.id,
    mainId: def.mainId || def.id,
    label: def.label || def.id.toUpperCase(),
    labelCn: def.labelCn || '',
    r: def.r,
    color: new THREE.Color(def.color),
    tilt: new THREE.Euler(def.tilt[0], def.tilt[1], def.tilt[2]),
    focusR: def.r,
    focusTilt: new THREE.Euler(def.tilt[0], def.tilt[1], def.tilt[2]),
    defaultR: def.defaultR || def.r,
    defaultTilt: new THREE.Euler(...(def.defaultTilt || def.tilt)),
    focusCenter: new THREE.Vector3(0, 0, 0),
    defaultCenter: new THREE.Vector3(...(def.defaultCenter || [0, 0, 0])),
    defaultPresence: def.defaultPresence ?? 1,
    speed: def.speed,
  };
  const grp = new THREE.Group();
  grp.rotation.copy(cfg.defaultTilt);
  grp.position.copy(cfg.defaultCenter);
  const defaultScale = cfg.defaultR / cfg.focusR;
  grp.scale.setScalar(defaultScale);
  cfg._displayScale = defaultScale;
  // attach to whichever planet group is currently active so rings slide with the planet
  (currentTheme === 'bloom' ? groupBloom : groupOrbit).add(grp);
  ringGroups[cfg.id] = grp;

  const arcMats = [];
  const arcDefs = [
    [-0.12, 0.42, 0.035],
    [0.68, 1.02, 0.022],
    [1.38, 1.68, 0.014],
  ];
  const offset = strHash01(cfg.id) * Math.PI * 2;
  for(const [startTurn, endTurn, opacity] of arcDefs){
    const start = offset + startTurn * Math.PI * 2;
    const end = offset + endTurn * Math.PI * 2;
    const { line, mat } = makeArcLine(cfg.r, start, end, 72, cfg.color, opacity);
    grp.add(line);
    arcMats.push(mat);
  }

  const glowGeo = new THREE.RingGeometry(cfg.r-0.003, cfg.r+0.003, 256);
  const glowMat = new THREE.MeshBasicMaterial({ color: cfg.color, transparent:true, opacity: 0.003, side:THREE.DoubleSide, blending: THREE.AdditiveBlending, depthTest:true, depthWrite:false });
  const glow = new THREE.Mesh(glowGeo, glowMat);
  glow.rotation.x = Math.PI/2;
  grp.add(glow);

  const hlGeo = new THREE.RingGeometry(cfg.r-0.012, cfg.r+0.012, 256);
  const hlMat = new THREE.MeshBasicMaterial({ color: cfg.color, transparent:true, opacity: 0, side:THREE.DoubleSide, blending: THREE.AdditiveBlending, depthTest:true, depthWrite:false });
  const hl = new THREE.Mesh(hlGeo, hlMat);
  hl.rotation.x = Math.PI/2;
  grp.add(hl);

  const beaconMats = [];
  const beacons = Array.from({ length: 3 }, (_, i) => {
    const mat = new THREE.SpriteMaterial({
      map: spriteTex(),
      color: cfg.color,
      transparent: true,
      opacity: 0,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
    });
    const sp = new THREE.Sprite(mat);
    sp.userData = { isOrbitBeacon: true };
    sp.scale.set(0.14, 0.14, 0.14);
    grp.add(sp);
    beaconMats.push(mat);
    return {
      mesh: sp,
      mat,
      phase: offset + i * Math.PI * 2 / 3 + strHash01(`${cfg.id}:beacon:${i}`) * 0.42,
      speed: cfg.speed * (0.72 + i * 0.16),
    };
  });

  cfg._lineMats = arcMats;
  cfg._lineMat = arcMats[0];
  cfg._glowMat = glowMat;
  cfg._hlMat = hlMat;
  cfg._beacons = beacons;
  cfg._beaconMats = beaconMats;
  cfg._group = grp;
  RINGS.push(cfg);
  return cfg;
}

// Build initial rings from persisted defs (or defaults)
loadRingDefs().forEach(buildRing);

// ---------------- theme switcher ----------------
// Tears down rings + nodes for the outgoing theme, then rebuilds from the
// incoming theme's persisted state. Earth, atmosphere, and background fields
// are pre-built for both themes — we just toggle visibility.
// ---- diagonal-slide transition state ----
// Outgoing planet slides off along a diagonal vector, incoming planet slides
// in from the opposite diagonal. Data swap happens mid-flight while both
// planets are off-axis. The animation loop reads `slideAnim` each frame.
const SLIDE_DUR = 1100;
const SLIDE_OFF_X = 13;
const SLIDE_OFF_Y = 6;     // diagonal lift — outgoing rises, incoming drops in (or vice versa)
let slideAnim = null;

function parkInactivePlanet(){
  if(currentTheme === 'orbit'){
    groupOrbit.visible = true;  groupOrbit.position.set(0, 0, 0);
    groupBloom.visible = false; groupBloom.position.set(SLIDE_OFF_X, -SLIDE_OFF_Y, 0);
  } else {
    groupBloom.visible = true;  groupBloom.position.set(0, 0, 0);
    groupOrbit.visible = false; groupOrbit.position.set(-SLIDE_OFF_X, SLIDE_OFF_Y, 0);
  }
}
parkInactivePlanet();

function applyTheme(name, opts={}){
  if(!THEMES[name]) return;
  if(name === currentTheme && !opts.force) return;
  if(slideAnim) return; // ignore re-clicks during a transition

  // 1. save outgoing world's data
  saveRingDefs();
  saveState();

  // 2. keep side modules hidden during the diagonal swap so the outgoing
  // world's panel layout does not briefly flash the incoming world's modules.
  document.body.classList.add('theme-transition');
  const t = THEMES[name];
  const brandNameEl = document.querySelector('.hud .brand .name');
  const brandTagEl = document.querySelector('.hud .brand .tag');
  if(brandNameEl){
    const m = t.brandName.match(/^(.+?)\s*&\s*(.+)$/);
    brandNameEl.innerHTML = m
      ? `${m[1]} <span class="amp">&amp;</span> ${m[2]}`
      : t.brandName;
  }
  if(brandTagEl) brandTagEl.textContent = t.tagline;
  document.querySelectorAll('[data-theme-pill]').forEach(el => {
    el.classList.toggle('active', el.dataset.themePill === name);
  });
  applyLanguage();

  // 3. kick off diagonal slide — actual data swap happens at the midpoint
  // ORBIT → BLOOM: orbit slides up-left, bloom enters from down-right
  // BLOOM → ORBIT: bloom slides down-right, orbit enters from up-left
  slideAnim = {
    t0: performance.now(),
    dur: SLIDE_DUR,
    fromTheme: currentTheme,
    toTheme: name,
    swapped: false,
  };
  groupOrbit.visible = true;
  groupBloom.visible = true;
}

// Called at the midpoint of the slide — outgoing is offscreen, incoming is
// still offscreen on the other side. We tear down the outgoing rings/nodes,
// flip currentTheme, rebuild from the new theme's storage attached to the
// incoming planet group.
function performThemeSwap(toTheme){
  closeAiDatabase();

  // tear down rings + nodes (they were parented to the OUTGOING planet group)
  for(const n of memoryNodes){
    if(n.mesh.parent) n.mesh.parent.remove(n.mesh);
    n.mesh.material.dispose();
  }
  memoryNodes.length = 0;
  for(const cfg of RINGS){
    if(cfg._group){
      cfg._group.children.slice().forEach(ch => {
        cfg._group.remove(ch);
        if(ch.geometry) ch.geometry.dispose();
        if(ch.material) ch.material.dispose();
      });
      if(cfg._group.parent) cfg._group.parent.remove(cfg._group);
    }
    delete ringGroups[cfg.id];
  }
  RINGS.length = 0;
  activeCat = null;
  activeCatSet = null;

  currentTheme = toTheme;
  try{ localStorage.setItem('skill-current-theme', toTheme); }catch(e){}
  document.body.classList.toggle('theme-bloom', toTheme === 'bloom');
  document.body.classList.toggle('theme-orbit', toTheme === 'orbit');

  // rebuild rings + nodes for the new theme — buildRing reads currentTheme
  // and parents the new ring groups onto the correct planet group.
  loadRingDefs().forEach(buildRing);
  const saved = loadState();
  if(saved && Array.isArray(saved) && saved.length){
    saved.forEach(s => addNode({
      id: s.id, name: s.name, cat: s.cat, note: s.note || '',
      created: s.created || Date.now(), angle: s.angle, animateBirth: false
    }));
  }
  refreshUI();
  applyLanguage();
}
window.__applyTheme = applyTheme;

// Generate a new ring def with cosmic-physics-inspired params
function generateNewRingDef(label, labelCn){
  const id = 'cat_' + Date.now().toString(36) + '_' + Math.floor(Math.random()*1e4).toString(36);
  // outer radius: step from current outermost
  const maxR = RINGS.reduce((m,r)=>Math.max(m,r.r), RING_BASE_R);
  const r = maxR + RING_STEP + (Math.random()*0.08 - 0.04);
  // Kepler: ω ∝ r^(-3/2)
  const speed = RING_BASE_SPEED * Math.pow(RING_BASE_R / r, 1.5);
  const tilt = tiltFromId(id);
  // hue cycles by 47° per ring index (golden-ratio-ish, avoids collisions)
  const hue = (200 + RINGS.length * 47) % 360;
  const color = oklchToHex(0.78, 0.13, hue);
  return { id, label: (label||'').toUpperCase() || 'NEW', labelCn: labelCn||'', color, r, tilt, speed };
}

// ---- category focus state ----
let activeCat = null;
let activeCatSet = null;
function focusRingIds(id){
  if(!id) return null;
  const main = AI_MAIN_CATEGORIES.find(cat => cat.id === id);
  if(currentTheme === 'orbit' && main){
    return RINGS.filter(r => r.mainId === id).map(r => r.id);
  }
  return RINGS.find(r => r.id === id) ? [id] : null;
}
function isRingFocused(id){
  return !activeCatSet || activeCatSet.has(id);
}
function setActiveCategory(cat){
  activeCat = (activeCat === cat) ? null : cat;
  const ids = focusRingIds(activeCat);
  activeCatSet = ids ? new Set(ids) : null;
  // sync UI stat rows
  document.querySelectorAll('.panel .stat.cat').forEach(el=>{
    const c = el.dataset.focusCat || el.dataset.cat;
    const ringId = el.dataset.cat;
    const rowFocusesRing = ringId && activeCatSet?.has(ringId);
    el.classList.toggle('active', activeCat === c || rowFocusesRing);
    el.classList.toggle('dimmed', !!activeCat && !rowFocusesRing && activeCat !== c);
  });
}
window.__setActiveCategory = setActiveCategory;

// ---------------- stars on orbits (memory nodes) ----------------
// circular sprite texture, generated once
function spriteTex(){
  const c = document.createElement('canvas'); c.width=c.height=128;
  const ctx = c.getContext('2d');
  const g = ctx.createRadialGradient(64,64,0, 64,64,60);
  g.addColorStop(0,'rgba(255,255,255,1)');
  g.addColorStop(0.25,'rgba(255,255,255,0.9)');
  g.addColorStop(0.5,'rgba(255,255,255,0.35)');
  g.addColorStop(1,'rgba(255,255,255,0)');
  ctx.fillStyle = g; ctx.beginPath(); ctx.arc(64,64,60,0,Math.PI*2); ctx.fill();
  // cross flare
  ctx.globalAlpha = 0.6;
  ctx.fillStyle = 'rgba(255,255,255,1)';
  ctx.fillRect(63, 8, 2, 112);
  ctx.fillRect(8, 63, 112, 2);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  return t;
}
const STAR_TEX = spriteTex();

const memoryNodes = []; // { mesh, ring, angle, speed, name, cat, day, color, idx, id, note, created }

let _idCounter = 0;
function genId(){ return 'n_' + Date.now().toString(36) + '_' + (_idCounter++).toString(36); }

function addNode({ id, name, cat='craft', day=0, animateBirth=true, note='', created=Date.now(), angle, suppressSave=false }){
  const cfg = RINGS.find(r=>r.id===cat) || RINGS[0];
  if(!cfg) return null;
  const grp = ringGroups[cfg.id];

  const mat = new THREE.SpriteMaterial({
    map: STAR_TEX,
    color: cfg.color,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
  const sp = new THREE.Sprite(mat);
  const baseScale = 0.16;
  sp.scale.set(baseScale, baseScale, baseScale);
  sp.userData = { isNode: true };
  grp.add(sp);

  const node = {
    id: id || genId(),
    mesh: sp,
    ring: cfg,
    angle: angle != null ? angle : Math.random() * Math.PI * 2,
    speed: cfg.speed * (0.85 + Math.random()*0.3),
    name, cat, day,
    color: cfg.color,
    twinklePhase: Math.random()*Math.PI*2,
    born: performance.now(),
    animateBirth,
    idx: memoryNodes.length + 1,
    note: note || '',
    created,
  };
  memoryNodes.push(node);
  if(!suppressSave){
    refreshUI();
    saveState();
  }
  return node;
}

let deleteConfirmResolve = null;
function showDeleteConfirm(kind='node'){
  const modal = document.getElementById('delete-confirm');
  const message = document.getElementById('delete-confirm-message');
  const cancel = document.getElementById('delete-confirm-cancel');
  const ok = document.getElementById('delete-confirm-ok');
  if(!modal || !message || !cancel || !ok) return Promise.resolve(false);
  message.textContent = kind === 'archive' ? t('confirmDeleteArchive') : t('confirmDeleteNode');
  cancel.textContent = t('confirmCancel');
  ok.textContent = t('confirmDelete');
  modal.classList.add('show');
  modal.setAttribute('aria-hidden', 'false');
  ok.focus();
  return new Promise(resolve => {
    deleteConfirmResolve = resolve;
  });
}

function closeDeleteConfirm(result=false){
  const modal = document.getElementById('delete-confirm');
  if(modal){
    modal.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
  }
  if(deleteConfirmResolve){
    const resolve = deleteConfirmResolve;
    deleteConfirmResolve = null;
    resolve(result);
  }
}

document.getElementById('delete-confirm-cancel')?.addEventListener('click', ()=>closeDeleteConfirm(false));
document.getElementById('delete-confirm-ok')?.addEventListener('click', ()=>closeDeleteConfirm(true));
document.getElementById('delete-confirm')?.addEventListener('click', (e)=>{
  if(e.target?.id === 'delete-confirm') closeDeleteConfirm(false);
});
addEventListener('keydown', (e)=>{
  if(e.key === 'Escape' && deleteConfirmResolve) closeDeleteConfirm(false);
});

function removeNode(id){
  const i = memoryNodes.findIndex(n=>n.id===id);
  if(i<0) return;
  const n = memoryNodes[i];
  if(n.mesh.parent) n.mesh.parent.remove(n.mesh);
  n.mesh.material.dispose();
  memoryNodes.splice(i,1);
  // re-index
  memoryNodes.forEach((m, k)=> m.idx = k+1);
  refreshUI();
  saveState();
}

// ---------------- persistence ----------------
const STORE_KEY_BASE = 'skill-orbit-v5';
const storeKey = () => `${STORE_KEY_BASE}:${currentTheme}`;
function saveState(){
  try{
    const data = memoryNodes.map(n => ({
      id: n.id, name: n.name, cat: n.cat, note: n.note,
      created: n.created, angle: n.angle,
    }));
    localStorage.setItem(storeKey(), JSON.stringify(data));
  }catch(e){}
}
function loadState(){
  try{
    const raw = localStorage.getItem(storeKey());
    if(!raw) return null;
    return JSON.parse(raw);
  }catch(e){ return null; }
}

// ---------------- raycaster for hover ----------------
const ray = new THREE.Raycaster();
ray.params.Sprite = { threshold: 0.01 };
const _tmpV = new THREE.Vector3();
const mouse = new THREE.Vector2(-9, -9);
const tooltipEl = document.getElementById('tooltip');
let hovered = null;

addEventListener('pointermove', (e)=>{
  mouse.x = (e.clientX / innerWidth)*2 - 1;
  mouse.y = -(e.clientY / innerHeight)*2 + 1;
  tooltipEl.style.left = e.clientX + 'px';
  tooltipEl.style.top  = e.clientY + 'px';
});

function updateMouseFromEvent(e){
  mouse.x = (e.clientX / innerWidth)*2 - 1;
  mouse.y = -(e.clientY / innerHeight)*2 + 1;
}

function getLandingRingHit(){
  return null;
}

// ---------------- UI ----------------
const $ = (s)=>document.querySelector(s);
const feedEl = $('#feed');
const inputEl = $('#input');
const sendBtn = $('#send');
const skillListEl = $('#skill-list');
const skillUl = $('#skill-ul');
const API_BASE = 'http://127.0.0.1:8000/api/v1';
const AI_CATEGORY_FILTERS = [
  ['all', 'ALL'],
  ['ai-models', 'MODELS'],
  ['ai-coding', 'CODING'],
  ['ai-visual', 'VISUAL'],
  ['ai-media', 'MEDIA'],
  ['ai-office', 'OFFICE'],
  ['ai-research', 'RESEARCH'],
  ['ai-agent', 'AGENT'],
  ['ai-business', 'BIZ'],
];
const AI_CATEGORY_FILTERS_ZH = [
  ['all', '全部'],
  ['ai-models', '模型'],
  ['ai-coding', '编程'],
  ['ai-visual', '视觉'],
  ['ai-media', '媒体'],
  ['ai-office', '办公'],
  ['ai-research', '研究'],
  ['ai-agent', '智能体'],
  ['ai-business', '商业'],
];
const AI_STACK_FILTERS = [
  ['all', 'ALL'],
  ['creation', 'CREATION'],
  ['research', 'RESEARCH'],
  ['coding', 'CODING'],
  ['business', 'BUSINESS'],
  ['automation', 'AUTOMATION'],
  ['data-meeting', 'DATA/MEET'],
];
const AI_STACK_FILTERS_ZH = [
  ['all', '全部'],
  ['creation', '创作交付'],
  ['research', '研究知识'],
  ['coding', '编程开发'],
  ['business', '商务运营'],
  ['automation', '自动化'],
  ['data-meeting', '数据会议'],
];
const AI_STACK_GROUPS = {
  creation: new Set(['ai-office', 'ai-visual', 'ai-media']),
  research: new Set(['ai-research', 'ai-models']),
  coding: new Set(['ai-coding']),
  business: new Set(['ai-business']),
  automation: new Set(['ai-agent']),
  'data-meeting': new Set(['ai-business', 'ai-office']),
};

const AI_STACK_GROUP_LABELS_ZH = {
  creation: '创作交付',
  research: '研究知识',
  coding: '编程开发',
  business: '商务运营',
  automation: '自动化',
  'data-meeting': '数据会议',
};

const AI_STACK_GROUP_LABELS_EN = {
  creation: 'CREATION',
  research: 'RESEARCH',
  coding: 'CODING',
  business: 'BUSINESS',
  automation: 'AUTOMATION',
  'data-meeting': 'DATA / MEETING',
};

const AI_STACK_GROUP_ORDER = ['creation', 'research', 'coding', 'business', 'automation', 'data-meeting'];

const AI_SUBCATEGORY_LABELS_ZH = {
  'models-general-assistants': '通用助手',
  'models-reasoning-long-context': '长文推理',
  'models-chinese-ecosystem': '中文模型',
  'models-local-open-source': '本地模型',
  'coding-app-prototype': '应用原型',
  'coding-code-edit-review': '代码生成审查',
  'coding-devops-testing': '部署测试',
  'coding-data-backend': '后端数据',
  'visual-image-generation': '图像生成修图',
  'visual-brand-design': '品牌设计',
  'visual-ui-prototype': 'UI 产品稿',
  'visual-3d-assets': '3D 资产',
  'media-video-editing': '视频生成剪辑',
  'media-audio-voice-music': '音频语音',
  'media-avatar-livestream': '数字人直播',
  'media-social-publishing': '社媒发布',
  'office-ppt-decks': 'PPT 汇报',
  'office-doc-writing': '文档写作',
  'office-sheets-data': '表格数据',
  'office-meetings-knowledge': '会议知识',
  'research-web-search': '来源核查',
  'research-academic-literature': '论文文献',
  'research-market-competitive': '市场竞品',
  'research-data-reports': '数据报告',
  'agent-workflow-automation': '工作流自动化',
  'agent-browser-task': '浏览器任务',
  'agent-bots-rag': 'Bot 与 RAG',
  'agent-api-mcp-integrations': 'API 与 MCP',
  'business-marketing-growth': '营销增长',
  'business-sales-crm': '销售 CRM',
  'business-support-community': '客服社群',
  'business-ops-finance-legal': '运营法务',
  'business-ecommerce-product': '电商产品',
};

const AI_SUBCATEGORY_LABELS_EN = {
  'models-general-assistants': 'GENERAL AI',
  'models-reasoning-long-context': 'REASONING',
  'models-chinese-ecosystem': 'CHINESE MODELS',
  'models-local-open-source': 'LOCAL MODELS',
  'coding-app-prototype': 'APP PROTOTYPE',
  'coding-code-edit-review': 'CODE REVIEW',
  'coding-devops-testing': 'DEVOPS QA',
  'coding-data-backend': 'BACKEND API',
  'visual-image-generation': 'IMAGE EDIT',
  'visual-brand-design': 'BRAND DESIGN',
  'visual-ui-prototype': 'UI MOCKUP',
  'visual-3d-assets': '3D ASSETS',
  'media-video-editing': 'VIDEO EDIT',
  'media-audio-voice-music': 'AUDIO VOICE',
  'media-avatar-livestream': 'AVATAR LIVE',
  'media-social-publishing': 'SOCIAL PUBLISH',
  'office-ppt-decks': 'PPT DECKS',
  'office-doc-writing': 'DOC WRITING',
  'office-sheets-data': 'SHEETS DATA',
  'office-meetings-knowledge': 'MEETING NOTES',
  'research-web-search': 'SOURCE CHECK',
  'research-academic-literature': 'PAPERS',
  'research-market-competitive': 'MARKET INTEL',
  'research-data-reports': 'DATA REPORTS',
  'agent-workflow-automation': 'WORKFLOW AUTO',
  'agent-browser-task': 'BROWSER AGENT',
  'agent-bots-rag': 'BOT RAG',
  'agent-api-mcp-integrations': 'API MCP',
  'business-marketing-growth': 'MARKETING SEO',
  'business-sales-crm': 'SALES CRM',
  'business-support-community': 'SUPPORT',
  'business-ops-finance-legal': 'OPS LEGAL',
  'business-ecommerce-product': 'ECOM PRODUCT',
};

const AI_SUBCATEGORY_GROUP_LABELS_ZH = {
  'models-general-assistants': '通用问答',
  'models-reasoning-long-context': '长文推理',
  'models-chinese-ecosystem': '中文模型',
  'models-local-open-source': '本地模型',
  'coding-code-edit-review': '写代码 / 审代码',
  'coding-app-prototype': '做应用原型',
  'coding-data-backend': '接后端数据',
  'coding-devops-testing': '部署测试',
  'visual-image-generation': '生成 / 修图片',
  'visual-brand-design': '做品牌海报',
  'visual-ui-prototype': '做 UI 原型',
  'visual-3d-assets': '做 3D 资产',
  'media-video-editing': '做视频',
  'media-audio-voice-music': '配音 / 音乐',
  'media-avatar-livestream': '做数字人',
  'media-social-publishing': '发社媒',
  'office-ppt-decks': '做 PPT',
  'office-doc-writing': '写文档 / 翻译',
  'office-sheets-data': '做 Excel',
  'office-meetings-knowledge': '做会议纪要',
  'research-web-search': '查资料',
  'research-academic-literature': '查论文',
  'research-market-competitive': '做竞品研究',
  'research-data-reports': '做数据报告',
  'agent-api-mcp-integrations': '连 API / MCP',
  'agent-workflow-automation': '搭自动化流程',
  'agent-browser-task': '做网页任务',
  'agent-bots-rag': '搭 Bot / RAG',
  'business-marketing-growth': '做营销内容',
  'business-sales-crm': '找销售线索',
  'business-support-community': '做客服支持',
  'business-ops-finance-legal': '做法务运营',
  'business-ecommerce-product': '做电商运营',
};

const AI_SUBCATEGORY_GROUP_LABELS_EN = {
  'models-general-assistants': 'General Q&A',
  'models-reasoning-long-context': 'Long Reasoning',
  'models-chinese-ecosystem': 'Chinese Models',
  'models-local-open-source': 'Local Models',
  'coding-code-edit-review': 'Code / Review',
  'coding-app-prototype': 'App Prototype',
  'coding-data-backend': 'Backend Data',
  'coding-devops-testing': 'Deploy / Test',
  'visual-image-generation': 'Image / Retouch',
  'visual-brand-design': 'Brand Visuals',
  'visual-ui-prototype': 'UI Prototype',
  'visual-3d-assets': '3D Assets',
  'media-video-editing': 'Video',
  'media-audio-voice-music': 'Voice / Music',
  'media-avatar-livestream': 'Avatar Video',
  'media-social-publishing': 'Social Publish',
  'office-ppt-decks': 'Make PPT',
  'office-doc-writing': 'Docs / Translate',
  'office-sheets-data': 'Excel / Sheets',
  'office-meetings-knowledge': 'Meeting Notes',
  'research-web-search': 'Web Research',
  'research-academic-literature': 'Papers',
  'research-market-competitive': 'Competitors',
  'research-data-reports': 'Data Reports',
  'agent-api-mcp-integrations': 'API / MCP',
  'agent-workflow-automation': 'Automation Flow',
  'agent-browser-task': 'Browser Tasks',
  'agent-bots-rag': 'Bot / RAG',
  'business-marketing-growth': 'Marketing Content',
  'business-sales-crm': 'Sales Leads',
  'business-support-community': 'Support',
  'business-ops-finance-legal': 'Ops / Legal',
  'business-ecommerce-product': 'E-commerce Ops',
};

const AI_SUBCATEGORY_ORDER = {
  'ai-models': ['models-general-assistants', 'models-reasoning-long-context', 'models-chinese-ecosystem', 'models-local-open-source'],
  'ai-coding': ['coding-code-edit-review', 'coding-app-prototype', 'coding-data-backend', 'coding-devops-testing'],
  'ai-visual': ['visual-image-generation', 'visual-brand-design', 'visual-ui-prototype', 'visual-3d-assets'],
  'ai-media': ['media-video-editing', 'media-audio-voice-music', 'media-avatar-livestream', 'media-social-publishing'],
  'ai-office': ['office-ppt-decks', 'office-sheets-data', 'office-doc-writing', 'office-meetings-knowledge'],
  'ai-research': ['research-web-search', 'research-academic-literature', 'research-market-competitive', 'research-data-reports'],
  'ai-agent': ['agent-workflow-automation', 'agent-api-mcp-integrations', 'agent-browser-task', 'agent-bots-rag'],
  'ai-business': ['business-marketing-growth', 'business-sales-crm', 'business-ecommerce-product', 'business-support-community', 'business-ops-finance-legal'],
};

const AI_SUBCATEGORY_HINTS_ZH = {
  'models-general-assistants': '日常问答、拆任务、写草稿',
  'models-reasoning-long-context': '复杂推理、长资料、方案设计',
  'models-chinese-ecosystem': '中文写作、中文资料、多模态',
  'models-local-open-source': '本地运行、隐私数据、开源模型',
  'coding-code-edit-review': '写代码、改代码、审查 diff',
  'coding-app-prototype': '网页、SaaS、全栈原型',
  'coding-data-backend': '数据库、认证、API 接入',
  'coding-devops-testing': '部署、CI、测试和日志',
  'visual-image-generation': '出图、修图、参考图改造',
  'visual-brand-design': 'Logo、海报、品牌视觉',
  'visual-ui-prototype': '产品界面、网站、交互原型',
  'visual-3d-assets': '3D 模型和资产生成',
  'media-video-editing': '视频生成、剪辑、分镜',
  'media-audio-voice-music': '配音、音乐、录音清理',
  'media-avatar-livestream': '数字人口播和营销视频',
  'media-social-publishing': '社媒排程和发布',
  'office-ppt-decks': 'PPT、提案、商业汇报',
  'office-doc-writing': '文档、翻译、英文润色',
  'office-sheets-data': '表格分析、公式、图表',
  'office-meetings-knowledge': '会议纪要、资料问答、知识库',
  'research-web-search': '联网搜索、来源引用、事实核查',
  'research-academic-literature': '论文检索、证据、引用',
  'research-market-competitive': '竞品、关键词、市场情报',
  'research-data-reports': 'CSV、数据洞察、图表报告',
  'agent-api-mcp-integrations': 'API、MCP、外部工具连接',
  'agent-workflow-automation': '触发器、流程、应用集成',
  'agent-browser-task': '网页操作、表单、多步骤任务',
  'agent-bots-rag': '知识库 Bot、RAG、Agent 应用',
  'business-marketing-growth': '营销文案、SEO、增长内容',
  'business-sales-crm': '线索、CRM、销售外联',
  'business-support-community': '客服工单、知识库、支持',
  'business-ops-finance-legal': '合同、法务、运营辅助',
  'business-ecommerce-product': '店铺、商品、电商运营',
};

const TOOL_WEBSITES = {
  'chatgpt': 'https://chatgpt.com',
  'gpt-4': 'https://chatgpt.com',
  'gpt-4o': 'https://chatgpt.com',
  'openai': 'https://platform.openai.com',
  'claude': 'https://claude.ai',
  'claude api': 'https://console.anthropic.com',
  'claude code': 'https://www.anthropic.com/claude-code',
  'gemini': 'https://gemini.google.com',
  'perplexity': 'https://www.perplexity.ai',
  'cursor': 'https://cursor.com',
  'v0': 'https://v0.dev',
  'v0.dev': 'https://v0.dev',
  'bolt': 'https://bolt.new',
  'bolt.new': 'https://bolt.new',
  'lovable': 'https://lovable.dev',
  'replit': 'https://replit.com',
  'github': 'https://github.com',
  'github actions': 'https://github.com/features/actions',
  'copilot': 'https://github.com/features/copilot',
  'supabase': 'https://supabase.com',
  'firebase': 'https://firebase.google.com',
  'vercel': 'https://vercel.com',
  'netlify': 'https://www.netlify.com',
  'posthog': 'https://posthog.com',
  'stripe': 'https://stripe.com',
  'notion': 'https://www.notion.com',
  'notion ai': 'https://www.notion.com/product/ai',
  'confluence': 'https://www.atlassian.com/software/confluence',
  'slack': 'https://slack.com',
  'linear': 'https://linear.app',
  'figma': 'https://www.figma.com',
  'canva': 'https://www.canva.com',
  'gamma': 'https://gamma.app',
  'midjourney': 'https://www.midjourney.com',
  'runway': 'https://runwayml.com',
  'suno': 'https://suno.com',
  'elevenlabs': 'https://elevenlabs.io',
  'heygen': 'https://www.heygen.com',
  'buffer': 'https://buffer.com',
  'whisper': 'https://openai.com/research/whisper',
  'assemblyai': 'https://www.assemblyai.com',
  'opus clip': 'https://www.opus.pro',
  'submagic': 'https://www.submagic.co',
  'yt-dlp': 'https://github.com/yt-dlp/yt-dlp',
  'youtube': 'https://www.youtube.com',
  'deepL': 'https://www.deepl.com',
  'deepl': 'https://www.deepl.com',
  'zapier': 'https://zapier.com',
  'make': 'https://www.make.com',
  'make.com': 'https://www.make.com',
  'n8n': 'https://n8n.io',
  'dify': 'https://dify.ai',
  'coze': 'https://www.coze.com',
  'langchain': 'https://www.langchain.com',
  'llamaindex': 'https://www.llamaindex.ai',
  'llamaindex': 'https://www.llamaindex.ai',
  'qdrant': 'https://qdrant.tech',
  'pinecone': 'https://www.pinecone.io',
  'langfuse': 'https://langfuse.com',
  'hubspot': 'https://www.hubspot.com',
  'salesforce': 'https://www.salesforce.com',
  'apollo': 'https://www.apollo.io',
  'clay': 'https://www.clay.com',
  'intercom': 'https://www.intercom.com',
  'zendesk': 'https://www.zendesk.com',
  'shopify': 'https://www.shopify.com',
  'semrush': 'https://www.semrush.com',
  'ahrefs': 'https://ahrefs.com',
  'similarweb': 'https://www.similarweb.com',
  'notebooklm': 'https://notebooklm.google.com',
  'elicit': 'https://elicit.com',
  'consensus': 'https://consensus.app',
  'zotero': 'https://www.zotero.org',
  'julius': 'https://julius.ai',
  'otter': 'https://otter.ai',
  'fireflies': 'https://fireflies.ai',
  'granola': 'https://www.granola.ai',
  'outlook': 'https://outlook.live.com',
  'google calendar': 'https://calendar.google.com',
  'google docs': 'https://docs.google.com',
  'google sheets': 'https://sheets.google.com',
  'gmail': 'https://mail.google.com',
  'excel': 'https://www.microsoft.com/microsoft-365/excel',
  'power bi': 'https://www.microsoft.com/power-platform/products/power-bi',
};

function colorForCat(cat){
  const cfg = RINGS.find(r=>r.id===cat);
  if(cfg) return '#' + cfg.color.getHexString();
  return '#ffb066';
}

function renderCategoryRows(counts){
  const list = document.getElementById('cat-list');
  if(!list) return;
  if(currentTheme === 'orbit'){
    list.innerHTML = AI_MAIN_CATEGORIES.map(main => {
      const subs = RINGS.filter(r => r.mainId === main.id);
      const mainLabel = currentLang === 'zh' ? main.labelCn : main.label;
      const mainTitle = currentLang === 'zh'
        ? `点击聚焦 ${mainLabel} 下的 ${subs.length} 个小技能光环`
        : `Click to focus ${subs.length} ${main.label} sub-skill rings`;
      const subRows = subs.map(r => {
        const hex = '#' + r.color.getHexString();
        const label = currentLang === 'zh' ? (r.labelCn || displayCategoryLabel(r.label)) : r.label;
        const title = currentLang === 'zh' ? `点击只显示 ${label} 光环` : `Click to isolate the ${r.label} ring`;
        return `<div class="stat cat subcat" data-cat="${r.id}" data-focus-cat="${r.id}" title="${escapeHtml(title)}">
          <span class="k" style="color:${hex}">${escapeHtml(label)}</span>
        </div>`;
      }).join('');
      return `<div class="stat cat maincat" data-main-cat="${main.id}" data-focus-cat="${main.id}" title="${escapeHtml(mainTitle)}">
        <span class="k" style="color:${main.color}">${escapeHtml(mainLabel)}</span>
      </div>${subRows}`;
    }).join('');
  }else{
    // build rows for each ring in order
    list.innerHTML = RINGS.map(r => {
      const hex = '#' + r.color.getHexString();
      const label = currentLang === 'zh' ? displayCategoryLabel(r.label) : r.label;
      const title = currentLang === 'zh' ? `点击聚焦 ${label} 轨道` : `Click to focus the ${r.label} ring`;
      return `<div class="stat cat" data-cat="${r.id}" data-focus-cat="${r.id}" title="${escapeHtml(title)}">
        <span class="k" style="color:${hex}">${escapeHtml(label)}</span>
        <span class="right" style="display:flex; align-items:center; gap:4px;">
          <span class="v">${String(counts[r.id]||0).padStart(2,'0')}</span>
          ${RINGS.length > 1 ? `<button class="del-cat" data-del-cat="${r.id}" aria-label="delete category" title="${escapeHtml(currentLang === 'zh' ? '删除分类及其中所有节点' : 'Delete category and all its nodes')}">×</button>` : ''}
        </span>
      </div>`;
    }).join('');
  }
  // restore active state
  list.querySelectorAll('.stat.cat').forEach(el=>{
    const c = el.dataset.focusCat || el.dataset.cat;
    const ringId = el.dataset.cat;
    const rowFocusesRing = ringId && activeCatSet?.has(ringId);
    el.classList.toggle('active', activeCat === c || rowFocusesRing);
    el.classList.toggle('dimmed', !!activeCat && !rowFocusesRing && activeCat !== c);
  });
}

function refreshUI(){
  const counts = {};
  memoryNodes.forEach(n => counts[n.cat] = (counts[n.cat]||0)+1 );
  setStat('stat-total', currentTheme === 'orbit' ? AI_MAIN_CATEGORIES.length : memoryNodes.length);
  renderCategoryRows(counts);
  const tc = document.getElementById('ticker-count');
  if(tc) tc.textContent = String(memoryNodes.length).padStart(2,'0');

  // skill list
  skillListEl.classList.toggle('empty', memoryNodes.length === 0);
  const q = (window.__skillQuery || '').trim().toLowerCase();
  const recent = memoryNodes.slice().reverse();
  const filtered = q ? recent.filter(n => displayNodeName(n).toLowerCase().includes(q) || n.name.toLowerCase().includes(q) || (n.note||'').toLowerCase().includes(q)) : recent;
  skillListEl.classList.toggle('no-results', q !== '' && filtered.length === 0);
  skillUl.innerHTML = filtered.map(n => {
    const sw = colorForCat(n.cat);
    const hasNote = n.note && n.note.trim() ? '<span class="note-dot" title="Has notes"></span>' : '';
    return `<li data-id="${n.id}">
      <span class="idx">${String(n.idx).padStart(2,'0')}</span>
      <span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span>
      <span class="nm">${highlightMatch(displayNodeName(n), q)}</span>
      ${hasNote}
      <button class="del" data-del="${n.id}" aria-label="delete">×</button>
    </li>`;
  }).join('');
}
function highlightMatch(text, q){
  const safe = escapeHtml(text);
  if(!q) return safe;
  const lower = text.toLowerCase();
  let out = '';
  let i = 0;
  while(i < text.length){
    const idx = lower.indexOf(q, i);
    if(idx === -1){ out += escapeHtml(text.slice(i)); break; }
    out += escapeHtml(text.slice(i, idx));
    out += '<mark>' + escapeHtml(text.slice(idx, idx + q.length)) + '</mark>';
    i = idx + q.length;
  }
  return out;
}
function setStat(id, n){
  const el = document.getElementById(id);
  if(!el) return;
  el.querySelector('.v').textContent = String(n).padStart(2,'0');
  el.classList.add('flash');
  setTimeout(()=>el.classList.remove('flash'), 400);
}
function escapeHtml(s){
  return String(s || '').replace(/[&<>"']/g, m => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[m]));
}

function firstAiSkillWebsite(skill){
  return (skill?.examples || []).find(x => /^https?:\/\//i.test(String(x || '').trim())) || '';
}

function renderAiSkillWebsite(skill){
  const url = firstAiSkillWebsite(skill);
  if(!url) return '';
  return `<a class="site" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">官网 ↗</a>`;
}

function setText(selector, value){
  const el = document.querySelector(selector);
  if(el) el.textContent = value;
}

function setPlaceholder(selector, value){
  const el = document.querySelector(selector);
  if(el) el.placeholder = value;
}

function assistantIntroText(){
  return currentTheme === 'bloom' ? t('bloomChatIntro') : t('chatIntro');
}

function assistantPlaceholderText(){
  return currentTheme === 'bloom' ? t('bloomChatPlaceholder') : t('chatPlaceholder');
}

function applyLanguage(){
  document.documentElement.lang = currentLang === 'zh' ? 'zh-CN' : 'en';
  document.title = currentLang === 'zh' ? '技能星球 - AI 技能宇宙' : 'SKILL ORBIT - A Personal Universe of Skills';
  const brandNameEl = document.querySelector('.hud .brand .name');
  if(brandNameEl){
    brandNameEl.innerHTML = currentLang === 'zh'
      ? t('brand')
      : `Skill <span class="amp">&amp;</span> Orbit`;
  }
  setText('.hud .brand .tag', t('tagline'));
  setText('[data-theme-pill="orbit"] .lbl', t('orbit'));
  setText('[data-theme-pill="bloom"] .lbl', t('bloom'));
  setText('[data-theme-pill="orbit"] .cn', currentLang === 'zh' ? t('work') : 'work');
  setText('[data-theme-pill="bloom"] .cn', currentLang === 'zh' ? t('life') : 'life');
  setText('#lang-toggle', t('langToggle'));
  setText('.corner.tr .label', t('lat'));
  const topLabels = document.querySelectorAll('.corner.tr .label');
  if(topLabels[1]) topLabels[1].textContent = t('lon');
  if(topLabels[2]) topLabels[2].textContent = 'UTC';
  const br = document.querySelector('.corner.br');
  if(br){
    br.children[0].textContent = t('scrollHelp');
    br.children[1].innerHTML = `${escapeHtml(t('spaceHelpPrefix'))}<span style="color:var(--ink)">${escapeHtml(t('pause'))}</span>${escapeHtml(t('clickCategory'))}<span style="color:var(--ink)">${escapeHtml(t('solo'))}</span>`;
  }
  const pauseBadge = document.getElementById('pause-badge');
  if(pauseBadge){
    pauseBadge.innerHTML = `❚❚&nbsp; ${escapeHtml(t('paused'))} &nbsp;·&nbsp; <span style="color:var(--dim)">${escapeHtml(t('spaceToResume'))}</span>`;
  }
  setText('#archive-section h3', t('memoryArchive'));
  setText('#stat-total .k', t('total'));
  setText('#add-cat', t('newCategory'));
  setPlaceholder('#add-cat-name', t('categoryPlaceholder'));
  setText('.db-module .eyebrow', t('knowledgeBase'));
  const dbTitle = document.querySelector('.db-card .title');
  if(dbTitle) dbTitle.innerHTML = `${escapeHtml(t('dbEntryTitle'))} <span class="arrow">→</span>`;
  setText('.db-card .desc', t('dbEntryDesc'));
  setText('#skill-list h3', t('recentNodes'));
  setPlaceholder('#skill-search', t('searchNodes'));
  setText('#skill-no-match', t('noMatchingNodes'));
  setText('#ai-db h2', t('dbTitle'));
  setText('#ai-db .sub', t('dbSub'));
  setText('[data-db-type="skills"]', t('skills'));
  setText('[data-db-type="stacks"]', t('stacks'));
  const dbEmpty = document.querySelector('#ai-db-list .db-empty');
  if(dbEmpty && dbEmpty.textContent.includes('LOADING')) dbEmpty.textContent = t('loadingDatabase');
  setText('#auth-title', authMode === 'register' ? t('register') : t('login'));
  document.querySelectorAll('[data-auth-mode="login"]').forEach(el => el.textContent = t('login'));
  document.querySelectorAll('[data-auth-mode="register"]').forEach(el => el.textContent = t('register'));
  setText('label[for="auth-username"]', t('username'));
  setText('label[for="auth-email"]', t('email'));
  setText('label[for="auth-password"]', t('password'));
  if(authSubmit) authSubmit.textContent = authMode === 'register' ? t('register') : t('login');
  setText('.detail .head-tag', t('memoryNode'));
  setText('.detail label', t('howUse'));
  setPlaceholder('#detail-note', t('notePlaceholder'));
  const hint = document.querySelector('.detail .hint');
  if(hint) hint.innerHTML = `${escapeHtml(t('autosaved'))} · <span class="key">ESC</span> ${escapeHtml(t('escToClose'))}`;
  setText('#detail-delete', t('deleteNode'));
  setText('#delete-confirm-cancel', t('confirmCancel'));
  setText('#delete-confirm-ok', t('confirmDelete'));
  const chatLeft = document.querySelector('.chat .bar .left span:last-child');
  if(chatLeft) chatLeft.textContent = t('assistant');
  setText('.chat .feed .msg.system .who', t('system'));
  setText('.chat .feed .msg.system .body', assistantIntroText());
  setPlaceholder('#input', assistantPlaceholderText());
  setText('.tooltip .head', t('memoryNodeHead'));
  renderAuthWidget();
  renderAiDbTypeTabs();
}

const AUTH_TOKEN_KEY = 'skill-orbit-auth-token';
const AUTH_USER_KEY = 'skill-orbit-auth-user';
let authToken = localStorage.getItem(AUTH_TOKEN_KEY) || '';
let currentUser = (() => {
  try{ return JSON.parse(localStorage.getItem(AUTH_USER_KEY) || 'null'); }
  catch(e){ return null; }
})();

const authWidget = document.getElementById('auth-widget');
const langToggle = document.getElementById('lang-toggle');
const authModal = document.getElementById('auth-modal');
const authForm = document.getElementById('auth-form');
const authTitle = document.getElementById('auth-title');
const authClose = document.getElementById('auth-close');
const authUsername = document.getElementById('auth-username');
const authEmail = document.getElementById('auth-email');
const authEmailRow = document.getElementById('auth-email-row');
const authPassword = document.getElementById('auth-password');
const authSubmit = document.getElementById('auth-submit');
const authMessage = document.getElementById('auth-message');
let authMode = 'login';

function authHeaders(){
  return authToken ? { Authorization: `Bearer ${authToken}` } : {};
}

function renderAuthWidget(){
  if(!authWidget) return;
  if(currentUser){
    authWidget.innerHTML = `
      <button type="button" class="user-chip" id="auth-open-login">${escapeHtml(currentUser.username)}</button>
      <button type="button" id="auth-logout">${escapeHtml(t('logout'))}</button>
    `;
    document.getElementById('auth-open-login')?.addEventListener('click', ()=>openAuthModal('login'));
    document.getElementById('auth-logout')?.addEventListener('click', logoutUser);
  }else{
    authWidget.innerHTML = `
      <button type="button" id="auth-open-login">${escapeHtml(t('login'))}</button>
      <button type="button" id="auth-open-register">${escapeHtml(t('register'))}</button>
    `;
    document.getElementById('auth-open-login')?.addEventListener('click', ()=>openAuthModal('login'));
    document.getElementById('auth-open-register')?.addEventListener('click', ()=>openAuthModal('register'));
  }
}

function setAuthMode(mode){
  authMode = mode === 'register' ? 'register' : 'login';
  if(authTitle) authTitle.textContent = authMode === 'register' ? t('register') : t('login');
  if(authSubmit) authSubmit.textContent = authMode === 'register' ? t('register') : t('login');
  if(authEmailRow) authEmailRow.style.display = authMode === 'register' ? 'flex' : 'none';
  authModal?.querySelectorAll('[data-auth-mode]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.authMode === authMode);
  });
  if(authMessage){
    authMessage.textContent = authMode === 'register'
      ? t('authRegisterHint')
      : t('authLoginHint');
    authMessage.classList.remove('error');
  }
  if(authPassword) authPassword.autocomplete = authMode === 'register' ? 'new-password' : 'current-password';
}

function openAuthModal(mode='login', message=''){
  setAuthMode(mode);
  if(message && authMessage){
    authMessage.textContent = message;
    authMessage.classList.remove('error');
  }
  authModal?.classList.add('show');
  authModal?.setAttribute('aria-hidden', 'false');
  setTimeout(()=>authUsername?.focus(), 60);
}

function closeAuthModal(){
  authModal?.classList.remove('show');
  authModal?.setAttribute('aria-hidden', 'true');
}

function requireAuth(){
  if(currentUser) return true;
  openAuthModal('login', t('authFullService'));
  return false;
}

function requireDatabaseAuth(){
  if(currentUser) return true;
  openAuthModal('login', t('authDbRequired'));
  return false;
}

function saveAuthSession(payload){
  authToken = payload.access_token;
  currentUser = payload.user;
  localStorage.setItem(AUTH_TOKEN_KEY, authToken);
  localStorage.setItem(AUTH_USER_KEY, JSON.stringify(currentUser));
  renderAuthWidget();
}

function logoutUser(){
  authToken = '';
  currentUser = null;
  localStorage.removeItem(AUTH_TOKEN_KEY);
  localStorage.removeItem(AUTH_USER_KEY);
  renderAuthWidget();
}

async function authRequest(path, body){
  const res = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if(!res.ok){
    let detail = `${res.status} ${res.statusText}`;
    try{ detail = (await res.json()).detail || detail; }catch(e){}
    throw new Error(detail);
  }
  return res.json();
}

async function restoreAuthSession(){
  if(!authToken) return;
  try{
    const res = await fetch(`${API_BASE}/auth/me`, { headers: authHeaders() });
    if(!res.ok) throw new Error('session expired');
    currentUser = await res.json();
    localStorage.setItem(AUTH_USER_KEY, JSON.stringify(currentUser));
  }catch(e){
    logoutUser();
  }
  renderAuthWidget();
}

authModal?.querySelectorAll('[data-auth-mode]').forEach(btn => {
  btn.addEventListener('click', ()=>setAuthMode(btn.dataset.authMode));
});
langToggle?.addEventListener('click', ()=>{
  currentLang = currentLang === 'en' ? 'zh' : 'en';
  localStorage.setItem('skill-orbit-lang', currentLang);
  applyLanguage();
  refreshUI();
});
authClose?.addEventListener('click', closeAuthModal);
authModal?.addEventListener('click', (e)=>{ if(e.target === authModal) closeAuthModal(); });
authForm?.addEventListener('submit', async (e)=>{
  e.preventDefault();
  if(!authUsername || !authPassword) return;
  authSubmit.disabled = true;
  if(authMessage){
    authMessage.textContent = authMode === 'register' ? t('creatingAccount') : t('loggingIn');
    authMessage.classList.remove('error');
  }
  try{
    const payload = authMode === 'register'
      ? { username: authUsername.value.trim(), email: authEmail.value.trim(), password: authPassword.value }
      : { username: authUsername.value.trim(), password: authPassword.value };
    const session = await authRequest(authMode === 'register' ? '/auth/register' : '/auth/login', payload);
    saveAuthSession(session);
    closeAuthModal();
    authForm.reset();
  }catch(err){
    if(authMessage){
      authMessage.textContent = err.message || 'Auth failed';
      authMessage.classList.add('error');
    }
  }finally{
    authSubmit.disabled = false;
  }
});
renderAuthWidget();
restoreAuthSession();

function appendMsg(who, body, opts={}){
  const div = document.createElement('div');
  div.className = `msg ${who}`;
  const whoLabel = who === 'user'
    ? (currentLang === 'zh' ? '你' : 'YOU')
    : who === 'ai'
      ? (currentLang === 'zh' ? 'AI 助手' : 'ORBIT')
      : t('system');
  div.innerHTML = `<div class="who">${whoLabel}</div><div class="body"></div>`;
  div.querySelector('.body').innerHTML = body;
  feedEl.appendChild(div);
  feedEl.scrollTop = feedEl.scrollHeight;
  return div;
}

async function fetchJson(path, options={}){
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...authHeaders(), ...(options.headers || {}) },
    ...options,
  });
  if(!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.status === 204 ? null : res.json();
}

function normalizeAiSkillToNode(skill){
  const subLabel = skill.sub_skill_label || skill.category_label || '';
  return {
    id: skill.id,
    name: skill.name,
    cat: skill.sub_skill_id || skill.category_id,
    note: `${skill.tool || subLabel}${skill.description ? ' · ' + descriptionWithSubSkill(skill) : ''}`.trim(),
    created: skill.created_at ? Date.parse(skill.created_at) : Date.now(),
    animateBirth: false,
  };
}

function normalizeAiLibraryItemToNode(item){
  const ring = item?.sub_skill_id ? RINGS.find(r => r.id === item.sub_skill_id) : null;
  const subLabel = ring?.labelCn || item?.sub_skill_label || item?.category_label || '';
  const tools = Array.isArray(item?.tools) ? item.tools.slice(0, 3).join(' + ') : '';
  return {
    id: `library-${item.id}`,
    name: item.title,
    cat: item.sub_skill_id || item.category_id,
    note: `${tools || subLabel}${item.summary ? ' · ' + item.summary : ''}`.trim(),
    created: item.created_at ? Date.parse(item.created_at) : Date.now(),
    animateBirth: false,
  };
}

function displayRecommendationTitle(rec){
  if(rec?.item){
    return rec.source_type === 'skill' ? displaySkillName(rec.item) : displayLibraryTitle(rec.item);
  }
  return rec?.title || '';
}

function recommendationPurpose(rec){
  if(rec?.item && rec.source_type !== 'skill') return stackPurpose(rec.item);
  return rec?.summary || '';
}

function renderRecommendation(rec, index){
  const item = rec.item || rec;
  const sw = colorForCat(rec.sub_skill_id || rec.category_id);
  const tools = Array.isArray(rec.tools) && rec.tools.length
    ? rec.tools.slice(0, 5).map(displayLibraryChip).join(' + ')
    : '';
  const purpose = recommendationPurpose(rec);
  const typeLabel = rec.source_type === 'workflow'
    ? t('workflow')
    : rec.source_type === 'combination'
      ? t('integration')
      : t('skill');
  return `
    <div class="chat-rec" data-chat-source="${escapeHtml(rec.source_id)}">
      <div class="chat-rec-top">
        <span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span>
        <strong>${index + 1}. ${escapeHtml(displayRecommendationTitle(rec))}</strong>
        <span>${escapeHtml(typeLabel)} · ${Math.round((rec.score || 0) * 100)}%</span>
      </div>
      ${tools ? `<div class="chat-rec-tools">${escapeHtml(tools)}</div>` : ''}
      ${purpose ? `<div class="chat-rec-purpose">${escapeHtml(purpose)}</div>` : ''}
    </div>
  `;
}

function renderRecommendedPlan(plan, index){
  const rec = plan.recommendation || {};
  const sw = colorForCat(rec.sub_skill_id || rec.category_id);
  const tools = Array.isArray(rec.tools) && rec.tools.length
    ? rec.tools.slice(0, 5).map(displayLibraryChip).join(' + ')
    : '';
  const inputs = Array.isArray(plan.required_inputs) ? plan.required_inputs.slice(0, 4).join(', ') : '';
  const outputs = Array.isArray(plan.expected_outputs) ? plan.expected_outputs.slice(0, 4).join(', ') : '';
  return `
    <div class="chat-rec" data-chat-source="${escapeHtml(rec.source_id || '')}">
      <div class="chat-rec-label">${escapeHtml(plan.label || plan.plan_type || '')}</div>
      <div class="chat-rec-top">
        <span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span>
        <strong>${index + 1}. ${escapeHtml(displayRecommendationTitle(rec))}</strong>
        <span>${Math.round((plan.score || rec.score || 0) * 100)}%</span>
      </div>
      ${tools ? `<div class="chat-rec-tools">${escapeHtml(tools)}</div>` : ''}
      ${plan.reason ? `<div class="chat-rec-reason">${escapeHtml(plan.reason)}</div>` : ''}
      ${plan.best_for ? `<div class="chat-rec-purpose"><strong>${escapeHtml(t('bestFor'))}:</strong> ${escapeHtml(plan.best_for)}</div>` : ''}
      ${inputs ? `<div class="chat-rec-small">${escapeHtml(t('needs'))}: ${escapeHtml(inputs)}</div>` : ''}
      ${outputs ? `<div class="chat-rec-small">${escapeHtml(t('outputs'))}: ${escapeHtml(outputs)}</div>` : ''}
    </div>
  `;
}

function highlightRecommendationNodes(recommendations){
  (recommendations || []).forEach(rec => {
    const nodeId = rec.source_type === 'skill' ? rec.source_id : `library-${rec.source_id}`;
    const node = memoryNodes.find(n => n.id === nodeId || n.id === rec.source_id);
    if(node) node._selected = true;
    setTimeout(()=>{ if(node) node._selected = false; }, 2400);
  });
}

function practicalSkillScore(skill){
  const text = `${skill.name || ''} ${skill.tool || ''} ${skill.stage || ''} ${skill.description || ''} ${(skill.tags || []).join(' ')}`.toLowerCase();
  let score = Number(skill.importance || 0);
  if(skill.is_core) score += 140;
  if(skill.tool) score += 18;
  if(/workflow|automation|agent|mcp|api|ppt|deck|report|data|code|review|meeting|search|video|image|crm|rag/i.test(text)) score += 12;
  if(/入门|概念|theory|principle|overview/i.test(text)) score -= 8;
  return score;
}

function practicalLibraryScore(item){
  const text = `${item.title || ''} ${item.summary || ''} ${(item.tools || []).join(' ')} ${(item.steps || []).join(' ')} ${(item.outputs || []).join(' ')} ${(item.tags || []).join(' ')}`.toLowerCase();
  let score = Number(item.importance || 0);
  if(item.item_type === 'workflow') score += 28;
  if(/workflow|流程|组合|sop|mcp|rag|ppt|report|dashboard|automation|agent|code|video|image|crm|meeting/i.test(text)) score += 14;
  return score;
}

function representativeItemsBySubSkill(skills, libraryItems=[]){
  const grouped = new Map(RINGS.map(r => [r.id, { skills: [], library: [] }]));
  for(const skill of skills || []){
    const subId = skill.sub_skill_id || skill.category_id;
    if(grouped.has(subId)) grouped.get(subId).skills.push(skill);
  }
  for(const item of libraryItems || []){
    const subId = item.sub_skill_id || item.category_id;
    if(grouped.has(subId)) grouped.get(subId).library.push(item);
  }
  const selected = [];
  for(const ring of RINGS){
    const bucket = grouped.get(ring.id) || { skills: [], library: [] };
    const skillNodes = bucket.skills
      .sort((a, b) => practicalSkillScore(b) - practicalSkillScore(a) || String(a.name || '').localeCompare(String(b.name || '')))
      .slice(0, 3)
      .map(normalizeAiSkillToNode);
    const libraryNodes = bucket.library
      .sort((a, b) => practicalLibraryScore(b) - practicalLibraryScore(a) || String(a.title || '').localeCompare(String(b.title || '')))
      .slice(0, Math.max(0, 3 - skillNodes.length))
      .map(normalizeAiLibraryItemToNode);
    const chosen = [...skillNodes, ...libraryNodes].slice(0, 3);
    const ringIndex = RINGS.indexOf(ring);
    chosen.forEach((node, index) => {
      const base = (ringIndex * Math.PI * (3 - Math.sqrt(5)) + strHash01(`${ring.id}:anchor`) * 0.65) % (Math.PI * 2);
      const spread = chosen.length === 1 ? Math.PI : (Math.PI * 2) / chosen.length;
      selected.push({ ...node, angle: base + index * spread + ringIndex * 0.11 });
    });
  }
  return selected;
}

function categoryMetaLabel(item){
  const main = displayCategoryLabel(item?.category_label || '');
  const sub = item?.sub_skill_id
    ? aiSkillSubCategoryLabel(item.sub_skill_id)
    : (item?.sub_skill_label || '');
  return sub ? `${main} · ${sub}` : main;
}

function descriptionWithSubSkill(skill){
  if(!skill?.sub_skill_label) return skill?.description || '';
  return `${skill.sub_skill_label} · ${skill.description || ''}`.trim();
}

function replaceOrbitWithRepresentativeItems(skills, libraryItems=[]){
  if(currentTheme !== 'orbit') return;
  if((!Array.isArray(skills) || !skills.length) && (!Array.isArray(libraryItems) || !libraryItems.length)) return;
  memoryNodes.slice().forEach(n => {
    if(n.mesh.parent) n.mesh.parent.remove(n.mesh);
    n.mesh.material.dispose();
  });
  memoryNodes.length = 0;
  representativeItemsBySubSkill(skills, libraryItems).forEach(node => addNode({ ...node, suppressSave: true }));
  saveState();
  refreshUI();
}

async function loadCoreSkillsFromBackend(){
  try{
    const [skills, libraryItems] = await Promise.all([
      fetchJson('/ai-skills?limit=2000'),
      fetchJson('/ai-skills/library?limit=2000'),
    ]);
    replaceOrbitWithRepresentativeItems(skills, libraryItems);
  }catch(e){
    // Static seed keeps the globe usable when the backend is not running.
  }
}

const aiDbDrawer = document.getElementById('ai-db');
const aiDbOpen = document.getElementById('open-ai-db');
const aiDbClose = document.getElementById('ai-db-close');
const aiDbSearch = document.getElementById('ai-db-search');
const aiDbTypeTabs = document.getElementById('ai-db-type-tabs');
const aiDbFilter = document.getElementById('ai-db-filter');
const aiDbList = document.getElementById('ai-db-list');
let aiDbType = 'skills';
let aiDbCategory = 'all';
let aiDbSubCategory = 'all';
let aiDbExpandedGroup = '';
let aiDbSkills = [];
let aiDbLibraryItems = [];

function isStackType(){
  return aiDbType === 'stacks' || aiDbType === 'combination' || aiDbType === 'workflow';
}

function stackGroupForItem(item){
  const source = String(item?.source_section || '').toLowerCase();
  const title = String(item?.title || '');
  const hay = `${title} ${(item?.tags || []).join(' ')} ${(item?.steps || []).join(' ')} ${(item?.outputs || []).join(' ')}`.toLowerCase();
  if(/编程|coding|code|cursor|github|repo|agentaudit|swe-ci|codex|claude code/.test(hay)) return 'coding';
  if(/研究|research|report|paper|论文|知识|notebook|perplexity|elicit|zotero/.test(hay)) return 'research';
  if(/自动化|automation|workflow|n8n|zapier|make|servicenow|agent|bot|mcp/.test(hay)) return 'automation';
  if(/数据|会议|meeting|sales call|granola|tactiq|hubspot|crm|finance|财务|客服|销售|商务|business|support/.test(hay)) return 'data-meeting';
  if(/社媒|写作|设计|音视频|ppt|提案|deck|video|audio|canva|gamma|media|visual|office/.test(hay)) return 'creation';
  if(source.includes('china_ai_tool') && item?.category_id === 'ai-business') return 'business';
  if(AI_STACK_GROUPS.business.has(item?.category_id)) return 'business';
  if(AI_STACK_GROUPS.creation.has(item?.category_id)) return 'creation';
  if(AI_STACK_GROUPS.research.has(item?.category_id)) return 'research';
  if(AI_STACK_GROUPS.automation.has(item?.category_id)) return 'automation';
  return 'business';
}

function stackCategoryMatches(item){
  if(aiDbCategory === 'all') return true;
  return stackGroupForItem(item) === aiDbCategory;
}

function aiSkillSubCategoryLabel(subId){
  const mapped = currentLang === 'zh'
    ? (AI_SUBCATEGORY_GROUP_LABELS_ZH[subId] || AI_SUBCATEGORY_LABELS_ZH[subId])
    : (AI_SUBCATEGORY_GROUP_LABELS_EN[subId] || AI_SUBCATEGORY_LABELS_EN[subId]);
  if(mapped) return mapped;
  const ring = RINGS.find(r => r.id === subId);
  if(ring){
    return currentLang === 'zh' ? (ring.labelCn || ring.label) : ring.label;
  }
  return titleFromSlug(subId);
}

function aiSkillSubCategoryHint(subId){
  if(currentLang === 'zh') return AI_SUBCATEGORY_HINTS_ZH[subId] || aiSkillSubCategoryLabel(subId);
  return aiSkillSubCategoryLabel(subId);
}

function aiSkillSubCategoryOptions(categoryId){
  if(!Array.isArray(aiDbSkills) || !aiDbSkills.length) return [];
  const present = new Set(
    aiDbSkills
      .filter(skill => skill.category_id === categoryId && skill.sub_skill_id)
      .map(skill => skill.sub_skill_id)
  );
  const preferred = AI_SUBCATEGORY_ORDER[categoryId] || RINGS.filter(ring => ring.mainId === categoryId).map(ring => ring.id);
  const ordered = preferred
    .filter(id => present.has(id))
    .map(id => [id, aiSkillSubCategoryLabel(id)]);
  const orderedIds = new Set(ordered.map(([id]) => id));
  const extras = [...present]
    .filter(id => !orderedIds.has(id))
    .sort()
    .map(id => [id, aiSkillSubCategoryLabel(id)]);
  return [...ordered, ...extras];
}

function aiMainCategoryLabel(categoryId){
  const main = AI_MAIN_CATEGORIES.find(item => item.id === categoryId);
  if(!main) return displayCategoryLabel(categoryId);
  return currentLang === 'zh' ? main.labelCn : main.label;
}

function aiMainCategoryOrder(categoryId){
  const index = AI_MAIN_CATEGORIES.findIndex(item => item.id === categoryId);
  return index === -1 ? 999 : index;
}

function aiSubCategoryOrder(categoryId, subId){
  const options = aiSkillSubCategoryOptions(categoryId);
  const index = options.findIndex(([id]) => id === subId);
  return index === -1 ? 999 : index;
}

function renderAiSkillCard(skill){
  return `
    <article class="db-skill" data-ai-skill="${escapeHtml(skill.id)}">
      <div class="top">
        <span>${escapeHtml(displaySkillName(skill))}</span>
        ${skill.is_core ? `<span class="core">${escapeHtml(t('core'))}</span>` : ''}
      </div>
      <div class="meta">${escapeHtml(categoryMetaLabel(skill))} · ${escapeHtml(skill.tool || t('tool'))} · ${escapeHtml(translateText(skill.stage || t('stage')))}</div>
      <div class="desc">${escapeHtml(displaySkillDescription(skill))}</div>
      <div class="actions">${renderAiSkillWebsite(skill)}</div>
    </article>
  `;
}

function renderAiSkillSubGroup(categoryId, subId, skills){
  const title = aiSkillSubCategoryLabel(subId || categoryId);
  const hint = aiSkillSubCategoryHint(subId || categoryId);
  const groupId = `${categoryId}::${subId || categoryId}`;
  const isOpen = aiDbExpandedGroup === groupId || !!(aiDbSearch?.value || '').trim();
  const actionLabel = currentLang === 'zh' ? (isOpen ? '收起' : '展开') : (isOpen ? 'COLLAPSE' : 'EXPAND');
  return `
    <section class="db-skill-group ${isOpen ? 'open' : ''}" data-ai-group="${escapeHtml(groupId)}">
      <button type="button" class="db-skill-group-head" data-ai-group-toggle="${escapeHtml(groupId)}" aria-expanded="${isOpen ? 'true' : 'false'}">
        <div>
          <div class="db-skill-group-title">${escapeHtml(title)}</div>
          <div class="db-skill-group-hint">${escapeHtml(hint)}</div>
        </div>
        <span class="db-skill-group-meta">
          <span class="db-skill-group-count">${String(skills.length).padStart(2, '0')}</span>
          <span class="db-skill-group-action">${escapeHtml(actionLabel)}</span>
        </span>
      </button>
      <div class="db-skill-group-body">
        ${skills.map(renderAiSkillCard).join('')}
      </div>
    </section>
  `;
}

function renderAiSkillGroups(skills){
  const sorted = skills.slice().sort((a, b) =>
    aiMainCategoryOrder(a.category_id) - aiMainCategoryOrder(b.category_id) ||
    aiSubCategoryOrder(a.category_id, a.sub_skill_id) - aiSubCategoryOrder(b.category_id, b.sub_skill_id) ||
    Number(b.importance || 0) - Number(a.importance || 0) ||
    displaySkillName(a).localeCompare(displaySkillName(b))
  );

  const byCategory = new Map();
  sorted.forEach(skill => {
    const categoryId = skill.category_id || 'unknown';
    if(!byCategory.has(categoryId)) byCategory.set(categoryId, []);
    byCategory.get(categoryId).push(skill);
  });

  return [...byCategory.entries()].map(([categoryId, categorySkills]) => {
    const bySub = new Map();
    categorySkills.forEach(skill => {
      const subId = skill.sub_skill_id || categoryId;
      if(!bySub.has(subId)) bySub.set(subId, []);
      bySub.get(subId).push(skill);
    });
    const subSections = [...bySub.entries()].map(([subId, subSkills]) =>
      renderAiSkillSubGroup(categoryId, subId, subSkills)
    ).join('');
    if(aiDbCategory !== 'all') return subSections;
    return `
      <section class="db-main-group">
        <div class="db-main-group-title">${escapeHtml(aiMainCategoryLabel(categoryId))}</div>
        ${subSections}
      </section>
    `;
  }).join('');
}

function stackMainGroupLabel(groupId){
  return currentLang === 'zh'
    ? (AI_STACK_GROUP_LABELS_ZH[groupId] || groupId)
    : (AI_STACK_GROUP_LABELS_EN[groupId] || titleFromSlug(groupId).toUpperCase());
}

function stackMainGroupOrder(groupId){
  const index = AI_STACK_GROUP_ORDER.indexOf(groupId);
  return index === -1 ? 999 : index;
}

function stackSubGroupForItem(item){
  return item?.sub_skill_id || stackGroupForItem(item);
}

function stackSubGroupLabel(subId){
  return aiSkillSubCategoryLabel(subId);
}

function stackSubGroupHint(subId){
  return aiSkillSubCategoryHint(subId);
}

function normalizeToolKey(value){
  return String(value || '')
    .trim()
    .toLowerCase()
    .replace(/[（(].*?[)）]/g, '')
    .replace(/\s+/g, ' ');
}

function toolWebsite(tool){
  const key = normalizeToolKey(tool);
  if(TOOL_WEBSITES[key]) return TOOL_WEBSITES[key];
  const compact = key.replace(/[^a-z0-9]+/g, '');
  const hit = Object.keys(TOOL_WEBSITES).find(name => name.replace(/[^a-z0-9]+/g, '') === compact);
  return hit ? TOOL_WEBSITES[hit] : '';
}

function cleanLibrarySentence(value){
  return String(value || '')
    .replace(/^来自《[^》]+》的工具组合[:：]\s*/i, '')
    .replace(/^来自《[^》]+》的项目工作流[:：]\s*/i, '')
    .replace(/^来自[^:：]+[:：]\s*/i, '')
    .replace(/工具分工[:：]\s*/g, '')
    .replace(/；/g, '； ')
    .replace(/\s+/g, ' ')
    .trim();
}

function stackPurpose(item){
  const title = displayLibraryTitle(item);
  const tools = (item.tools || []).slice(0, 4).map(displayLibraryChip).join(' + ');
  const sub = stackSubGroupLabel(stackSubGroupForItem(item));
  if(currentLang === 'zh'){
    return `目的：用${tools ? ` ${tools} ` : ' AI 工具'}完成「${title}」，适合${sub}场景。`;
  }
  return `Purpose: use ${tools || 'AI tools'} to complete "${title}" for ${sub} work.`;
}

function stackTutorialSteps(item){
  const rawSteps = (item.steps || []).map(step => cleanLibrarySentence(displayLibraryChip(step))).filter(Boolean);
  if(rawSteps.length) return rawSteps.slice(0, 5);
  const tools = (item.tools || []).slice(0, 5).map(displayLibraryChip).filter(Boolean);
  if(currentLang === 'zh'){
    return [
      '先明确目标、输入素材、交付格式和限制。',
      tools.length ? `按顺序使用 ${tools.join(' → ')} 处理核心任务。` : '按工作流顺序处理核心任务。',
      '检查结果是否可交付，补齐缺口和人工判断。',
      '导出、发布或交给下一个系统继续执行。',
    ];
  }
  return [
    'Define the goal, inputs, output format, and constraints.',
    tools.length ? `Run the workflow through ${tools.join(' → ')}.` : 'Run the workflow in order.',
    'Review the result, fill gaps, and add human judgment.',
    'Export, publish, or hand off to the next system.',
  ];
}

function renderStackTutorial(item){
  return stackTutorialSteps(item)
    .map((step, index) => `<div><span>${index + 1}</span>${escapeHtml(step)}</div>`)
    .join('');
}

function stackToolLinks(item){
  const seen = new Set();
  return (item.tools || [])
    .map(tool => [displayLibraryChip(tool), toolWebsite(tool)])
    .filter(([label, url]) => {
      if(!url || seen.has(url)) return false;
      seen.add(url);
      return true;
    })
    .slice(0, 8);
}

function renderStackToolLinks(item){
  const links = stackToolLinks(item);
  if(!links.length) return `<span class="db-no-link">${escapeHtml(currentLang === 'zh' ? '暂无官网链接' : 'No official link yet')}</span>`;
  return links.map(([label, url]) =>
    `<a class="site" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(label)} ↗</a>`
  ).join('');
}

function renderAiLibraryCard(item){
  return `
    <article class="db-skill workflow-card" data-ai-library="${escapeHtml(item.id)}">
      <div class="top">
        <span>${escapeHtml(displayLibraryTitle(item))}</span>
        <span class="core">${escapeHtml(t('stacks'))}</span>
      </div>
      <div class="meta">${escapeHtml(categoryMetaLabel(item) || displayCategoryLabel(item.category_label || t('aiLibrary')))} · ${escapeHtml(item.item_type === 'workflow' ? t('workflow') : t('integration'))}</div>
      <div class="workflow-detail">
        <div class="workflow-label">${escapeHtml(currentLang === 'zh' ? '目的' : 'Purpose')}</div>
        <div class="workflow-text">${escapeHtml(stackPurpose(item))}</div>
      </div>
      <div class="workflow-detail">
        <div class="workflow-label">${escapeHtml(currentLang === 'zh' ? '使用教程' : 'How to use')}</div>
        <div class="workflow-steps">${renderStackTutorial(item)}</div>
      </div>
      <div class="workflow-detail">
        <div class="workflow-label">${escapeHtml(currentLang === 'zh' ? '官网' : 'Official sites')}</div>
        <div class="actions">${renderStackToolLinks(item)}</div>
      </div>
    </article>
  `;
}

function renderAiLibrarySubGroup(mainGroup, subId, items){
  const groupId = `stack::${mainGroup}::${subId || mainGroup}`;
  const isOpen = aiDbExpandedGroup === groupId || !!(aiDbSearch?.value || '').trim();
  const actionLabel = currentLang === 'zh' ? (isOpen ? '收起' : '展开') : (isOpen ? 'COLLAPSE' : 'EXPAND');
  return `
    <section class="db-skill-group ${isOpen ? 'open' : ''}" data-ai-group="${escapeHtml(groupId)}">
      <button type="button" class="db-skill-group-head" data-ai-group-toggle="${escapeHtml(groupId)}" aria-expanded="${isOpen ? 'true' : 'false'}">
        <div>
          <div class="db-skill-group-title">${escapeHtml(stackSubGroupLabel(subId || mainGroup))}</div>
          <div class="db-skill-group-hint">${escapeHtml(stackSubGroupHint(subId || mainGroup))}</div>
        </div>
        <span class="db-skill-group-meta">
          <span class="db-skill-group-count">${String(items.length).padStart(2, '0')}</span>
          <span class="db-skill-group-action">${escapeHtml(actionLabel)}</span>
        </span>
      </button>
      <div class="db-skill-group-body">
        ${items.map(renderAiLibraryCard).join('')}
      </div>
    </section>
  `;
}

function renderAiLibraryGroups(items){
  const sorted = items.slice().sort((a, b) => {
    const groupA = stackGroupForItem(a);
    const groupB = stackGroupForItem(b);
    return stackMainGroupOrder(groupA) - stackMainGroupOrder(groupB) ||
      aiSubCategoryOrder(a.category_id, stackSubGroupForItem(a)) - aiSubCategoryOrder(b.category_id, stackSubGroupForItem(b)) ||
      practicalLibraryScore(b) - practicalLibraryScore(a) ||
      displayLibraryTitle(a).localeCompare(displayLibraryTitle(b));
  });

  const byMain = new Map();
  sorted.forEach(item => {
    const main = stackGroupForItem(item);
    if(!byMain.has(main)) byMain.set(main, []);
    byMain.get(main).push(item);
  });

  return [...byMain.entries()].map(([mainGroup, groupItems]) => {
    const bySub = new Map();
    groupItems.forEach(item => {
      const subId = stackSubGroupForItem(item);
      if(!bySub.has(subId)) bySub.set(subId, []);
      bySub.get(subId).push(item);
    });
    const subSections = [...bySub.entries()].map(([subId, subItems]) =>
      renderAiLibrarySubGroup(mainGroup, subId, subItems)
    ).join('');
    if(aiDbCategory !== 'all') return subSections;
    return `
      <section class="db-main-group">
        <div class="db-main-group-title">${escapeHtml(stackMainGroupLabel(mainGroup))}</div>
        ${subSections}
      </section>
    `;
  }).join('');
}

function renderAiDbTypeTabs(){
  if(!aiDbTypeTabs) return;
  aiDbTypeTabs.querySelectorAll('[data-db-type]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.dbType === aiDbType);
  });
  if(aiDbSearch){
    aiDbSearch.placeholder = aiDbType === 'skills'
      ? t('searchSkills')
      : t('searchStacks');
  }
}

function renderAiDbFilters(){
  if(!aiDbFilter) return;
  const filters = aiDbType === 'skills'
    ? (currentLang === 'zh' ? AI_CATEGORY_FILTERS_ZH : AI_CATEGORY_FILTERS)
    : (currentLang === 'zh' ? AI_STACK_FILTERS_ZH : AI_STACK_FILTERS);
  const mainButtons = filters.map(([id, label]) =>
    `<button type="button" data-ai-cat="${id}" class="${aiDbCategory === id ? 'active' : ''}">${escapeHtml(label)}</button>`
  ).join('');
  aiDbSubCategory = 'all';
  aiDbFilter.innerHTML = `<div class="db-filter-row">${mainButtons}</div>`;
}

function renderAiDbList(){
  if(!aiDbList) return;
  const q = (aiDbSearch?.value || '').trim().toLowerCase();
  const previousScroll = aiDbList.scrollTop || 0;
  if(aiDbType === 'skills'){
    if(q) aiDbExpandedGroup = '';
    const filtered = aiDbSkills.filter(skill => {
      const catOk = aiDbCategory === 'all' || skill.category_id === aiDbCategory;
      if(!catOk) return false;
      if(!q) return true;
      const hay = `${skill.name} ${skill.tool} ${skill.category_label} ${skill.sub_skill_label} ${skill.stage} ${skill.description} ${(skill.tags||[]).join(' ')} ${(skill.examples||[]).join(' ')}`.toLowerCase();
      return hay.includes(q);
    });
    if(!filtered.length){
      aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(t('noMatchingSkills'))}</div>`;
      return;
    }
    aiDbList.innerHTML = renderAiSkillGroups(filtered);
    aiDbList.scrollTop = previousScroll;
    return;
  }

  const filtered = aiDbLibraryItems.filter(item => {
    const catOk = stackCategoryMatches(item);
    if(!catOk) return false;
    if(!q) return true;
    const hay = `${item.title} ${item.category_label} ${item.summary} ${(item.tools||[]).join(' ')} ${(item.steps||[]).join(' ')} ${(item.outputs||[]).join(' ')} ${(item.tags||[]).join(' ')}`.toLowerCase();
    return hay.includes(q);
  });
  if(!filtered.length){
    aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(t('noMatchingType', aiDbType))}</div>`;
    return;
  }
  aiDbList.innerHTML = renderAiLibraryGroups(filtered);
  aiDbList.scrollTop = previousScroll;
}

async function loadAiDatabase(){
  if(!aiDbList) return;
  if(currentTheme !== 'orbit'){
    aiDbSkills = [];
    aiDbLibraryItems = [];
    renderAiDbFilters();
    aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(currentLang === 'zh' ? 'Bloom 数据库会单独建立' : 'Bloom database is separate and empty for now.')}</div>`;
    return;
  }
  aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(t('loadingDatabase'))}</div>`;
  try{
    renderAiDbTypeTabs();
    if(aiDbType === 'skills'){
      aiDbSkills = await fetchJson('/ai-skills?limit=2000');
    }else{
      aiDbLibraryItems = await fetchJson('/ai-skills/library?limit=2000');
    }
    renderAiDbFilters();
    renderAiDbList();
  }catch(e){
    aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(t('startBackend'))}</div>`;
  }
}

function openAiDatabase(){
  if(!requireDatabaseAuth()) return;
  if(currentTheme !== 'orbit') return;
  if(!aiDbDrawer) return;
  aiDbDrawer.classList.add('show');
  document.body.classList.add('ai-db-open');
  aiDbDrawer.setAttribute('aria-hidden', 'false');
  loadAiDatabase();
  setTimeout(()=>aiDbSearch?.focus(), 80);
}

function closeAiDatabase(){
  if(!aiDbDrawer) return;
  aiDbDrawer.classList.remove('show');
  document.body.classList.remove('ai-db-open');
  aiDbDrawer.setAttribute('aria-hidden', 'true');
}

aiDbOpen?.addEventListener('click', openAiDatabase);
aiDbClose?.addEventListener('click', closeAiDatabase);
aiDbSearch?.addEventListener('input', renderAiDbList);
aiDbTypeTabs?.addEventListener('click', (e)=>{
  const btn = e.target.closest('[data-db-type]');
  if(!btn) return;
  aiDbType = btn.dataset.dbType;
  aiDbCategory = 'all';
  aiDbSubCategory = 'all';
  aiDbExpandedGroup = '';
  if(aiDbSearch) aiDbSearch.value = '';
  loadAiDatabase();
});
aiDbFilter?.addEventListener('click', (e)=>{
  const btn = e.target.closest('[data-ai-cat]');
  if(!btn) return;
  aiDbCategory = btn.dataset.aiCat;
  aiDbSubCategory = 'all';
  aiDbExpandedGroup = '';
  renderAiDbFilters();
  renderAiDbList();
});
aiDbList?.addEventListener('click', (e)=>{
  const btn = e.target.closest('[data-ai-group-toggle]');
  if(!btn) return;
  const groupId = btn.dataset.aiGroupToggle || '';
  aiDbExpandedGroup = aiDbExpandedGroup === groupId ? '' : groupId;
  renderAiDbList();
  if(aiDbExpandedGroup){
    requestAnimationFrame(() => {
      aiDbList.querySelector(`[data-ai-group="${CSS.escape(aiDbExpandedGroup)}"]`)?.scrollIntoView({ block:'nearest', behavior:'smooth' });
    });
  }
});

// classify a skill (heuristic fallback if AI fails)
function heuristicClassify(text){
  const s = text.toLowerCase();
  // legacy keyword sets — only useful if the corresponding category still exists
  const tables = {
    craft: ['code','coding','program','framework','css','html','js','javascript','react','vue','python','algorithm','function','api','debug','tool','software','design','engineering','vim','git','sql'],
    theory: ['principle','theory','proof','derivation','bayes','physics','chemistry','biology','philosophy','concept','logic','math','formula','history','economic','politic'],
    life: ['cook','cooking','coffee','tea','recipe','running','yoga','sleep','communication','relationship','emotion','parenting','travel','photography','music','instrument']
  };
  for(const [id, words] of Object.entries(tables)){
    if(RINGS.find(r=>r.id===id) && words.some(k=>s.includes(k))) return id;
  }
  return RINGS[0] ? RINGS[0].id : 'craft';
}

function heuristicBloomClassify(text){
  const s = text.toLowerCase();
  const tables = {
    forge: [
      'learned','made','built','created','cooked','baked','recipe','dish','paint','draw','write','repair','organize',
      '学会','做','制作','完成','写','画','修','整理','收纳','做饭','做菜','红烧','排骨','烘焙','拍照','手工'
    ],
    rest: [
      'sleep','rest','walk','run','yoga','meditation','health','workout','relax','habit','mood',
      '睡','休息','散步','跑步','瑜伽','冥想','运动','健身','放松','情绪','习惯','早起'
    ],
    kin: [
      'friend','family','partner','relationship','date','talk','call','message','gift','meet',
      '朋友','家人','男朋友','女朋友','伴侣','关系','聊天','沟通','约会','见面','送礼','聚会'
    ],
  };
  for(const [id, words] of Object.entries(tables)){
    if(RINGS.find(r=>r.id===id) && words.some(k=>s.includes(k))) return id;
  }
  return RINGS.find(r=>r.id==='forge') ? 'forge' : (RINGS[0]?.id || 'forge');
}

function extractBloomNoteName(text){
  let name = text.trim()
    .replace(/^[\s"'“”‘’]+|[\s"'“”‘’。.!！?？]+$/g, '')
    .replace(/^(今天|昨天|刚刚|最近|这周|周末|我|俺|本人|we|i)\s*/i, '')
    .replace(/^(今天|昨天|刚刚|最近|这周|周末|我|俺|本人)\s*/i, '')
    .replace(/^(已经|终于|刚|新)?\s*(学会了|学会|会了|会|完成了|完成|做了|做出|做完了|做完|记录一下|记一下)\s*/i, '')
    .replace(/^(i|we)\s+(learned|learnt|made|finished|completed|cooked|built|created)\s+/i, '');
  name = name.replace(/^(做|制作|完成)\s*/, '').trim();
  name = name.trim();
  if(!name) name = text.trim();
  return name.length > 32 ? name.slice(0, 32) : name;
}

async function classifyBloomNote(text){
  const cat = heuristicBloomClassify(text);
  const name = extractBloomNoteName(text);
  const cfg = RINGS.find(r=>r.id===cat);
  const catLabel = cfg ? displayCategoryLabel(cfg.label) : cat.toUpperCase();
  const oneLine = currentLang === 'zh'
    ? `已归类到 ${catLabel}，并添加为生活 note。`
    : `Filed under ${catLabel} and added as a life note.`;
  return { name, cat, note: text, oneLine };
}

async function classifyWithAI(text){
  const cats = RINGS.map(r => ({ id: r.id, label: r.label, cn: r.labelCn }));
  const validIds = cats.map(c => c.id);
  // graceful fallback if running outside the host environment (no window.claude)
  if(typeof window === 'undefined' || !window.claude || typeof window.claude.complete !== 'function'){
    return { name: text.length > 32 ? text.slice(0,32) : text, cat: heuristicClassify(text), oneLine: t('loggedOrbit') };
  }
  const catBlock = cats.map(c => `- ${c.id} (${c.label})`).join('\n');
  const idsLine = validIds.join('|');
  const prompt = `User said: "${text}"

Extract the specific skill/idea being learned and assign it to one of these categories:
${catBlock}

Return ONLY a JSON object, no extra prose, in exactly this shape:
{"name":"<a short skill name, 3-8 words>","cat":"${idsLine}","oneLine":"<one short encouraging sentence in English, max ~16 words, optionally hint at where to use it>"}`;
  try{
    const res = await window.claude.complete(prompt);
    const m = res.match(/\{[\s\S]*\}/);
    if(!m) throw new Error('no json');
    const parsed = JSON.parse(m[0]);
    if(!validIds.includes(parsed.cat)) parsed.cat = heuristicClassify(text);
    if(!parsed.name) parsed.name = text.slice(0, 32);
    return parsed;
  }catch(e){
    return {
      name: text.slice(0, 32),
      cat: heuristicClassify(text),
      oneLine: t('loggedMemoryOrbit')
    };
  }
}

async function handleSend(){
  const text = inputEl.value.trim();
  if(!text) return;
  if(!requireAuth()){
    appendMsg('ai', escapeHtml(t('authFullService')));
    inputEl.focus();
    return;
  }
  inputEl.value = '';
  sendBtn.disabled = true;

  appendMsg('user', escapeHtml(text));

  // typing indicator
  const ind = appendMsg('ai', `<span class="dots">${escapeHtml(t('parsing'))}</span>`);
  const dots = ind.querySelector('.dots');
  let d=0; const tID = setInterval(()=>{ d=(d+1)%4; dots.textContent=t('parsing')+'.'.repeat(d) }, 220);

  if(currentTheme === 'bloom'){
    const parsed = await classifyBloomNote(text);
    clearInterval(tID);
    ind.remove();
    const cfg = RINGS.find(r=>r.id===parsed.cat);
    const catLabel = cfg ? displayCategoryLabel(cfg.label) : displayCategoryLabel(parsed.cat.toUpperCase());
    const sw = colorForCat(parsed.cat);
    appendMsg('ai',
      `${escapeHtml(parsed.oneLine)}<br/>
       <span class="pill"><span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span> ${escapeHtml(t('addNodeLabel'))} · <code>${escapeHtml(catLabel)}</code></span>
       <div style="margin-top:6px; color:var(--dim); font-family:JetBrains Mono,monospace; font-size:10px; letter-spacing:0.2em;">→ ${escapeHtml(parsed.name)}</div>`
    );
    addNode({ name: parsed.name, cat: parsed.cat, note: parsed.note, day: 0, animateBirth: true });
    sendBtn.disabled = false;
    inputEl.focus();
    return;
  }

  try{
    const plan = await fetchJson('/ai-skills/recommend', {
      method: 'POST',
      body: JSON.stringify({ query: text, top_k: 3 }),
    });
    clearInterval(tID);
    ind.remove();
    const plans = Array.isArray(plan?.plans) ? plan.plans : [];
    if(plans.length){
      appendMsg('ai',
        `${escapeHtml(t('foundPlans', plans.length))}<br/>` +
        plans.map(renderRecommendedPlan).join('')
      );
      highlightRecommendationNodes(plans.map(p => p.recommendation).filter(Boolean));
    } else {
      appendMsg('ai', escapeHtml(t('noDirectMatch')));
    }
    sendBtn.disabled = false;
    inputEl.focus();
    return;
  }catch(e){
    // If the backend is unavailable, fall back to the old local node parser.
  }

  const parsed = await classifyWithAI(text);
  clearInterval(tID);

  // remove the indicator and replace
  ind.remove();
  const cfg = RINGS.find(r=>r.id===parsed.cat);
  const catLabel = cfg ? displayCategoryLabel(cfg.label) : displayCategoryLabel(parsed.cat.toUpperCase());
  const sw = colorForCat(parsed.cat);
  appendMsg('ai',
    `${escapeHtml(parsed.oneLine || t('loggedMemoryOrbit'))}<br/>
     <span class="pill"><span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span> ${escapeHtml(t('addNodeLabel'))} · <code>${escapeHtml(catLabel)}</code></span>
     <div style="margin-top:6px; color:var(--dim); font-family:JetBrains Mono,monospace; font-size:10px; letter-spacing:0.2em;">→ ${escapeHtml(parsed.name)}</div>`
  );

  addNode({ name: parsed.name, cat: parsed.cat, day: 0, animateBirth: true });

  sendBtn.disabled = false;
  inputEl.focus();
}

sendBtn.addEventListener('click', handleSend);
inputEl.addEventListener('keydown', (e)=>{
  if(e.key === 'Enter') handleSend();
});

// click on skill list -> open detail card; or delete via × button
skillUl.addEventListener('click', async (e)=>{
  const delBtn = e.target.closest('button.del');
  if(delBtn){
    e.stopPropagation();
    const id = delBtn.dataset.del;
    const n = memoryNodes.find(x=>x.id===id); if(!n) return;
    const ok = await showDeleteConfirm('node');
    if(!ok) return;
    flyOutAndRemove(n);
    return;
  }
  const li = e.target.closest('li'); if(!li) return;
  const id = li.dataset.id;
  const n = memoryNodes.find(x=>x.id===id); if(!n) return;
  openDetail(n);
});

function flyOutAndRemove(n){
  // brief fade-out animation
  const start = performance.now();
  const dur = 380;
  const baseS = n.mesh.scale.x;
  function step(){
    const t = Math.min(1, (performance.now()-start)/dur);
    const s = baseS * (1 - t) + 0.001;
    n.mesh.scale.set(s,s,s);
    n.mesh.material.opacity = 1 - t;
    if(t<1) requestAnimationFrame(step);
    else removeNode(n.id);
  }
  step();
}

// ---------- detail card ----------
const detailEl = document.getElementById('detail');
const detailName = document.getElementById('detail-name');
const detailMeta = document.getElementById('detail-meta');
const detailNote = document.getElementById('detail-note');
const detailSwatch = document.getElementById('detail-swatch');
let openNode = null;

function openDetail(n){
  openNode = n;
  detailName.textContent = displayNodeName(n);
  const cfg = RINGS.find(r=>r.id===n.cat);
  const catName = cfg ? displayCategoryLabel(cfg.label) : displayCategoryLabel(n.cat.toUpperCase());
  const catCn = cfg && cfg.labelCn ? cfg.labelCn : '';
  const catLabel = currentLang === 'zh' ? catName : (catCn ? `${catName} · ${catCn}` : catName);
  const dateStr = new Date(n.created || Date.now()).toLocaleDateString('zh-CN');
  detailMeta.innerHTML = `<span>${escapeHtml(catLabel)}</span><span class="sep">·</span><span>${currentLang === 'zh' ? '节点' : 'NODE'} ${String(n.idx).padStart(3,'0')}</span><span class="sep">·</span><span>${dateStr}</span>`;
  const sw = colorForCat(n.cat);
  detailSwatch.style.background = sw;
  detailSwatch.style.boxShadow = `0 0 16px ${sw}`;
  detailNote.value = n.note || '';
  detailEl.classList.add('show');
  setTimeout(()=> detailNote.focus(), 240);

  // briefly enlarge that star to show selection
  n._selected = true;
}
function closeDetail(){
  if(openNode){
    openNode.note = detailNote.value;
    openNode._selected = false;
    saveState();
    refreshUI();
  }
  openNode = null;
  detailEl.classList.remove('show');
}
document.getElementById('detail-close').addEventListener('click', closeDetail);
document.getElementById('detail-delete').addEventListener('click', async ()=>{
  if(!openNode) return;
  const ok = await showDeleteConfirm('node');
  if(!ok) return;
  const n = openNode;
  closeDetail();
  flyOutAndRemove(n);
});
detailNote.addEventListener('input', ()=>{
  if(!openNode) return;
  openNode.note = detailNote.value;
  // debounced save
  clearTimeout(openNode._saveT);
  openNode._saveT = setTimeout(saveState, 400);
});
addEventListener('keydown', (e)=>{
  if(e.key === 'Escape' && openNode) closeDetail();
});

// click on canvas to open node
renderer.domElement.addEventListener('click', (e)=>{
  updateMouseFromEvent(e);
  const landingMainId = getLandingRingHit();
  if(landingMainId){
    setActiveCategory(landingMainId);
    return;
  }

  ray.setFromCamera(mouse, camera);
  const hits = ray.intersectObjects(memoryNodes.map(n=>n.mesh), false);
  if(hits.length){
    const node = memoryNodes.find(n=>n.mesh===hits[0].object);
    if(node) openDetail(node);
  }
});

// ---------- collapse toggle ----------
const recentToggle = document.getElementById('recent-toggle');
if(recentToggle){
  recentToggle.addEventListener('click', ()=>{
    skillListEl.classList.toggle('collapsed');
    recentToggle.textContent = skillListEl.classList.contains('collapsed') ? '+' : '−';
  });
}
const archiveSection = document.getElementById('archive-section');
const archiveToggle = document.getElementById('archive-toggle');
if(archiveToggle && archiveSection){
  archiveToggle.addEventListener('click', ()=>{
    archiveSection.classList.toggle('collapsed');
    archiveToggle.textContent = archiveSection.classList.contains('collapsed') ? '+' : '−';
  });
}

// ---------- recent nodes search ----------
const skillSearchEl = document.getElementById('skill-search');
const skillSearchClear = document.getElementById('skill-search-clear');
if(skillSearchEl){
  skillSearchEl.addEventListener('input', ()=>{
    const v = skillSearchEl.value;
    window.__skillQuery = v;
    skillListEl.classList.toggle('has-query', v.length > 0);
    refreshUI();
  });
  skillSearchEl.addEventListener('keydown', (e)=>{
    if(e.key === 'Escape'){
      skillSearchEl.value = '';
      window.__skillQuery = '';
      skillListEl.classList.remove('has-query');
      refreshUI();
      skillSearchEl.blur();
    }
  });
}
if(skillSearchClear){
  skillSearchClear.addEventListener('click', ()=>{
    skillSearchEl.value = '';
    window.__skillQuery = '';
    skillListEl.classList.remove('has-query');
    refreshUI();
    skillSearchEl.focus();
  });
}

// ---------- chat collapse toggle ----------
const chatEl = document.getElementById('chat');
const chatToggle = document.getElementById('chat-toggle');
if(chatToggle && chatEl){
  // restore persisted state
  try{
    if(localStorage.getItem('chatCollapsed') === '1'){
      chatEl.classList.add('collapsed');
      chatToggle.textContent = '+';
    }
  }catch(e){}
  chatToggle.addEventListener('click', ()=>{
    chatEl.classList.toggle('collapsed');
    const isCollapsed = chatEl.classList.contains('collapsed');
    chatToggle.textContent = isCollapsed ? '+' : '−';
    try{ localStorage.setItem('chatCollapsed', isCollapsed ? '1' : '0'); }catch(e){}
  });
}

// ---------- category list: click/dblclick/rename + add/delete via delegation ----------
(function(){
  const list = document.getElementById('cat-list');
  if(!list) return;
  const catClickTimer = { id: null };

  list.addEventListener('click', (e)=>{
    const delBtn = e.target.closest('[data-del-cat]');
    if(delBtn){
      e.stopPropagation();
      const cat = delBtn.dataset.delCat;
      deleteCategory(cat);
      return;
    }
    const row = e.target.closest('.stat.cat'); if(!row) return;
    const k = row.querySelector('.k');
    if(k && k.isContentEditable) return;
    if(catClickTimer.id) return;
    catClickTimer.id = setTimeout(()=>{
      catClickTimer.id = null;
      const cat = row.dataset.focusCat || row.dataset.cat;
      if(typeof window.__setActiveCategory === 'function') window.__setActiveCategory(cat);
    }, 220);
  });

  list.addEventListener('dblclick', (e)=>{
    const row = e.target.closest('.stat.cat'); if(!row) return;
    if(currentTheme === 'orbit') return;
    if(catClickTimer.id){ clearTimeout(catClickTimer.id); catClickTimer.id = null; }
    e.preventDefault();
    const k = row.querySelector('.k'); if(!k) return;
    k.setAttribute('contenteditable', 'true');
    k.focus();
    const range = document.createRange();
    range.selectNodeContents(k);
    const sel = window.getSelection();
    sel.removeAllRanges(); sel.addRange(range);

    const cleanup = ()=>{
      k.removeEventListener('blur', onBlur);
      k.removeEventListener('keydown', onKey);
    };
    const commit = (cancel)=>{
      const cat = row.dataset.cat;
      const cfg = RINGS.find(r=>r.id===cat);
      k.removeAttribute('contenteditable');
      if(!cancel && cfg){
        const txt = (k.textContent || '').trim().toUpperCase();
        if(txt) cfg.label = txt;
        saveRingDefs();
      }
      cleanup();
      refreshUI();
      if(typeof openNode !== 'undefined' && openNode && detailEl.classList.contains('show')) openDetail(openNode);
    };
    const onBlur = ()=> commit(false);
    const onKey = (ev)=>{
      if(ev.key === 'Enter'){ ev.preventDefault(); commit(false); }
      if(ev.key === 'Escape'){ ev.preventDefault(); commit(true); }
    };
    k.addEventListener('blur', onBlur);
    k.addEventListener('keydown', onKey);
  });
})();

// ---------- delete category ----------
async function deleteCategory(catId){
  if(RINGS.length <= 1){ alert(t('keepOneCategory')); return; }
  const cfg = RINGS.find(r=>r.id===catId); if(!cfg) return;
  const ok = await showDeleteConfirm('archive');
  if(!ok) return;

  memoryNodes.filter(n=>n.cat===catId).forEach(n => {
    if(n.mesh && n.mesh.parent) n.mesh.parent.remove(n.mesh);
    if(n.mesh && n.mesh.material) n.mesh.material.dispose();
  });
  for(let i = memoryNodes.length - 1; i >= 0; i--){
    if(memoryNodes[i].cat === catId) memoryNodes.splice(i, 1);
  }
  memoryNodes.forEach((n, idx) => {
    n.idx = idx + 1;
  });
  // remove ring visuals
  if(cfg._group){
    cfg._group.children.slice().forEach(ch => {
      cfg._group.remove(ch);
      if(ch.geometry) ch.geometry.dispose();
      if(ch.material) ch.material.dispose();
    });
    if(cfg._group.parent) cfg._group.parent.remove(cfg._group);
  }
  if(ringGroups[catId]) delete ringGroups[catId];
  const idx = RINGS.indexOf(cfg);
  if(idx >= 0) RINGS.splice(idx, 1);
  if(activeCat === catId){
    activeCat = null;
    activeCatSet = null;
  }
  saveRingDefs();
  saveState();
  refreshUI();
}

// ---------- add new category ----------
(function(){
  const btn = document.getElementById('add-cat');
  const wrap = document.getElementById('add-cat-input');
  const input = document.getElementById('add-cat-name');
  if(!btn || !wrap || !input) return;
  let cancelTimer = null;
  btn.addEventListener('click', ()=>{
    if(!requireAuth()) return;
    btn.classList.add('editing');
    wrap.classList.add('show');
    input.value = '';
    input.focus();
  });
  const cancel = ()=>{
    btn.classList.remove('editing');
    wrap.classList.remove('show');
    input.value = '';
  };
  const commit = ()=>{
    const raw = input.value.trim();
    if(!raw){ cancel(); return; }
    let label = raw, labelCn = '';
    const m = raw.match(/^(.+?)\s*[·•\-—|/]\s*(.+)$/);
    if(m){ label = m[1].trim(); labelCn = m[2].trim(); }
    label = label.toUpperCase();
    const def = generateNewRingDef(label, labelCn);
    buildRing(def);
    saveRingDefs();
    cancel();
    refreshUI();
  };
  input.addEventListener('keydown', (e)=>{
    if(e.key === 'Enter'){ e.preventDefault(); commit(); }
    if(e.key === 'Escape'){ e.preventDefault(); cancel(); }
  });
  input.addEventListener('blur', ()=>{
    cancelTimer = setTimeout(()=>{ if(document.activeElement !== input) cancel(); }, 120);
  });
  input.addEventListener('focus', ()=>{ if(cancelTimer){ clearTimeout(cancelTimer); cancelTimer = null; } });
})();

// ---------- node name editing in detail dialog ----------
(function(){
  const nameEl = document.getElementById('detail-name');
  if(!nameEl) return;
  const commitName = ()=>{
    if(!openNode) return;
    const v = (nameEl.textContent || '').trim();
    if(v && v !== openNode.name){
      openNode.name = v;
      saveState();
      refreshUI();
    } else {
      nameEl.textContent = openNode.name;
    }
  };
  nameEl.addEventListener('blur', commitName);
  nameEl.addEventListener('keydown', (e)=>{
    if(e.key === 'Enter'){ e.preventDefault(); nameEl.blur(); }
    if(e.key === 'Escape'){
      e.preventDefault();
      if(openNode) nameEl.textContent = displayNodeName(openNode);
      nameEl.blur();
    }
  });
  // prevent newlines on paste
  nameEl.addEventListener('paste', (e)=>{
    e.preventDefault();
    const t = (e.clipboardData || window.clipboardData).getData('text').replace(/\s+/g, ' ').trim();
    document.execCommand('insertText', false, t);
  });
})();

// ---------------- seed nodes ----------------
const saved = loadState();
if(saved && Array.isArray(saved) && saved.length){
  saved.forEach(s => addNode({
    id: s.id, name: s.name, cat: s.cat, note: s.note || '',
    created: s.created || Date.now(), angle: s.angle, animateBirth: false
  }));
} else if(currentTheme === 'orbit') {
  try{
    const seed = JSON.parse(document.getElementById('seed-skills').textContent);
    seed.forEach(s => addNode({ id: s.id, name: s.name, cat: s.cat, day: s.day, animateBirth: false }));
  }catch(e){}
}
loadCoreSkillsFromBackend();

// ---------------- HUD live values ----------------
function pad(n,l=2){ return String(n).padStart(l,'0') }
function tickHud(){
  const d = new Date();
  document.getElementById('hud-utc').textContent =
    `${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}:${pad(d.getUTCSeconds())}`;
  // pseudo lat/lon based on camera
  const e = new THREE.Euler().setFromQuaternion(camera.quaternion, 'YXZ');
  const lat = THREE.MathUtils.radToDeg(-e.x);
  const lon = THREE.MathUtils.radToDeg(-e.y);
  document.getElementById('hud-lat').textContent = `${lat>=0?'+':''}${lat.toFixed(2)}°`;
  document.getElementById('hud-lon').textContent = `${lon>=0?'+':''}${lon.toFixed(2)}°`;
}
setInterval(tickHud, 250); tickHud();

// ---------------- resize ----------------
addEventListener('resize', ()=>{
  camera.aspect = innerWidth/innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});

// ---------------- animate ----------------
// Global motion controls — give the user calm anchors when density is high.
// 1. Spacebar toggles a hard pause (visualises "world frozen").
// 2. Hovering a node smoothly decelerates everything to 25% speed so the
//    user can read what they're pointing at without it sliding away.
// 3. When a category is solo'd, only that ring's nodes keep moving;
//    the others freeze at their current angle and dim.
let isPaused = false;
let motionScale = 1; // smoothed multiplier toward target speed (0..1)
addEventListener('keydown', (e)=>{
  if(e.key === ' ' && document.activeElement !== inputEl &&
     document.activeElement !== detailNote && !document.activeElement?.isContentEditable){
    e.preventDefault();
    isPaused = !isPaused;
    const badge = document.getElementById('pause-badge');
    if(badge) badge.style.opacity = isPaused ? '1' : '0';
  }
});

let last = performance.now();
function animate(now){
  const dt = Math.min(0.05, (now - last)/1000); last = now;
  controls.update();

  earthMat.uniforms.uTime.value = now * 0.001;
  earthMat.uniforms.uCamPos.value.copy(camera.position);
  earthBloomMat.uniforms.uTime.value = now * 0.001;
  earthBloomMat.uniforms.uCamPos.value.copy(camera.position);
  pollen.material.uniforms.uTime.value = now * 0.001;

  // smooth toward target motion scale
  // — 0 when paused, 0.25 when hovering a node, 1 otherwise
  const targetMotion = isPaused ? 0 : (hovered ? 0.25 : 1);
  motionScale += (targetMotion - motionScale) * (1 - Math.pow(0.001, dt));

  // earth slow rotation (also slows with the system so it feels coherent)
  earth.rotation.y += dt * 0.04 * motionScale;
  atmo.rotation.y = earth.rotation.y;
  // BLOOM exoplanet rotates a touch slower so the lava bands read more clearly
  earthBloom.rotation.y += dt * 0.018 * motionScale;
  atmoBloom.rotation.y = earthBloom.rotation.y;

  // ---- diagonal-slide transition tick ----
  if(slideAnim){
    const k = Math.min(1, (now - slideAnim.t0) / slideAnim.dur);
    // ease-in-out cubic for buttery acceleration/deceleration
    const e = k < 0.5 ? 4*k*k*k : 1 - Math.pow(-2*k + 2, 3) / 2;
    if(slideAnim.toTheme === 'bloom'){
      // ORBIT slides up-left, BLOOM enters from down-right
      groupOrbit.position.set(-SLIDE_OFF_X * e,  SLIDE_OFF_Y * e, 0);
      groupBloom.position.set( SLIDE_OFF_X * (1 - e), -SLIDE_OFF_Y * (1 - e), 0);
    } else {
      // BLOOM slides down-right, ORBIT enters from up-left
      groupBloom.position.set( SLIDE_OFF_X * e, -SLIDE_OFF_Y * e, 0);
      groupOrbit.position.set(-SLIDE_OFF_X * (1 - e),  SLIDE_OFF_Y * (1 - e), 0);
    }
    if(!slideAnim.swapped && k >= 0.5){
      performThemeSwap(slideAnim.toTheme);
      slideAnim.swapped = true;
    }
    if(k >= 1){
      parkInactivePlanet();
      document.body.classList.remove('theme-transition');
      slideAnim = null;
    }
  }

  const landingVisible = currentTheme === 'orbit' && !activeCatSet;
  const landingK = 1 - Math.pow(0.001, dt);
  starfield.visible = true;
  landingMainRingGroup.visible = false;
  landingMainRingGroup.rotation.z += dt * 0.0025 * motionScale;
  landingMainRings.forEach((ring, i) => {
    if(ring.bandMat.uniforms?.uTime) ring.bandMat.uniforms.uTime.value = now * 0.001;
    const pulse = 0.84 + 0.16 * Math.sin(now * 0.0012 + ring.phase);
    const sweep = Math.max(0, Math.sin(now * 0.0007 + ring.phase * 1.4));
    const bandNow = ring.bandMat.uniforms?.uOpacity?.value ?? ring.bandMat.opacity ?? 0;
    const haloNow = ring.haloMat.opacity ?? 0;
    const innerNow = ring.innerEdgeMat.opacity ?? 0;
    const outerNow = ring.outerEdgeMat.opacity ?? 0;
    const bandTarget = landingVisible ? (0.078 + sweep * 0.018) * pulse * ring.emphasis : 0;
    const haloTarget = landingVisible ? (0.044 + sweep * 0.012) * ring.emphasis : 0;
    const innerEdgeTarget = landingVisible ? (0.105 + sweep * 0.030) * pulse : 0;
    const outerEdgeTarget = landingVisible ? (0.135 + sweep * 0.036) * pulse : 0;
    setLandingOpacity(ring.bandMat, bandNow + (bandTarget - bandNow) * landingK);
    ring.haloMat.opacity += (haloTarget - ring.haloMat.opacity) * landingK;
    ring.innerEdgeMat.opacity += (innerEdgeTarget - innerNow) * landingK;
    ring.outerEdgeMat.opacity += (outerEdgeTarget - outerNow) * landingK;
  });

  // animate ring opacity toward target based on activeCat
  for(const cfg of RINGS){
    const isActive = activeCatSet ? activeCatSet.has(cfg.id) : false;
    const isOther  = activeCatSet && !isActive;
    const isFocusedView = !!activeCatSet;
    const targetR = isFocusedView ? cfg.focusR : cfg.defaultR;
    const targetScale = targetR / cfg.focusR;
    const targetTilt = isFocusedView ? cfg.focusTilt : cfg.defaultTilt;
    const targetCenter = isFocusedView ? cfg.focusCenter : cfg.defaultCenter;
    const poseK = 1 - Math.pow(0.00008, dt);
    cfg._displayScale = cfg._displayScale || cfg._group.scale.x || 1;
    cfg._displayScale += (targetScale - cfg._displayScale) * poseK;
    cfg._group.scale.setScalar(cfg._displayScale);
    cfg._group.rotation.x += (targetTilt.x - cfg._group.rotation.x) * poseK;
    cfg._group.rotation.y += (targetTilt.y - cfg._group.rotation.y) * poseK;
    cfg._group.rotation.z += (targetTilt.z - cfg._group.rotation.z) * poseK;
    cfg._group.position.lerp(targetCenter, poseK);

    const orbitPhase = strHash01(cfg.id) * Math.PI * 2;
    const defaultPulse = isFocusedView ? 1 : 0.88 + 0.12 * Math.sin(now * 0.001 + orbitPhase);
    const defaultSweep = isFocusedView ? 0 : Math.max(0, Math.sin(now * 0.00055 + orbitPhase * 1.7));
    const presence = cfg.defaultPresence ?? 1;
    const targLine = isActive ? 0.38 : isOther ? 0.012 : (0.17 + defaultSweep * 0.035) * presence;
    const targGlow = isActive ? 0.065 : isOther ? 0.002 : (0.034 + defaultSweep * 0.010) * presence;
    const targHl   = isActive ? 0.16 : isFocusedView ? 0.0 : 0.040 * defaultPulse * presence;
    const k = 1 - Math.pow(0.001, dt); // smooth lerp
    const lineMats = cfg._lineMats || [cfg._lineMat];
    lineMats.forEach((mat, i)=>{
      const weight = i === 0 ? 1 : i === 1 ? 0.62 : 0.42;
      const arcPulse = isFocusedView ? 1 : 0.86 + 0.14 * Math.sin(now * 0.0009 + orbitPhase + i * 1.8);
      mat.opacity += (targLine * weight * arcPulse - mat.opacity) * k;
    });
    cfg._glowMat.opacity += (targGlow - cfg._glowMat.opacity) * k;
    cfg._hlMat.opacity   += (targHl   - cfg._hlMat.opacity)   * k;

    (cfg._beacons || []).forEach((beacon, i) => {
      const angle = beacon.phase + now * 0.001 * beacon.speed * 8.0;
      const wobble = Math.sin(angle * 2.0 + orbitPhase) * 0.014;
      beacon.mesh.position.set(
        Math.cos(angle) * cfg.r,
        wobble,
        Math.sin(angle) * cfg.r
      );
      const target = isActive ? 0.78 + 0.18 * Math.sin(now * 0.003 + beacon.phase) : 0;
      beacon.mat.opacity += (target - beacon.mat.opacity) * k;
      const scale = (isActive ? 0.13 + i * 0.015 : 0.001) / Math.max(0.001, cfg._displayScale || 1);
      beacon.mesh.scale.setScalar(scale);
      beacon.mesh.visible = beacon.mat.opacity > 0.006;
    });
  }

  // camera world position, used for depth-based attenuation below
  const camWorld = camera.position;

  // animate nodes
  for(const n of memoryNodes){
    n.mesh.visible = !!n._selected;
    if(!n.mesh.visible) continue;
    // motion: pause non-active categories when one is solo'd, and apply
    // global motionScale (pause / hover-slowdown).
    const isActiveCat = !activeCatSet || activeCatSet.has(n.cat);
    const moveK = motionScale * (isActiveCat ? 1 : 0);
    n.angle += n.speed * dt * moveK;

    const r = n.ring.r;
    const x = Math.cos(n.angle) * r;
    const z = Math.sin(n.angle) * r;
    // tiny vertical wobble for life
    const y = Math.sin(n.angle*3 + n.twinklePhase) * 0.012;
    n.mesh.position.set(x, y, z);

    // twinkle scale: default nodes sit back like a quiet starfield.
    const tw = 0.82 + 0.14*Math.sin(now*0.003 + n.twinklePhase);
    const isFocusedNode = n._selected || hovered === n || (activeCatSet && activeCatSet.has(n.cat));
    const parentScale = n.ring._displayScale || 1;
    const baseNodeScale = activeCatSet ? 0.085 : 0.045;
    let s = (isFocusedNode ? 0.15 : baseNodeScale) * tw;
    if(n._selected) s = 0.28 * (0.9 + 0.15*Math.sin(now*0.012));

    // ---- depth attenuation ----
    // Distance from camera, normalized roughly to the orbit shell so that
    // back-side nodes fade & shrink. This recovers a strong sense of front/back
    // and stops dense rings from reading as a flat conveyor belt.
    const wp = n.mesh.getWorldPosition(_tmpV);
    const distCam = wp.distanceTo(camWorld);
    // map [near .. far] of plausible distances into [1 .. 0.25]
    const near = camWorld.length() - n.ring.r;
    const far  = camWorld.length() + n.ring.r;
    const depthT = THREE.MathUtils.clamp((distCam - near) / Math.max(0.001, far - near), 0, 1);
    const depthScale   = THREE.MathUtils.lerp(1.0, 0.42, depthT);
    const depthOpacity = activeCatSet
      ? THREE.MathUtils.lerp(0.26, 0.075, depthT)
      : THREE.MathUtils.lerp(0.20, 0.045, depthT);
    s *= depthScale;

    // category focus: boost active cat nodes, dim others
    let targetOpacity = depthOpacity;
    if(activeCatSet){
      if(activeCatSet.has(n.cat)){ s *= 1.35; targetOpacity = THREE.MathUtils.lerp(0.92, 0.38, depthT); }
      else { s *= 0.48; targetOpacity = 0.045; }
    }
    if(hovered === n){
      s *= 1.35;
      targetOpacity = Math.max(targetOpacity, 0.9);
    }
    if(n._selected){
      targetOpacity = 1.0;
    }

    // birth animation
    if(n.animateBirth){
      const age = (now - n.born)/1000;
      if(age < 1.6){
        const k = age/1.6;
        s = 0.16 * tw * (1 + (1-k) * 2.0);
        n.mesh.material.opacity = 1.0;
      } else {
        n.animateBirth = false;
      }
    } else {
      const km = 1 - Math.pow(0.001, dt);
      n.mesh.material.opacity += (targetOpacity - n.mesh.material.opacity) * km;
    }

    const localS = s / Math.max(0.001, parentScale);
    n.mesh.scale.set(localS, localS, localS);
  }

  // hover detection (sprites only)
  ray.setFromCamera(mouse, camera);
  const hits = ray.intersectObjects(memoryNodes.map(n=>n.mesh), false);
  if(hits.length){
    const h = hits[0].object;
    const node = memoryNodes.find(n=>n.mesh===h);
    if(node){
      hovered = node;
      tooltipEl.classList.add('show');
      document.getElementById('tt-name').textContent = displayNodeName(node);
      const ringLabel = currentLang === 'zh'
        ? (node.ring.labelCn || displayCategoryLabel(node.ring.label))
        : node.ring.label;
      document.getElementById('tt-meta').textContent =
        `${ringLabel} · ${currentLang === 'zh' ? '节点' : 'NODE'} ${String(node.idx).padStart(3,'0')}`;
      document.body.style.cursor = 'pointer';
    }
  } else {
    const landingMainId = getLandingRingHit();
    if(landingMainId){
      document.body.style.cursor = 'pointer';
      if(hovered){ tooltipEl.classList.remove('show'); hovered = null; }
    } else if(hovered){
      tooltipEl.classList.remove('show');
      document.body.style.cursor='';
      hovered = null;
    } else {
      document.body.style.cursor='';
    }
  }

  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);

// ---------------- boot fade ----------------
setTimeout(()=>{ document.getElementById('boot').classList.add('gone'); }, 700);

// ---------------- initial theme sync ----------------
// rings + nodes were already loaded for `currentTheme` above; here we just
// reflect that theme in the DOM (body class, brand text, theme-pill state).
// Both planets share the same cosmic background — the slide swaps which
// group sits at origin (parkInactivePlanet already positioned them).
(function initThemeVisuals(){
  document.body.classList.add(`theme-${currentTheme}`);
  const t = THEMES[currentTheme];
  const brandNameEl = document.querySelector('.hud .brand .name');
  const brandTagEl  = document.querySelector('.hud .brand .tag');
  if(brandNameEl){
    const m = t.brandName.match(/^(.+?)\s*&\s*(.+)$/);
    brandNameEl.innerHTML = m ? `${m[1]} <span class="amp">&amp;</span> ${m[2]}` : t.brandName;
  }
  if(brandTagEl) brandTagEl.textContent = t.tagline;
  document.querySelectorAll('[data-theme-pill]').forEach(el => {
    el.classList.toggle('active', el.dataset.themePill === currentTheme);
  });
})();

// ---------------- theme switch wiring ----------------
document.querySelectorAll('[data-theme-pill]').forEach(btn => {
  btn.addEventListener('click', ()=>{
    const target = btn.dataset.themePill;
    if(target === currentTheme) return;
    applyTheme(target);
  });
});
applyLanguage();
