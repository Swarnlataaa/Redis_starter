import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Key-value caching example
def get_data_from_database():
    # Simulate fetching data from a database
    return "Data from the database"

def get_cached_data():
    cached_data = r.get("cached_data")
    if cached_data:
        return cached_data.decode('utf-8')  # Convert bytes to string
    else:
        data = get_data_from_database()
        r.set("cached_data", data)
        return data

# Fetch data (first time, it will be retrieved from the database, cached thereafter)
data = get_cached_data()
print(data)
