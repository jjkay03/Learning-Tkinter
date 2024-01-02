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


# ---------------------------------- Events ---------------------------------- #
# This event trigers when item is selected in the combobox
combo.bind(
    sequence = "<<ComboboxSelected>>",
    func = (lambda event: combo_label.config(text=f"SELECTED: {choices_str.get()}"))
)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()