# AI Skill Combination Backend Design

项目目标：用户在 AI 搜索框输入需求，例如“我今天想做一个 PPT”，后端返回一组或多组合理的技能 combination。前端随后在地球上高亮相关技能节点、绘制连线，并弹出“你需要这些技能”。

## 1. 核心判断

这个功能不建议从一开始就“训练一个自己的大模型”。更合理的做法是：

1. 先建设结构化技能库。
2. 用 embedding / 检索找出相关技能。
3. 用规则或轻量算法组合技能。
4. 最后让 LLM 解释为什么推荐这些组合，并生成多个方案。

也就是说，AI 不应该凭空发明技能，而应该基于你们自己的技能库做推荐。

## 2. 推荐的技能数据结构

每条技能不只存一个名字，而要存可检索、可组合、可展示的信息。

```json
{
  "id": "claude-ppt-design",
  "name": "用 Claude 设计 PPT",
  "category": "AI Presentation",
  "tool": "Claude",
  "intent_tags": ["presentation", "slides", "storyline", "writing"],
  "input_types": ["topic", "outline", "documents"],
  "output_types": ["ppt_outline", "slide_copy", "speaker_notes"],
  "difficulty": 2,
  "stage": "planning",
  "description": "用 Claude 生成 PPT 结构、页面逻辑、讲稿和视觉建议。",
  "examples": [
    "我今天想做一个产品介绍 PPT",
    "帮我做一个课程汇报 slides"
  ]
}
```

推荐的一级分类：

- AI Presentation：PPT、slides、deck、演示、讲稿
- AI Coding：Cursor、Claude Code、GitHub Copilot、debug、测试
- AI Research：搜索、资料整理、文献总结、竞品分析
- AI Writing：文案、邮件、文章、脚本、改写
- AI Design：图片、海报、UI、品牌视觉
- AI Automation：工作流、Agent、批处理、Zapier/n8n
- AI Data：表格、分析、图表、SQL、报告
- AI Learning：学习计划、知识总结、复习卡片

## 3. 多种后端方案

### 方案 A：规则 + 标签匹配

做法：

- 给每个技能手动打标签。
- 用户输入后做关键词解析，例如 PPT、slides、presentation 命中 AI Presentation。
- 按标签返回技能。

优点：

- 实现最快，不需要外部 AI API。
- 成本低，结果稳定。
- 适合早期验证前端交互。

缺点：

- 同义词能力弱。
- 中文表达、模糊需求、复杂任务容易漏掉。
- 很难生成多种组合方案。

适合阶段：v0 原型。

### 方案 B：Embedding 检索

做法：

- 每条技能生成 embedding。
- 用户需求也生成 embedding。
- 用向量相似度找 top_k 相关技能。
- 再按 category、stage、tool 做去重和排序。

推荐技术：

- embedding model：OpenAI `text-embedding-3-small`
- vector store：v0 可以用 SQLite + sqlite-vec，之后再换 Postgres + pgvector
- similarity：cosine
- top_k：先用 8 到 12
- threshold：先从 0.60 到 0.70 试

优点：

- 中文、英文、同义表达都能更好地匹配。
- 不需要训练模型。
- 非常适合“我今天想做一个 PPT”这种自然语言需求。

缺点：

- 需要维护 embedding 生成和刷新。
- 初期要准备真实技能样本。
- 组合逻辑仍然需要额外设计。

适合阶段：v1 主推荐。

### 方案 C：Embedding + LLM 组合生成

做法：

1. 先用 embedding 检索出 10 到 20 个候选技能。
2. 把候选技能作为上下文给 LLM。
3. 要求 LLM 只能从候选技能里选择，生成 2 到 4 套方案。
4. 后端校验 LLM 返回的 skill_id 是否真实存在。

示例输出：

```json
{
  "message": "你需要这些技能",
  "plans": [
    {
      "title": "快速完成 PPT",
      "goal": "适合今天就要交付",
      "skill_ids": ["claude-ppt-design", "canva-slide-polish", "chatgpt-speaker-notes"],
      "reason": "先确定内容结构，再优化视觉，最后补讲稿。"
    },
    {
      "title": "高质量演示方案",
      "goal": "适合正式汇报",
      "skill_ids": ["perplexity-research", "claude-ppt-storyline", "midjourney-visual-style", "canva-slide-polish"],
      "reason": "先补资料，再搭叙事，再统一视觉风格。"
    }
  ]
}
```

优点：

- 可以生成不同路线：快速版、高质量版、低成本版、学习版。
- 解释性强，前端弹窗内容更自然。
- 不需要微调模型。

缺点：

- 需要调用 LLM API。
- 必须做 JSON schema 校验，防止模型编造不存在的技能。

适合阶段：v1.5 到 v2。

### 方案 D：训练 / 微调分类模型

做法：

- 收集用户 query 和理想组合结果。
- 标注每个 query 对应哪些技能、哪些组合。
- 微调一个分类或 rerank 模型。

优点：

- 长期稳定，符合你们自己的产品风格。
- 对固定领域的判断更一致。

缺点：

- 需要大量高质量数据。
- 早期成本高，调试慢。
- 微调不能替代技能库和检索。

适合阶段：有 500 到 2000 条真实 query 之后。

