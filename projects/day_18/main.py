import colorgram
from turtle import Turtle, Screen
import turtle
import random

rgb_colors = []


def extract_colors_from_image():  # extract colors in rgb form from 'image.jpg'
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        final_color = (r, g, b)
        rgb_colors.append(final_color)


def create_random_colors():
    return random.choice(rgb_colors)


turtle.colormode(255)
extract_colors_from_image()

tim = Turtle()
tim.shape("turtle")
tim.speed("fast")
tim.penup()
tim.hideturtle()
tim.goto(-225, -225)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, create_random_colors())
        tim.forward(50)
    x, y = tim.position()
    tim.goto(x-500, y+50)
tim.home()

screen = Screen()
screen.exitonclick()
