# task07_greeter.py
# Ask the user for their name and display it on a label
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def greet():
    name = name_box.get()
    output_label.config(text=f"Kia ora, {name}!")

window = tk.Tk()
window.title("Personal Greeter")
window.geometry("360x180")

tk.Label(window, text="What is your name?").pack(pady=5)
name_box = tk.Entry(window)
name_box.pack()

tk.Button(window, text="Greet me", command=greet).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()