from turtle import Turtle, Screen
import random


def create_turtle(color: str, position: tuple) -> Turtle:
    """Create a turtle with a specified color and starting position."""
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    return turtle


def setup_turtles(colors: list[str]) -> list[Turtle]:
    """Set up turtles at the starting positions."""
    turtles = []
    start_y = -150
    for color in colors:
        turtle = create_turtle(color, (START_X, start_y))
        turtles.append(turtle)
        start_y += 60
    return turtles


def start_race(turtles: list[Turtle]) -> str:
    """Start the race and return the winning turtle's color."""
    while True:
        for turtle in turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() >= FINISH_LINE_X:
                return turtle.pencolor()


# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
START_X = -200
FINISH_LINE_X = 230
TURTLE_COLORS = ["red", "blue", "yellow", "green", "black", "pink"]

# Set up screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Get user bet
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    # Set up turtles
    turtles = setup_turtles(TURTLE_COLORS)

    # Start race
    winner_color = start_race(turtles)

    # Print result
    if winner_color == user_bet:
        print(f"Congratulations! The {winner_color} turtle won!")
    else:
        print(f"Sorry, the {winner_color} turtle won. Better luck next time!")

# Exit on click
screen.exitonclick()
