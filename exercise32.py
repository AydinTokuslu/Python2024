# Write a function called user_name, that creates a username
# for the user. The function should ask a user to input their name.
# The function should then reverse the name and attach a
# randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.

import random
from random import *

def user_name():
    name = input("please enter your name : ")
    nameReverse = name[::-1]
    random_num = randint(0, 9)
    return f"{nameReverse}{random_num}"

print(user_name())
