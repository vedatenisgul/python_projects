from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.update()
continue_game = True
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while continue_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        scoreboard.increase_score()
        snake.extend()
        food.go_random_location()

    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
