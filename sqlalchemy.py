from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_url'
db = SQLAlchemy(app)
r = redis.Redis(host='localhost', port=6379)

class User(db.Model):
    # Define the User model

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    key = f'user_{user_id}'
    user_data = r.get(key)
    if user_data:
        return jsonify({'user': user_data.decode('utf-8')})
    else:
        user = User.query.get(user_id)
        if user:
            user_data = user.serialize()
            r.setex(key, 3600, json.dumps(user_data))  # Cache user data for an hour
            return jsonify({'user': user_data})
        else:
            return jsonify({'error': 'User not found'}, 404)

if __name__ == '__main__':
    app.run(debug=True)
