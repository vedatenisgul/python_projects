from turtle import Turtle

COORDINATE_X = 0
COORDINATE_Y = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        global COORDINATE_X
        for _ in range(3):
            self.add_part()
            COORDINATE_X -= 20

    def add_part(self, position=(COORDINATE_X, COORDINATE_Y)):
        part = Turtle(shape="square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.parts.append(part)

    def extend(self):
        self.add_part(self.parts[-1].pos())

    def move(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            new_x, new_y = self.parts[part_num - 1].pos()
            self.parts[part_num].goto(new_x, new_y)
        self.parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
