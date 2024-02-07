from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, "center", ("courier", 24, "normal"))

    def new_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", True, "center", ("courier", 50, "normal"))


