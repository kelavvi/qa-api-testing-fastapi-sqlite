# QA API Testing Project (FastAPI + SQLite)

Mini portfolio project for the path: **QA now → test automation in the near future**
Project focused on practicing real-life QA workflow for REST API testing.

## Project goal
- API testing (Swagger / manual testing)
- Database validation (SQLite / SQL)
- Business rules and correct HTTP status codes (200 / 409 / 422)
- Bug lifecycle: finding -> fixing -> retesting

## Tech stack
- Python
- FastAPI
- Uvicorn
- SQLite (DB Browser for SQLite)
- Swagger UI (`/docs`)

## How to run

### 1) Create and activate virtual environment
```bash
cd ~/backend_project
python3 -m venv venv
source venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the API server
```bash
uvicorn app.main:app --reload
```

### 4) Open Swagger UI
- http://127.0.0.1:8000/docs

## Quick API checks (manual)

Use Swagger UI:
- http://127.0.0.1:8000/docs

Suggested checks:
- `GET /health` -> **200** `{ "status": "ok" }`
- `POST /users` valid payload -> **200** + new `id`
- `POST /users` missing field -> **422**
- `POST /users` duplicate username -> **409**
- `GET /users/{id}` existing id -> **200**
- `GET /users/{id}` non-existing id -> **404**

## What I practiced as a QA (skills demonstrated)
- Manual API testing in Swagger UI (`/docs`)
- Designing test cases: happy path + negative tests
- Validating HTTP status codes (200 / 409 / 422)
- Verifying persistence using SQL queries (SQLite)
- Bug lifecycle: finding -> fix -> retest

## Key QA scenarios covered
- Create user (valid payload) -> 200 + record saved in DB
- Create user (missing required field) -> 422 validation error
- Create user (empty values) -> 422 validation error
- Create user (duplicate username / login) -> 409 conflict

## Findings & fixes (mini story)
- Empty `username` was accepted (returned 200) -> fixed with input validation -> retested (422)
- Duplicate login allowed -> fixed by checking DB before INSERT -> retested (409)
- SQLite DB lock during writes when DB Browser was open -> identified and resolved

## Next steps (automation path)
- Add automated API tests with `pytest` + `httpx`
- Add CI workflow (GitHub Actions) to run tests on every push
