# A school has asked you to write a program that will calculate
# teachers' salaries. The program should ask the user to enter the
# teacher’s name, the number of periods taught in a month,
# and the rate per period. The monthly salary is calculated by
# multiplying the number of periods by the monthly rate.
# The current monthly rate per period is $20. If a teacher has
# more than 100 periods in a month, everything above 100 is
# overtime. Overtime is $25 per period. For example, if a teacher
# has taught 105 periods, their monthly gross salary should be
# 2,125. Write a function called your_salary that calculates a
# teacher’s gross salary. The function should return the
# teacher’s name, periods taught, and gross salary. Here is
# how you should format your output:
# Teacher: John Kelly,
# Periods: 105
# Gross salary:2,125

def your_salary():
    name = input("please enter your name: ")
    the_number_of_periods = int(input("please enter the number of periods that you worked in a month: "))
    #the_rate_per_period = int(input("please enter the rate per period: "))
    #gross_salary = 0
    if the_number_of_periods > 100:
        gross_salary = ((the_number_of_periods -100) * 25) + 2000
    else:
        gross_salary = the_number_of_periods * 20

    print(f"The teacher {name} earned {gross_salary}$ this month")
    gross_salary_x = gross_salary // 1000
    gross_salary_y = gross_salary % 1000
    gross_salary = str(gross_salary_x) + "," + str(gross_salary_y)
    print("")
    print(f"Teacher: {name},\nPeriods: {the_number_of_periods}\nGross salary: {gross_salary}$")

your_salary()
