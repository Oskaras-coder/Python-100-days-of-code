from turtle import Turtle


class TextAppear(Turtle):
    def __init__(self, answer, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.hideturtle()
        self.write(f"{answer}", align="center", font=FONT)
        self.goto(x, y)