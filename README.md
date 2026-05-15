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

### ✅ Week 1 — Core Data Structures & Big O Execution

What I learned:  
Understanding how different data structures behave in real code: lists vs hash maps, O(1) vs O(N), and how lookup performance actually works.

Project:
FastAPI backend + benchmarking suite

- Generate 10,000 fake notes

- Compare list search vs dictionary lookup

- Benchmark real execution time

- Validate Big O theory with real data

Folder: `week1-data-structures/`

### 🔜 Week 2 — Relational Databases & Schema Design

What I’ll learn:  
How relational databases structure data, why normalization matters, and how indexes change performance.

Project (planned):

- Design a multi‑table schema (SQLite/Postgres)

- Add foreign keys

- Add indexes

- Benchmark indexed vs non‑indexed queries

### 🔜 Week 3 — Networking, Protocols & HTTP Lifecycle

What I’ll learn:  
How APIs actually communicate: HTTP methods, headers, status codes, TCP/IP, DNS, and the full request/response lifecycle.

Project (planned):

- Build a custom /inspect endpoint

- Return raw request metadata

- Test from another client or service

### 🔜 Week 4 — Operating Systems, Linux & Process Management

What I’ll learn:  
How code runs on a real machine: processes, threads, permissions, file systems, environment variables, and logs.

Project (planned):

- Deploy the Notes API on Linux

- Inspect processes, permissions, logs

- Automate tasks with Bash

### 🔜 Week 5 — SDLC, Git & CI/CD Pipelines

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
