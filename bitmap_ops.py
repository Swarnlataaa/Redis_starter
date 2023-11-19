# Perform bitwise operations on bitmaps
r.setbit('bitmap1', 1, 1)  # Set bit 1
r.setbit('bitmap2', 2, 1)  # Set bit 2

# Perform bitwise AND operation
r.bitop('AND', 'result_bitmap', 'bitmap1', 'bitmap2')

# Check the result
result = r.get('result_bitmap')
print(result)  # b'\x00'
