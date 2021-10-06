import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data[data["state"] == "Alabama"])

# coordinates for the 50 states csv file
# def get_mouse_click_coor(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # THIS IS WHAT WAS CHANGED
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        # missing_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states to learn (missing states from guessed)

screen.exitonclick()
