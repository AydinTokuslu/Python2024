# Write a function called even_or_average that ask a user to
# input five numbers. Once the user is done, the code should
# return the largest even number in the inputted numbers. If
# there is no even number in the list, the code should return the
# average of all the five numbers.

def even_or_average():
    maxNum = 0
    list = []
    for i in range(5):
        num = int(input(f"{i+1}. sayıyı giriniz : "))
        list.append(num)
        if num > maxNum:
            maxNum = num
    return f"Maksimum numara : {maxNum}"

print(even_or_average())