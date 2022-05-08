from turtle import Turtle, Screen
import time
from Snake import *
from food import *
from Scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game.")

screen.tracer(0)

snake = Snake()
food = food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
score = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on == False
            scoreboard.game_over()

screen.exitonclick()
