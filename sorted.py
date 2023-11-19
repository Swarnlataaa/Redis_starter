# Add elements with scores to a sorted set
r.zadd('my_sorted_set', {'item1': 10, 'item2': 5, 'item3': 20})

# Retrieve elements from the sorted set by score range
elements = r.zrangebyscore('my_sorted_set', 0, 15)
for element in elements:
    print(element.decode('utf-8'))