## 4. 我建议的实现路线

### v0：先做规则版

目标：前端流程先跑通。

新增接口：

```text
POST /api/v1/skill-combos/compose
```

请求：

```json
{
  "query": "我今天想做一个 PPT",
  "mode": "balanced"
}
```

返回：

```json
{
  "message": "你需要这些技能",
  "plans": [
    {
      "title": "PPT 快速完成方案",
      "skill_ids": ["claude-ppt-design", "canva-slide-polish"],
      "edges": [
        ["claude-ppt-design", "canva-slide-polish"]
      ],
      "reason": "先生成内容结构，再优化页面呈现。"
    }
  ]
}
```

### v1：加入 embedding 检索

新增表：

```text
ai_skills
skill_embeddings
skill_combo_logs
```

核心流程：

1. 管理员导入 AI 技能库。
2. 后端为每个技能生成 embedding。
3. 用户 query 生成 embedding。
4. 检索 top_k 技能。
5. 用组合算法生成多个方案。
6. 返回给前端绘制节点和连线。

### v2：加入 LLM 解释和多方案生成

LLM prompt 规则：

- 只能选择给定候选技能里的 skill_id。
- 必须输出 JSON。
- 每个 plan 需要 title、goal、skill_ids、edges、reason。
- 至少给 2 个方案：快速方案、质量方案。
- 如果技能不足，要返回缺失技能建议。

## 5. Combination 怎样才合理

一个好的 combination 不应该只是“相似技能堆在一起”，而应该满足：

1. 覆盖任务阶段：例如资料搜集、结构设计、视觉制作、检查优化。
2. 避免同质重复：不要同时推荐 4 个都只会写大纲的工具。
3. 有明确顺序：先做什么，再做什么。
4. 有不同路线：快、精、省、学习。
5. 能映射到前端连线：每个 edge 都代表一个流程关系。

PPT 示例：

```text
用户需求：我今天想做一个 PPT

快速方案：
Claude 生成 PPT 大纲 -> Canva 美化 slides -> ChatGPT 生成讲稿

高质量方案：
Perplexity 做资料研究 -> Claude 设计叙事结构 -> Midjourney/Canva 确定视觉 -> Gamma/Canva 生成页面

学习方案：
ChatGPT 拆解 PPT 制作步骤 -> Claude 评审大纲 -> Canva 模板练习
```

## 6. 是否需要训练 AI

短期：不需要训练。

你们更需要的是：

- 一份真实 AI 技能库。
- 每条技能的标签、描述、例子。
- embedding 检索。
- LLM 只负责从候选技能里组合和解释。

中期：可以做数据积累。

每次用户选择、删除、保存某个组合，都记录下来：

```json
{
  "query": "我今天想做一个 PPT",
  "recommended_skill_ids": ["claude-ppt-design", "canva-slide-polish"],
  "selected_skill_ids": ["claude-ppt-design"],
  "user_feedback": "useful",
  "created_at": "..."
}
```

长期：当你们有足够数据后再训练。

可训练内容：

- query intent 分类
- skill reranker
- combination ranker
- 不同用户偏好的推荐排序

## 7. 后端模块设计

推荐新增目录：

```text
backend/app/services/retrieval.py
backend/app/services/combination.py
backend/app/services/llm.py
backend/app/api/routes/skill_combos.py
backend/app/models/skill_combo.py
backend/app/repositories/skill_library.py
```

职责：

- `retrieval.py`：把 query 转 embedding，召回候选技能。
- `combination.py`：按任务阶段和工具类别生成多套组合。
- `llm.py`：调用 OpenAI / Anthropic，负责解释和重排。
- `skill_combos.py`：提供 `/compose` 接口。
- `skill_library.py`：管理 AI 技能库和 embedding。

## 8. API 接入建议

OpenAI 路线：

- embedding：`text-embedding-3-small`
- LLM：用于 JSON 输出和解释

Anthropic 路线：

- LLM：适合生成解释、拆任务、生成多方案
- embedding：Anthropic 不作为 embedding 首选，建议仍用 OpenAI 或其他 embedding provider

建议后端做 provider 抽象：

```text
AI_PROVIDER=openai
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
```

这样以后可以切换模型，不影响前端和业务逻辑。

## 9. 最小可实施版本

第一步：

- 准备 50 到 100 条 AI 工具技能。
- 每条技能包含 name、category、tool、tags、description、examples。

第二步：

- 做 `/api/v1/skill-combos/compose`。
- 先用标签和关键词返回组合。
- 前端拿 `skill_ids` 和 `edges` 绘制连线。

第三步：

- 加 embedding。
- 测试 10 个真实 query。
- 肉眼检查召回质量。

第四步：

- 加 LLM 多方案生成。
- 做 JSON schema 校验。
- 记录用户反馈。

## 10. 结论

最推荐的路线是：

```text
结构化 AI 技能库
-> embedding 检索候选技能
-> combination 算法生成多方案
-> LLM 解释和润色
-> 前端高亮节点与绘制连线
-> 记录反馈，未来再训练
```

这条路线既聪明，又不会一开始就被“训练模型”拖住。你们现在的后端已经有 FastAPI、用户、技能、分类、chat assist 雏形，可以在现有基础上继续扩展。
