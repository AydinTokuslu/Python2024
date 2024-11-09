# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.

def hide_password():
    password = input("please enter a password : ")
    newPassword = ""
    for i in range(0, len(password)):
        newPassword += "*"
    print(f"Your new Password is {newPassword}")

hide_password()
