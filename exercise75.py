# Write a function called student_marks that records marks
# achieved by students in a test. The function should ask the user
# to input the name of the student and then ask the user to input
# the marks achieved by the student. The information should be
# stored in a dictionary. The name is the key and the marks is the
# value. When the user enters done, the function should return a
# dictionary of names and values entered.

def student_marks():
    marks = {}
    while True:
        name = input("please enter your name or '0' to exit: ")
        if name == "0":
            break
        else:
            mark = input("please enter your mark : ")
            marks[name] = mark

    print(marks)


student_marks()