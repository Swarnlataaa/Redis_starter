# Pipelining allows you to send multiple commands in a batch for improved performance
pipe = r.pipeline()

# Queue multiple commands
pipe.set('name', 'John')
pipe.get('name')

# Execute the commands in a single round trip
result = pipe.execute()

# Retrieve the result
print(result[1].decode('utf-8'))  # 'John'
