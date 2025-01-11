from turtle import Turtle

FONT_ALIGN = "center"
FONT = "Ariel"
FONT_SIZE = 48
FONT_TYPE = "normal"

class Left_Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-100,200)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(f"{self.score}", align="left", font=(FONT, FONT_SIZE, FONT_TYPE))
        self.goto(350,350)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
        
class Right_Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(100,265)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(100,200)
        self.write(f"{self.score}", align="right", font=(FONT, FONT_SIZE, FONT_TYPE))
        self.goto(350,350)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()