# ---------------------------------------------------------------------------- #
#                                     Menus                                    #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="journal")
window.title("Menus")
window.geometry("600x400")


# ----------------------------------- Menus ---------------------------------- #
# Main menu 
menu = ttk.Menu(window)

# Sub menu: File
file_menu = ttk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command=(lambda: print("NEW FILE")))
file_menu.add_command(label="Open", command=(lambda: print("OPEN FILE")))
file_menu.add_separator()  # Creates a separator
file_menu.add_command(label="Delete", command=(lambda: print("DELETE FILE")))
menu.add_cascade(label="File", menu=file_menu)  # Add sub menu to main menu

# Sub menu: Help
help_menu = ttk.Menu(menu, tearoff=False)
help_menu.add_command(label="Help entry", command=(lambda: print(help_check_string.get())))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label="Check", onvalue="on", offvalue="off", variable=help_check_string)
menu.add_cascade(label="Help", menu=help_menu)

# Sub menu with a sub menu
sub_menu = ttk.Menu(menu, tearoff=False)
sub_menu.add_command(label="Stuff")
menu.add_cascade(label="Sub", menu=sub_menu)
# Create the sub sub menu
subsub_menu = ttk.Menu(menu, tearoff=False)
subsub_menu.add_command(label="Stuff stuff")
sub_menu.add_cascade(label="More stuff", menu=subsub_menu)

# Add main menu to the window
window.configure(menu=menu)


# -------------------------------- Menu button ------------------------------- #
# Menu button works like menus but inside a widget
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()

# Create a sub menu for the menu button
button_sub_menu = ttk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="Entry 1")
button_sub_menu.add_checkbutton(label="Check 1")
menu_button.configure(menu=button_sub_menu)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()