# This program removes elements from a list
# Author: Chris Bagalwa
# 30/05/2023

# Removing an item using the del statement
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
# Use del statement when you know the positionof the item
del motorcycles[0]
print(motorcycles)

# Use pop method to remove the last item in a list
motorcycles.pop()
print(motorcycles)

# Popping items from any position in a list
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value
motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)