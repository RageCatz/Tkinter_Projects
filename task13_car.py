# task13_car.py
# Let the user enter the base price of a car and calculate GST plus set fees (licence plates, tow bar, sound system and, seat covers)
# Author: Huan Qi Low     Date: 14/05/2026

import tkinter as tk

def calculate():
    price = float(price_box.get())
    license_plates = 120
    tow_bar = 450
    sound_system = 680
    seat_covers = 200

    no_gst = price + license_plates + tow_bar + sound_system + seat_covers
    with_gst = 1.15 * no_gst

    output_label.config(text=f"Total On-Road Price = ${no_gst}")

window = tk.Tk()
window.title("Car Saleperson")
window.geometry("360x280")

tk.Label(window, text="Enter car base price").pack(pady=5)
price_box = tk.Entry(window)
price_box.pack()

fees = ("Licence Plates = $120\nTow Bar = $450\nSound System = $680\nSeat Covers = $200\nGST = 15%")
tk.Label(window, text=f"Included Set Fees: \n{fees}").pack(pady=5)

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()