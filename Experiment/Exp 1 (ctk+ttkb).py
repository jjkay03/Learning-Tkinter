# Testing to combine customtkinter and ttkbootstrap

import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk


# ----------------------------------- Setup ---------------------------------- #
window = ctk.CTk()
#window = ttk.Window()
window.title("Murge ctk & ttkb")
ttk.Style().theme_use("darkly")  # Set the ttkbootstrap theme
window.geometry("600x400")
window.iconbitmap("Assets/py-mono.ico")  # Change window icon


# ---------------------------------- Widgets --------------------------------- #
# Title
title_label = ttk.Label(master=window, text="TEST WINDOW", font="Arial 24 bold").pack(pady=10)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()