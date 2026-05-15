import time
from generate_data import fake_notes_list, fake_notes_dict


def slow_lookup(note_id):
    for note in fake_notes_list:
        if note["id"] == note_id:
            return note
    return None


def fast_lookup(note_id):
    return fake_notes_dict.get(note_id)


def benchmark(note_id="note_9999", runs=1000):
    slow_times = []
    fast_times = []

    for _ in range(runs):
        t1 = time.perf_counter()
        slow_lookup(note_id)
        slow_times.append(time.perf_counter() - t1)

        t2 = time.perf_counter()
        fast_lookup(note_id)
        fast_times.append(time.perf_counter() - t2)

    slow_avg = sum(slow_times) / runs
    fast_avg = sum(fast_times) / runs

    print("Slow avg:", slow_avg)
    print("Fast avg:", fast_avg)
    print("Speedup:", slow_avg / fast_avg)


if __name__ == "__main__":
    benchmark()
