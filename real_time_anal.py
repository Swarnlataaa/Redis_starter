import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Increment a counter
r.incr('page_views:home')

# Retrieve the counter value
page_views = r.get('page_views:home')
print(page_views.decode('utf-8'))
