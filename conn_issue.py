import redis

try:
    r = redis.Redis(host='localhost', port=6379)
    r.ping()  # Ping to test the connection
except redis.exceptions.ConnectionError as e:
    print(f"Redis connection error: {e}")
