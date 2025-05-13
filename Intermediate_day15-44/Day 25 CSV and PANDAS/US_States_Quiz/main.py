import turtle
import pandas

background = "Intermediate_day15-44/Day 25 CSV and PANDAS/US_States_Quiz/blank_states_img.gif"
csv = r"Intermediate_day15-44\Day 25 CSV and PANDAS\US_States_Quiz\50_states.csv"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(background)


turtle.shape(background)

# def get_mouse_click_color(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_color)
# turtle.mainloop()
data = pandas.read_csv(csv)
list_of_states = data.state.to_list()
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                              prompt="What's another state's name?").title()
    if answer in list_of_states:
        guessed_states.append(answer)
        turtle = turtle.Turtle()
        turtle.penup()
        turtle.hideturtle()
        state_data = data[data.state == answer]
        turtle.goto(state_data.x.item(), state_data.y.item())
        turtle.write(answer)
    if answer == "Exit":
        states_to_learn = [state for state in list_of_states if state not in guessed_states]
        for state in list_of_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    
    