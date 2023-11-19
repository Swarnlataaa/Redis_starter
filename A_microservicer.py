import redis

r = redis.Redis(host='localhost', port=6379)

# Publish a message
r.publish('microservice_events', 'New data available')
