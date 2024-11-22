# Write a function called unique_numbers that takes a list of
# numbers as an argument. Your function is going to find all the
# unique numbers in the list. It will then sum up the unique
# numbers. You will calculate the difference between the sum of
# all the numbers in the original list and the sum of unique
# numbers in the list. If the difference is an even number, your
# function should return the original list. If the difference is an
# odd number, your function should return a list with unique
# numbers only. For example [1, 2, 4, 5, 6, 7, 8, 8] should
# return [1, 2, 4, 5, 6, 7, 8, 8].

def unique_numbers(list):
    repeatedList = []
    unique = []

    for i in list:
        if i not in unique:
            unique.append(i)
        else:
            repeatedList.append(i)


    if (sum(list) - sum(unique)) % 2 == 0:
        print(list)
    else:
        print(unique)

x = [1, 2, 4, 5, 6, 7, 8, 1]
unique_numbers(x)

