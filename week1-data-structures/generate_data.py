fake_notes_list = [
    {"id": f"note_{i}", "content": f"Log data for event {i}"} for i in range(10000)
]
fake_notes_dict = {note["id"]: note["content"] for note in fake_notes_list}
