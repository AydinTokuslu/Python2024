# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

def biggest_odd(str):
    num = int(str)
    new_num = []
    for i in range(0,len(str)):
        new_num.append(num%10)
        num = int(num / 10)
    return new_num

def maximum(list):
    max = 1
    for i in list:
        if i > max:
            max = i
    print(max)

maximum(biggest_odd("23569"))