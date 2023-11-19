import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Subscribe to a channel
pubsub = r.pubsub()
pubsub.subscribe('chat:general')

# Listen for messages
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Received: {message['data'].decode('utf-8')}")
