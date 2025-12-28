import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25/squirrel game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_clicke_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_clicke_coor)
# turtle.mainloop()

states = pandas.read_csv("Day_25/squirrel game/50_states.csv")
all_states = states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's the another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if  state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data .to_csv("Day_25/squirrel game/states_to_learn.csv")
        break

    # can't use the in keyword unless convert it into the list.
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_state = states[states.state == answer_state]
        t.goto(correct_state.x.item(), correct_state.y.item())
        # t.write(answer_state)
        t.write(correct_state.state.item())


# states to learn.csv