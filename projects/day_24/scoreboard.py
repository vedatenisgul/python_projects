from turtle import Turtle
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ALIGNMENT = "center"
FONT = ("arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

        with open("game_data.txt",mode="r") as file:
            content = file.read()
            self.high_score = int(content)

        self.penup()
        self.color("white")
        self.goto(0, SCREEN_HEIGHT/2-30)
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
            self.show_score()
        self.score = 0
        self.show_score()

    def update_high_score(self):
        with open("game_data.txt", mode="w") as file:
            file.write(str(self.high_score))

