import turtle
from random import random
import random
import time
from turtle import Screen, Turtle
from random import randint

SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 30, 'normal')
LARGE_FONT = ('Arial', 50, 'normal')

screen = Screen()
screen.bgcolor("green")
screen.title("Python Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle_instance.shape("turtle")



score = 0
score_keeper = Turtle()
score_keeper.hideturtle()
score_keeper.penup()
def update_score():
    global score

    score += 1
    score_keeper.clear()
    score_keeper.write(score, align='center', font=SMALL_FONT)


#drawing_board.listen()
#drawing_board.onclick()
def turtle_disapper():
    count = 0
    while count <51:
        count += 1
        distance = random.randint(50, 100)
        if (-300 < turtle.xcor() <300) and (-300 < turtle.ycor() <300):
            turtle_instance.penup()
            turtle_instance.right(random.randint(0,360))
            turtle_instance.hideturtle()
            turtle_instance.forward(distance)

            time.sleep(1)
            turtle_instance.showturtle()
        else:
            turtle_instance.home()
            turtle_instance.right(180)
            turtle_instance.forward(distance)



seconds = int(screen.numinput("Timer", "Enter the seconds", minval=0, maxval=59))

def update_time():
    time_keeper.undo()
    time_keeper.write(seconds, align='center', font=LARGE_FONT)
def target_clicked(x, y):
    if seconds > 0:
        update_score()
        turtle_disapper()

def action():
    global seconds

    seconds -= 1

    if seconds <= 0:
        turtle_instance.hideturtle()

        time_keeper.clear()
        time_keeper.sety(320)
        time_keeper.write("Time Over", align='center', font=MEDIUM_FONT)
    else:
        update_time()
        screen.ontimer(action, 1000)  # 1 second = 1,000 milliseconds

time_keeper = score_keeper.clone()

time_keeper.sety(370)
time_keeper.write("Time Left:", align='center', font=SMALL_FONT)
time_keeper.sety(300)
time_keeper.write(seconds, align='center', font=LARGE_FONT)

turtle_instance.onclick(target_clicked)

action()

turtle.done()