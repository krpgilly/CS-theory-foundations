import time
from fastapi import FastAPI, HTTPException
from generate_data import fake_notes_list, fake_notes_dict

app = FastAPI()


@app.get("/slow/{note_id}")
def slow_search(note_id: str):
    start = time.perf_counter()

    result = None
    for note in fake_notes_list:
        if note["id"] == note_id:
            result = note
            break

    elapsed = time.perf_counter() - start

    if not result:
        raise HTTPException(status_code=404, detail="Not found")

    return {"result": result, "time": elapsed, "complexity": "O(n)"}


@app.get("/fast/{note_id}")
def fast_search(note_id: str):
    start = time.perf_counter()

    result = fake_notes_dict.get(note_id)
    elapsed = time.perf_counter() - start

    if not result:
        raise HTTPException(status_code=404, detail="Not found")

    return {"result": result, "time": elapsed, "complexity": "O(1)"}
