# task10_calculator.py
# Ask the user for 2 numbers and calculate using 5 different operator
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def calculate():
    num1 = float(num1_box.get())
    num2 = float(num2_box.get())
    output_label.config(text=f"x + y = {num1 + num2}")
    output_label1.config(text=f"x - y = {num1 - num2}")
    output_label2.config(text=f"x * y = {num1 * num2}")
    output_label3.config(text=f"x / y = {num1 / num2}")
    output_label4.config(text=f"x % y = {num1 % num2}")

window = tk.Tk()
window.title("Calculator")
window.geometry("360x280")

tk.Label(window, text="Give me one number known as x").pack(pady=5)
num1_box = tk.Entry(window)
num1_box.pack()

tk.Label(window, text="Give me another number known as y").pack(pady=5)
num2_box = tk.Entry(window)
num2_box.pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

output_label1 = tk.Label(window, text="")
output_label1.pack()

output_label2 = tk.Label(window, text="")
output_label2.pack()

output_label3 = tk.Label(window, text="")
output_label3.pack()

output_label4 = tk.Label(window, text="")
output_label4.pack()

window.mainloop()