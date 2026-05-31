# task16_guess.py
# Let the user play a guess the number game
# Author: Huan Qi Low     Date: 15/05/2026

import tkinter as tk

def guess_number():
    num = int(num_box.get())
    if num == 5:
        result.config(text="You guessed correctly!")
    elif num < 5:
        result.config(text="Too low.")
    elif num > 5:
        result.config(text="Too high.")

window = tk.Tk()
window.title("Guess my number")
window.geometry("360x150")

tk.Label(window, text="Guess a number: ").pack()
num_box = tk.Entry(window, text="")
num_box.pack()

tk.Button(window, text="Guess", command=guess_number).pack(pady=5)
result = tk.Label(window, text="")
result.pack()

window.mainloop()