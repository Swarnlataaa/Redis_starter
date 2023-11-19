# HyperLogLog is used for approximate cardinality estimation
# Add elements to a HyperLogLog structure
r.pfadd('my_hyperloglog', 'item1')
r.pfadd('my_hyperloglog', 'item2')

# Retrieve the estimated cardinality
cardinality = r.pfcount('my_hyperloglog')
print(cardinality)
