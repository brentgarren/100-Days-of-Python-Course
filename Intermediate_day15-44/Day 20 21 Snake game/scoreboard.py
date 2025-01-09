from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,-270)
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 24, "normal"))
        
    def increase_Score(self):
        self.score += 1