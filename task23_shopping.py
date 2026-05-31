# task23_shopping.py
# Letting the user Add and Clear all items from a shopping list
# Author: Huan Qi Low     Date: 17/05/2026

import tkinter as tk

def add_item():
    item = item_entry.get()
    if item:
        shopping_list.insert(tk.END, item)
        item_entry.delete(0, tk.END)

def clear_items():
    shopping_list.delete(0, tk.END)

window = tk.Tk()
window.title("Shopping List")
window.geometry("360x250")

item_entry = tk.Entry(window)
item_entry.pack(pady=10)

tk.Button(window, text="Add Item", command=add_item).pack(pady=10)
tk.Button(window, text="Clear All", command=clear_items).pack(pady=10)

shopping_list = tk.Listbox(window, height=5, width=25)
shopping_list.pack(pady=10)

window.mainloop()