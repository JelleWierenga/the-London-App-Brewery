import turtle
import random

timmy = turtle.Turtle()
timmy.pensize(10)
turtle.colormode(255)

sides = [0, 90, 180, 270]

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    timmy.color(color)
    timmy.forward(30)
    timmy.setheading(random.choice(sides))

screen = turtle.Screen()
screen.exitonclick()

