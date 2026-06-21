# FastAPI Practice

Learning exercises and small examples built while working through FastAPI.

## Structure

- **`full_course/`** — Basic FastAPI app covering routing, path parameters, and query parameters (`/`, `/greet`, `/greet/{name}`, `/age`).
- **`start/`** — Example app that runs shell commands via a query parameter, with a pytest suite (including a test that demonstrates command injection). This app is intentionally vulnerable and meant for learning/security-testing purposes only — do not deploy it or expose it publicly.

## Setup

Each subdirectory is a standalone app. From inside a subdirectory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
```

## Running

```bash
uvicorn main:app --reload
```

Then visit http://127.0.0.1:8000/docs for the interactive API docs.

## Testing (`start/`)

```bash
pytest
```
