import os
import sqlite3
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
schema_path = os.path.join(BASE_DIR, "schema.sql")
db_path = os.path.join(BASE_DIR, "week2.db")

print("Schema path:", schema_path)
print("DB path:", db_path)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

with open(schema_path) as f:
    cur.executescript(f.read())

print("Schema loaded successfully!")

for i in range(10000):
    cur.execute("INSERT INTO users (username) VALUES (?)", (f"user{i}",))

for i in range(50000):
    cur.execute(
        "INSERT INTO notes (user_id, content) VALUES (?, ?)",
        (random.randint(1, 10000), "hello world"),
    )

tag_names = ["work", "urgent", "personal", "fun", "school"]
for name in tag_names:
    cur.execute("INSERT INTO tags (name) VALUES (?)", (name,))

for note_id in range(1, 50001):
    tag_id = random.randint(1, len(tag_names))
    cur.execute(
        "INSERT INTO note_tags (note_id, tag_id) VALUES (?, ?)", (note_id, tag_id)
    )

conn.commit()
conn.close()

print("Seeding complete!")
