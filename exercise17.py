# Write a function called zeros_last. This function takes a list as
# argument. If a list has zeros (0), it will move them to the front of
# the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the
# original list sorted in ascending order. For example, if you pass
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].

def zeros_last(list):
    zero_list = []
    count_zero = 0
    #list.sort()
    for i in list:
        #print(i)
        if i != 0:
            zero_list.append(i)
            #list.remove(i)
        else:
            count_zero += 1
    zero_list.sort()
    for i in range(0,(count_zero)):
        zero_list.append(0)
    return zero_list

#def new_list(count_zero, zero_list):


numbers = [0, 1, 4, 0, 7, 6, 0, 0, 0, 9, 0]
#numbers = [2, 1, 4, 7, 6]
print(zeros_last(numbers))
#new_list(zeros_last(numbers))