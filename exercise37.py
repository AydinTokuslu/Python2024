# Write a function called capitalize. This function takes a string
# as an argument and capitalizes the first letter of each word. For
# example, ‘i like learning’ becomes ‘I Like Learning’.

def capitalize(str):
    str2 = ""
    for i in str.split(" "):
        str2 += i.capitalize() + " "
    print(str2)

str = "i like learning"
capitalize(str)