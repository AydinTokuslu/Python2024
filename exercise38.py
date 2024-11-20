# str1= 'leArning is hard, bUt if You appLy youRself ' \
#  'you can achieVe success'

# You are given a string of words. Some-of the words in the string
# contain uppercase letters. Write a code that will return all the
# words that have an uppercase letter. Your code should return a
# list of the words. Each word in the list should be reversed. Here
# is how your output should look:

# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']

str1= "leArning is hard, bUt if You appLy youRself you can achieVe success"
def uppercase(str):
    new_str = ""
    for i in str.split(" "):
        #print(i)
        if i.islower():
            continue
        else:
            new_str += i + " "
    new_str2 = ""
    for i in new_str.split(" "):
        new_str2 += i[::-1] + " "
    return new_str2

print(uppercase(str1))

