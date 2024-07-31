from tkinter import *

MILES_TO_KILOS = 1.609
SCREEN_SIZE = "300x200"
FONT = ("Ariel", 20, "bold")


def button_clicked():
    miles = float(miles_input.get())
    kilos = miles * MILES_TO_KILOS
    kilos_output.config(text=str(kilos))


window = Tk()
window.title("Miles to Kilometer")
window.geometry(SCREEN_SIZE)
window.config(padx=20, pady=40)
window.resizable(False, False)


label_miles = Label(text="Miles", font=FONT)
label_miles.grid(row=0, column=2, sticky="w")

label_miles = Label(text="Kilometers", font=FONT)
label_miles.grid(row=1, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

kilos_output = Label(text="0")
kilos_output.grid(row=1, column=1)

normal_label = Label(text="is equal to")
normal_label.grid(row=1, column=0)
window.mainloop()
