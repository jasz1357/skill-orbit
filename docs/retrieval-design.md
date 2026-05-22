# AI Vector Knowledge Base

## Goal

The AI assistant should turn a natural-language task such as “我今天想做一个 PPT” into related workflow stacks and tool combinations from the existing AI Skill Database.

## Indexed Data

- `ai_skills`: individual AI skills and tools.
- `ai_library_items`: combinations and workflows.
- `ai_embedding_records`: generated retrieval index for the two sources above.

Each index row stores the source type, title, category, subcategory, searchable content, metadata, content hash, and embedding vector.

## Embedding Strategy

Default local mode:

- Provider: `local`
- Model: `local-hash-384`
- Dimension: `384`
- Similarity: cosine
- Default threshold: `0.24`
- Default top_k for chat: `5`

Optional OpenAI mode:

- Set `EMBEDDING_PROVIDER=openai`
- Set `OPENAI_API_KEY=...`
- Default model: `text-embedding-3-small`

The backend keeps the same endpoints either way. Local mode lets the project run without an API key; OpenAI mode can improve semantic quality later.

## Natural Language Intent Layer

Before ranking, the backend now detects task intent categories such as:

- `presentation_deck`: PPT, slides, deck, proposal, 演示文档, 演示稿, 汇报
- `research_report`: research, papers, reports, 调研, 研报, 文献
- `coding_build`: code, Cursor, Claude Code, app build, 前端, 后端
- `visual_design`: image generation, brand visuals, posters, 视觉设计
- `video_audio`: video, audio, music, voice, short-form production
- `automation_agent`: workflow automation, agents, bots, RAG, MCP
- `business_growth`: sales, marketing, CRM, support, ecommerce
- `data_analysis`: spreadsheet, dashboard, chart, finance, visualization

Every skill/workflow is indexed with a generated intent profile:

- semantic intent ids
- human-readable meaning
- likely use cases
- equivalent user wording

Ranking combines vector similarity, intent overlap, direct title/category match, workflow preference, and importance. This makes queries like “我想做 PPT” and “我想做演示文档” return the same workflow stack order.

## Endpoints

- `GET /api/v1/ai-skills/search?q=...&types=combination,workflow&top_k=8`
- `POST /api/v1/ai-skills/compose`
- `POST /api/v1/ai-skills/recommend`
- `POST /api/v1/ai-skills/advice`

`advice` is what the frontend chat uses. It first checks whether the user request has enough context. If the request is too vague, it returns `needs_clarification=true` and 1-3 clarification questions. If the request is specific enough, it returns the same recommendation plan shape as `recommend`.

`recommend` retrieves candidate combinations/workflows, then reranks them into a small set of recommendation plans such as fastest path, best visual deck, or business-ready proposal. Each plan includes:

- recommendation type
- reason
- best-fit scenario
- tradeoff
- pros and cons
- execution steps
- required inputs
- expected outputs

`compose` remains available as the lower-level semantic retrieval endpoint.

## Feedback Learning

The frontend can post lightweight recommendation feedback to:

- `POST /api/v1/ai-skills/feedback`

Supported ratings:

- `up`
- `down`
- `too_complex`
- `too_slow`
- `want_faster`
- `want_better`
- `used`

Feedback is stored in `ai_recommendation_feedback`. The recommender reads accumulated feedback and applies a small ranking adjustment, so repeatedly useful workflows become slightly more likely to appear, while poor-fit workflows are gently demoted.

## Clarification Option Reranking

Clarification choices are appended to the original request before recommendation. The recommender now gives those choices explicit weight:

- audience, such as client, class, boss/team, investor, thesis defense
- material state, such as existing docs, from scratch, data table, links, old PPT polish
- priority, such as fast, visual polish, professional quality, logical rigor, business proposal

The option-aware reranker only adjusts candidates already retrieved by semantic search, then adds a stable query-specific tie break. This keeps results relevant while making different option combinations produce different plan orders.

## Update Flow

On backend startup, the app seeds skills and workflows, then refreshes the vector index. Existing embeddings are reused unless the indexed content hash changes.
