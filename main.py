from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# set up screen
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# create logo
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# create text labels
website_label = Label(text="Website:").grid(column=0, row=1, sticky="E")
user_label = Label(text="Email/Username:").grid(column=0, row=2, sticky="E")
pwd_label = Label(text="Password:").grid(column=0, row=3, sticky="E")

# create text entry fields
website_entry = Entry().grid(column=1, row=1, columnspan=2, sticky="EW")
user_entry = Entry().grid(column=1, row=2, columnspan=2, sticky="EW")
pwd_entry = Entry().grid(column=1, row=3, sticky="EW")

# create buttons
generate_button = Button(text="Generate Password").grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=35).grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
