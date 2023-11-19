# Bitmaps are used for compact bit-level data storage
# Set or clear individual bits
r.setbit('my_bitmap', 5, 1)
r.setbit('my_bitmap', 7, 1)

# Get the value of a specific bit
bit_value = r.getbit('my_bitmap', 5)
print(bit_value)
