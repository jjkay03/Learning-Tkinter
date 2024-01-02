# ---------------------------------------------------------------------------- #
#                              Combobox & Spinbox                              #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk

# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="united")
window.title("Combo & Spin")
window.geometry("400x500")


# --------------------------------- Combobox --------------------------------- #
items = ("Choice 1", "Choice 2", "Choice 3", "Choice 4")
choices_str = tk.StringVar(value=items[0])

# Combo label to display the combo item selected
combo_label = ttk.Label(window, text="SELECTED: ?", font="Calibri 20 bold")
combo_label.pack()

# Combobox
combo = ttk.Combobox(master=window, textvariable=choices_str)
combo.config(values=items)  # Set the values of the combobox as items
#combo['values'] = items  # Does the same as the line above
combo.pack(pady=10)


# ---------------------------------- Spinbox --------------------------------- #
# Creating the spinbox with values from 3 to 20 (with an increment of 3)
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
    master = window, 
    from_ = 3, to = 20, 
    increment = 3,
    textvariable = spin_int,
    command = (lambda: print(f"SPIN: {spin_int.get()}"))
    )
#spin.config(values=[1,2,3,4,5])
spin.pack(pady=10)


# ---------------------------------- Events ---------------------------------- #
# This event trigers when item is selected in the combobox
combo.bind(
    sequence = "<<ComboboxSelected>>",
    func = (lambda event: combo_label.config(text=f"SELECTED: {choices_str.get()}"))
)

# This event trigers when the spinbox increments
spin.bind(
    sequence = "<<Increment>>",
    func = (lambda event: print("UP"))
)

# This event trigers when the spinbox decrements
spin.bind(
    sequence = "<<Decrement>>",
    func = (lambda event: print("DOWN"))
)

# ------------------------------------ Run ----------------------------------- #
window.mainloop()