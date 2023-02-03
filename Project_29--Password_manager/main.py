from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


# import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:

        try:
            with open("data.json", mode="r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating the old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    user_text = website_entry.get()

    try:
        with open("data.json") as data_file:
            values = json.load(data_file)

            # Checking if the user_text is in value dict or not, "try + except"
            try:
                result = values[user_text]

            except KeyError:
                messagebox.showinfo(title="Error", message="No details for the website exists.")

            else:
                email = result["email"]
                password = result["password"]
                messagebox.showinfo(title=f"{user_text}", message=f"Email: {email} \nPassword:{password}")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# 1st Line
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, sticky=E, padx=5)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, sticky=W, padx=2)

# 2nd Line
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=5)

email_entry = Entry(width=50)
email_entry.insert(0, "khan786@gmail.com")
email_entry.grid(row=2, column=1, sticky=E, columnspan=2, padx=2)

# 3rd Line
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, padx=5, sticky=E)

password_button = Button(text="Generate Password", width=15, command=password_generator)
password_button.grid(row=3, column=2)

# 4th Line
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=E, pady=5)

window.mainloop()
