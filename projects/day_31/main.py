from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
LANGUAGE_FONT = (FONT_NAME, 40, "italic")
WORD_FONT = (FONT_NAME, 60, "bold")


def learned():
    learned_pair = {"English": current_card_front, "Turkish": current_card_back}
    datas_to_learn.remove(learned_pair)

    df = pandas.DataFrame(datas_to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)

    next_word()


def next_word():
    global current_card_back, current_card_front, flip_timer
    window.after_cancel(flip_timer)
    random_pair = random.choice(datas_to_learn)

    current_card_front = random_pair['English']
    current_card_back = random_pair['Turkish']

    canvas.itemconfig(language_name_text, text="English", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(word_name_text, text=current_card_front, fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_name_text, text="Turkish",  fill="white")
    canvas.itemconfig(word_name_text, text=current_card_back, fill="white")


datas_to_learn = None

try:
    file = open("./data/words_to_learn.csv")
    file.close()

except FileNotFoundError:
    datas_to_learn = pandas.read_csv("./data/eng_to_tr.csv").to_dict(orient="records")
else:
    datas_to_learn = pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")

current_card_front = None
current_card_back = None

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

language_name_text = canvas.create_text(400, 150, text="title", font=LANGUAGE_FONT)
word_name_text = canvas.create_text(400, 263, text="word", font=WORD_FONT)


right_image = PhotoImage(file="./images/right.png")
button1 = Button(image=right_image, highlightthickness=0, borderwidth=0, highlightbackground=BACKGROUND_COLOR
                 , command=learned)
button1.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
button2 = Button(image=wrong_image, highlightthickness=0, borderwidth=0, highlightbackground=BACKGROUND_COLOR
                 , command=next_word)
button2.grid(row=1, column=0)

next_word()


window.mainloop()
