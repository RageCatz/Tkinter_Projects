# task22_avengers.py
# Display a list of Avengers
# Author: Huan Qi Low     Date: 16/05/2026

import tkinter as tk

def special():
    output_label.config(text=f"The character who has a special hammer is {avengers[1]}")

avengers = ["Captain America", "Thor", "The Hulk", "Iron Man"]

window = tk.Tk()
window.title("Avengers")
window.geometry("360x180")

hero_box = tk.Listbox(window, height=5, width=25)
for hero in avengers:
    hero_box.insert(tk.END, hero)
hero_box.pack(pady=10)

tk.Button(window, text="Special Hammer", command=special).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
