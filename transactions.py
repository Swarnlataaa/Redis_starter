# Create a Redis transaction
pipe = r.pipeline()

# Queue multiple commands within the transaction
pipe.multi()
pipe.set('name', 'John')
pipe.incr('counter')
pipe.execute()

# Execute the transaction atomically
result = r.get('name')
counter = r.get('counter')
print(result.decode('utf-8'))  # 'John'
print(counter.decode('utf-8'))  # '1'
