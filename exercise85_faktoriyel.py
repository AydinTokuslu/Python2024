# bir sayının faktöriyelini bulma

def faktoriyelAl(x):
    fakt = ""
    faktoriyel = 1
    """
    for i in range(1,x):
        faktoriyel *= i
        fakt += str(i) +"*"
    print(f"Girilen {x} sayısının faktoriyeli : {fakt}{x}={faktoriyel*x}")
    """
    for i in range(1,x+1):
        faktoriyel *= 1
        if x > i+1:
            fakt += str(x-i)+" - "
    print(f"{x} sayısının faktöriyeli {x} - {fakt}1 = {faktoriyel}")
faktoriyelAl(6)