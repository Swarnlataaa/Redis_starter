import redis
import threading

# Create a Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

def publisher():
    # Publish a message to a channel
    r.publish('my_channel', 'Hello, subscribers!')

def subscriber():
    # Subscribe to a channel
    pubsub = r.pubsub()
    pubsub.subscribe('my_channel')

    # Listen for messages
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received: {message['data']}")

# Start a subscriber thread
subscriber_thread = threading.Thread(target=subscriber)
subscriber_thread.start()

# Publish a message
publisher()
