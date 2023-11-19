import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Publish a message to a channel
r.publish('chat:general', 'Hello, everyone!')
