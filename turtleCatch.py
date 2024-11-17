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
    score_keeper.sety(320)
    score_keeper.write(f"Score: {score}", align='center', font=SMALL_FONT)

seconds = int(screen.numinput("Timer", "Enter the seconds", minval=0, maxval=59))
def turtle_disapper():
    turtle_instance.penup()
    while seconds > 0:
        distance = random.randint(50, 100)
        if (-300 < turtle.xcor() < 300) and (-300 < turtle.ycor() < 300):
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



def target_clicked(x, y):
    turtle_instance.penup()
    if seconds > 0:
        update_score()
        turtle_disapper()


def action():
    global seconds

    seconds -= 1

    if seconds <= 0:
        time_keeper.clear()
        time_keeper.sety(270)
        time_keeper.write("Time Over", align='center', font=MEDIUM_FONT)
    else:
        update_time()
        screen.ontimer(action, 1000)  # 1 second = 1,000 milliseconds
        time_keeper.sety(370)
        time_keeper.write(f"Time Left: {seconds}", align='center', font=SMALL_FONT)


def update_time():
    time_keeper.undo()


time_keeper = score_keeper.clone()

turtle_instance.onclick(target_clicked)
action()

turtle.done()