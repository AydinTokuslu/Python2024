



def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,

}
def calculator():
    num1 = int(input("enter the first number : "))
    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        operation_symbol = input("pick an operation symbol : ")
        num2 = int(input("enter the second nummer : "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        if input(f"type 'y' to continue with {result} : ") == "y" :
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()