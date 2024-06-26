import threading
import queue

q = queue.Queue(maxsize=10)
count = 0


def worker():
    global count
    while True:
        item = q.get()
        print(f"Working on {item}")
        if count == 28:
            print(f"Task {count} not done")
        else:
            print(f"Finished {item}")
            q.task_done()
        count += 1


# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print("All work completed")
