# task12_tipper.py
# Let the user enter a restaurant bill total and display 2 amount of tips
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def calculate():
    bill = float(bill_box.get())
    fifteen = 1.15 * bill
    twenty = 1.20 * bill

    output_label.config(text=f"15% tip = ${fifteen:.2f}")
    output_label1.config(text=f"20% tip = ${twenty:.2f}")

window = tk.Tk()
window.title("Tips")
window.geometry("360x280")

tk.Label(window, text="Enter a restaurant bill total").pack(pady=5)
bill_box = tk.Entry(window)
bill_box.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

output_label1 = tk.Label(window, text="")
output_label1.pack()

window.mainloop()