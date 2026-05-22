import sqlite3
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "week2.db")

print("Using database:", db_path)

conn = sqlite3.connect(db_path)
cur = conn.cursor()


def benchmark(query, params=()):
    start = time.time()
    cur.execute(query, params)
    cur.fetchall()
    return time.time() - start


query = """
SELECT notes.content
FROM notes
JOIN note_tags ON notes.id = note_tags.note_id
JOIN tags ON tags.id = note_tags.tag_id
WHERE tags.name = ?
"""

t = benchmark(query, ("urgent",))
print("Join query time:", t)


cur.execute("DROP INDEX IF EXISTS idx_notes_user_id;")
conn.commit()

t1 = benchmark("SELECT * FROM notes WHERE user_id = ?", (12345,))
print("Without index:", t1)

cur.execute("CREATE INDEX idx_notes_user_id ON notes(user_id);")
conn.commit()

t2 = benchmark("SELECT * FROM notes WHERE user_id = ?", (12345,))
print("With index:", t2)

conn.close()
