import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists notes(id integer primary key, note text, created_at text)")
    # Migrate existing rows that lack a timestamp
    cursor.execute("pragma table_info(notes)")
    columns = [col[1] for col in cursor.fetchall()]
    if "created_at" not in columns:
        cursor.execute("alter table notes add column created_at text")
    conn.commit()
    conn.close()

def save_note(note):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("insert into notes (note, created_at) values (?, ?)", (note, datetime.now().strftime("%b %d, %Y  %I:%M %p")))
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