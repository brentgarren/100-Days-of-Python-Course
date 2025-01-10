from turtle import Turtle

FONT_ALIGN = "center"
FONT = "Ariel"
FONT_SIZE = 24
FONT_TYPE = "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,265)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(0,265)
        self.write(f"Score: {self.score}", align=FONT_ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.goto(350,350)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align=FONT_ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))