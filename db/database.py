import sqlite3

DB_PATH = "db/database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    with open("db/schema.sql", encoding="utf-8") as query:
        conn.executescript(query.read())

    try:
        with open("db/seed.sql", encoding="utf-8") as query:
            conn.executescript(query.read())
    except sqlite3.IntegrityError: # this error occurs when a constrains is violated in sqlite3
                                   # this prevent errors when the database is already created
        pass
        
    conn.commit()
    conn.close()
