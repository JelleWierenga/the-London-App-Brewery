import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    timmy.forward(10)

def move_back():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)
def clear_field():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_field)

screen = turtle.Screen()
screen.exitonclick()
