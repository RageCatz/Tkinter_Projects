# task09_food_fusion.py
# Ask the user for 2 of their favourite food and combine to display it on a label
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def combine():
    fav1 = fav1_box.get()
    fav2 = fav2_box.get()
    output_label.config(text=fav1 + fav2)

window = tk.Tk()
window.title("Food Fusion")
window.geometry("360x180")

tk.Label(window, text="What is your first favourite food?").pack(pady=5)
fav1_box = tk.Entry(window)
fav1_box.pack()

tk.Label(window, text="What is your second favourite food?").pack(pady=5)
fav2_box = tk.Entry(window)
fav2_box.pack()

tk.Button(window, text="Combine", command=combine).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()