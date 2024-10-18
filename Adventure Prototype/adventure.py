from levels import stages
from functions import *

def start(level, prompt):
    print(stages[level][prompt])
    input()

#Gameloop
while True:
    start("start_room", "prompt")
    
    
    
