import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a string value
r.set('my_key', 'Hello, Redis!')

# Get the value of a key
value = r.get('my_key')
print(value.decode('utf-8'))  # Convert bytes to string
