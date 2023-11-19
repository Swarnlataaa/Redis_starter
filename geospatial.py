# Geospatial data allows you to store and query location-based data
# Add locations with longitude and latitude coordinates
r.geoadd('my_geo', (13.361389, 38.115556, 'Palermo'))
r.geoadd('my_geo', (15.087269, 37.502669, 'Catania'))

# Calculate distance between two points
distance = r.geodist('my_geo', 'Palermo', 'Catania', unit='km')
print(f"Distance between Palermo and Catania: {distance} km")
