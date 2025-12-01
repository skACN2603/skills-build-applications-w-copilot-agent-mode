# Guidance for AI coding agents (Copilot / Agent Mode)

This file collects repository-specific conventions, important workflows, and examples to help an AI coding agent be productive immediately.

1. Scope & Big picture
- The project implements an "Octofit Tracker" exercise with two main components:
  - `octofit-tracker/backend/` — Django REST backend (uses `venv` and `requirements.txt`).
  - `octofit-tracker/frontend/` — React frontend (created with `create-react-app`).
- Important: many repository instructions live under `.github/instructions/*` and step-by-step commands under `.github/steps/*.md`. Prefer those as authoritative.

2. Environment / execution rules (must follow)
- Never change directories when running commands. Always reference the target directory explicitly (e.g. `python3 -m venv octofit-tracker/backend/venv`).
- Forwarded ports (do not add others): `8000` (public), `3000` (public), `27017` (private).

3. Backend (Django) conventions & examples
- Virtualenv: create and activate at `octofit-tracker/backend/venv`. Install with:
  ```bash
  python3 -m venv octofit-tracker/backend/venv
  source octofit-tracker/backend/venv/bin/activate
  pip install -r octofit-tracker/backend/requirements.txt
  ```
- `settings.py`: expect `ALLOWED_HOSTS` to include `localhost`, `127.0.0.1`, and Codespace host when `CODESPACE_NAME` is present. See `.github/instructions/octofit_tracker_django_backend.instructions.md` for exact snippet.
- URLs: server base URL should use `CODESPACE_NAME` when available. Example pattern is provided in `urls.py` in the instructions file.
- Serializers: convert MongoDB `ObjectId` fields to strings before returning JSON (see `serializers.py` guidance).
- Database: although MongoDB is referenced, always use Django ORM to create schema/data rather than direct MongoDB scripts.
- Test endpoints using `curl` (the instruction files explicitly recommend `curl` for endpoint validation).

4. Frontend (React) conventions & examples
- Commands should use explicit `--prefix` or path to avoid changing directories. Example from `.github/instructions/octofit_tracker_react_frontend.instructions.md`:
  ```bash
  npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
  npm install bootstrap --prefix octofit-tracker/frontend
  npm install react-router-dom --prefix octofit-tracker/frontend
  ```
- Add bootstrap import to `octofit-tracker/frontend/src/index.js` (instructions include a `sed` snippet).
- App image: `docs/octofitapp-small.png` is the canonical app image mentioned in instructions.

5. MongoDB and processes
- Check mongod with: `ps aux | grep mongod` before assuming a MongoDB service is running.
- Use `mongosh` if manual inspection is required, but prefer Django ORM for app data operations.

6. Source-of-truth for agent behavior
- The `.github/instructions/*.instructions.md` files are authoritative for this exercise — follow them exactly when asked to run commands or scaffold parts of the app.
- Step-by-step human-facing tasks live in `.github/steps/*.md` — these often contain example PR titles, branch names, and Copilot interaction guidance.

7. Examples of explicit command usage (copyable)
- Create venv and install (from repo root):
  ```bash
  python3 -m venv octofit-tracker/backend/venv
  source octofit-tracker/backend/venv/bin/activate
  pip install -r octofit-tracker/backend/requirements.txt
  ```
- Create React app and install deps (from repo root):
  ```bash
  npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
  npm install bootstrap --prefix octofit-tracker/frontend
  ```

8. What not to do
- Do not change working directories during automated or agent-run commands — always reference target paths.
- Do not forward additional ports beyond `8000`, `3000`, and `27017`.
- Do not bypass Django ORM to write initial data into MongoDB.

9. Where to look for more context
- `.github/instructions/octofit_tracker_setup_project.instructions.md`
- `.github/instructions/octofit_tracker_django_backend.instructions.md`
- `.github/instructions/octofit_tracker_react_frontend.instructions.md`
- `.github/steps/*.md` (step-by-step activities and PR guidance)

10. If you need to modify or run code
- Prefer minimal, targeted changes. When adding code follow existing patterns in `backend` and `frontend` directories and mirror the examples in `.github/instructions`.

If any of the above is unclear or you want more detailed run/debug commands (for example: how to run the Django server with Codespaces environment variables), tell me which area to expand and I will iterate.
