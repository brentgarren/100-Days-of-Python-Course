from turtle import Turtle
MOVE_SPEED = 10


class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def bounce(self):
        self.y_move *= -1
        self.ball_speed *= 0.9
        
    def redirect(self):
        self.x_move *= -1
        
    def ball_out_of_bounds(self):
        self.goto(0,0)
        self.x_move *= -1
        self.ball_speed = 0.1
        return False
    
        