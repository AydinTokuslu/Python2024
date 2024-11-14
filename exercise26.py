# Write a function called flat_list that takes one argument, a
# nested list. The function converts the nested list into a one-dimension list.
# For example [[2,4,5,6]] should return
# [2,4,5,6].

newList = []

def flat_list(list):
    for i in list:
        for j in i:
            newList.append(j)
    print(newList)

nestedList = [[2,4,5,6]]
flat_list(nestedList)