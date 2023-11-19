import redis

r = redis.Redis(host='localhost', port=6379)
info = r.info()
used_memory = int(info['used_memory'])
max_memory = int(info['maxmemory'])

if used_memory > max_memory:
    print("Redis is running out of memory.")
    # Configure eviction policy or increase memory limit
