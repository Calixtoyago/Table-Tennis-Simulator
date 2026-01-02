from athletes import Athlete
from db.database import get_connection

def get_all_athletes():
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("SELECT name, attack, defense, serve FROM athletes ORDER BY name").fetchall()
    conn.close()

    athletes_list = [Athlete(*athlete) for athlete in rows]

    return athletes_list

def create_athlete(name, attack, defense, serve):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO athletes (name, attack, defense, serve) 
                   VALUES (?, ?, ?, ?)""", (name, attack, defense, serve))
    
    conn.commit()
    conn.close()

    return get_all_athletes()
