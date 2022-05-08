from turtle import Turtle, Screen
import time
from Paddle import *
from Scoreboard import *
from Ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detection the collision with the wall

    if ball.ycor()>280 or ball.ycor()<-280:
        #need to bounce
        ball.bounce_y()

    #detect collition with paddle
    if ((ball.distance(r_paddle) < 50 and ball.xcor() >320) or (ball.distance(l_paddle) < 50 and ball.xcor()<-320)):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        # ball.speed(scoreboard.l_score)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        # ball.speed(scoreboard.l_score)



screen.exitonclick()
