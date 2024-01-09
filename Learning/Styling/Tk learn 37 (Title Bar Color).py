# ---------------------------------------------------------------------------- #
#                                Title Bar Color                               #
# ---------------------------------------------------------------------------- #

import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int

# ---------------------------------- Window ---------------------------------- #
# Setup
app = ctk.CTk(fg_color="#FF00FF")
app.geometry("300x200")

# Change title bar color
HWND = windll.user32.GetParent(app.winfo_id())  # Get the app
title_bar_color = 0x00FF00FF
windll.dwmapi.DwmSetWindowAttribute(
    HWND,
    35,
    byref(c_int(title_bar_color)),
    sizeof(c_int)
)

# ------------------------------------ Run ----------------------------------- #
app.mainloop()
