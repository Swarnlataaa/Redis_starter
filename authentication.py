import redis

try:
    r = redis.Redis(host='localhost', port=6379, password='your_password', ssl=True)
    r.ping()
except redis.exceptions.ResponseError as e:
    print(f"Redis authentication error: {e}")
