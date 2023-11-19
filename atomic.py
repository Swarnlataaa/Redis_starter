# Incrementing a value atomically
r.set('counter', 5)
r.incr('counter')  # Increment by 1
new_value = r.get('counter')
print(new_value.decode('utf-8'))

# Decrementing a value atomically
r.decr('counter')  # Decrement by 1
new_value = r.get('counter')
print(new_value.decode('utf-8'))
