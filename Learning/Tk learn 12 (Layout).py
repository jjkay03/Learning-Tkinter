# ---------------------------------------------------------------------------- #
#                                    Layout                                    #
# ---------------------------------------------------------------------------- #
# NOTES: Main placing methods: pack, grid and place
# Pack: Places the widgets in order
# Grid: Allows you to create a grid and place the widgets on it
# Place: Allows you to place widgets using coards

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="journal")
window.title("Layout")
window.geometry("600x400")


# ---------------------------------- Widgets --------------------------------- #
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")


# -------------------------------- Layout Pack ------------------------------- #
'''
label1.pack(side="left", expand=True, fill="y")
label2.pack(side="left",  expand=True, fill="both")
'''


# -------------------------------- Layout Grid ------------------------------- #
# Creating grids
'''
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
'''

# Placing widgets on grid
'''
label1.grid(row=0, column=1, sticky="nsew")
label2.grid(row=1, column=1, columnspan=2, sticky="nsew")
'''


# ------------------------------- Layout Place ------------------------------- #
label1.place(x=100, y=200, width=200, height=100)
label2.place(relx=0.5 , rely=0.5, relwidth=1, anchor="center")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()

