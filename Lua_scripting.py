# Define a Lua script
lua_script = """
return redis.call('set', KEYS[1], ARGV[1])
"""

# Execute the Lua script
r.eval(lua_script, 1, 'my_key', 'my_value')

# Verify the result
value = r.get('my_key')
print(value.decode('utf-8'))  # 'my_value'
