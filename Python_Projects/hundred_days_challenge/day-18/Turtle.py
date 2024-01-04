from turtle import Turtle, Screen
import random
import colorgram
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

tim = Turtle()


screen = Screen()

# angle = [0, 90, 180, 270, 360]
# new_turtle.shape("circle")
# new_turtle.pensize(10)
# new_turtle.speed(7)
# while True:
#     new_turtle.setheading(random.choice(angle))
#     new_turtle.forward(25)
#     change_color()
for _ in range(50):
    tim.speed(0)
    tim.circle(100, 360)
    change_color()
    tim.speed(3)
    tim.left(360/50)

screen.exitonclick()