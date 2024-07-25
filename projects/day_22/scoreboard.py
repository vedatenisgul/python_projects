from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
COLOR = "white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def update(self, l_or_r):
        if l_or_r == "right":
            self.r_score += 1
        else:
            self.l_score += 1
        self.show_score()
