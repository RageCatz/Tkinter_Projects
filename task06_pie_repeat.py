# task06_pie_repeat.py
# Displays a string repeated ten times on ten separate lines in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

window = tk.Tk()
window.title("Pie")
window.geometry("400x230")

for i in range(10):
    tk.Label(window, text="I want a pie for lunch.").pack()

window.mainloop()