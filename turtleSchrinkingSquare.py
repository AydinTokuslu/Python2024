import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def schrinkingSquare(size):
    for i in range(5):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -5

schrinkingSquare(200)
schrinkingSquare(170)
schrinkingSquare(140)
schrinkingSquare(110)
schrinkingSquare(80)
schrinkingSquare(50)
schrinkingSquare(20)


turtle.done()