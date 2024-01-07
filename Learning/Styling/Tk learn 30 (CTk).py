# ---------------------------------------------------------------------------- #
#                                 CustomTkinter                                #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


# ---------------------------------- Window ---------------------------------- #
window = ctk.CTk()
window.title('CTk App')
window.geometry('600x400')


# ---------------------------------- Widgets --------------------------------- #
# Label
string_var = ctk.StringVar(value = 'Custom string')
label = ctk.CTkLabel(
	window, 
	text = 'A ctk label', 
	fg_color = ('blue','red'),  # First agr color for light mode and 2nd for dark mode
	text_color = ('black','white'),
	corner_radius = 10,
	textvariable = string_var)
label.pack()

# Button
button = ctk.CTkButton(
	window, 
	text = 'A ctk button',
	fg_color = '#FF0', 
	text_color = '#000',
	hover_color = '#AA0',
	command = lambda: ctk.set_appearance_mode('light'))  # Make the button activate light mode
button.pack()

# Frame
frame = ctk.CTkFrame(window)
frame.pack()

# Slider
slider = ctk.CTkSlider(frame)
slider.pack(padx = 20, pady = 20)

# Switch
switch = ctk.CTkSwitch(
	window, 
	text = 'Switch',
	fg_color = ('blue','red'),
	progress_color = 'pink',
	button_color = 'green',
	button_hover_color = 'yellow',
	switch_width = 60,
	switch_height = 30,
	corner_radius = 2
    )
switch.pack()


# ------------------------------------ Run ----------------------------------- #
window.mainloop()