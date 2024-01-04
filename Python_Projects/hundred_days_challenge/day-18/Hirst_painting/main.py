# import colorgram
from turtle import Turtle, Screen
import random
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
colour_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]


tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(canvwidth=100, canvheight=100,)
tim.hideturtle()
tim.setheading(225)
tim.forward(50*5)
tim.setheading(0)
home = 0
for y in range(10):
    for x in range(10):
        tim.pencolor(random.choice(colour_list))
        tim.dot(10)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    home += 1
    tim.penup()
    tim.home()
    tim.setheading(90)
    tim.forward(50 * home)
    tim.setheading(0)
    tim.pendown()

screen.exitonclick()