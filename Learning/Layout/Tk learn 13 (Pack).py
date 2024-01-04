# ---------------------------------------------------------------------------- #
#                                     Pack                                     #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window()
window.title("Pack")
window.geometry("400x600")


# ---------------------------------- Widgets --------------------------------- #
label1 = ttk.Label(window, text="First label", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Las of the label", background="green")
button = ttk.Button(window, text="Button")


# ---------------------------------- Layout ---------------------------------- #
label1.pack(side="top", expand=True, fill="both", padx=5, pady=5)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()
