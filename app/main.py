from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3

DB_PATH = "/Users/kelavvi/Desktop/test.db"

app = FastAPI()

class User(BaseModel):
    username: str = Field(..., min_length=1, strip_whitespace=True)
    role: str = Field(..., min_length=1, strip_whitespace=True)

def get_conn():
    # check_same_thread=False allows usage with FastAPI dev server threads
    return sqlite3.connect(DB_PATH, check_same_thread=False)

@app.get("/")
def home():
    return {"message": "Server dziala"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: User):
    conn = get_conn()
    cur = conn.cursor()
    # Check if username already exists (login must be unique)
    cur.execute("SELECT id FROM users WHERE username = ? LIMIT 1;", (user.username,))
    existing = cur.fetchone()
    if existing is not None:
        conn.close()
        raise HTTPException(status_code=409, detail="username already exists")

    # Insert user into DB
    cur.execute(
        "INSERT INTO users (username, role) VALUES (?, ?)",
        (user.username, user.role),
    )
    conn.commit()

    # Get the new ID
    new_id = cur.lastrowid
    conn.close()

    return {"id": new_id, "username": user.username, "role": user.role}

@app.get("/users")
def list_users():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, username, role FROM users ORDER BY id;")
    rows = cur.fetchall()
    conn.close()

    return [{"id": r[0], "username": r[1], "role": r[2]} for r in rows]
