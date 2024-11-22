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