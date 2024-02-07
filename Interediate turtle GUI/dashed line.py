import turtle

timmy = turtle.Turtle()
timmy.color("black")

for i in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = turtle.Screen()
screen.exitonclick()
