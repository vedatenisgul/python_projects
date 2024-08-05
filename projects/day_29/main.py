from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pyperclip
import json
# ---------------------------- Search ------------------------------- #


def search():
    try:
        with open("data.json") as file:
            datas = json.load(file)
            website_name = entry_1.get()
            website_datas = datas[website_name]
            messagebox.showinfo(title=website_name, message=f"Email: {website_datas['email']}"
                                                            f"\nPassword: {website_datas['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No data file found!")
    except KeyError:
        messagebox.showinfo(title="Oops!", message="No details for the website exists!")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = create_password()
    pyperclip.copy(password)
    entry_3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_the_file():
    website = entry_1.get()
    email_or_user_name = entry_2.get()
    password = entry_3.get()
    new_data = {
        website: {
            "email": email_or_user_name,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_or_user_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            data_file = open("data.json")
            data_file.close()
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json") as file:
                data = json.load(file)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            reset_entries()


def reset_entries():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_2.insert(0, "user@gmail.com")
    entry_3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website:")
label_1.grid(row=1, column=0)

label_2 = Label(text="Email/Username:")
label_2.grid(row=2, column=0)

label_3 = Label(text="Password:")
label_3.grid(row=3, column=0)

entry_1 = Entry(width=21)
entry_1.grid(row=1, column=1, columnspan=2, sticky="EW")
entry_1.focus()


entry_2 = Entry(width=35)
entry_2.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_2.insert(0, "user@gmail.com")

entry_3 = Entry(width=21)
entry_3.grid(row=3, column=1, sticky="EW")

button_1 = Button(text="Generate Password", command=generate_password)
button_1.grid(row=3, column=2, sticky="EW")

button_2 = Button(text="Add", width=35, command=save_to_the_file)
button_2.grid(row=4, column=1, columnspan=2, sticky="EW")

button_3 = Button(text="Search", command=search)
button_3.grid(row=1, column=2, sticky="EW")


window.mainloop()
