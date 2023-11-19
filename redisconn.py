import redis

try:
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379)

    # Perform Redis operations
    r.set('key', 'value')
    value = r.get('key')
    print(value.decode('utf-8'))
    
except redis.exceptions.ConnectionError as e:
    print(f"Redis connection error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
