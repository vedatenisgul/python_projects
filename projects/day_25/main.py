from turtle import Turtle, Screen
import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


def go_and_write(position, name_of_state):
    name_writer.goto(position)
    name_writer.write(arg=name_of_state, align=ALIGNMENT, font=FONT)
    guessed_states.append(name_of_state)


def update_number():
    global number_of_found_states
    number_of_found_states += 1


def create_missing_states_csv():
    new_states_list = [item for item in states_list if item not in guessed_states]
    missing_states = pandas.DataFrame(new_states_list)
    missing_states.to_csv("learn.csv")


NUMBER_OF_STATES = 50
number_of_found_states = 0
guessed_states = []

screen = Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

name_writer = Turtle()
name_writer.hideturtle()
name_writer.penup()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
x_cor_list = data.x.to_list()
y_cor_list = data.y.to_list()
continue_game = True

while continue_game:
    answer_state = screen.textinput(title=f"Guess the State {number_of_found_states}/{NUMBER_OF_STATES}"
                                    , prompt="What's another state's name?").title()

    if answer_state == "Exit":
        create_missing_states_csv()
        break

    if answer_state not in guessed_states:
        if answer_state in states_list:
            state_data = data[data.state == answer_state]
            x_cor = state_data.x.item()
            y_cor = state_data.y.item()
            pos = (x_cor, y_cor)
            go_and_write(pos, answer_state)
            update_number()

    if NUMBER_OF_STATES == number_of_found_states:
        break


screen.exitonclick()
