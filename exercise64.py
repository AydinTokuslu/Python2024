# Write a function called check_pangram that takes a string
# and checks if it is a pangram. A pangram is a sentence that
# contains all the letters of the alphabet. If it is a pangram,
# the function should return True, otherwise, return False. The
# following sentence is a pangram so it should return True:
# 'the quick brown fox jumps over a lazy dog'

def check_pangram(str):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    str = str.replace(" ","")
    pangram = []
    for i in str:
        if i not in pangram:
            pangram.append(i)
    pangram.sort()
    print(pangram)
    if pangram != letters:
        print("this sentence is not a pangram")
    else:
        print("this sentence is a pangram")

x = "the quick brown fox jumps over a lazy dog"
check_pangram(x)