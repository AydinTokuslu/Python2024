# Write a function called largest_number that takes a list of
# integers and re-arrange the individual digits to create the largest
# number possible. For example, if you pass the following as an
# argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
# number in this exact format: 9,877,632 as the largest number.

def largest_number(list):
    nummer = ""
    for i in list:
        nummer += str(i)

    nummer = ''.join(sorted(nummer, reverse = True))
    numList = ""
    sayi1 = int(nummer) % 1000
    sayi2 = int(nummer) // 1000
    sayi3 = sayi2 % 1000
    sayi4 = sayi2 // 1000

    return f"{sayi4},{sayi3},{sayi1}"


list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))