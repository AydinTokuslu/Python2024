# Create three functions. The first called add_hash takes a string and
# adds a hash # between the words. The second function called
# add_underscore removes the hash (#) and replaces it with an
# underscore "_" The third function called remove_underscore,
# removes the underscore and replaces it with nothing. if you pass
# ‘Python’ as an argument for the three functions, and you call them at
# the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

def add_hash(str):
    newStr=""
    for i in str:
        newStr += i + "#"
    return newStr[:-1]

def add_underscore(str1):
    newStr2 = ""
    for i in str1:
        if i != "#":
            newStr2 += i + "_"
        else:
            continue
    return newStr2[:-1]

def remove_underscore(str2):
    newStr3 = ""
    for i in str2:
        if i != "_":
            newStr3 += i
        else:
            continue
    return newStr3

print(remove_underscore(add_underscore(add_hash("Python"))))

def add_hash1(a: str):
    return "#".join(a)
def add_underscore1(a: str):
    return str(a).replace("#", "_")
def remove_underscore1(a: str):
    return str(a).replace("_", "")
print(remove_underscore1(add_underscore1(add_hash1('Python'))))