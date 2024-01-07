# ---------------------------------------------------------------------------- #
#                                    Colors                                    #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk


# ---------------------------------- Window ---------------------------------- #
window = tk.Tk()
window.title("Colors")
window.geometry("400x300")


# ---------------------------------- Widgets --------------------------------- #
ttk.Label(window, background="red").pack(expand=True, fill="both")
ttk.Label(window, background="#08f").pack(expand=True, fill="both")
ttk.Label(window,  background="#ff7c00").pack(expand=True, fill="both")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()