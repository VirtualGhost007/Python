from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detection with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.new_score()
        snake.extend()
    # Detection with wall
    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or
            snake.segments[0].ycor() < -280):
        is_game_on = False
        scoreboard.game_over()
    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()





















screen.exitonclick()
