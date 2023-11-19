import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Add locations with longitude and latitude coordinates
r.geoadd('locations', (13.361389, 38.115556, 'Palermo'))
r.geoadd('locations', (15.087269, 37.502669, 'Catania'))

# Calculate distance between two points
distance = r.geodist('locations', 'Palermo', 'Catania', unit='km')
print(f"Distance between Palermo and Catania: {distance} km")
