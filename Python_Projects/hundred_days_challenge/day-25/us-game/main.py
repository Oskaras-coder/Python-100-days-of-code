import turtle
import pandas as pd
from text_appear import TextAppear

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states_data = pd.read_csv("50_states.csv")

guessing_happening = True
correct_guess = 0


while guessing_happening:
    screen.update()
    answer_state = screen.textinput(title=f"{correct_guess}/50 States correct", prompt="What's another state's name?")

    if answer_state.capitalize() == states_data[states_data['state'] == answer_state.capitalize()]:
        x_coordinate = states_data.loc[states_data['state'] == answer_state.capitalize(), 'x'].iloc[0]
        y_coordinate = states_data.loc[states_data['state'] == answer_state.capitalize(), 'y'].iloc[0]
        state = TextAppear(answer_state.capitalize(), x_coordinate, y_coordinate)



screen.exitonclick()