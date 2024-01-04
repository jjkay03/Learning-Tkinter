# ---------------------------------------------------------------------------- #
#                               Frames & Parents                               #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Frames & Parents")
window.geometry("600x400")


# ---------------------------------- Frames ---------------------------------- #
frame = ttk.Frame(
    master = window, 
    width = 200, height = 200,
    borderwidth = 10,
    relief = ttk.SOLID
    )
frame.pack_propagate(False)  # Don't change feame size depending on child
frame.pack(padx=10, side="left")


# ------------------------------ Master Setting ------------------------------ #
label = ttk.Label(frame, text="Label in frame")
label.pack(pady=5)

button = ttk.Button(frame, text="Button in frame")
button.pack(pady=5)

label_2 = ttk.Label(window, text="Label outisde frame")
label_2.pack(side="left")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()