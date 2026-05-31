# task18_count.py
# Counting even numbers until 20
# Author: Huan Qi Low     Date: 16/05/2026

import tkinter as tk

def count():
    number = ""
    for i in range(2, 21, 2):
        number += str(i) + "\n"
    result.config(text=number)

window = tk.Tk()
window.title("Counting to 20")
window.geometry("360x250")

tk.Button(window, text="Count to 20", command=count).pack(pady=5)
result = tk.Label(window, text="")
result.pack()

window.mainloop()