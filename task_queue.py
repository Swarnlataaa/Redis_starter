import redis
import time
import threading

r = redis.Redis(host='localhost', port=6379)
queue_name = 'task_queue'

def worker():
    while True:
        task = r.brpop(queue_name, timeout=0)  # Get a task from the queue
        if task:
            _, task_data = task
            print(f"Processing task: {task_data.decode('utf-8')}")
            # Perform the task (e.g., send an email)
        time.sleep(1)  # Simulate work

# Start worker threads
for _ in range(3):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Enqueue tasks
for i in range(10):
    r.lpush(queue_name, f'Task {i}')
    time.sleep(0.5)
