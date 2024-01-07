# ---------------------------------------------------------------------------- #
#                                    Styling                                   #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk, font

# ---------------------------------- Window ---------------------------------- #
window = tk.Tk()
window.title("Styling")
window.geometry("400x300")

#print(font.families())  # List all fonts you can use

# ----------------------------------- Style ---------------------------------- #
style = ttk.Style()
#print(style.theme_names())  # List all themes you can use
#style.theme_use("clam")

style.configure("new.TButton", foreground="green", font = ("Jokerman", 20))
style.map("new.TButton", 
          foreground = [("pressed", "red"),("disabled", "yellow")],
          background = [("pressed", "green"),("active", "blue")]
          )

# ---------------------------------- Widgets --------------------------------- #
label = ttk.Label(
    window, 
    text = "A label\nAnd type and other line", 
    background = "red", 
    foreground = "white",
    font = ("Jokerman", 20),
    justify = "center"
    )
label.pack(pady=10)

button = ttk.Button(window, text = "A button", style="new.TButton")
button.pack(pady=10)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()