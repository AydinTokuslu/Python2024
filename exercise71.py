# Write a function called translate that takes the following
# words and translates them into pig Latin.
# a = 'i love python'
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
# end. For example, ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move
# the first letter to the end and add ‘ay’ to the end. For
# example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay

def translate(a):
    a = a.split(" ")
    newStr=""
    vowel = ["a", "e", "i", "o", "u"]
    for i in a:
        if i[0] in vowel:
            newStr += i[0] + "yay "
        else:
            newStr += i[1::] + i[0] + "ay "
    print(newStr)


a = 'i love python too much'
translate(a)