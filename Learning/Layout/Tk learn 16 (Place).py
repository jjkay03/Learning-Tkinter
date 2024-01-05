# ---------------------------------------------------------------------------- #
#                                     Place                                    #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk


# ----------------------------------- Setup ---------------------------------- #
window = tk.Tk()
window.title("Place")
window.geometry("400x600")


# ---------------------------------- Widgets --------------------------------- #
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Label 3", background="green")
button = ttk.Button(window, text="Button 1")


# ---------------------------------- Layout ---------------------------------- #
label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4 , relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button.place(relx=1, rely=1, anchor="se")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()