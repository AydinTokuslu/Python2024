


def bmiCalculation():
    weight = int(input("please enter your weight in kg : "))
    height = int(input("please enter your height in cm : "))/100
    bmi = (weight / (height * height))
    print(bmi)
    if bmi < 16 :
        print("Your category is severely underweight")
    elif 16 < bmi < 18.4 :
        print("Your category is underweight")
    elif 18.5 < bmi < 24.9 :
        print("Your category is normal")
    elif 25 < bmi < 29.9 :
        print("Your category is overweight")
    elif 30 < bmi < 34.9 :
        print("Your category is moderately obese")
    elif 35 < bmi < 39.9 :
        print("Your category is severely obese")
    else :
        print("Your category is morbidly obese")


bmiCalculation()