# Write a function called age_in_minutes that tells a user how
# old they are in minutes. Your code should ask the user to
# enter their year of birth, and it should return their age in
# minutes (by subtracting their year of birth to the current year).
# Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For
# example, 1930 is a valid year. However, entering any
# number longer or less than 4 digits long should render
# input invalid. Notify the user to input a four digits
# number.
# b. If a user enters a year before 1900, your code should
# tell the user that input is invalid. If the user enters the
# year after the current year, the code should tell the user,
# to input a valid year.
# The code should run until the user inputs a valid year.
# Your function should return the user's age in minutes. For
# example, if someone enters 1930, as their year of birth your
# function should return:
# You are 48,355,200 minutes old.

import datetime

today=datetime.date.today().year

def age_in_minutes():
    while True:
        birth = int(input("plase enter your 4-digit year of birth : "))

        if len(str(birth)) < 4 or len(str(birth)) > 5 or birth > 1990:
            print("please enter a valid 4-digit year of birth")
        else:
            age = (today - birth) * 12 * 30 * 24 * 60
            #print(f"your age is {age} minute")
            #return age
            b = age % 1000
            c = age // 1000
            d = c // 1000
            if c > 1000:
                c = c % 1000

            newAge= str(d)+","+str(c)+","+str(b)
            return f"Your age in minute is : {newAge} minutes"
            break
print(age_in_minutes())