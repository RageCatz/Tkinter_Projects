# task17_mood.py
# Displays a random, colour-coded mood emoji whenever the user clicks a button
# Author: Huan Qi Low     Date: 15/05/2026

import random
import tkinter as tk

def roll_mood():
    mood_number = random.randint(1, 3)

    if mood_number == 1:
        result.config(text="😊 Happy", fg="orange")
    elif mood_number == 2:
        result.config(text="— Neutral", fg="grey")
    elif mood_number == 3:
        result.config(text="😞 Sad", fg="blue")

window = tk.Tk()
window.title("Mood Randomizer")
window.geometry("360x150")

tk.Button(window, text="Roll my mood", command=roll_mood).pack(pady=5)
result = tk.Label(window, text="")
result.pack()

window.mainloop()