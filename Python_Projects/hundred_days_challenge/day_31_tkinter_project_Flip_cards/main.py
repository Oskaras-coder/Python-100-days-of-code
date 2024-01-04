from tkinter import *  # only import classes
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- csv DATA IMPORT ------------------------------- #
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    
to_learn = data.to_dict(orient="records")
current_card = {}


def save_new_words():
    global to_learn

    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    generate_word()


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # resets timer after press
    current_card = random.choice(to_learn)
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_text, text=current_card["French"], fill="black")
    card.itemconfig(card_background, image=card_f_img)
    flip_timer = window.after(3000, func=flip_card)  # starts timer immediately
    print(current_card)


# ---------------------------- Timer flip ------------------------------- #

def flip_card():
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_text, text=current_card["English"], fill="white")
    card.itemconfig(card_background, image=card_e_img)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_f_img = PhotoImage(file="./images/card_front.png")
card_e_img = PhotoImage(file="./images/card_back.png")
card_background = card.create_image(400, 263, image=card_f_img)
card_title = card.create_text(400, 150, fill="black", font=("Ariel", 40, "italic"))
card_text = card.create_text(400, 253, fill="black", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = PhotoImage(file="./images/right.png")
right = Button(image=right_button, highlightthickness=0, command=save_new_words)
right.grid(column=1, row=1)

wrong_button = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_button, highlightthickness=0, command=generate_word)
wrong.grid(column=0, row=1)

generate_word()

window.mainloop()
