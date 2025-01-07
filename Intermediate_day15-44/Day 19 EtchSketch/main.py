from turtle import Turtle, Screen

class Move:
    
    def __init__(self):
        self.heading = 0
          
    
    def move_forward(self):
        etch.forward(10)

    def move_counterclockwise(self):
        self.heading -= 10
        etch.setheading(self.heading) 

    def move_clockwise(self):
        self.heading += 10
        etch.setheading(self.heading)

    def move_backwards(self):
        etch.backward(10)

    def clear(self):
        etch.goto(0,0)
        self.heading = 0
        etch.clear()
    
    
        
    
    
etch = Turtle()
# etch.hideturtle()
screen = Screen()
mover = Move()
screen.title("Etch n Sketch")
etch.speed("fastest")

screen.listen()
screen.onkeypress(key="w", fun=mover.move_forward)
screen.onkeypress(key="a", fun=mover.move_counterclockwise)
screen.onkeypress(key="s", fun=mover.move_backwards)
screen.onkeypress(key="d", fun=mover.move_clockwise)
screen.onkeypress(key="c", fun=mover.clear)


screen.exitonclick()