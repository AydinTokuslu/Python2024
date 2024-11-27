# Create a function called generate_password that generates any
# length of password for the user. The password should have a
# random mix of upper letters, lower letters, numbers, and
# punctuation symbols. The function should ask the user how
# strong they want the password to be. The user should pick from -
# weak, strong, and very strong. If the user picks weak, the
# function should generate a 5-character long password. If the user
# picks strong, generate an 8-character password and if they pick
# very strong, generate a 12-character password.

import random
import string

def generate_password():

    while True:
        password = input("how strong want you the password? \nfor weak :1, for strong:2, for very strong :3 : ")
        passwd = []
        if password == "1":
            get_random_string(5)
            break
        elif password == "2":
            get_random_string(8)
            break
        elif password == "3":
            get_random_string(12)
            break
        else:
            print("wrong choice, you made, try again!!")


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Your strong password is:", password)

generate_password()