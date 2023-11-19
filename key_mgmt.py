# Deleting a key
r.delete('my_key')

# Checking if a key exists
key_exists = r.exists('my_key')
print(key_exists)  # False
