# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.

def equal_strings(str1,str2):
    if len(str1) == len(str2):
        for i in str1:
            if i not in str2:
                return False
        return True
    else:
        return False

#print(equal_strings("love","evol"))
print(equal_strings("alim","mila"))