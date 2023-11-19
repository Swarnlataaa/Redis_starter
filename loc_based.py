const redis = require('redis');
const client = redis.createClient({ host: 'localhost', port: 6379 });

// Add locations
client.geoadd('locations', [13.361389, 38.115556, 'Palermo'], [15.087269, 37.502669, 'Catania']);

// Find locations within a radius
client.georadius('locations', 13.361389, 38.115556, 100, 'km', (err, locations) => {
    if (err) {
        console.error('Error:', err);
    } else {
        console.log('Locations within 100 km:', locations);
    }
});
