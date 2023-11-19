# Set field-value pairs in a hash
r.hset('my_hash', 'field1', 'value1')
r.hset('my_hash', 'field2', 'value2')

# Get the value of a field in a hash
value = r.hget('my_hash', 'field1')
print(value.decode('utf-8'))
