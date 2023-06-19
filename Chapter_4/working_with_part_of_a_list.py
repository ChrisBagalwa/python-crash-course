# This program works with part of a list
# Author: Chris Bagalwa
# 31/05/2023

# Slicing a list
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:4])
print(players[2:])

# Looping through a slice
players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

