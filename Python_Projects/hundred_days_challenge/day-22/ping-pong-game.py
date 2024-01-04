from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Bing-Bong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "s")

speed = 0.01

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        speed *= 0.9



    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        speed = 0.01

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        speed = 0.01
screen.exitonclick()