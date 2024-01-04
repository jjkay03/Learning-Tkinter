# ---------------------------------------------------------------------------- #
#                                 Pack + Frames                                #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk


# ----------------------------------- Setup ---------------------------------- #
window = tk.Tk()
window.title("Pack + Frames")
window.geometry("400x600")


# ---------------------------------- Widgets --------------------------------- #
# Top frames
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text="First label", background="red")
label2 = ttk.Label(top_frame, text="Label 2", background="blue")

# Middle widget
label3 = ttk.Label(window, text="Another label", background="green")

# Bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text="Las of the label", background="orange")
button = ttk.Button(bottom_frame, text="Button")
button2 = ttk.Button(bottom_frame, text="Another Button")

# Bottom side frame
bottom_side_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(bottom_side_frame, text="Button 3")
button4 = ttk.Button(bottom_side_frame, text="Button 4")
button5 = ttk.Button(bottom_side_frame, text="Button 5")


# ---------------------------------- Layout ---------------------------------- #
# Top layout
label2.pack(side="left", fill="both", expand=True)
label1.pack(side="left", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)

# Muiddle layout
label3.pack(expand=True)

# Bottom layout
button.pack(side="left", fill="both", expand=True)
label4.pack(side="left", fill="both", expand=True)
button2.pack(side="left", fill="both", expand=True)
bottom_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Bottom side layout
button3.pack(expand=True, fill="both")
button4.pack(expand=True, fill="both")
button5.pack(expand=True, fill="both")
bottom_side_frame.pack(expand=True, fill="both")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()
