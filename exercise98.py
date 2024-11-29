def maxc(str):
    dict = {}
    for i in str:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    #return dict.values()

    max = 0
    karakter = ""
    for i,j in dict.items():
        #print(i)
        if j > max:
            max = j
            karakter = i
    return f"{karakter}:{max}"


print(maxc("mert mekatronik udemy dersleri"))