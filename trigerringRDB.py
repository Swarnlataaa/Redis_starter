import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Trigger an RDB snapshot
r.save()
