# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element
# appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.


def count(s):
    dict = {}
    for i in s:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1

    print(dict)

s = "hello boby"
count(s)

