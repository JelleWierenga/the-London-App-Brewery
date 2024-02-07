import colorgram
import turtle
import random
rgb_colors = [(235, 234, 232), (235, 232, 234), (185, 147, 93), (151, 104, 46), (229, 229, 231), (178, 150, 22), (83, 34, 27), (11, 57, 73), (31, 100, 121), (101, 41, 47), (56, 137, 122), (108, 39, 29), (22, 65, 50), (39, 81, 7), (200, 91, 64), (95, 62, 68), (110, 7, 9), (227, 233, 229), (116, 167, 78), (131, 178, 92), (139, 167, 177), (218, 203, 137), (181, 147, 151), (177, 206, 176), (44, 81, 4), (226, 177, 167), (162, 107, 111), (24, 77, 95), (215, 177, 180), (91, 143, 151)]
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     if (r, g, b) not in rgb_colors:
#         rgb_colors.append((r, g, b))
#
# print(rgb_colors)

timmy = turtle.Turtle()
timmy.speed(10)
turtle.colormode(255)
timmy.penup()
x = -300
y = -200
timmy.goto(-300, -200)
timmy.pendown()
for j in range(10):
    for i in range(10):
        timmy.dot(20, rgb_colors[random.randint(0, len(rgb_colors)-1)])
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    y += 50
    timmy.penup()
    timmy.goto(x, y)
    timmy.pendown()
# for i in range(10, 20):
#     timmy.dot(20, rgb_colors[i])
#     timmy.penup()
#     timmy.forward(50)
#     timmy.pendown()



screen = turtle.Screen()
screen.screensize(500, 500)
screen.exitonclick()
