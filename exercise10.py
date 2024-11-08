# Write a function called user_name that generates a username
# from the user’s email. The code should ask the user to input an
# email and the code should return everything before the @ sign
# as their user_name. For example, if someone enters
# ben@gmail.com, the code should return ben as their user_name

def user_name():
    email = input("please enter your email : ")
    name = ""
    for i in email:
        if i != "@":
            name += i
        else:
            break
    return name

def user_name2():
    email = input("please enter your email addresses: ")
    email = email.split("@")
    email_name = email[0]
    return email_name.upper()

print(user_name())
print(user_name2())
