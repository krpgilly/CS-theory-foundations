# Week 3 — HTTP, REST & CORS Request Inspector

This project is a small Flask backend designed to visualise how HTTP actually works. It exposes an `/inspect` endpoint that returns the raw details of any request sent to it.

The goal is to understand:

- How HTTP methods behave (`GET` vs `POST` vs `PUT` vs `DELETE`)
- How browsers send headers
- How JSON bodies and form bodies are parsed
- How query parameters work
- What CORS is and why it matters
- What a real request lifecycle looks like

## Features

### Inspect any HTTP request

The `/inspect` endpoint returns:

- HTTP method
- Path
- Query parameters
- JSON body
- Form data
- Raw body
- Client IP
- All request headers

This makes it easy to see the difference between:

- Browser requests
- `curl` requests
- JavaScript `fetch()`
- `POST` vs `GET`
- JSON vs form data

### CORS enabled

The project uses:

```python
from flask_cors import CORS
CORS(app)
```

This allows cross-origin requests, meaning a frontend running on another port (e.g. React on `localhost:3000`) can call this API without being blocked by the browser.

## Endpoints

### `GET /inspect`

Returns request metadata.

Example:

```
/inspect?hello=world&user=harry
```

### `POST /inspect`

Send JSON:

```bash
curl -X POST "http://127.0.0.1:5000/inspect" ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"Harry\"}"
```

### `GET /health`

Simple health check:

```json
{ "status": "ok" }
```

## What I Learned

- How HTTP requests are structured
- How browsers send different headers than `curl`
- How JSON bodies are parsed in Flask
- How query parameters appear in `request.args`
- How CORS works and why browsers enforce it
- How to build a small RESTful API
- How to use virtual environments properly

## Project Structure

```
week3-Networking-HTTP/
│
├── app.py
├── requirments.txt
└── README.md
```

## Running the Project

### Activate the virtual environment

```bash
.venv\Scripts\activate
```

### Run the server

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```
