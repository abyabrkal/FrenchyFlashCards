# ***********************************************
# FRENCH FLASH CARDS - Capstone Project - D#31
#
# ***********************************************
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('french_words.csv')
to_learn = data.to_dict(orient="records")

current_card = {}


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=bcard_img)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=fcard_img)
    flip_timer = window.after(3000, func=flip_card)


window = Tk()
window.title("FrenchyFlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# --------  ROW 0 ---------
canvas = Canvas(width=800, height=526)
fcard_img = PhotoImage(file="images/card_front.png")
bcard_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=fcard_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 160, text="", font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))

# --------  ROW 1 ---------
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.config(highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=next_card)
right_button.config(highlightthickness=0)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
