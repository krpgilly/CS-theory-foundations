# Backend Engineering & System Architecture Foundations

This repository is my structured, project‑based curriculum for becoming a strong junior backend engineer with real system‑level understanding.

The goal isn’t to memorise theory it’s to build intuition through small, focused projects that mirror real backend engineering work:

- data structures

- databases

- networking

- operating systems

- Git & CI/CD

Each week introduces one core backend concept and includes a hands‑on project to make the theory real.

This repo will grow as I progress.

## Why This Exists

I built this curriculum because backend engineering requires more than just writing code — it requires understanding:

- how data is stored

- how systems communicate

- how servers run

- how code is deployed

- how performance works

This repo is my personal roadmap to build those foundations properly, one week at a time.

## Curriculum Roadmap

A high‑level overview of each week and the project attached to it.

### ✅ Module 1 — Core Data Structures & Big O Execution

What I learned:  
Understanding how different data structures behave in real code: lists vs hash maps, O(1) vs O(N), and how lookup performance actually works.

Project:
FastAPI backend + benchmarking suite

- Generate 10,000 fake notes

- Compare list search vs dictionary lookup

- Benchmark real execution time

- Validate Big O theory with real data

Folder: `week1-data-structures/`

### ✅ Module 2 — Relational Databases, Normalisation & Query Performance

What I learned:
How relational databases structure data, why normalisation matters (1NF → 3NF), and how indexes dramatically change performance.
Also learned how JOINs work across multiple tables and how to benchmark SQL queries using Python.

Project:  
SQLite schema + Python benchmarking suite

Designed a fully normalised 3NF schema (`users`, `notes`, `tags`, `note_tags`)

Added foreign keys and indexes

Inserted large datasets using a seed script

Benchmarked indexed vs non‑indexed lookups

Benchmarked JOIN performance across multiple tables

Key Results:

```bash

Join query time: 0.0102s
Without index:   0.0045s
With index:      0.00012s
```

Indexes improved lookup speed by ~37×.

Folder: `week2-database-normalisation/`

### ✅ Module 3 — Networking, Protocols & HTTP Lifecycle

What I learned:  
How APIs actually communicate over the web: HTTP methods, headers, status codes, CORS, and the full request/response lifecycle.
Also learned the difference between browser requests, curl requests, JSON bodies, form data, and how Flask handles each part of an incoming request.

Project:
Custom `/inspect` endpoint built with Flask.

The endpoint returns raw request metadata so I can see how HTTP works in real time:

HTTP method (GET, POST, PUT, DELETE)

Path

Query parameters

JSON body

Form data

Raw body

Client IP

All request headers

CORS enabled using `flask_cors` so the API can be called from other origins (e.g., a frontend running on a different port).

Examples tested:

GET request (browser):

```json
{
  "method": "GET",
  "query_params": { "hello": "world", "user": "harry" },
  "json_body": null,
  "headers": { ... }
}
```

POST request (curl):

```json
{
  "method": "POST",
  "json_body": { "name": "Harry" },
  "raw_body": "{\"name\": \"Harry\"}",
  "headers": { ... }
}
```

Key Results:  
I can now clearly see the differences between:

Browser vs curl requests

GET vs POST

Query params vs JSON body

Raw body vs parsed body

Browser security (CORS)

How Flask exposes request metadata

Folder: `week3-Networking-HTTP/`

### 🔜 Module 4 — Operating Systems, Linux & Process Management

What I’ll learn:  
How code runs on a real machine: processes, threads, permissions, file systems, environment variables, and logs.

Project (planned):

- Deploy the Notes API on Linux

- Inspect processes, permissions, logs

- Automate tasks with Bash

### 🔜 Module 5 — SDLC, Git & CI/CD Pipelines

What I’ll learn:  
How real engineering teams work: branching, pull requests, testing, and automated pipelines.

Project (planned):

- Create a GitHub Actions pipeline

- Lint, test, and build on every PR

- Produce a verified build artifact

## Advanced CS Roadmap (Optional Level‑Up Path)

These topics are not required for junior backend, but they are powerful for deeper CS understanding or interview prep.

I will tackle these after the core 5‑week curriculum.

### Advanced Week A — Algorithms & Sorting

- Implement bubble, merge, quicksort

- Benchmark on large datasets

- Visualize performance differences

### Advanced Week B — Recursion & Trees

- Build a tree structure

- Implement DFS & BFS

- Explore recursion vs iteration

### Advanced Week C — Hashing & Caching

- Build an in‑memory cache

- Add LRU/FIFO eviction

- Benchmark cache hits vs misses

### Advanced Week D — Concurrency & Async

- Explore async/await

- Build concurrent API endpoints

- Compare sync vs async performance

### Advanced Week E — Databases & Indexing

- Build indexes

- Compare indexed vs non‑indexed queries

- Understand O(log N) database lookup
