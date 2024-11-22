# str1 = "the love is real"
# Write a function called read_backwards that takes a string as
# an argument and reverses it. For example, the string above
# should return: "real is love the"

def read_backwards(s):
    list = ""
    s = s.split(" ")
    for i in s[::-1]:
        list += i + " "
    print(list)

'''
def read_backwards(str):
    new_str = str.split()
    for i in reversed(new_str):
        print(i, end=" ")

'''
str1 = "the love is real"
read_backwards(str1)