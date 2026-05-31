# task05_royals.py
# Displays four lines from Lorde’s song Royals in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

window = tk.Tk()
window.title("Royals")
window.geometry("400x150")

line1 = tk.Label(window, text="I’ve never seen a diamond in the flesh")
line2 = tk.Label(window, text="I cut my teeth on wedding rings in the movies")
line3 = tk.Label(window, text="And I’m not proud of my address")
line4 = tk.Label(window, text="I cut my teeth on wedding rings in the movies")

line1.pack(pady=(20,0))
line2.pack()
line3.pack()
line4.pack()

window.mainloop()