# launcher.py
# Displays a simple GUI to launch various Python scripts for different tasks
# Author: Huan Qi Low     Date: 31/05/2026

import tkinter as tk
import subprocess

def run_task(file):
    subprocess.run(["python", file])

root = tk.Tk()
root.title("My Python Projects")

tk.Label(root, text="Select a Task").pack()

tk.Button(root, text="Task 1", command=lambda: run_task("task01_hello.py")).pack()
tk.Button(root, text="Task 2", command=lambda: run_task("task02_eggs_colours.py")).pack()
tk.Button(root, text="Task 3", command=lambda: run_task("task03_joke.py")).pack()
tk.Button(root, text="Task 4", command=lambda: run_task("task04_quote.py")).pack()
tk.Button(root, text="Task 5", command=lambda: run_task("task05_royals.py")).pack()
tk.Button(root, text="Task 6", command=lambda: run_task("task06_pie_repeat.py")).pack()
tk.Button(root, text="Task 7", command=lambda: run_task("task07_greeter.py")).pack()
tk.Button(root, text="Task 8", command=lambda: run_task("task08_two_inputs.py")).pack()
tk.Button(root, text="Task 9", command=lambda: run_task("task09_food_fusion.py")).pack()
tk.Button(root, text="Task 10", command=lambda: run_task("task10_calculator.py")).pack()
tk.Button(root, text="Task 11", command=lambda: run_task("task11_gst.py")).pack()
tk.Button(root, text="Task 12", command=lambda: run_task("task12_tipper.py")).pack()
tk.Button(root, text="Task 13", command=lambda: run_task("task13_car.py")).pack()
tk.Button(root, text="Task 14", command=lambda: run_task("task14_password.py")).pack()
tk.Button(root, text="Task 15", command=lambda: run_task("task15_welcome.py")).pack()
tk.Button(root, text="Task 16", command=lambda: run_task("task16_guess.py")).pack()
tk.Button(root, text="Task 17", command=lambda: run_task("task17_mood.py")).pack()
tk.Button(root, text="Task 18", command=lambda: run_task("task18_count.py")).pack()
tk.Button(root, text="Task 19", command=lambda: run_task("task19_times.py")).pack()
tk.Button(root, text="Task 20", command=lambda: run_task("task20_many_labels.py")).pack()
tk.Button(root, text="Task 21", command=lambda: run_task("task21_countdown.py")).pack()
tk.Button(root, text="Task 22", command=lambda: run_task("task22_avengers.py")).pack()
tk.Button(root, text="Task 23", command=lambda: run_task("task23_shopping.py")).pack()
tk.Button(root, text="Task 24", command=lambda: run_task("task24_analyser.py")).pack()
tk.Button(root, text="Task 25", command=lambda: run_task("task25_minitool.py")).pack()

root.mainloop()