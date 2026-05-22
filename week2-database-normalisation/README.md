# Week 2 — Databases, Normalisation & Query Performance

This week covers how relational databases structure data, how normalisation (1NF → 3NF) prevents duplication, and how indexes improve query performance. The exercises use SQLite and Python to benchmark real SELECT and JOIN queries.

## Concepts Covered

- **Normalisation (1NF → 3NF)**
 	- `1NF` — Atomic values: no lists or comma-separated values; every column holds a single value. Achieved by splitting tags into a separate table.
 	- `2NF` — No partial dependencies: all non-key attributes depend on the whole primary key. Achieved by separating `users`, `notes`, and `tags` into their own tables.
 	- `3NF` — No transitive dependencies: non-key attributes depend only on the primary key. Remove derived or redundant fields (for example, do not store a username in `notes`). The final schema is in `3NF`.

- **Indexes & performance**
 	- Indexes (B-tree) let the database jump directly to matching rows instead of scanning the whole table.
 	- Benchmarks show the difference between full table scans and indexed lookups, and measure JOIN performance across multiple tables.

## Quickstart

### Seed the database

Creates the database, loads the schema, and inserts data.

Run:

```bash
python seed.py
```

Expected output (examples):

- `Schema loaded successfully!`
- `Seeding complete!`

This generates (but does NOT commit) `week2.db`.

### Run the benchmark

Runs SELECT and JOIN performance tests.

Run:

```bash
python benchmark.py
```

Example output:

- `Join query time: 0.0102 seconds`
- `Without index:   0.0045 seconds`
- `With index:      0.00012 seconds`

Indexes improved lookup speed by ~37× in this example.

## Files

- `schema.sql` — Defines the full `3NF` database schema: `users`, `notes`, `tags`, and `note_tags` (many-to-many join table). Includes indexes on foreign keys for faster lookups.
- `seed.py` — Loads the schema, inserts thousands of users/notes/tags, creates random note↔tag relationships, and saves the database to `week2.db`.
- `benchmark.py` — Runs SELECT and JOIN performance tests, measures execution time, and prints results.
- `README.md` — This file.
- `week2.db` — Generated database file (ignored in version control).

## Why this matters for backend engineering

- Backend systems rely on relational databases for user accounts, posts/comments, tags, permissions, analytics, logs, and product catalogs.
- Choosing the right schema and indexes can mean the difference between:
 	- fast — thousands of queries per second
 	- slow — timeouts and server overload

This week builds the foundation for scalable backend design, efficient SQL queries, and practical understanding of JOINs and database optimisation.

## Goals

- See the difference in real SQL queries (not just theory) by benchmarking lookups and JOINs using SQLite + Python.
