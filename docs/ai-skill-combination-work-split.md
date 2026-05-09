# AI Skill Combination Work Split

本文说明 Skill Orbit 的 AI 技能组合功能中，哪些部分需要人工完成，哪些部分可以由 AI 覆盖，以及人工准备 Embedding 数据和 LLM 后端接口时的注意事项。

## 1. 需要人工完成的内容

人工工作的核心是定义“真实、可信、可复用”的 AI 技能库。AI 可以帮忙生成草稿，但最终质量需要人工审核。

### 1.1 技能库建设

需要人工准备 50 到 100 条真实 AI 工具技能。

每条技能建议包含：

- 技能 ID
- 技能名称
- 所属分类
- 使用工具
- 标签
- 任务阶段
- 描述
- 示例 query
- 输入类型
- 输出类型
- 难度

示例：

```json
{
  "id": "claude-ppt-outline",
  "name": "用 Claude 设计 PPT 大纲",
  "category": "AI Presentation",
  "tool": "Claude",
  "tags": ["ppt", "slides", "presentation", "outline", "storyline"],
  "stage": "planning",
  "description": "用 Claude 根据主题生成 PPT 结构、页面逻辑和章节安排。",
  "examples": [
    "我今天想做一个 PPT",
    "帮我做一个产品介绍 slides",
    "我要准备课堂展示"
  ]
}
```

### 1.2 分类体系

建议人工先定义一级分类：

- AI Presentation：PPT、slides、演示、讲稿
- AI Coding：Cursor、Claude Code、debug、测试
- AI Research：搜索、资料整理、竞品分析、文献总结
- AI Writing：文案、邮件、文章、脚本
- AI Design：图片、海报、UI、品牌视觉
- AI Automation：工作流、Agent、自动化
- AI Data：表格、SQL、图表、分析报告
- AI Learning：学习计划、知识总结、复习卡片

### 1.3 组合质量标准

人工需要判断推荐组合是否合理。

一个好的 combination 应该满足：

- 覆盖任务阶段：例如资料搜集、内容结构、视觉制作、检查优化
- 避免重复：不要推荐多个功能高度相同的技能
- 有执行顺序：先做什么，再做什么
- 有不同路线：快速方案、高质量方案、学习方案、低成本方案
- 能映射到前端连线：每条 edge 都代表流程关系或依赖关系

### 1.4 测试 query

人工需要准备真实测试问题，例如：

```text
我今天想做一个 PPT
我想用 AI 写一个网站
我要做竞品分析
我想用 AI 做一份商业计划书
我要把一篇论文总结成展示材料
我想做一个产品发布海报
```

每个 query 最好人工写一个理想组合，用来检查系统推荐结果。

## 2. 可以由 AI 覆盖的内容

AI 更适合处理“理解、检索、组合、解释”。

AI 可以覆盖：

- 理解用户需求
- 提取任务意图
- 识别同义词
- 从技能库召回相关技能
- 给同一需求生成多套方案
- 给技能组合排序
- 解释为什么推荐这些技能
- 生成弹窗文案
- 为新技能生成标签草稿
- 检查技能库是否有重复技能
- 根据用户反馈优化推荐排序

但 AI 不应该无限制自由发挥。后端必须限制：

```text
只能从已有 skill_id 中选择技能
不能编造不存在的技能
必须输出固定 JSON 格式
后端必须校验 skill_id 是否真实存在
```

## 3. Embedding 应该用什么格式

Embedding 不需要人工手写向量。人工需要写的是“适合被 embedding 的技能文本”。

推荐 v0 使用 JSON 格式维护技能库，因为 JSON 比 CSV 更适合存数组、标签和示例。

### 3.1 推荐 JSON 格式

```json
{
  "id": "claude-ppt-outline",
  "name": "用 Claude 设计 PPT 大纲",
  "category": "AI Presentation",
  "tool": "Claude",
  "tags": ["ppt", "slides", "presentation", "outline", "storyline"],
  "stage": "planning",
  "input_types": ["topic", "outline", "documents"],
  "output_types": ["ppt_outline", "slide_copy", "speaker_notes"],
  "difficulty": 2,
  "description": "用 Claude 根据主题生成 PPT 结构、页面逻辑和章节安排。",
  "examples": [
    "我今天想做一个 PPT",
    "帮我做一个产品介绍 slides",
    "我要准备课堂展示"
  ]
}
```

### 3.2 后端生成 Embedding 文本

后端可以把 JSON 拼成一段用于 embedding 的文本：

```text
技能：用 Claude 设计 PPT 大纲
分类：AI Presentation
工具：Claude
标签：ppt, slides, presentation, outline, storyline
阶段：planning
输入：topic, outline, documents
输出：ppt_outline, slide_copy, speaker_notes
描述：用 Claude 根据主题生成 PPT 结构、页面逻辑和章节安排。
例子：我今天想做一个 PPT；帮我做一个产品介绍 slides；我要准备课堂展示
```

