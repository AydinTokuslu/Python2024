# öğrenci notlarının girildiği ve kaydedildiği bir program

import csv
import os

def students_marks():
    name_surname = input("please enter your name and surname : ")
    visa_note = int(input("please enter your visa note : "))
    final_note = int(input("please enter your final note : "))

    avr_note = (visa_note * 0.4) + (final_note * 0.6)
    avr_note = round(avr_note,2)
    print("total average note : ", avr_note)

    if avr_note >= 90:
        letter_grade = "AA"
    elif avr_note >= 85:
        letter_grade = "BA"
    elif avr_note >= 80:
        letter_grade = "BB"
    elif avr_note >= 75:
        letter_grade = "CB"
    elif avr_note >= 70:
        letter_grade = "CC"
    elif avr_note >= 65:
        letter_grade = "DC"
    elif avr_note >= 60:
        letter_grade = "DD"
    else:
        letter_grade = "FF"

    filename = "grades.txt"

    # Check if the file exists
    if not os.path.exists(filename):
        # Write the header only once
        with open(filename, "w") as file:
            file.write(f"{'name_surname':<15}{'avr_note':<10}{'letter_grade':<10}\n")

    # Append new data
    with open(filename, "a") as file:
        file.write(f"{name_surname:<15}{avr_note:<10}{letter_grade:<10}\n")
        file.close()

    with open("grades.txt", mode='r', encoding="utf-8") as file:
        print(file.read())
        file.close()


num_of_students = int(input("how many students information will you enter (to exit hit '0') : "))
for i in range(num_of_students):
     students_marks()
