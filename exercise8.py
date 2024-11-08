# Create a function called my_discount. The function takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For
# example, if the user enters 150 as price and 15% as the discount,
# your function should return 127.5.

def my_discount():
    while True:
        try:
            price = int(input("please enter the price : "))
            discount = int(input("please enter the discount (percentage) : "))
            last_price = price - (price * discount) / 100
            print(f"Total price with discount is  : {last_price}")
        except:
            print("please enter digit number for price and discount !!!!")



print(my_discount())