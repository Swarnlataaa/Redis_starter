from flask import Flask, request, jsonify
import redis

app = Flask(__name)
r = redis.Redis(host='localhost', port=6379)

@app.route('/api/data')
def get_data():
    key = 'cached_data'
    cached_data = r.get(key)
    if cached_data:
        return jsonify({'data': cached_data.decode('utf-8')})
    else:
        # Fetch data from the database
        data = fetch_data_from_database()
        r.setex(key, 3600, data)  # Cache data for an hour
        return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True)
