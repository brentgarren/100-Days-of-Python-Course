from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        self.forward(10)
        
    def is_at_finsh(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
        

