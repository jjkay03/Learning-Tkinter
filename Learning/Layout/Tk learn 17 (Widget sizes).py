# ---------------------------------------------------------------------------- #
#                                 Widget sizes                                 #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk


# ----------------------------------- Setup ---------------------------------- #
window = tk.Tk()
window.title("Widget sizes")
window.geometry("400x300")


# ---------------------------------- Widget ---------------------------------- #
label1 = ttk.Label(window, text="Label 1", background="green")
label2 = ttk.Label(window, text="Label 2", background="red", width=50)


# ---------------------------------- Layout ---------------------------------- #
# Pack
#label1.pack()
#label2.pack()

# Grid
window.columnconfigure((0,1), weight=1, uniform="a")
window.rowconfigure((0,1), weight=1, uniform="a")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky="nsew")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()
