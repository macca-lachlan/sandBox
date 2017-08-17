"""
Lachlan McDonald
"""

username = input("What is your name? :")
while len(username) == 0:
    print("You need to enter your name")
    username = input("What is your name? :")
for i in range(0, len(username), 2):
    print(username[i])
