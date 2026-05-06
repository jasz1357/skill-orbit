# GitHub Collaboration Workflow

This project should use GitHub as the shared source of truth. Local `.env`, SQLite database files, logs, virtual environments, and uploads stay on each computer and are not committed.

## Roles

- `main`: stable version. Only merge reviewed pull requests here.
- `develop`: shared integration branch for active work.
- `feature/<short-name>`: one feature or fix per branch.

## First-time setup

If this folder is not a git repo yet:

```bash
cd "/Users/jasminezhang1357/Desktop/MP3 2"
git init
git add .
git commit -m "Initial Skill Orbit project"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

Then create `develop`:

```bash
git checkout -b develop
git push -u origin develop
```

Your boyfriend can then clone the same repository:

```bash
git clone <your-github-repo-url>
cd <repo-folder>
cp .env.example .env
```

## Daily workflow

Before starting work:

```bash
git checkout develop
git pull
git checkout -b feature/<short-name>
```

After Codex or either person changes files:

```bash
git status
git add .
git commit -m "Describe the change"
git push -u origin feature/<short-name>
```

Open a pull request from `feature/<short-name>` into `develop`. GitHub Actions will run backend migrations/tests and a frontend static check. Merge only after the checks pass.

## How Codex changes reach GitHub

Codex edits the files in this local folder. Those edits become part of GitHub when you commit and push them from this same folder:

```bash
git status
git add .
git commit -m "Implement backend change"
git push
```

If you want Codex to do that part too, ask: "commit these changes, push the branch, and open a PR."

## Local run

Backend:

```bash
./start_backend.sh
```

Frontend:

```bash
./start_frontend.sh
```

Or double-click:

```text
Start Skill Orbit.command
```

Default local admin:

```text
username: admin
password: admin123
```

Change the default password in `.env` before using shared or deployed environments.
