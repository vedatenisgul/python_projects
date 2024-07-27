from turtle import Turtle
FONT = ("Courier", 24, "normal")
COLOR = "black"
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Level : {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
