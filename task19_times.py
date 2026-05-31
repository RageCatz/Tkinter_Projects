# task19_times.py
# Let user pick the multiplication table
# Author: Huan Qi Low     Date: 16/05/2026

import tkinter as tk

def count():
    n = num_box.get()
    final_number = ""
    for i in range(1, 13):
        number = f"{n} x {i} = {int(n) * i}\n"
        final_number += number
    result.config(text=final_number)

window = tk.Tk()
window.title("Counting to 20")
window.geometry("360x300")

tk.Label(window, text="Enter a number:").pack(pady=5)
num_box = tk.Entry(window)
num_box.pack()

tk.Button(window, text="Show times table", command=count).pack(pady=5)
result = tk.Label(window, text="")
result.pack()

window.mainloop()