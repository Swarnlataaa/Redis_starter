import redis

r = redis.Redis(host='localhost', port=6379)
slow_logs = r.slowlog_get(10)  # Get the last 10 slow queries
for log in slow_logs:
    print(f"Slow query: {log['command']} took {log['duration']} microseconds")
