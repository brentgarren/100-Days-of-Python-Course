from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Left_Scoreboard, Right_Scoreboard

#Adjust Screen
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Pong Game"
game_running = True
left_score = 0
right_score = 0

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
left_scoreboard = Left_Scoreboard()
right_scoreboard = Right_Scoreboard()


#Sets keybinds
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


while game_running == True:
    
    time.sleep(ball.ball_speed)
    screen.update()
    screen.listen()
    ball.move()
    
    
    #Make ball bound off boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        
    #Detect collision with right paddel
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.redirect()
    
    #Detect collision with left paddel
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.redirect()
    #detect if ball goes off screen
    if ball.xcor() > 340 or ball.xcor() < -340:
        #increase right score
            if ball.xcor() > 1:
                right_scoreboard.increase_score()
                right_scoreboard.update_scoreboard()
        #increase left score
            elif ball.xcor() < -1:
                left_scoreboard.increase_score()
                left_scoreboard.update_scoreboard()
            ball.ball_out_of_bounds()
        
    














screen.exitonclick()