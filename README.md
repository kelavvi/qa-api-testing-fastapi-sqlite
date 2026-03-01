]# QA API Testing Project (FastAPI + SQLite)

Mini projekt portfolio pod ścieżkę: **QA teraz -> automatyzacja w bliskiej przyszłości**

## Cel projektu
- Testowanie API (Swagger / manual API testing)
- Weryfikacja danych w bazie (SQLite / SQL)
- Reguły biznesowe i poprawne status codes (200/409/422)
- Przykład bug lifecycle: znalezienie problemu -> fix -> retest

## Tech stack
- Python, FastAPI, Uvicorn
- SQLite (DB Browser for SQLite)
- Swagger UI ('/docs')

## Jak uruchomić

### 1) Create and activate virtual environment
cd ~/backend_project
python3 -m venv venv
source venv/bin/activate

### 2) Install dependencies
pip install -r requirements.txt

### 3) Run the API server
uvicorn app.main:app --reload

### 4) Open Swagger UI
- http://127.0.0.1:8000/docs

## Quick API checks (manual)

Use Swagger UI:
- http://127.0.0.1:8000/docs

Suggested checks:
- 'GET /health' → **200**'`{ "status": "ok" '
- 'POST /users' valid payload → **200** + new'`i'`
- 'POST /users' missing field → **422**
- 'POST /users' duplicate username → **409**
- 'GET /users/{id}' existing id → **200**
- 'GET /users/{id}' non-existing id → **404**

## What I practiced as a QA (skills demonstrated)
- Manual API testing in Swagger UI ('/docs')
- Designing test cases: happy path + negative tests
- Validating HTTP status codes (200 / 409/ 422)
- Verifying persistence using SQL queries (SQLite)
- Bug lifecycle: finding -> fix -> retest

## Key QA scenarios covered
- Create user (valid payload) -> 200 + record saved in DB
- Create user (missing required field) -> 422 validation error
- Create user (empty values) -> 422 validation error
- Create user (duplicate username / login) -> 409 conflict

## Findings & fixes (mini story)
- Empty 'username' was accepted (returned 200) -> fixed with input validation -> retested (422)
- Duplicate login allowed -> fixed by checking DB before INSERT -> retested (409)
- SQLite DB lock during writes when DB Browser was open -> identified and resolved

## Next steps (autmation path)
- Add autmated API tests with 'pytest' + 'httpx'
- Add CI workflow (GitHub Actions) to run tests on every push

/
