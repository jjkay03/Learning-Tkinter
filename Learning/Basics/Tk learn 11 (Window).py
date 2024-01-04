# ---------------------------------------------------------------------------- #
#                                    Window                                    #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="journal")
window.title("Window")
#window.geometry("600x400+100+200")
window.iconbitmap("Assets/py.ico")  # Change window icon


# ------------------------------ Start at midle ------------------------------ #
# Start the window in the middle of the screen
window_width = 600
window_hight = 400
display_width = window.winfo_screenwidth()  # Get screen width
display_hight = window.winfo_screenheight()  # Get screen height

left = int(display_width/2 - window_width/2)
top = int(display_width/2 - display_hight/2)
window.geometry(f"{window_width}x{window_hight}+{left}+{top}")


# ------------------------------ Window options ------------------------------ #
# Window sizes
window.minsize(400, 200)  # Window minimum size
#window.maxsize(800,600)  # Window max size
window.resizable(True, False)  # Define if the app is resizable and in what axes

# Window attribtes
window.attributes("-alpha", 0.8)  # Set how transparent the window is (between 0->1)
window.attributes("-topmost", True)  # Make it so the window is always on top
window.attributes("-disable", False)  # Disables the window if True (can't interact with)
window.attributes("-fullscreen", False)  # Starts the window in fullscreen if set to True

# Window title bar
window.overrideredirect(False)  # Removes title bar if set to true
grip = ttk.Sizegrip(window)  # Grip wifget that allows resize if title is removed
grip.place(relx=1.0, rely=1.0, anchor="se")


# ---------------------------------- Events ---------------------------------- #
# Security event: makes it so when esc is pressed the window gets closed
window.bind("<Escape>", lambda event: window.quit())


# ------------------------------------ Run ----------------------------------- #
window.mainloop()