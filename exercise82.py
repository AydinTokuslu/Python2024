# Write a function called search_binary that searches for the
# number 22 in the following list and returns its index. The
# function should take two parameters, the list and the item that
# is being searched for. Use binary search (iterative Method).
# list1 = [12, 34, 56, 78, 98, 22, 45, 13]

def search_binary(list,num):
    for i in list:
        if num == i:
            print(f"The element index of {num} is : {list.index(i)}")

list = [12, 34, 56, 78, 98, 22, 45, 13]
num = 45
search_binary(list,num)