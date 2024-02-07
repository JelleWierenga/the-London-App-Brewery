import turtle
import random

timmy = turtle.Turtle()
timmy.color("black")


def triangle():
    sides = 3
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def square():
    sides = 4
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def pentagon():
    sides = 5
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def hexagon():
    sides = 6
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def heptagon():
    sides = 7
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def octagon():
    sides = 8
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def nonagon():
    sides = 9
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def decagon():
    sides = 10
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
screen = turtle.Screen()
screen.exitonclick()

