from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface(Tk):
    def __init__(self, quiz: QuizBrain):
        super().__init__()
        self.quiz = quiz

        self.title("Quiz App")
        self.configure(background=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Question", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, borderwidth=0,
                                   highlightbackground=THEME_COLOR, command=self.true_button_pushed)
        self.right_button.grid(row=2, column=0, pady=20, padx=20)

        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0,
                                   highlightbackground=THEME_COLOR, command=self.false_button_pushed)
        self.wrong_button.grid(row=2, column=1, pady=20, padx=20)

        self.score_label = Label(text=f"Score:{self.quiz.score}", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.next_question()
        self.mainloop()

    def true_button_pushed(self):
        self.update_screen(self.quiz.check_answer("true"))

    def false_button_pushed(self):
        self.update_screen(self.quiz.check_answer("false"))

    def update_screen(self, true_or_false):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
        if true_or_false:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")

        self.after(1000, self.next_question)

    def turn_white(self):
        self.canvas.configure(background="white")

    def next_question(self):
        self.turn_white()
        self.score_label.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_questions():
            self.right_button.config(state="active")
            self.wrong_button.config(state="active")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")

