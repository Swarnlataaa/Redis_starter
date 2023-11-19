import redis
import uuid

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Generate a unique session ID
session_id = str(uuid.uuid4())

# Store session data with an expiry time
session_data = {'user_id': 123, 'username': 'john_doe'}
r.hmset(f'session:{session_id}', session_data)
r.expire(f'session:{session_id}', 3600)  # Set session timeout to 1 hour

# Retrieve session data
session_data = r.hgetall(f'session:{session_id}')
print(session_data)
