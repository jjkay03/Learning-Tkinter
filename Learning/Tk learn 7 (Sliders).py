# ---------------------------------------------------------------------------- #
#                                    Sliders                                   #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk

# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Sliders")
#window.geometry("600x400")


# ---------------------------------- Slider ---------------------------------- #
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    master = window,
    from_ = 0, to = 25,
    length = 300,
    orient = "vertical", 
    variable = scale_float,
    command = (lambda value: progress.stop()),
    bootstyle = "success"
    )
scale.pack(pady=5)


# ------------------------------- Progress Bar ------------------------------- #
progress = ttk.Progressbar(
    master = window,
    maximum = 25,
    length = 400,
    orient = "horizontal",
    mode = "determinate",
    variable = scale_float,
    bootstyle = "success-striped"
)
progress.pack(pady=5)

progress.start(100)  # Starts the progess bar


# ------------------------------- Scrolledtext ------------------------------- #
scrolled_text = ttk.ScrolledText(master=window)
scrolled_text.pack(pady=10)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()