# Write a function called index_position. This function takes a
# string as a parameter and returns the positions or indexes of all
# lower letters in the string. For example, ‘LovE’ should return
# [1,2].

def index_position(s):
    indexA = []
    for i in s:
        if i.islower():
            indexA.append(s.index(i))
    return indexA


s = "LovEr"
print(index_position(s))