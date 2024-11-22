# s = "love live and laugh"
# Write a function called multiply_words that takes a string as an
# argument and multiplies the length of each word in the string by
# the length of other words in the string. For example, the string
# above should return 240 - love (4) live (4) and (3) laugh (5).
# However, your function should only multiply wordss will all
# lowercase letters. If a word has one upper case letter, it should be
# ignored. For example, the following string:
# s = "Hate war love Peace" should return 12 – war (3) love (4).
# Hate and Peace will be ignored because they have at least one
# uppercase letter.

def multiply_words(s):
    sum = 1
    s_new = ""
    s = s.split(" ")
    for i in s:
        if i.islower():
            sum *= len(i)
            s_new += i + " "
            s_new += str(len(i)) + " "
        else:
            continue
    return f"{sum} - {s_new}"


#s = "love live and laugh"
s = "Hate war love Peace"
print(multiply_words(s))


