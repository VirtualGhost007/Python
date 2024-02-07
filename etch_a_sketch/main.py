from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()
tim.speed("fastest")


def clear():
    screen.reset()


def forward():
    tim.fd(10)


def backward():
    tim.bk(10)


def clock():
    tim.right(10)


def counter():
    tim.lt(10)


screen.onkeypress(counter, "a")
screen.onkeypress(clock, "d")
screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(clear, "c")
screen.exitonclick()
