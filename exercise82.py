# Write a function called search_binary that searches for the
# number 22 in the following list and returns its index. The
# function should take two parameters, the list and the item that
# is being searched for. Use binary search (iterative Method).
# list1 = [12, 34, 56, 78, 98, 22, 45, 13]


"""
def search_binary(list1,x):
    low = 0
    high = len(list1)-1
    while low <= high:
        mid_index = (high + low) // 2
        if list1[mid_index] == x:
            return mid_index
        elif list1[mid_index] > x :
            high = mid_index -1
        elif list1[mid_index] < x :
            low = mid_index + 1
    return "no element"



list1 = [12, 34, 56, 78, 98, 22, 45, 13]
list1 = sorted(list1)
print(list1)
number = 45

results = search_binary(list1,number)
if results == "no element":
    print("Element is not in the list")
else:
    print(f"The element index is {results}")
"""

def search_binary(list,num):
    for i in list:
        if num == i:
            print(f"The element index of {num} is : {list.index(i)}")

list = [12, 34, 56, 78, 98, 22, 45, 13]
num = 45
search_binary(list,num)