# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.
# register = {'Michael':'yes','John': 'no',
#  'Peter':'yes', 'Mary': 'yes'}

def register_check(dic):
    number_of_students = 0
    for i in dic:
        #print(dic[i])
        if dic[i] == "yes":
            number_of_students += 1
    return number_of_students

register = {'Michael': 'yes', 'John': 'no', 'Peter':'yes', 'Mary': 'yes', "Thomas": "yes"}
print(register_check(register))
print(list(filter(lambda string : "yes" in string, register)))