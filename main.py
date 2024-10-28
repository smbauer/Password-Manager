from tkinter import *
from tkinter import messagebox
from pwd_generator import generate_password
import pyperclip
import json


def get_password():
    '''Generate a random password and input to the password entry box'''
    pwd_entry.delete(0, END)
    pwd = generate_password()
    pwd_entry.insert(0, pwd)
    pyperclip.copy(pwd)


def add_entry():
    '''Validate entries and add record to data.json if confirmed'''
    website = website_entry.get()
    email = user_entry.get()
    password = pwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # validate that none of the entry fields are empty
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
            try:
                # read data if file exists
                with open("data.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                # otherwise create new file and add data
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as f:
                    # write the updated data
                    json.dump(data, f, indent=4)
            finally:
                # clear the entry forms for the next entry
                website_entry.delete(0, END)
                user_entry.delete(0, END)
                pwd_entry.delete(0, END)


def find_entry():
    '''
    Search data.json to see if record exists for website being searched.
    If it exists, return the email and password being used for that website.
    '''
    website = website_entry.get()

    try:
        # read the file if it exists
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="There are no entries yet. Please add record.")
    else:
        if website in data:
            # display the email and password associated with the website
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            # copy the password to the clipboard and clear the entry form
            pyperclip.copy(password)
            website_entry.delete(0, END)
        else:
            # website not found
            messagebox.showwarning(title="Warning", message="There are no entries for this website")


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
website_entry.grid(column=1, row=1, sticky="EW")
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

search_button = Button(text="Search", command=find_entry)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
