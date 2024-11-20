# Write a function called even_or_average that ask a user to
# input five numbers. Once the user is done, the code should
# return the largest even number in the inputted numbers. If
# there is no even number in the list, the code should return the
# average of all the five numbers.

list = []
for i in range(5):
    num = int(input(f"{i+1}. sayıyı giriniz : "))
    list.append(num)

def even_or_average(list):
    average = 0
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            average += i

    if len(even_list) > 0:
        print(f"The max even number from the entered is : {max(even_list)} ")
    else:
        print(f"the average of the entered numbers is : {average // len(list)}")

even_or_average(list)