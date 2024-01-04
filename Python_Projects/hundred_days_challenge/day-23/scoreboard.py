from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_count = 0
        self.update_level()
    def update_level(self):
        self.level()
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level {self.level_count}", align="center", font=FONT)

    def level(self):
        self.level_count += 1

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER", align="center", font=FONT)