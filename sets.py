# Add elements to a set
r.sadd('my_set', 'item1')
r.sadd('my_set', 'item2')

# Retrieve elements from a set
elements = r.smembers('my_set')
for element in elements:
    print(element.decode('utf-8'))
