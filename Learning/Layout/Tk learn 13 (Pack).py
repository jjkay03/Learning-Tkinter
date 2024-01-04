# ---------------------------------------------------------------------------- #
#                                     Pack                                     #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window()
window.title("Layout")
window.geometry("400x600")


# ---------------------------------- Widgets --------------------------------- #
label1 = ttk.Label(window, text="First label", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Las label", background="green")
button = ttk.Button(window, text="Button")


# ---------------------------------- Layout ---------------------------------- #
label1.pack(side="bottom")
label2.pack(side="bottom")
label3.pack(side="bottom")
button.pack(side="bottom")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()
