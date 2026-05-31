# task25_minitool.py
# Analyzing user input to validate names and calculate table arrangements for an event guest list
# Author: Huan Qi Low     Date: 17/05/2026

import tkinter as tk

def update_table_count():
    total_guests = guest_list.size()
    tables_needed = 0

    for i in range(0, total_guests, 5):
        tables_needed += 1

    result_label.config(text=f"Total Guests: {total_guests} | Tables Needed: {tables_needed}", fg="blue",)

def add_guest():
    guest_name = guest_entry.get()
    if guest_name.strip():
        if len(guest_name) <= 20:
            if guest_name in guest_list.get(0, tk.END):
                result_label.config(text=f"Error: Guest '{guest_name}' is already in the list!", fg="orange")
                guest_entry.delete(0, tk.END)
            else:
                guest_list.insert(tk.END, guest_name)
                status_label.config(text=f"Success! Guest '{guest_name}' added to the list.", fg="green")
                guest_entry.delete(0, tk.END)
                update_table_count()
        else:
            status_label.config(text="Error: Name cannot exceed 20 characters!", fg="red")
            guest_entry.delete(0, tk.END)
    else:
        status_label.config(text="Error: Name cannot be blank!", fg="red")
        guest_entry.delete(0, tk.END)

def delete_selected():
    selected_indices = guest_list.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            guest_list.delete(index)
        result_label.config(text="Selected guest(s) removed from the list.", fg="green")
        update_table_count()
        clear_status(None)
    else:
        result_label.config(text="Error: No guest selected to delete!", fg="red")

def clear_guest():
    guest_list.delete(0, tk.END)
    update_table_count()
    result_label.config(text="All guests have been removed from the list.", fg="green")
    clear_status(None)

def clear_status(event):
    status_label.config(text="")

window = tk.Tk()
window.title("Event Seating Planner")
window.geometry("380x460")

tk.Label(window, text="Enter Guest Full Name:", font=("Arial", 12, "bold")).pack(pady=(15, 0))
guest_entry = tk.Entry(window, width=25)
guest_entry.pack(pady=5)
guest_entry.bind("<Key>", clear_status)

tk.Button(window, text="Add to Guest List", command=add_guest).pack(pady=5)

status_label = tk.Label(window, text="Waiting for input...", font=("Arial", 10, "italic"), fg="gray")
status_label.pack(pady=5)

tk.Label(window, text="Current Invitation List:", font=("Arial", 10, "bold")).pack(pady=(10, 0))
guest_list = tk.Listbox(window, height=8, width=30)
guest_list.pack(pady=5)

result_label = tk.Label(window, text="Total Guests: 0 | Tables Needed: 0", font=("Arial", 10, "bold"), fg="blue")
result_label.pack(pady=5)

tk.Button(window, text="Delete Selected", command=delete_selected).pack(pady=2)
tk.Button(window, text="Clear All", command=clear_guest).pack(pady=2)

window.mainloop()