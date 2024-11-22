def average_calories():
    calories = []
    while True:
        calori = input("please enter the calorie, or enter 'done' to exit : ")
        if calori == "done":
            break
        else:
            calories.append(int(calori))
    return f"Average intake is {sum(calories)/len(calories)}"

print(average_calories())