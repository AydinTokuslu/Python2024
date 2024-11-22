# Create a function called all_the_same that takes one
# argument, a string, a list, or a tuple and checks if all the
# elements are the same. If the elements are the same, the function
# should return True. If not, it should return False. For example,
# [‘Mary’, ‘Mary’, ‘Mary’] should return True

def all_the_same(s):
    for i in range(len(s)-1):

        if s[i] != s[i+1]:
            return False
    return True



s = ["Mary", "Mary", "kary"]
print(all_the_same(s))