# task14_password.py
# Displays a password checker GUI
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def check_password():
    entered = password_box.get()
    if entered == "eggs2026":
        status.config(text="Access Granted", fg="green")
    else:
        status.config(text="Access Denied", fg="red")

window = tk.Tk()
window.title("EGGS Login")
tk.Label(window, text="Password:").pack()
password_box = tk.Entry(window, show="*")
password_box.pack()
tk.Button(window, text="Log in", command=check_password).pack(pady=5)
status = tk.Label(window, text="")
status.pack()
window.mainloop()
