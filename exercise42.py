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
            print("please enter a valid value")
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