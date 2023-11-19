# Push elements to a list
r.lpush('my_list', 'item1')
r.lpush('my_list', 'item2')
r.rpush('my_list', 'item3')  # Right push

# Retrieve elements from a list
elements = r.lrange('my_list', 0, -1)
for element in elements:
    print(element.decode('utf-8'))
