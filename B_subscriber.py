import redis

r = redis.Redis(host='localhost', port=6379)
pubsub = r.pubsub()
pubsub.subscribe('microservice_events')

for message in pubsub.listen():
    if message['type'] == 'message':
        data = message['data'].decode('utf-8')
        print(f"Received: {data}")
