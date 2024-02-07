from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to Turtle-Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nEnter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle()
rocky = Turtle()
tom = Turtle()
dom = Turtle()
sam = Turtle()
dam = Turtle()
turtles = [tim, rocky, tom, dom, sam, dam]
for i in range(6):
    turtles[i].color(colors[i])


def start_line(turtle, x, y):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x, y)


y = -100
for i in range(6):
    start_line(turtles[i], -230, y)
    y += 25

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for i in range(6):
        if turtles[i].xcor() > 230:
            is_race_on = False
            winner = turtles[i].pencolor()
            screen.clear()
            if winner == user_bet:
                Turtle().write("WINNER", True, "center", font=("Arial", 100, "normal"))
            else:
                Turtle().write("LOSER", True, "center", font=("Arial", 100, "normal"))
        distance = random.randint(0, 10)
        turtles[i].forward(distance)


screen.exitonclick()
