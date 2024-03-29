from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y = self.ycor() + 20
        x = self.xcor()
        self.penup()
        self.goto(x=x, y=y)

    def down(self):
        y = self.ycor() - 20
        x = self.xcor()
        self.penup()
        self.goto(x=x, y=y)
