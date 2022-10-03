from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=40, padx=40)
window.title("Password Manager")


website_text = Label(text="Website")
website_text.grid(row=1, column=0)
input_website = Entry(width=37)
input_website.grid(row=1, column=1, columnspan=2)

user_name_text = Label(text="Email/Username")
user_name_text.grid(row=2, column=0)
input_user_name = Entry(width=37)
input_user_name.grid(row=2, column=1, columnspan=2)

password_text = Label(text="Password")
password_text.grid(row=3, column=0)
input_password = Entry(width=18)
input_password.grid(row=3, column=1)

second_password_text = Button(text="Generate Password")
second_password_text.grid(row=3, column=2)

add_button = Button(text="Add", width=37)
add_button.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)




window.mainloop()
