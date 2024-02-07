import turtle

timmy = turtle.Turtle()
tom = turtle.Turtle()

timmy.shape("turtle")
timmy.color("red")

tom.shape("turtle")
tom.color("green")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)
    tom.forward(150)
    tom.left(90)

screen = turtle.Screen()
screen.exitonclick()
