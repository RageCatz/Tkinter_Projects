# task11_gst.py
# Ask the user to enter a price (excluding GST) then calculate the amount after GST
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def calculate():
    price = float(price_box.get())
    GST = 0.15 * price
    total_price = price + GST

    output_label.config(text=f"GST amount = ${GST:.2f}")
    output_label1.config(text=f"Total Price = ${total_price:.2f}")

window = tk.Tk()
window.title("GST Calculator")
window.geometry("360x280")

tk.Label(window, text="Enter a price excluding GST").pack(pady=5)
price_box = tk.Entry(window)
price_box.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

output_label1 = tk.Label(window, text="")
output_label1.pack()

window.mainloop()