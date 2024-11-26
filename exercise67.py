# Create a function called count_the_vowels. The function
# takes one argument, a string, and returns the number of vowels
# in the string. For example, ‘hello’ should return 2 vowels. If a
# vowel appears in a string more than once it should be counted
# as one. For example, ‘saas’ should return 1 vowel. Your code
# should count lowercase and uppercase vowels.

def count_the_vowels(s):
    vowels = ["a","e","i","o","u"]
    vowelsList = {}
    for i in s:
        if i in vowels:
            if i not in vowelsList:
                vowelsList[i] = 1
            else:
                vowelsList[i] += 1
        else:
            continue
    return vowelsList

#s = "hello"
#s = "saas"
s = "hayati coook yasa"
print(count_the_vowels(s))