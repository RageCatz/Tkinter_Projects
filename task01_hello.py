# task01_hello.py
# Displays a friendly greeting in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

window = tk.Tk()
window.title("My First App")
window.geometry("400x150")

greeting = tk.Label(window, text="Hello World, nice to meet you.", font=("Arial", 14))
greeting.pack(pady=20)

window.mainloop()