import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

for i in range(10):
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)




turtle.done()