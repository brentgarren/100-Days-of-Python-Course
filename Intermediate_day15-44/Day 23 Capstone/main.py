import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Configures Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Keybinds
screen.onkeypress(key="w", fun=player.move_forward)

#Game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    
    #detect collision between player and car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
           game_is_on = False
           scoreboard.game_over() 
           
    #detect turtle has crossed road
    if player.is_at_finsh():
        player.go_to_start()
        car_manager.increase_level()
        scoreboard.increase_level()
        




screen.exitonclick()