from turtle import Turtle
import random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.go_random_location()

    def go_random_location(self):
        random_x, random_y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(random_x, random_y)
