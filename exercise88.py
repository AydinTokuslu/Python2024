## Finding prime numbers from the entered number

prime = 2
primeList = []
number = int(input("please enter a number : "))
while number>0:
    primeList.append(number)
    while prime < number:
        if number % prime == 0:
            primeList.remove(number)
            break
        prime += 1
    prime = 2
    number -=1
print(primeList)
