import redis

r = redis.Redis(host='localhost', port=6379)
clients = r.client_list()
for client in clients:
    if int(client['age']) > 100 and float(client['idle']) < 100:
        print(f"High CPU usage client: {client['name']} (idle: {client['idle']}, age: {client['age']})")
