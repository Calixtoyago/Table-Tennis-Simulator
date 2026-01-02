import sqlite3

DB_PATH = "db/database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    with open("db/schema.sql") as query:
        conn.executescript(query.read())

    with open("db/seed.sql") as query:
        conn.executescript(query.read())
        
    conn.commit()
    conn.close()
