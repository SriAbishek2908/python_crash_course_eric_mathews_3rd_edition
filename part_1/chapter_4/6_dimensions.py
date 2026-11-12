# Tuple
dimensions = (100,10)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 200
my_t =(3,)
print(list(my_t))

# Looping Through All Values in a Tuple
dimensions = (200,20)
for dimension in dimensions:
    print(dimension)

# Writing Over a Tuple
dimensions = (1000,100)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (2000,200)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)