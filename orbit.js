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
      { id:'ai-models',   label:'AI MODELS',   labelCn:'', color:'#ffb066', r:1.45, tilt:[ 0.26, 0.10, 0.04], speed:0.060 },
      { id:'ai-coding',   label:'AI CODING',   labelCn:'', color:'#7ed6e6', r:1.78, tilt:[-0.38, 0.34, 0.12], speed:0.044 },
      { id:'ai-visual',   label:'AI VISUAL',   labelCn:'', color:'#e69aa3', r:2.11, tilt:[ 0.62,-0.22, 0.10], speed:0.034 },
      { id:'ai-media',    label:'AI MEDIA',    labelCn:'', color:'#b99cff', r:2.44, tilt:[-0.70,-0.10,-0.15], speed:0.027 },
      { id:'ai-office',   label:'AI OFFICE',   labelCn:'', color:'#ffe27a', r:2.77, tilt:[ 0.14, 0.52,-0.08], speed:0.022 },
      { id:'ai-research', label:'AI RESEARCH', labelCn:'', color:'#91e6a7', r:3.10, tilt:[-0.18,-0.46, 0.18], speed:0.018 },
      { id:'ai-agent',    label:'AI AGENT',    labelCn:'', color:'#ff8ed1', r:3.43, tilt:[ 0.78, 0.22,-0.18], speed:0.015 },
      { id:'ai-business', label:'AI BUSINESS', labelCn:'', color:'#9fb7ff', r:3.76, tilt:[-0.58, 0.58, 0.22], speed:0.013 },
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
    dbSub: 'Complete AI skill library from the guide. Core skills appear as orbit nodes.',
    skills: 'SKILLS',
    combo: 'COMBO',
    workflow: 'WORKFLOW',
    searchSkills: 'Search all AI skills...',
    searchCombos: 'Search combinations...',
    searchWorkflows: 'Search workflows...',
    loadingDatabase: 'LOADING DATABASE',
    noMatchingSkills: 'NO MATCHING AI SKILLS',
    core: 'CORE',
    tool: 'TOOL',
    stage: 'STAGE',
    aiLibrary: 'AI LIBRARY',
    noMatchingType: type => `NO MATCHING ${type.toUpperCase()} ITEMS`,
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
    dbSub: '来自指南的完整 AI 技能库。核心技能会显示在星球轨道上。',
    skills: '技能',
    combo: '组合',
    workflow: '工作流',
    searchSkills: '搜索所有 AI 技能...',
    searchCombos: '搜索技能组合...',
    searchWorkflows: '搜索工作流...',
    loadingDatabase: '正在加载数据库',
    noMatchingSkills: '没有匹配的 AI 技能',
    core: '核心',
    tool: '工具',
    stage: '阶段',
    aiLibrary: 'AI 资料库',
    noMatchingType: type => type === 'workflow' ? '没有匹配的工作流' : '没有匹配的组合',
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
    .replace(/^combo-|^workflow-/, '')
    .split('-')
    .filter(Boolean)
    .map(titleCaseToken)
    .join(' ');
}

function englishSkillName(skill){
  if(!hasCjk(skill?.name)) return skill?.name || '';
  const tool = skill.tool || titleFromSlug(skill.id).split(' ')[0] || 'AI';
  const task = titleFromSlug(String(skill.id || '').replace(String(tool).toLowerCase().replace(/[^a-z0-9]+/g, '-'), ''))
    .replace(/^Ai /, '')
    .trim();
  const fallback = titleFromSlug(skill.id);
  return `Use ${tool} for ${task || fallback}`;
}

function englishSkillDescription(skill){
  if(!hasCjk(skill?.description)) return skill?.description || '';
  const tags = (skill.tags || []).filter(Boolean).slice(0, 4);
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
  if(currentLang === 'en' && hasCjk(item?.title)) return titleFromSlug(item.id);
  return currentLang === 'zh' ? translateText(item?.title || '') : (item?.title || '');
}

function displayLibrarySummary(item){
  if(currentLang === 'en' && hasCjk(item?.summary)){
    const tools = (item.tools || []).slice(0, 4).join(', ');
    return item.item_type === 'workflow'
      ? `A reusable project workflow built around ${tools || 'AI tools'}.`
      : `A reusable AI tool combination for ${displayCategoryLabel(item.category_label || 'AI').toLowerCase()} work.`;
  }
  return currentLang === 'zh' ? translateText(item?.summary || '') : (item?.summary || '');
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

const RINGS_KEY_BASE = 'skill-orbit-rings-v3';
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
  return THEMES[currentTheme].defaultRings.map(d => ({ ...d }));
}
function saveRingDefs(){
  try{
    const data = RINGS.map(r => ({
      id: r.id, label: r.label, labelCn: r.labelCn,
      color: '#' + new THREE.Color(r.color).getHexString(),
      r: r.r, tilt: [r.tilt.x, r.tilt.y, r.tilt.z], speed: r.speed,
    }));
    localStorage.setItem(ringsKey(), JSON.stringify(data));
  }catch(e){}
}

