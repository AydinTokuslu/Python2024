# Write a function called difference that takes two lists as
# arguments. This function should return all the elements that are
# in list a but not in list b and all the elements in list b not in list
# a. For example:
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]
# Use list comprehension in your function.

def difference(l1,l2):
    list3 = []
    for i in l1:
        if i not in l2:
            list3.append(i)
    for j in l2:
        if j not in l1:
            list3.append(j)
    return list3

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1,list2))
