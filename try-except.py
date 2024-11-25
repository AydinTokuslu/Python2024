# Create a simple calculator. The calculator should be able to perform
# basic math operations, add, subtract, divide and multiply. The
# calculator should take input from users. The calculator should be
# able to handle ZeroDivisionError, NameError, and ValueError.

def calculator():
    while True:
        try:
            opt = input("please enter any operations that you wan to make (+ - * / ) : ")
            num1 = int(input("please enter first nummer : "))
            num2 = int(input("please enter second nummer : "))
            if opt not in ["+", "-", "*", "/"] or len(opt) > 1 :
                print("please enter a valid operations (+ - * /) !!!!!")
        except ValueError:
            print("please enter a valid value, just the numbers!!!")
        except ZeroDivisionError:
            print("You cannot divide a number by zero.Try again ")
        except NameError:
            print("please don't enter any letter, just the numbers!!! ")
        else:
            if opt == "+":
                return f"answer is {num1 + num2}"
            elif opt == "_":
                return f"answer is {num1 - num2}"
            elif opt == "/":
                return f"answer is {num1 / num2}"
            elif opt == "*":
                return f"answer is {num1 * num2}"
        #return "Try again"

print(calculator())

"""
def average_calories():
    average = 0
    while True:
        try:
            days = input("please enter any number of days for calorie or enter 'done' to exit : ")
            for i in range(int(days)):
                if i == "done":
                    break
                else:
                    calorie = int(input(f"{i+1}. gün kalorisini giriniz : "))
                    average += calorie
            return (f"{days} gün için ortalama {round(average/int(days), 2)} kalori ortalamanız vardır")
        except ValueError:
            print("Geçerli bir giriş yapınız !!!!")
"""
"""
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
"""