# QA API Testing Project (FastAPI + SQLite)

Mini projekt portfolio pod ścieżkę: **QA teraz -> automatyzacja w bliskiej przyszłości**

## Cel projektu
- Testowanie API (Swagger / manual API testing)
- Weryfikacja danych w bazie (SQLite / SQL)
- Reguły biznesowe i poprawne status codes (200/409/422)
- Przykład buf lifecycle: znalezienie problemu -> fix -> retest

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


