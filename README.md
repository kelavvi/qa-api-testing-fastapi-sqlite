# QA API Testing Project (FastAPI + SQLite)

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
'''bash
python 3 -m venv venv
source venv/bin/activate
pip istall -r requirements.txt
uvicorn app.main:app --reload

/ Markdown

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
