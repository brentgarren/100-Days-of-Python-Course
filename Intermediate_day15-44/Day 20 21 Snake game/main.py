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
    screen.onkeypress(snake.up, "w")
    screen.onkeypress(snake.down,"s")
    screen.onkeypress(snake.left,"a")
    screen.onkeypress(snake.right,"d")
    screen.update()
    time.sleep(0.1)
    if not snake.move():
        scoreboard.game_over()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_running = False
    
scoreboard.game_over()   





screen.exitonclick()