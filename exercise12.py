# Write a function called string_range that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.) For example, if you pass 6 as
# an argument, your function should return ‘0.1.2.3.4.5’.

def string_range():
    num = input("please enter a single number : ")
    for i in range(0, int(num)):
        if i == int(num) - 1:
            print("{}".format(i), end=" ")
        else:
            print("{}.".format(i), end="")
            continue

def string_range2(num:int):
    x = [str(i) for i in range(num)]
    #Using join method to add dots
    x = ".".join(x)
    return x

print(string_range())
print(string_range2(6))