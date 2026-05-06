#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/backend"

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

.venv/bin/pip install -r requirements.txt
.venv/bin/alembic upgrade head
.venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload --reload-exclude .venv --reload-exclude __pycache__
