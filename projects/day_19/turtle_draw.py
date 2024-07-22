from turtle import Turtle, Screen

# Constants
MOVE_DISTANCE = 10
TURN_ANGLE = 10


def move_forwards() -> None:
    """Move the turtle forwards by MOVE_DISTANCE."""
    tim.forward(MOVE_DISTANCE)


def move_backwards() -> None:
    """Move the turtle backwards by MOVE_DISTANCE."""
    tim.backward(MOVE_DISTANCE)


def turn_counter_clockwise() -> None:
    """Turn the turtle counter-clockwise by TURN_ANGLE degrees."""
    tim.left(TURN_ANGLE)


def turn_clockwise() -> None:
    """Turn the turtle clockwise by TURN_ANGLE degrees."""
    tim.right(TURN_ANGLE)


def clear_screen() -> None:
    """Clear the screen and reset the turtle to the starting position."""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def setup_screen(screen: Screen) -> None:
    """Set up the screen with key bindings."""
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=turn_counter_clockwise)
    screen.onkey(key="d", fun=turn_clockwise)
    screen.onkey(key="c", fun=clear_screen)


# Main program
if __name__ == "__main__":
    tim = Turtle()
    screen = Screen()
    setup_screen(screen)
    screen.exitonclick()
