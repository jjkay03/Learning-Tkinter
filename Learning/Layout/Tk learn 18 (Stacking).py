# ---------------------------------------------------------------------------- #
#                                Stacking order                                #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Stacking")
window.geometry("400x400")


# ---------------------------------- Widget ---------------------------------- #
label1 = ttk.Label(window, text="Label 1", background="green")
label2 = ttk.Label(window, text="Label 2", background="red")
label3 = ttk.Label(window, text="Label 3", background="blue")

#label1.lift()
#label2.lower()

button1 = ttk.Button(window, text = "Raise label 1", command=(lambda: label1.tkraise()))
button2 = ttk.Button(window, text = "Raise label 2", command=(lambda: label2.tkraise()))
button3 = ttk.Button(window, text = "Raise label 3", command=(lambda: label3.tkraise()))


# ---------------------------------- Layout ---------------------------------- #
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=20, y=80, width=180, height=100)

button1.place(rely=1, relx=0.4, anchor="se")
button2.place(rely=1, relx=0.7, anchor="se")
button3.place(rely=1, relx=1, anchor="se")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()

