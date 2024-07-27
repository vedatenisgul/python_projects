from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR = "black"
SPEED = "fastest"
SHAPE = "turtle"
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.speed(SPEED)
        self.shape(SHAPE)
        self.setheading(UP)
        self.goto(STARTING_POSITION)
        self.level = 1

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def is_level_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.level += 1
            self.goto(STARTING_POSITION)
            return True
        return False
