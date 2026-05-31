# task03_joke.py
# Displays a question on the first line and a punchline on the second line in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

window = tk.Tk()
window.title("Joke Time")
window.geometry("400x150")

line1 = tk.Label(window, text="Why did the golfer wear two pairs of pants?")
line2 = tk.Label(window, text="Just in case he got a hole in one.")
line1.pack(pady=20)
line2.pack()

window.mainloop()