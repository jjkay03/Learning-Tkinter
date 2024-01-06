# ---------------------------------------------------------------------------- #
#                              Custom Conmponents                              #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk


# ------------------------------- Cusstom conmp ------------------------------ #
def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master=parent)
    
    # Grid layout
    frame.rowconfigure(0, weight=1, uniform="a")
    frame.columnconfigure((0,1,2), weight=1, uniform="a")
    
    # Widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew")
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky="nsew")

    return frame

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, box_text, label_background):
        super().__init__(parent)

        # Grid layout
        self.rowconfigure(0, weight=1, uniform="a")
        self.columnconfigure((0,1,2), weight=1, uniform="a")

        # Widgets
        ttk.Label(self, text=label_text, background=label_background).grid(row=0, column=0, sticky="nsew")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew")
        self.create_box(box_text).grid(row=0, column=2, sticky="nsew")

        self.pack(expand=True, fill="both", padx=10, pady=10)

    def create_box(self, text):
        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(expand=True, fill="both")
        ttk.Button(frame, text=text).pack(expand=True, fill="both")
        return frame


# ------------------------------- Window Setup ------------------------------- #
window = tk.Tk()
window.title("Custom conmponenets")
window.geometry("400x600")


# ---------------------------------- Widgets --------------------------------- #
Segment(window, label_text="Label 1", button_text="Button 1", box_text="Box 1", label_background="red")
Segment(window, label_text="Label 2", button_text="Button 2", box_text="Box 2", label_background="orange")
Segment(window, label_text="Label 3", button_text="Button 3", box_text="Box 3", label_background="yellow")
Segment(window, label_text="Label 4", button_text="Button 4", box_text="Box 4", label_background="lime")
Segment(window, label_text="Label 5", button_text="Button 5", box_text="Box 5", label_background="green")

# create_segment(window, label_text="Label 1", button_text="Button 1").pack(expand=True, fill="both")
# create_segment(window, label_text="Label 2", button_text="Button 2").pack(expand=True, fill="both")
# create_segment(window, label_text="Label 3", button_text="Button 3").pack(expand=True, fill="both")
# create_segment(window, label_text="Label 4", button_text="Button 4").pack(expand=True, fill="both")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()