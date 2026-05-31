# task02_eggs_colors.py
# Displays a friendly greeting with a navy background and gold font in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

window = tk.Tk()
window.title("My First App")
window.geometry("400x150")
window.configure(bg="navy")

greeting = tk.Label(window, text="Hello World, nice to meet you.", font=("Arial", 14), fg=("gold"), bg=("navy"))
greeting.pack(pady=20)

window.mainloop()