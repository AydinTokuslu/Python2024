# Strings to Integers
# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.

def convert_add(list):
    newlist = []
    sum = 0
    for i in list:
        newlist.append(int(i))
        sum += int(i)
    return newlist, sum

xList = ["1", "3", "5"]
print(convert_add(xList))