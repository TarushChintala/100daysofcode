import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states_list = pd.read_csv("50_states.csv")


states_guessed = 0
correct_guesses = []
states_to_learn = []
all_states = states_list.state.to_list()


while len(correct_guesses) < 50:
    answer_state = (screen.textinput(title=f"{states_guessed}/50 states guessed",prompt="Enter the name of a state:")
                    .title())

    if answer_state == "Exit":
        for states in states_list.state:
            if states not in correct_guesses:
                states_to_learn.append(states)
                new_csv = pd.DataFrame(states_to_learn)
                new_csv.to_csv("states_to_learn")
        break

    # print(answer_state)

    if answer_state in all_states:
        states_guessed += 1
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.up()
        t.ht()
        state_entry = states_list[states_list.state == answer_state]
        t.goto(state_entry.x.item(), state_entry.y.item())
        t.write(align="center", arg=f"{answer_state}")




