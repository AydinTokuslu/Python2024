# Write a function called repeated_name that finds the most
# repeated name in the following list.
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]

def repeated_name(s):
    repeated = {}
    for i in s:
        if i not in repeated.keys():
            #repeat += 1
            repeated[i] = 1
            #print(repeated)
        else:
            repeated[i] += 1
    return f"most repeated name is : {max(repeated, key=repeated.get)} and repeat number is : {max(repeated.values())}"

name = ["John", "Peter", "John", "Peter", "Jones", "Peter", "Petre", "John", "John"]
print(repeated_name(name))
