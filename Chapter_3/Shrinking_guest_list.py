# This program informs some guest that they are no longer invited and others that they are still invited
# Author: Chris Bagalwa
# 04/02/2023

guest_list = ['Spike Lee','James Cameron','Denzel Washington','Kwameh Kuruman','Thomas Sankara','Mobutu Seseseko','Robert Mugabe']
guest_list[2] = 'Elon Musk'
guest_list.insert(0,'Patrice Lumumba')
print(guest_list)
guest_list.insert(3,'Kevin Whelan')
print(guest_list)
guest_list.append('Jilius Nyerere')
print(guest_list)
print("You can invite only two people for dinner")
while len(guest_list) >= 3:
    guest_removed = guest_list.pop(0)
    print(f'''Dear {guest_removed}, Unfortunately we can no longer invite you for Dinner, We apologise for any inconvinience caused.''')
print("\n")
print(f'''Dear {guest_list[-1]}, you are still invited for dinner''')
print(f'''Dear {guest_list[-2]}, you are still invited for dinner''')
