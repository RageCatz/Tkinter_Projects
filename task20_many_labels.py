# task20_many_labels.py
# Create the amount of labels the user wants
# Author: Huan Qi Low     Date: 16/05/2026

import tkinter as tk

def create():
    num_labels = int(num_box.get())
    output_label.config(text="Hello World!\n" * num_labels)

window = tk.Tk()
window.title("Many Labels")
window.geometry("360x180")

tk.Label(window, text="Number of labels to create:").pack(pady=5)
num_box = tk.Entry(window)
num_box.pack()

tk.Button(window, text="Create Labels", command=create).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()