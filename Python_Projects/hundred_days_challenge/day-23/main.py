import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

car_speed = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_count = []
player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()


screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > FINISH_LINE_Y:
        player.refresh()
        scoreboard.update_level()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            screen.update()
            game_end = Scoreboard().game_over()
            game_is_on = False




screen.exitonclick()