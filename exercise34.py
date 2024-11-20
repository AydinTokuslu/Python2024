# Write a function called any_number that can receive any
# number of arguments (integers and floats) and return the
# average of those integers. If you pass 12, 90, 12, 34 as
# arguments your function should return 37.0 as average. If you
# pass 12, 90 your function should return 51.0 as average.

def any_number():
    average = 0
    sayi = int(input("how many number want to enter : "))
    for i in range(sayi):
        num = int(input(f"{i+1}. sayıyı giriniz : "))
        average += num
    average //= sayi
    print(f"Girilen {sayi} sayının ortalaması : {average}")

any_number()
