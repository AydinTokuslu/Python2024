# Write a function called guess_a_number. The function
# should ask a user to guess a randomly generated number. If the
# user guesses a higher number, the code should tell them that the
# guess is too high, if the user guesses low, the code should tell
# them that their guess is too low. The user should get a maximum
# of three guesses. When the user guesses right, the code should
# declare them a winner. After three wrong guesses, the code
# should declare them a loser.
import random



def guess_a_number():
    guess = 0
    randomNummer = random.randint(0, 9)
    print(randomNummer)
    while guess <= 3:
        guess += 1
        num = int(input("please guess a number between 0-9 = "))

        if num > randomNummer:
            print("please guess a lower nummer!!!!")
        elif num < randomNummer:
            print("please guess a higher nummer!!!!")
        else:
            print("tebrikler sayıyı buldunuz")
            break

    if guess >= 3:
        print("you lost it, try again")
    else:
        print("you are winner")

guess_a_number()