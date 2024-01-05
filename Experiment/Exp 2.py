# Random thing I codded with my friends because why not

import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk
from random import choice

# --------------------------------- Variables -------------------------------- #
list = ["Nick", "Sea", 
        "So", "Soare",
        "jj", "kay", 
        "Alligator", "Aleks",
        "Gonk","Ass"
        ]


# --------------------------------- Functions -------------------------------- #
def generate_name():
    generated_name = choice(list) + choice(list)
    title_var.set(generated_name)
    print(f"GENERATED NAME: {generated_name}")


# ---------------------------------- Window ---------------------------------- #
# Window settings
window = ctk.CTk()
window.title("Goobers Name Gen")
window.geometry('300x150')
window.iconbitmap("Assets/py-mono.ico")
window.resizable(False, False)  # Define if the app is resizable and in what axes

# Window style
ctk.set_appearance_mode("dark")  # Force ctk dark mode
ttk.Style().load_user_themes(file="Assets/TTKB-Themes/darkly-ctk.json")  # Load custom ttkb theme
ttk.Style().theme_use("darkly-ctk")  # Set the ttkbootstrap theme

# Widgets
title_var = tk.StringVar(value="Press Generate")
title_label = ttk.Label(master=window, textvariable=title_var, font="Calibri 24 bold")
title_label.pack(pady=20)

generate_button = ttk.Button(
    master = window, 
    text = "GENERATE", 
    bootstyle = "secondary-outline", 
    command = generate_name
    )
generate_button.pack()

window.mainloop()


