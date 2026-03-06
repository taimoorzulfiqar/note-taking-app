import sqlite3

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists notes(id integer primary key, note text)")
    conn.commit()
    conn.close()

def save_note(note):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("insert into notes (note) values (?)", (note,))
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("select * from notes")
    results = cursor.fetchall()
    conn.close()
    return results

def delete_all_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("delete from notes")
    conn.commit()
    conn.close()