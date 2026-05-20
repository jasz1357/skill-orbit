# Skill Orbit Backend

FastAPI backend skeleton for the Skill Orbit memory globe.

## Local Run

```bash
cd "/Users/jasminezhang1357/Desktop/MP3 2"
./start_backend.sh
```

Open `http://localhost:8000/docs`.

## Docker Run

```bash
cd "/Users/jasminezhang1357/Desktop/MP3 2"
cp .env.example .env
docker compose up --build
```

## Current Scope

This backend now includes a real SQLite persistence layer:

- `skills`: memory nodes shown as orbit stars
- `categories`: orbit rings
- `chat`: parse a user learning sentence into a skill node
- `health`: service readiness checks
- `auth`: register/login/current-user endpoints
- `ai_embedding_records`: vector-style retrieval index for AI skills, combinations, and workflows
- `migrations`: Alembic schema versioning
- `docs/schema.md`: database schema notes

The AI assistant uses `/api/v1/ai-skills/compose` to retrieve related workflow stacks. By default it runs with a local hash embedding index, so no API key is required. To use OpenAI embeddings later, set `EMBEDDING_PROVIDER=openai`, `OPENAI_API_KEY`, and optionally `OPENAI_EMBEDDING_MODEL=text-embedding-3-small`.

Default local admin:

- Username: `admin`
- Password: `admin123`

Change these in `.env` before using the project beyond local development.
