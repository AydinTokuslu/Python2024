import turtle
from random import random
import time
import pygame

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle_instance.shape("turtle")

"""""
directions = [0, 90, 180, 270]
for _ in range (300): # set it 300 times to draw
    turtle_instance.penup()
    turtle.forward(random.randint(30, 100))
    turtle_instance.forward(30)
    turtle_instance.setheading(random.choice(directions))


for i in range(100):
    turtle_instance.penup()
    turtle_instance.fd(100)
    turtle_instance.hideturtle()
    time.sleep(1)
    turtle_instance.showturtle()
"""""


turtle.done()