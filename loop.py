# loop.py
# Displays a loop-generated times table in a tkinter window
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def show_times_table():
    output = ""
    for i in range(1, 11):
        output = output + f"{i} x 5 = {i * 5}\n"
    # This line works now because 'result' is created below
    result.config(text=output)


# 1. Create the main window
root = tk.Tk()
root.title("Times Table")
root.geometry("200x300")

# 2. Create the button to trigger the function
btn = tk.Button(root, text="Show 5 Times Table", command=show_times_table)
btn.pack(pady=10)

# 3. Create the missing 'result' label widget
result = tk.Label(root, text="", font=("Arial", 12), justify="left")
result.pack(pady=10)

# 4. Start the application
root.mainloop()