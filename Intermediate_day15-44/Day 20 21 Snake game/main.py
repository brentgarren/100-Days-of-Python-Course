from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Adjust Screen
WIDTH = 600
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Snake Game"

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_running = True
while game_running:
    
    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down,"Down")
    screen.onkeypress(snake.left,"Left")
    screen.onkeypress(snake.right,"Right")
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        print("nom")
        food.refresh()
        scoreboard.increase_Score()
    
    





screen.exitonclick()