from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, check_marks, timer
    reps = 0
    check_marks = ""
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    if timer is not None:
        window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        start_counter(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        start_counter(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        start_counter(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_counter(counter):
    global check_marks, timer
    counter_minutes = counter // 60
    counter_seconds = counter % 60

    if counter_seconds < 10:
        counter_seconds = f"0{counter_seconds}"
    if counter_minutes < 10:
        counter_minutes = f"0{counter_minutes}"

    canvas.itemconfig(timer_text, text=f"{counter_minutes}:{counter_seconds}")
    if counter > 0:
        timer = window.after(1000, start_counter, counter - 1)
    else:
        if reps % 2 == 0:
            check_marks += "✓"
            check_mark_label.config(text=check_marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1, pady=15)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark_label.grid(row=3, column=1)

window.mainloop()
