# names = ["kerry", "dickson", "John", "Mary",
#  "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order. Using the list above, your
# code should return: ('kerry', 'dickson', 'carol', 'adam')

def tuple_list(list):
    lower_case = []
    for i in list:
        if i.islower():
            lower_case.append(i)
    lower_case.sort(reverse=True)
    return lower_case


names = ["kerry", "altar", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(tuple_list(names))