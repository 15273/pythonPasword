from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_simbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_simbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_user_name.get()
    password = input_password.get()
    new_dict = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="No an option", message="please make sure you haven't left any fields empty.")
    else:
        with open("data.json", "w") as data_file:
            json.dump(new_dict, data_file)
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=40, padx=40)
window.title("Password Manager")

website_text = Label(text="Website")
website_text.grid(row=1, column=0)
input_website = Entry(width=37)
input_website.grid(row=1, column=1, columnspan=2)
website_text.focus()

user_name_text = Label(text="Email/Username")
user_name_text.grid(row=2, column=0)
input_user_name = Entry(width=37)
input_user_name.insert(0, "merp770g@gmail.com")
input_user_name.grid(row=2, column=1, columnspan=2)

password_text = Label(text="Password")
password_text.grid(row=3, column=0)
input_password = Entry(width=18)
input_password.grid(row=3, column=1)

second_password_text = Button(text="Generate Password", command=generate_password)
second_password_text.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

window.mainloop()
