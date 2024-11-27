# Write a function called spelling_checker. This code asks the
# user to input a word and if a user inputs a wrong spelling it
# should suggest the correct spelling by asking the user if they
# meant to type that word. If the user says no, it should ask the
# user to enter the word again. If the user says yes, it should
# return the correct word. If the word entered by the user is
# correctly spelled the function should return the correct word.
# Use the module textblob.

from textblob import TextBlob

def spelling_checker():
    while True:
        word = input("please enter a word : ")
        if word != str(TextBlob(word).correct()):
            print("you entered a wrong spelling word")
            answer = input(f"Did you mean : {str(TextBlob(word).correct())}? \ntype yes/no : ")
            if answer == "yes":
                #print(f"corrected text: {str(TextBlob(word).correct())}")
                break
            else:
                print("Please try again")
        elif word == TextBlob(word).correct():
            break
        #     print("you enter the wrong choice, please only 'yes' or 'no' ")
    return f'Your word is, {TextBlob(word).correct()}'

spelling_checker()

