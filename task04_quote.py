# task04_quote.py
# Displays a quote and the person who said it in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

window = tk.Tk()
window.title("Quote")
window.geometry("800x150")

line1 = tk.Label(window, text=' "Be who you are and say what you feel, because those who mind don\'t matter, and those who matter don\'t mind" ', font=("Arial", 12))
line2 = tk.Label(window, text="- Bernard M. Baruch",  font=("Arial", 12, "italic"))
line1.pack(pady=20)
line2.pack()

window.mainloop()