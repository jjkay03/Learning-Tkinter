# ---------------------------------------------------------------------------- #
#                                    Images                                    #
# ---------------------------------------------------------------------------- #

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


# ----------------------------------- Setup ---------------------------------- #
window = tk.Tk()
window.geometry('600x400')
window.title('Images')


# ---------------------------------- Images ---------------------------------- #
image_original = Image.open("Assets/Images/raccoon.jpg")  # Import image as image object
image_ratio = image_original.size[0] / image_original.size[1]  # Get the image ratio
image_tk = ImageTk.PhotoImage(image_original)  # Convert into a file Tk can use

image_python_dark = Image.open("Assets/Images/python_dark.png").resize((30,30))  # Import image
image_tk_pyhton_dark = ImageTk.PhotoImage(image_python_dark)  # Convert into a file Tk can use

# Import images forr ctk light and dark modes
image_ctk_pyhton = ctk.CTkImage(
    light_image = Image.open("Assets/Images/python_dark.png").resize((30,30)), 
    dark_image = Image.open("Assets/Images/python_light.png").resize((30,30))
    )


# --------------------------------- Functions -------------------------------- #
# Function that stretch the image
def stretch_image(event):
    global resized_tk  # ImageTk always has to be in global scope

	# Size
    width = event.width
    height = event.height

	# Create an image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

	# Place on canvas
    canvas.create_image(0,0,image = resized_tk, anchor = 'nw')

# Function that fills the image
def fill_image(event):
    global resized_tk

    # Get current ratio
    canvas_ratio = event.width / event.height

    # Get coordinates 
    if canvas_ratio > image_ratio:  # Canvas is wider than the image
        height = int(event.height)
        width = int(height * image_ratio) 
    else:  # Canvas is narrower than the image
        width = int(event.width) 
        height = int(width / image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # Create the canvas with image
    canvas.create_image(
		int(event.width / 2),
		int(event.height / 2),
		anchor = 'center',
		image = resized_tk)


# ---------------------------------- Layout ---------------------------------- #
# Create grid
window.columnconfigure((0,1,2,3), weight=1, uniform="a")
window.rowconfigure(0, weight=1)


# ---------------------------------- Widgets --------------------------------- #
#label = ttk.Label(window, text="Raccoon", image=image_tk).pack()

# Buttons
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text=" Button", image=image_tk_pyhton_dark, compound="left").pack(pady=5)
button_ctk = ctk.CTkButton(button_frame, text=" Button CTk", image=image_ctk_pyhton, compound="left").pack(pady=5)
button_frame.grid(column=0, row=0, sticky="nsew")

# Canvas for image
canvas = tk.Canvas(window, background="black", bd=0, highlightthickness=0, relief="ridge")
canvas.grid(column=1, row=0, columnspan=3, sticky="nsew")
#canvas.create_image(0, 0, image=image_tk, anchor="nw")
canvas.bind("<Configure>", func=fill_image)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()