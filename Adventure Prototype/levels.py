
stages = {}


stages["start"] = {
    "prompt": "Welcome to the game! You suck. Have fun. Try not to die.",
    "choices": "What do you do? \n 1. Quit 2. Die (AKA start the game)",
    "is_completed": False,
    
}

stages['level1'] = {
    "prompt": "You are in a room with a locked door, a gold chest to your left, a chest to your right.",
    "completed_prompt": "You are in a room with a locked door, a gold chest to your left, a chest to your right. The chest",
    "choices": "What do you do? \n 1. Open the gold chest. 2. Open the chest",
    "is_completed": False,

    
    
    }

stages['level2'] = {
    "prompt": "You are in a room with a locked door, a gold chest to your left, a chest to your right.",
    "choices": "What do you do? \n 1. Open the gold chest. 2. Open the chest",
}