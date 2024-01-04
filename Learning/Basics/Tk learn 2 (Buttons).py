# ---------------------------------------------------------------------------- #
#                                    Buttons                                   #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Buttons")
window.geometry("600x400")


# ---------------------------------- Button ---------------------------------- #
def button_func(): 
    global button_time_pressed
    button_time_pressed += 1
    button_str.set(button_time_pressed)

button_time_pressed = 0
button_str = tk.StringVar(value="Magic Button")
button = ttk.Button(
    master = window, 
    text = "Magic Button", 
    command = button_func, 
    textvariable = button_str
    )
button.pack(pady=5)


# ------------------------------ Check Button 1 ------------------------------ #
check_1_var = tk.BooleanVar()
check_1 = ttk.Checkbutton(
    master = window, 
    text = "Magic Check 1", 
    command = (lambda: print(f"Magic Check 1: {check_1_var.get()}")),
    variable = check_1_var
    )
check_1.pack(pady=5)


# ------------------------------ Check Button 2 ------------------------------ #
check_2_var = tk.IntVar(value=10)
check_2 = ttk.Checkbutton(
    master = window, 
    text = "Magic Check 2", 
    command = (lambda: print(f"Magic Check 2: {check_2_var.get()}")),
    variable = check_2_var,
    onvalue = 10,
    offvalue = 5
    )
check_2.pack(pady=5)


# ------------------------- Check Button 3 bootstrap ------------------------- #
check_3_var = tk.BooleanVar()
check_3 = ttk.Checkbutton(
    master = window, 
    text = "Magic Check 3", 
    command = (lambda: print(f"Magic Check 3: {check_1_var.get()}")),
    variable = check_3_var,
    bootstyle = "danger-square-toggle"
    )
check_3.pack(pady=5)


# ------------------------------- Radio Buttons ------------------------------ #
radio_var = tk.StringVar()
radio_1 = ttk.Radiobutton(
    master=window, 
    text = "Radiobutton 1", 
    value = "Radio 1", 
    variable= radio_var,
    command = (lambda: print(f"Radio: {radio_var.get()}"))
    )
radio_1.pack(pady=5)

radio_2 = ttk.Radiobutton(
    master = window, 
    text = "Radiobutton 2", 
    value = 2,
    variable= radio_var,
    command = (lambda: print(f"Radio: {radio_var.get()}"))
    )
radio_2.pack(pady=5)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()