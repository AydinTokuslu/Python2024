# Write a function called zeroed_code that takes a list of numbers
# as an argument. The code should zero (0) the first and the last
# number in the list. For example, if the input is [2, 5, 7, 8, 9],
# your code should return [0, 5, 7, 8, 0].

def zeroed_code(list):
    new_list = []
    if list[0] % 2 == 1 or list[0] % 2 == 0:
       list[0] = 0
    if list[-1] % 2 == 1 or list[-1] % 2 == 0:
        list[-1] = 0
    return list


list1 = [2, 5, 7, 8, 9]
print(zeroed_code(list1))