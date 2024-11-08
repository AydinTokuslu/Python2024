#  Odd and Even
# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the
# difference between the largest even number in the list and the
# smallest odd number in the list. For example, if you pass
# [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(list):
    odd = 1000
    even = 0
    for i in list:
        if i % 2 == 0:
            if i > even :
                even = i
        elif i % 2 == 1 :
            if i < odd :
                odd = i
    print(f"{even} - {odd} = {even-odd}")

numbers = [3, 2, 4, 6,7,8]

def odd2_even2(list):
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f"{max(even)} - {min(odd)} = {max(even) - min(odd)}"
odd_even(numbers)
print(odd2_even2(numbers))