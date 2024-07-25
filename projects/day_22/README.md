# Pong Game

This is a simple Pong game implemented in Python using the Turtle graphics library. The game features two paddles controlled by players, a ball that bounces around the screen, and a scoreboard to keep track of the scores.

## Files

- `main.py`: The main script that sets up the game screen, initializes the paddles, ball, and scoreboard, and contains the game loop.
- `ball.py`: Contains the `Ball` class that handles the ball's movement and collision logic.
- `paddle.py`: Contains the `Paddle` class that handles the paddles' movement.
- `scoreboard.py`: Contains the `ScoreBoard` class that displays and updates the game score.

## Controls

- Right paddle (Player 1):
  - Move up: `Up` arrow key
  - Move down: `Down` arrow key
- Left paddle (Player 2):
  - Move up: `W` key
  - Move down: `S` key 

## Game Logic

- The ball bounces off the top and bottom edges of the screen.
- The ball bounces off the paddles.
- A point is scored when the ball passes a paddle and goes off the screen. The scoreboard is updated, and the ball resets to the center.
