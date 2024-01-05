# ---------------------------------------------------------------------------- #
#                                   Toggling                                   #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Toggling")
window.geometry("600x400")


# --------------------------------- Functions -------------------------------- #
# for grids: widget.grid_forget()
# for pack: widget.pack_forget()

def toggle_label_place():
    global label_visibile
    if label_visibile:
        label.place_forget()
        label_visibile = False
    else:
        label.place(relx=0.5, rely=0.5, anchor="center")
        label_visibile = True
        

# ----------------------------- Widgets & Layout ----------------------------- #
button = ttk.Button(window, text="TOGGLE", command=toggle_label_place)
button.place(x=10, y=10)

label_visibile = True
label = ttk.Label(window, text="THIS IS A LABEL", font="Arial 40 bold")
label.place(relx=0.5, rely=0.5, anchor="center")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()