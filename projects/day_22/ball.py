from turtle import Turtle
COLOR = "white"
SHAPE = "circle"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.x_direction_value = 10
        self.y_direction_value = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direction_value
        new_y = self.ycor() + self.y_direction_value
        self.goto(new_x, new_y)

    def turn_back(self):
        self.bounce_y()
        self.bounce_x()

    def bounce_y(self):
        self.y_direction_value *= -1

    def bounce_x(self):
        self.x_direction_value *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
