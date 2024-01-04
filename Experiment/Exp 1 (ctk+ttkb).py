# Testing to combine customtkinter and ttkbootstrap

import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk


# ----------------------------------- Setup ---------------------------------- #
window = ctk.CTk()
#window = ttk.Window()
window.title("Murge ctk & ttkb")
window.geometry("600x400")
window.iconbitmap("Assets/py-mono.ico")  # Change window icon

# Window style
ctk.set_appearance_mode("dark")  # Force ctk dark mode
ttk.Style().load_user_themes(file="Assets/TTKB-Themes/darkly_ctk.json")  # Load custom ttkb theme
ttk.Style().theme_use("darkly_ctk")  # Set the ttkbootstrap theme


# ---------------------------------- Widgets --------------------------------- #
# Title
title_label = ttk.Label(master=window, text="TEST WINDOW", font="Arial 24 bold").pack(pady=10)

# Meter
meter = ttk.Meter(
    master=window,
    metersize=180,
    amountused=25,
    metertype="semi",
    meterthickness=15,
    stripethickness=10,
    interactive=True,
    bootstyle="danger"
).pack(pady=10)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()