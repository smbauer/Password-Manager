from tkinter import *
from tkinter import messagebox
from pwd_generator import generate_password
import pyperclip


def get_password():
    '''Generate a random password and input to the password entry box'''
    pwd_entry.delete(0, END)
    pwd = generate_password()
    pwd_entry.insert(0, pwd)
    pyperclip.copy(pwd)


def add_entry():
    '''Validate entries and add record to data.txt if confirmed'''
    website = website_entry.get()
    email = user_entry.get()
    password = pwd_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        if len(website) == 0:
            messagebox.showwarning(title="Warning", message="Please enter a website")
        if len(email) == 0:
            messagebox.showwarning(title="Warning", message="Please enter an email address or username")
        if len(password) == 0:
            messagebox.showwarning(title="Warning", message="Please enter a password")
    else:
        is_confirmed = messagebox.askokcancel(title=website, message=f'Accept password for {website}?')

        if is_confirmed:
            with open("data.txt", 'a') as f:
                f.write(f'{website} | {email} | {password}\n')
            
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            pwd_entry.delete(0, END)


# UI setup
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
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

user_entry = Entry()
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

pwd_entry = Entry()
pwd_entry.grid(column=1, row=3, sticky="EW")

# create buttons
generate_button = Button(text="Generate Password", command=get_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=add_entry)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
