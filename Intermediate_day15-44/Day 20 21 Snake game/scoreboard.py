from turtle import Turtle
from save import highscore

FONT_ALIGN = "center"
FONT = "Ariel"
FONT_SIZE = 24
FONT_TYPE = "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = highscore
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,265)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0,265)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=FONT_ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.goto(350,350)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\Users\brent\OneDrive\Desktop\Python Coding Learning\100 days Challenge\100-Days-of-Python-Course\Intermediate_day15-44\Day 20 21 Snake game\save.py", mode="w") as file:
                file.write(f"highscore = {self.high_score}")
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!", align=FONT_ALIGN, font=(FONT, FONT_SIZE, FONT_TYPE))