const RINGS = [];
const ringGroups = {};

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
    depthWrite: false,
  });
  return { line: new THREE.Line(geo, mat), mat };
}

function buildRing(def){
  const cfg = {
    id: def.id,
    label: def.label || def.id.toUpperCase(),
    labelCn: def.labelCn || '',
    r: def.r,
    color: new THREE.Color(def.color),
    tilt: new THREE.Euler(def.tilt[0], def.tilt[1], def.tilt[2]),
    speed: def.speed,
  };
  const grp = new THREE.Group();
  grp.rotation.copy(cfg.tilt);
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
  const glowMat = new THREE.MeshBasicMaterial({ color: cfg.color, transparent:true, opacity: 0.004, side:THREE.DoubleSide, blending: THREE.AdditiveBlending, depthWrite:false });
  const glow = new THREE.Mesh(glowGeo, glowMat);
  glow.rotation.x = Math.PI/2;
  grp.add(glow);

  const hlGeo = new THREE.RingGeometry(cfg.r-0.012, cfg.r+0.012, 256);
  const hlMat = new THREE.MeshBasicMaterial({ color: cfg.color, transparent:true, opacity: 0, side:THREE.DoubleSide, blending: THREE.AdditiveBlending, depthWrite:false });
  const hl = new THREE.Mesh(hlGeo, hlMat);
  hl.rotation.x = Math.PI/2;
  grp.add(hl);

  cfg._lineMats = arcMats;
  cfg._lineMat = arcMats[0];
  cfg._glowMat = glowMat;
  cfg._hlMat = hlMat;
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
let activeCat = null; // 'craft' | 'theory' | 'life' | null
function setActiveCategory(cat){
  activeCat = (activeCat === cat) ? null : cat;
  // sync UI stat rows
  document.querySelectorAll('.panel .stat.cat').forEach(el=>{
    const c = el.dataset.cat;
    el.classList.toggle('active', activeCat === c);
    el.classList.toggle('dimmed', activeCat && activeCat !== c);
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

function addNode({ id, name, cat='craft', day=0, animateBirth=true, note='', created=Date.now(), angle }){
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
  refreshUI();
  saveState();
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
const STORE_KEY_BASE = 'skill-orbit-v3';
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

function colorForCat(cat){
  const cfg = RINGS.find(r=>r.id===cat);
  if(cfg) return '#' + cfg.color.getHexString();
  return '#ffb066';
}

function renderCategoryRows(counts){
  const list = document.getElementById('cat-list');
  if(!list) return;
  // build rows for each ring in order
  list.innerHTML = RINGS.map(r => {
    const hex = '#' + r.color.getHexString();
    const label = currentLang === 'zh' ? displayCategoryLabel(r.label) : r.label;
    const title = currentLang === 'zh' ? `点击聚焦 ${label} 轨道` : `Click to focus the ${r.label} ring`;
    return `<div class="stat cat" data-cat="${r.id}" title="${escapeHtml(title)}">
      <span class="k" style="color:${hex}">${escapeHtml(label)}</span>
      <span class="right" style="display:flex; align-items:center; gap:4px;">
        <span class="v">${String(counts[r.id]||0).padStart(2,'0')}</span>
        ${RINGS.length > 1 ? `<button class="del-cat" data-del-cat="${r.id}" aria-label="delete category" title="${escapeHtml(currentLang === 'zh' ? '删除分类及其中所有节点' : 'Delete category and all its nodes')}">×</button>` : ''}
      </span>
    </div>`;
  }).join('');
  // restore active state
  list.querySelectorAll('.stat.cat').forEach(el=>{
    const c = el.dataset.cat;
    el.classList.toggle('active', activeCat === c);
    el.classList.toggle('dimmed', activeCat && activeCat !== c);
  });
}

function refreshUI(){
  const counts = {};
  memoryNodes.forEach(n => counts[n.cat] = (counts[n.cat]||0)+1 );
  setStat('stat-total', memoryNodes.length);
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
  setText('[data-db-type="combination"]', t('combo'));
  setText('[data-db-type="workflow"]', t('workflow'));
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
  return {
    id: skill.id,
    name: skill.name,
    cat: skill.category_id,
    note: `${skill.tool || skill.category_label || ''}${skill.description ? ' · ' + skill.description : ''}`.trim(),
    created: skill.created_at ? Date.parse(skill.created_at) : Date.now(),
    animateBirth: false,
  };
}

function replaceOrbitWithCoreSkills(skills){
  if(currentTheme !== 'orbit' || !Array.isArray(skills) || !skills.length) return;
  memoryNodes.slice().forEach(n => {
    if(n.mesh.parent) n.mesh.parent.remove(n.mesh);
    n.mesh.material.dispose();
  });
  memoryNodes.length = 0;
  skills.forEach(skill => addNode(normalizeAiSkillToNode(skill)));
  saveState();
  refreshUI();
}

async function loadCoreSkillsFromBackend(){
  try{
    const skills = await fetchJson('/ai-skills/core');
    replaceOrbitWithCoreSkills(skills);
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
let aiDbSkills = [];
let aiDbLibraryItems = [];

function renderAiDbTypeTabs(){
  if(!aiDbTypeTabs) return;
  aiDbTypeTabs.querySelectorAll('[data-db-type]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.dbType === aiDbType);
  });
  if(aiDbSearch){
    aiDbSearch.placeholder = aiDbType === 'skills'
      ? t('searchSkills')
      : aiDbType === 'combination'
        ? t('searchCombos')
        : t('searchWorkflows');
  }
}

function renderAiDbFilters(){
  if(!aiDbFilter) return;
  const filters = currentLang === 'zh' ? AI_CATEGORY_FILTERS_ZH : AI_CATEGORY_FILTERS;
  aiDbFilter.innerHTML = filters.map(([id, label]) =>
    `<button type="button" data-ai-cat="${id}" class="${aiDbCategory === id ? 'active' : ''}">${label}</button>`
  ).join('');
}

function renderAiDbList(){
  if(!aiDbList) return;
  const q = (aiDbSearch?.value || '').trim().toLowerCase();
  if(aiDbType === 'skills'){
    const filtered = aiDbSkills.filter(skill => {
      const catOk = aiDbCategory === 'all' || skill.category_id === aiDbCategory;
      if(!catOk) return false;
      if(!q) return true;
      const hay = `${skill.name} ${skill.tool} ${skill.category_label} ${skill.stage} ${skill.description} ${(skill.tags||[]).join(' ')}`.toLowerCase();
      return hay.includes(q);
    });
    if(!filtered.length){
      aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(t('noMatchingSkills'))}</div>`;
      return;
    }
    aiDbList.innerHTML = filtered.map(skill => `
      <article class="db-skill" data-ai-skill="${escapeHtml(skill.id)}">
        <div class="top">
          <span>${escapeHtml(displaySkillName(skill))}</span>
          ${skill.is_core ? `<span class="core">${escapeHtml(t('core'))}</span>` : ''}
        </div>
        <div class="meta">${escapeHtml(displayCategoryLabel(skill.category_label))} · ${escapeHtml(skill.tool || t('tool'))} · ${escapeHtml(translateText(skill.stage || t('stage')))}</div>
        <div class="desc">${escapeHtml(displaySkillDescription(skill))}</div>
      </article>
    `).join('');
    return;
  }

  const filtered = aiDbLibraryItems.filter(item => {
    const catOk = aiDbCategory === 'all' || item.category_id === aiDbCategory;
    if(!catOk) return false;
    if(!q) return true;
    const hay = `${item.title} ${item.category_label} ${item.summary} ${(item.tools||[]).join(' ')} ${(item.steps||[]).join(' ')} ${(item.outputs||[]).join(' ')} ${(item.tags||[]).join(' ')}`.toLowerCase();
    return hay.includes(q);
  });
  if(!filtered.length){
    aiDbList.innerHTML = `<div class="db-empty">${escapeHtml(t('noMatchingType', aiDbType))}</div>`;
    return;
  }
  aiDbList.innerHTML = filtered.map(item => {
    const primary = item.outputs?.length ? item.outputs : item.tools || [];
    return `
      <article class="db-skill" data-ai-library="${escapeHtml(item.id)}">
        <div class="top">
          <span>${escapeHtml(displayLibraryTitle(item))}</span>
          <span class="core">${escapeHtml(item.item_type === 'workflow' ? t('workflow') : t('combo'))}</span>
        </div>
        <div class="meta">${escapeHtml(displayCategoryLabel(item.category_label || t('aiLibrary')))} · ${escapeHtml(translateText(item.source_section || 'PDF'))}</div>
        <div class="desc">${escapeHtml(displayLibrarySummary(item))}</div>
        <div class="chips">${primary.slice(0, 8).map(x => `<span>${escapeHtml(translateText(x))}</span>`).join('')}</div>
      </article>
    `;
  }).join('');
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
      aiDbSkills = await fetchJson('/ai-skills?limit=1000');
    }else{
      aiDbLibraryItems = await fetchJson(`/ai-skills/library?type=${encodeURIComponent(aiDbType)}&limit=1000`);
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
  aiDbDrawer.setAttribute('aria-hidden', 'false');
  loadAiDatabase();
  setTimeout(()=>aiDbSearch?.focus(), 80);
}

function closeAiDatabase(){
  if(!aiDbDrawer) return;
  aiDbDrawer.classList.remove('show');
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
  if(aiDbSearch) aiDbSearch.value = '';
  loadAiDatabase();
});
aiDbFilter?.addEventListener('click', (e)=>{
  const btn = e.target.closest('[data-ai-cat]');
  if(!btn) return;
  aiDbCategory = btn.dataset.aiCat;
  renderAiDbFilters();
  renderAiDbList();
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
    const matches = await fetchJson(`/ai-skills?q=${encodeURIComponent(text)}&limit=8`);
    clearInterval(tID);
    ind.remove();
    if(matches.length){
      const top = matches.slice(0, 5);
      appendMsg('ai',
        `${escapeHtml(t('foundSkills', top.length))}<br/>` +
        top.map(skill => {
          const sw = colorForCat(skill.category_id);
          return `<span class="pill"><span class="sw" style="background:${sw}; box-shadow:0 0 8px ${sw}"></span>${escapeHtml(displaySkillName(skill))}</span>`;
        }).join('<br/>')
      );
      top.forEach(skill => {
        const node = memoryNodes.find(n => n.id === skill.id);
        if(node) node._selected = true;
        setTimeout(()=>{ if(node) node._selected = false; }, 1800);
      });
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
  // use current mouse coords already tracked
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
      const cat = row.dataset.cat;
      if(typeof window.__setActiveCategory === 'function') window.__setActiveCategory(cat);
    }, 220);
  });

  list.addEventListener('dblclick', (e)=>{
    const row = e.target.closest('.stat.cat'); if(!row) return;
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
  if(activeCat === catId) activeCat = null;
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

  // animate ring opacity toward target based on activeCat
  for(const cfg of RINGS){
    const isActive = activeCat === cfg.id;
    const isOther  = activeCat && !isActive;
    const targLine = isActive ? 0.72 : isOther ? 0.018 : 0.035;
    const targGlow = isActive ? 0.18 : isOther ? 0.004 : 0.006;
    const targHl   = isActive ? 0.55 : 0.0;
    const k = 1 - Math.pow(0.001, dt); // smooth lerp
    const lineMats = cfg._lineMats || [cfg._lineMat];
    lineMats.forEach((mat, i)=>{
      const weight = i === 0 ? 1 : i === 1 ? 0.62 : 0.42;
      mat.opacity += (targLine * weight - mat.opacity) * k;
    });
    cfg._glowMat.opacity += (targGlow - cfg._glowMat.opacity) * k;
    cfg._hlMat.opacity   += (targHl   - cfg._hlMat.opacity)   * k;
  }

  // camera world position, used for depth-based attenuation below
  const camWorld = camera.position;

  // animate nodes
  for(const n of memoryNodes){
    // motion: pause non-active categories when one is solo'd, and apply
    // global motionScale (pause / hover-slowdown).
    const isActiveCat = !activeCat || n.cat === activeCat;
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
    const isFocusedNode = n._selected || hovered === n || (activeCat && n.cat === activeCat);
    let s = (isFocusedNode ? 0.15 : 0.085) * tw;
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
    const depthOpacity = THREE.MathUtils.lerp(0.26, 0.075, depthT);
    s *= depthScale;

    // category focus: boost active cat nodes, dim others
    let targetOpacity = depthOpacity;
    if(activeCat){
      if(n.cat === activeCat){ s *= 1.35; targetOpacity = THREE.MathUtils.lerp(0.92, 0.38, depthT); }
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

    n.mesh.scale.set(s, s, s);
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
      document.getElementById('tt-meta').textContent =
        `${displayCategoryLabel(node.cat.toUpperCase())} · ${currentLang === 'zh' ? '节点' : 'NODE'} ${String(node.idx).padStart(3,'0')}`;
      document.body.style.cursor = 'pointer';
    }
  } else {
    if(hovered){ tooltipEl.classList.remove('show'); document.body.style.cursor=''; hovered = null; }
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
