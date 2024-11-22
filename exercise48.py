# Write a function called sort_words that takes a string of words
# as an argument, removes the whitespaces, and returns a list of
# letters sorted in alphabetical order. Letters will be separated by
# commas. All letters should appear once in the list. This means
# that you sort and remove duplicates. For example ‘love life’
# should return as ['e,f,i,l,o,v']

def sort_words(s):
    list = []
    for i in s:
        if i != " ":
            if i not in list:
                list.append(i)
                list.sort()
        else:
            continue
    print(list)


s = "love life love"
sort_words(s)