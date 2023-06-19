# This program make numerical lists
# Author: Chris Bagalwa
# 31/05/2023

for value in range(1,5):
    print(value)

print("\n")
# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

print("\n")
# Using range() to Make a List of Numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# Simple statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))