const redis = require('redis');
const express = require('express');
const app = express();
const port = 3000;

const client = redis.createClient({ host: 'localhost', port: 6379 });

app.get('/pageviews', (req, res) => {
    client.incr('page_views');
    res.send('Page Viewed');
});

app.get('/stats', (req, res) => {
    client.get('page_views', (err, pageViews) => {
        if (err) {
            res.send('Error fetching data');
        } else {
            res.send(`Page Views: ${pageViews}`);
        }
    });
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
});
