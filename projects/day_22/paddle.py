from turtle import Turtle
COLOR = "white"
SHAPE = "square"
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.setheading(UP)
        self.speed("fastest")

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)
