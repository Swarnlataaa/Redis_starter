import redis

r = redis.Redis(host='localhost', port=6379)
info = r.info()
print(f"Used memory: {info['used_memory']} bytes")
print(f"Total connections: {info['total_connections_received']}")
