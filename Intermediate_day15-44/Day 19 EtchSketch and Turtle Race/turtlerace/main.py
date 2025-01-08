from turtle import Turtle, Screen
import random

def draw_checkered_finish_line():
    square_size = 20
    y_start = -180
    x_position = 175
    line_drawer = Turtle()
    line_drawer.hideturtle()
    line_drawer.speed("fastest")
    for i in range(20):  # Adjust number of squares based on screen height
        line_drawer.penup()
        line_drawer.goto(x_position, y_start + (i * square_size))
        line_drawer.pendown()
        line_drawer.fillcolor("black" if i % 2 == 0 else "white")
        line_drawer.begin_fill()
        for _ in range(4):  # Draw square
            line_drawer.forward(square_size)
            line_drawer.right(90)
        line_drawer.end_fill()

screen = Screen()
screen.setup(height = 400,width = 500)
screen.title("Turtle Racer!")
screen.bgcolor("grey")
turtle_colors = ["red","orange","yellow","green","blue","indigo","violet"]
turtle_racers = []
game_on = True
race = True
y_pos= -150

line_drawer = Turtle()
line_drawer.speed("fastest")
line_drawer.hideturtle()
line_drawer.penup()
line_drawer.goto(-200, -200)
line_drawer.pendown()
line_drawer.goto(-200, 200)

line_drawer.penup()
line_drawer.goto(175, -200)
line_drawer.pendown()
line_drawer.goto(175, 200)
score = 0
games_played =0


draw_checkered_finish_line()

while game_on:
    
    if race == False:
        for racer in turtle_racers:
            racer.clear()
            racer.home()
            racer.hideturtle()
        turtle_racers = []
        y_pos= -150


    for color in turtle_colors:
        racer = Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.goto(-200, y_pos)
        y_pos += 50
        turtle_racers.append(racer)
        
    pick = screen.textinput(title="Choose your Winner!", prompt=f"Pick a turtle: {turtle_colors}")
    
    race = True
    while race:          
        for racer in turtle_racers:
            racer.forward(random.randint(1,5))
            if racer.xcor() >= 175:
                race = False
                winner = racer.color()[0]
                games_played += 1

    if winner == pick:
        score += 1
        pick = screen.textinput(title="Results!", prompt=f"The winner was {winner} \n You picked correctly, Wanna play again? Yes/No\n{score}/{games_played}")
        
    else:
        pick = screen.textinput(title="Results!", prompt=f"The winner was {winner} \n You picked {pick}, Wanna play again? Yes/No\n{score}/{games_played}")

    if pick == None: 
        game_on = False
    if pick.lower() == 'no':
        game_on == False


screen.bye()        
screen.exitonclick()