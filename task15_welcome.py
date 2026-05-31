# task15_welcome.py
# Displays a password checker GUI with user's name
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def check_password():
    name = name_box.get()

    entered = password_box.get()
    if entered == "eggs2026":
        status.config(text=f"Welcome, {name}!", fg="green")
    else:
        status.config(text="Try harder", fg="red")

window = tk.Tk()
window.title("EGGS Login")
window.geometry("360x200")

tk.Label(window, text="Name:").pack()
name_box = tk.Entry(window, text="")
name_box.pack()

tk.Label(window, text="Password:").pack()
password_box = tk.Entry(window, show="*")
password_box.pack()

tk.Button(window, text="Log in", command=check_password).pack(pady=5)
status = tk.Label(window, text="")
status.pack()

window.mainloop()