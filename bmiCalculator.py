

bmi = 0
def bmiCalculation():
    global bmi
    while True:
        try:
            weight = float(input("please enter your weight in kg : "))
            height = float(input("please enter your height in cm : ")) / 100
            bmi = (weight / (height * height))
        except:
            print("please enter valid numbers, not string!!!")
            continue
    #return bmi
        return (round(bmi, 2))
    #print(round(bmi, 2))

def bmiResult(bmi):
    result = f"Your BMI is {bmi}. You are "
    #result = f"Your BMI is {round(bmi, 2)}. You are {bmiCalculation} "
    if bmi <= 16:
        result += "severely underweight"
    elif 16 < bmi < 18.4:
        result += "underweight"
    elif 18.5 < bmi < 24.9:
        result += "normal"
    elif 25 < bmi < 29.9:
        result += "overweight"
    elif 30 < bmi < 34.9:
        result += "moderately obese"
    elif 35 < bmi < 39.9:
        result += "severely obese"
    else:
        result += "morbidly obese"
    return result



print(bmiResult(bmiCalculation()))