# Write a function called your_vat. The function takes no
# parameter. The function asks the user to input the price of an
# item and VAT (vat should be a percentage). The function should
# return the price of the item plus VAT. If the price is 220 and,
# VAT is 15% your code should return a vat inclusive price of 253.
# Make sure that your code can handle ValueError. Ensure the
# code runs until valid numbers are entered. (hint: Your code
# should include a while loop)

def your_vat():
    while True:
        try:
            price = int(input("please enter the price : "))
            vat = int(input("please enter percentage of the VAT : "))
            if vat > 0 and vat < 100:
                last_price = price - (price * vat)/100
                print(f"Your payment after the discount is : {last_price}")
                break
        except ValueError:
            print("please enter a valid integer regarding item_price and vat")

your_vat()