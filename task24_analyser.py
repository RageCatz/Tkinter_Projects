# task24_analyser.py
# Analyzing the number of characters and whether there is a letter 'e' in user's message
# Author: Huan Qi Low     Date: 17/05/2026

import tkinter as tk

def analyze_labels():
    message_text = entry.get()

    # Analyze the message
    char_count = len(message_text)
    has_e = 'e' in message_text.lower()

    if has_e == False:
        has_e = "The letter ‘e’ IS NOT in your message."
    else:
        has_e = "The letter ‘e’ IS in your message."

    # Update results
    result_label.config(text=f"Your message has {char_count} characters.\n {has_e}")

window = tk.Tk()
window.title("Label Analyzer")
window.geometry("400x200")

tk.Label(window, text="Message:").pack()
entry = tk.Entry(window)
entry.pack(pady=5)

tk.Button(window, text="Analyze", command=analyze_labels).pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()