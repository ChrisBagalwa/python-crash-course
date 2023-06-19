# This program looks at tuples
# Author: Chris Bagalwa
# 31/05/2023

# Define a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# Looping through all values in a tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
