# In this challenge, copy the text below and save it as a CSV file.
# Save it in the same folder as your Python file. Save it as
# python.csv.
# Write a function called just_digits that reads the text from the
# CSV file and returns only digit elements from the file. Your
# function should return 1991, 2, 200, 3, 2008 as a list of
# strings.
# “Python was released in 1991 for the first time. Python 2 was
# released in 2000 and introduced new features, such as list
# comprehensions and a cycle-detecting garbage collection system
# (in addition to reference counting). Python 3 was released in 2008
# and was a major revision of the language that is not
# completely backward-compatible.”

def just_digits():
    path_w = 'python.csv'

    s = """Python was released in 1991 for the first time. 
Python 2 was released in 2000 and introduced new features, 
such as list comprehensions and a cycle-detecting garbage 
collection system (in addition to reference counting). 
Python 3 was released in 2008 and was a major revision 
of the language that is not completely backward-compatible"""

    with open(path_w, mode='w') as f:
        f.write(s)
        f.close()

    digits = []
    with open("python.csv", "r", encoding="utf-8") as file:
        files = file.read()
        files = files.split(" ")
        for i in files:
            print(i)
            if i.isdigit():
                digits.append(i)
    print(digits)

just_digits()