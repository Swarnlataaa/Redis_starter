import redis
import time

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Add data points to a time-series
current_time = int(time.time())
r.zadd('time_series', {current_time: 'data_point_1'})

# Retrieve data points for a specific time range
start_time = current_time - 3600  # 1 hour ago
end_time = current_time
data_points = r.zrangebyscore('time_series', start_time, end_time)

for data_point in data_points:
    print(data_point.decode('utf-8'))
