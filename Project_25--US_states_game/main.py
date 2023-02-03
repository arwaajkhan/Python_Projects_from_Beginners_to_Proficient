import pandas as pd
import turtle

# turtle and screen related codes
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# csv related codes
df = pd.read_csv("50_states.csv")
states_list = df["state"].tolist()

# other codes
# score = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                     prompt="What's another state's name?")).title()

    if answer_state == "Exit":

        remaining_states = [s for s in states_list if s not in guessed_states]
        # for s in states_list:
        #     if s not in guessed_states:
        #         remaining_states.append(s)
        new_data = pd.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        value = df[df.state == answer_state]
        t.goto(int(value["x"]), int(value["y"]))
        t.write(answer_state)
