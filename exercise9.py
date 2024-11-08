# Tuple of Student Sex
# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list. Here is a
# list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male',
#  'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should
# return:
# [(‘Male’,7), (‘female’,6)]

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def students_genre(list):
    male_students = []
    female_students = []
    for i in list:
        if i.lower() == "male":
            male_students.append(i)
        else:
            female_students.append(i)
    return [("Male", len(male_students)), ("Female", len(female_students))]

print(students_genre(students))