from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(n=0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

sleep = 0.1

game_is_on = True
while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball.move()

    # bouncing the ball from the wall
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce_y()

    # ball misses r_paddle
    if ball.xcor() == 380:
        scoreboard.l_win()
        ball.reset_pos()

    # ball misses l_paddle
    if ball.xcor() == -380:
        scoreboard.r_win()
        ball.reset_pos()

    # ball bounce with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        sleep -= 0.001
        ball.bounce_x()

screen.exitonclick()

