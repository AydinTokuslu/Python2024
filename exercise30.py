# Write a function called sum_list with one parameter that takes
# a nested list of integers as an argument and returns the sum of
# the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
# as an argument your function should return a sum of 33.

def sum_list(list):
    total = 0
    for i in list:
        for j in i:
            total += j
    return f"total number of nested list is : {total}"

nestedList = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(nestedList))