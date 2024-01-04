from tkinter import *  # only import classes
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_1 = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list_2 = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list_3 = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_list_1 + password_list_2 + password_list_3

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Insufficient info", message="Website and/or password info is missing")

    # else:
    #     is_ok = messagebox.askokcancel(title=website,
    #                        message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok "
    #                                f"to save?")


    else:
        try:
            with open("email.json", "r") as emails:
                # Reading old data
                data = json.load(emails)  # converts data into dictionary, cool

        except FileNotFoundError:
            with open("email.json", "w") as emails:
                json.dump(new_data, emails, indent=4)

        else:
            # Uploading new data
            data.update(new_data)
            with open("email.json", "w") as emails:
                # Saving updated data
                json.dump(data, emails, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


def find_password():
    website = website_entry.get()
    try:
        with open("email.json", "r") as emails:
            read_info = json.load(emails)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data file found")

    else:
        if website in read_info:
            messagebox.showinfo(title=f"{website}", message=f"Email is {read_info[website]['email']}\nPassword is {read_info[website]['password']}")
        else:
            messagebox.showinfo(message="No details for the website exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons

generate_password = Button(text="Generate_password", command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=34, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)

# entries

website_entry = Entry(width=22)
website_entry.grid(sticky=W, column=1, row=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(sticky=W, column=1, row=2, columnspan=2)
email_entry.insert(0, "osafinas@mail.com")  # END , the last character

password_entry = Entry(width=22)
password_entry.grid(sticky=W, column=1, row=3)

window.mainloop()
