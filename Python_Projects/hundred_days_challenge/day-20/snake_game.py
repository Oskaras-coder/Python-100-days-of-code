from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game - BAZINGA")
screen.tracer(0)


all_squares = []
square_distance = 20

for squares in range(3):
    square = Turtle("square")
    square.color("white")
    square.penup()
    all_squares.append(square)
    square.goto(x=square_distance * -squares, y=0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in all_squares:
        seg.forward(20)


screen.exitonclick()