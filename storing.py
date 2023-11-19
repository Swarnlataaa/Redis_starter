import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Storing data
r.set('my_key', 'my_value')

# Retrieving data
value = r.get('my_key')
print(value.decode('utf-8'))  # Convert bytes to string
