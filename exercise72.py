# Create a function called words_with_vowels, this function
# takes a string of words and returns a list of only words that
# have vowels in them. For example, ‘You have no rhythm’ should
# return [‘You’,’have’, ‘no’].

def words_with_vowels(s):
    listVowels = []
    vowel = ["a", "e", "i", "o", "u"]
    s = s.split(" ")
    for i in s:
        for j in i:
            if j in vowel:
                if i not in listVowels:
                    listVowels.append(i)
            else:
                continue
    return listVowels

a = "You have no rhythm no soul"
print(words_with_vowels(a))
