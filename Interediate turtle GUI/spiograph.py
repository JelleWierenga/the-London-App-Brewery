import turtle
import random

timmy = turtle.Turtle()
timmy.color("black")
timmy.speed(10)
turtle.colormode(255)

for i in range(18):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    timmy.color(color)
    timmy.circle(100)
    timmy.left(20)
    for j in range(4):
        timmy.forward(50)
        timmy.left(90)


screen = turtle.Screen()
screen.exitonclick()
