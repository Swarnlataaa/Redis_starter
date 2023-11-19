# Set a key to expire in 60 seconds
r.setex('my_key', 60, 'my_value')

# Get the remaining time to live (TTL) of a key in seconds
ttl = r.ttl('my_key')
print(ttl)  # Remaining time in seconds
