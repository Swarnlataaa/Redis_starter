# Publish a message to a stream
r.xadd('mystream', {'field1': 'value1', 'field2': 'value2'})

# Read messages from a stream
entries = r.xread({'mystream': '0'}, count=1)
for entry in entries:
    stream_name, message_data = entry
    message_id, fields = message_data[0]
    print(f"Received message: {fields}")
