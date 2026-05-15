# Week 1 — Data Structures & Lookup Performance

This week focuses on understanding how data structures affect performance, specifically comparing:

O(n) linear search using a Python list

O(1) constant‑time lookup using a Python dictionary

This is a foundational concept in computer science and backend engineering.
The goal is to see the difference in real code, not just theory.

## Concepts Covered

### O(n) — Linear Search

- Uses a Python list

- Must scan each item one by one

- Worst case: check all 10,000 notes

- Time grows linearly with data size

### O(1) — Constant-Time Lookup

- Uses a Python dictionary (hash map)

- Computes a hash → jumps directly to the value

- No scanning, no loops

- Time stays the same even with millions of items

## How to Run the API

Start the FastAPI server:

```bash

python -m uvicorn app:app --reload
```

Then visit:

- Slow lookup O(n)
`http://127.0.0.1:8000/slow/note_5000`

- Fast lookup O(1)  
`http://127.0.0.1:8000/fast/note_5000`

## How to Run the Benchmark

Run:

```bash

python benchmark.py
```

You’ll see output similar to:
,,,

Slow avg: 0.00042
Fast avg: 0.000003
Speedup: 140x
,,,

This shows how much faster dictionary lookups are compared to list scans.

## What Each File Does

### generate_data.py

Creates 10,000 fake notes in two formats:

- `fake_notes_list` → list of dicts (for O(n) search)

- `fake_notes_dict` → dict mapping IDs to content (for O(1) search)

### app.py

FastAPI app with two endpoints:

- `/slow/{note_id}` → linear scan (O(n))

- `/fast/{note_id}` → dictionary lookup (O(1))

Each endpoint returns:

- the result

- the time taken

- the complexity label

### benchmark.py

Runs both lookup methods 1000 times and prints:

- average slow time

- average fast time

- speedup factor

### Why This Matters for Backend Engineering

Backend systems constantly look things up:

- user sessions

- API keys

- routing tables

- cached responses

- database indexes

Choosing the right data structure can make the difference between:

- fast → 1 million requests per second

- slow → server meltdown

This week builds the foundation for everything that comes next.