这段文本送给 embedding model，得到向量后存数据库。

### 3.3 推荐 Embedding 配置

建议：

```text
Embedding model: OpenAI text-embedding-3-small
Vector store: v0 用 sqlite-vec
Similarity: cosine
top_k: 8 到 12
threshold: 0.60 到 0.70
```

### 3.4 人工注意事项

写技能库时要注意：

- 技能名称要具体，不要只写“PPT”
- 描述要包含真实使用场景
- examples 要写用户真实会问的话
- tags 同时放中英文关键词，例如 ppt、slides、演示、讲稿
- 同一个工具可以有多个技能，但每个技能应该对应不同任务
- 不要把一个技能写得太宽泛，否则 embedding 会召回不准

## 4. LLM 后端接口要怎么处理

LLM 不应该直接决定全部结果。推荐流程是：

```text
用户输入 query
-> 后端生成 query embedding
-> 检索候选技能 top_k
-> 后端把候选技能交给 LLM
-> LLM 只从候选技能里组合方案
-> 后端校验 JSON 和 skill_id
-> 返回给前端
```

## 5. 推荐接口

新增接口：

```text
POST /api/v1/skill-combos/compose
```

请求：

```json
{
  "query": "我今天想做一个 PPT",
  "mode": "balanced",
  "max_plans": 3
}
```

返回：

```json
{
  "message": "你需要这些技能",
  "plans": [
    {
      "title": "快速完成 PPT",
      "goal": "适合今天就要交付",
      "skill_ids": ["claude-ppt-outline", "canva-slide-polish"],
      "edges": [
        ["claude-ppt-outline", "canva-slide-polish"]
      ],
      "reason": "先用 Claude 搭结构，再用 Canva 美化页面。"
    }
  ]
}
```

前端根据：

- `skill_ids` 高亮地球上的技能节点
- `edges` 绘制节点之间的连线
- `message` 和 `plans.reason` 展示弹窗

## 6. LLM Prompt 注意事项

Prompt 需要强约束：

```text
你是 Skill Orbit 的技能组合规划器。
你只能从候选技能列表中选择 skill_id。
不要创造新的 skill_id。
根据用户需求生成 2 到 3 个方案。
每个方案必须包含 title、goal、skill_ids、edges、reason。
输出必须是 JSON。
```

后端传给 LLM 的候选技能示例：

```json
[
  {
    "id": "claude-ppt-outline",
    "name": "用 Claude 设计 PPT 大纲",
    "category": "AI Presentation",
    "stage": "planning",
    "description": "生成 PPT 结构和页面逻辑"
  },
  {
    "id": "canva-slide-polish",
    "name": "用 Canva 美化 PPT 页面",
    "category": "AI Presentation",
    "stage": "production",
    "description": "优化视觉、模板和排版"
  }
]
```

## 7. 后端保护机制

后端必须做三层保护：

### 7.1 JSON Schema 校验

LLM 返回必须符合固定结构。

如果不是合法 JSON，直接 fallback 到规则方案。

### 7.2 skill_id 校验

LLM 返回的每个 `skill_id` 必须存在于候选技能列表。

如果模型编造了不存在的技能，后端删除该 skill_id，或重新请求 LLM。

### 7.3 Fallback 方案

如果 LLM 调用失败：

- 使用 embedding 相似度最高的技能
- 按 stage 排序
- 自动生成一个基础方案

这样即使 AI API 失败，前端也不会完全无结果。

## 8. 推荐分工

```text
人工：
写技能库、审核分类、准备测试 query、判断组合质量

AI：
embedding 检索、同义词理解、方案组合、解释文案

后端：
限制 AI、校验结果、记录反馈、返回前端需要的节点和连线

前端：
高亮节点、绘制连线、展示“你需要这些技能”弹窗
```

## 9. 最推荐的落地顺序

第一步：

```text
人工准备 50 到 100 条 AI 技能 JSON
```

第二步：

```text
后端实现 /api/v1/skill-combos/compose 的规则版
```

第三步：

```text
加入 text-embedding-3-small + sqlite-vec
```

第四步：

```text
加入 LLM 多方案生成，并做 schema 校验
```

第五步：

```text
记录用户选择和反馈，未来再考虑训练 reranker
```

## 10. 结论

现在最适合你们的方案不是直接训练大模型，而是：

```text
人工建设高质量 AI 技能库
-> 后端生成 embedding
-> 检索候选技能
-> LLM 从候选技能中组合多个方案
-> 后端校验结果
-> 前端展示节点连线和弹窗
```

这样既能保证推荐结果合理，又能避免 AI 胡乱编造不存在的技能。
