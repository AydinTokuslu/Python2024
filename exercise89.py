## Finding prime numbers from the entered number

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


num=int(input("please enter a number : "))
prime_numbers=[]

for i in range(2, num+1):
    if prime(i):
        prime_numbers.append(i)


print(prime_numbers)