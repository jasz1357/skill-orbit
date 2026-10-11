#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$ROOT/backend"
FRONTEND_URL="http://127.0.0.1:5173/Skill%20Memory%20Globe.html?fresh=$(date +%s)"
FRONTEND_HEALTH_URL="http://127.0.0.1:5173/Skill%20Memory%20Globe.html"
BACKEND_URL="http://127.0.0.1:8000/api/v1/health"
LOG_DIR="$ROOT/.logs"

mkdir -p "$LOG_DIR"

cleanup() {
  if [ -z "${BACKEND_PID:-}" ] && [ -z "${FRONTEND_PID:-}" ]; then
    return
  fi
  echo
  echo "Stopping Skill Orbit..."
  if [ -n "${BACKEND_PID:-}" ]; then kill "$BACKEND_PID" 2>/dev/null || true; fi
  if [ -n "${FRONTEND_PID:-}" ]; then kill "$FRONTEND_PID" 2>/dev/null || true; fi
}
trap cleanup EXIT INT TERM

wait_for_url() {
  local url="$1"
  local name="$2"
  local tries=40
  while [ "$tries" -gt 0 ]; do
    if curl -fsS "$url" >/dev/null 2>&1; then
      echo "$name is ready."
      return 0
    fi
    tries=$((tries - 1))
    sleep 0.5
  done
  echo "$name did not become ready. Check logs in $LOG_DIR."
  return 1
}

is_url_ready() {
  local url="$1"
  curl -fsS "$url" >/dev/null 2>&1
}

echo "Starting Skill Orbit..."
echo "Project: $ROOT"
echo

cd "$BACKEND_DIR"
if [ ! -d ".venv" ]; then
  echo "Creating backend virtual environment..."
  python3 -m venv .venv
fi

echo "Installing backend dependencies..."
. .venv/bin/activate
pip install -r requirements.txt

echo "Applying database migrations..."
alembic upgrade head

if is_url_ready "$BACKEND_URL"; then
  echo "Backend is already running on http://127.0.0.1:8000."
else
  echo "Starting backend on http://127.0.0.1:8000 ..."
  uvicorn app.main:app \
    --host 127.0.0.1 \
    --port 8000 \
    --reload \
    --reload-exclude .venv \
    --reload-exclude __pycache__ \
    > "$LOG_DIR/backend.log" 2>&1 &
  BACKEND_PID=$!
fi

cd "$ROOT"
if is_url_ready "$FRONTEND_HEALTH_URL"; then
  echo "Frontend is already running on http://127.0.0.1:5173."
else
  echo "Starting frontend on http://127.0.0.1:5173 ..."
  python3 -m http.server 5173 --bind 127.0.0.1 > "$LOG_DIR/frontend.log" 2>&1 &
  FRONTEND_PID=$!
fi

wait_for_url "$BACKEND_URL" "Backend"
wait_for_url "$FRONTEND_HEALTH_URL" "Frontend"

echo
echo "Opening Skill Orbit..."
if ! open "$FRONTEND_URL"; then
  echo "Could not open the browser automatically."
  echo "Open this URL manually:"
  echo "  $FRONTEND_URL"
fi
echo
echo "Default backend login: see DEFAULT_ADMIN_* in .env.example"
echo
echo "Logs:"
echo "  $LOG_DIR/backend.log"
echo "  $LOG_DIR/frontend.log"
echo
if [ -n "${BACKEND_PID:-}" ] || [ -n "${FRONTEND_PID:-}" ]; then
  echo "Keep this window open while using the app."
  echo "Press Control-C in this window to stop the servers started here."
  echo
  tail -f "$LOG_DIR/backend.log" "$LOG_DIR/frontend.log"
else
  echo "Backend and frontend were already running."
  echo "This launcher did not start new servers, so closing this window will not stop them."
fi
