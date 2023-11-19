import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Cache an item with a time-to-live (TTL)
r.setex('user:123', 3600, 'user_data_json')

# Retrieve cached data
cached_data = r.get('user:123')
if cached_data:
    print(cached_data.decode('utf-8'))  # Convert bytes to string
else:
    # If data is not in cache, fetch it from the primary source and cache it
    data = fetch_data_from_database()
    r.setex('user:123', 3600, data)
    print(data)
