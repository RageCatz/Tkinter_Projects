# task21_countdown.py
# Create a countdown timer
# Author: Huan Qi Low     Date: 16/05/2026

import tkinter as tk

def countdown():
    final_number = ""

    for i in range(10, 0, -1):
        final_number += str(i) + "\n"

    final_number += "Blast off!"
    output_label.config(text=final_number)

window = tk.Tk()
window.title("Countdown Timer")
window.geometry("360x250")

tk.Button(window, text="Countdown", command=countdown).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()