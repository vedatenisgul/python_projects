from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WIDTH = 800
HEIGHT = 600
SCREEN_COLOR = "black"

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title("PONG GAME")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
continue_game = True

while continue_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320)):
        ball.turn_back()

    if ball.xcor() > 380:
        scoreboard.update("left")
        ball.reset_pos()
    elif ball.xcor() < -380:
        scoreboard.update("right")
        ball.reset_pos()


screen.exitonclick()
