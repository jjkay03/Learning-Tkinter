# ---------------------------------------------------------------------------- #
#                               Animated Widgets                               #
# ---------------------------------------------------------------------------- #

import customtkinter as ctk
from random import choice


# ---------------------------------- Classes --------------------------------- #
class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # General attributes
        self.start_pos = start_pos + 0.01
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)  # abs makes sure the number is positive
        self.rely = 0.05
        self.relheight = 0.9

        # Animation logic
        self.pos = self.start_pos  # Track position of the panel
        self.in_start_pos = True  # Track if the pannel is in the start position

        # Layout
        self.place(relx=self.start_pos, rely=self.rely, relwidth=self.width, relheight=self.relheight)

    # Determinte in what diration the animation should play
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    # Forward animation
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008  # Determine animation speed
            self.place(relx=self.pos, rely=self.rely, relwidth=self.width, relheight=self.relheight)
            self.after(3, self.animate_forward)  # Re-run the function until the animation is completed
        else:
            self.in_start_pos = False

    # Backwards animation
    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008  # Determine animation speed
            self.place(relx=self.pos, rely=self.rely, relwidth=self.width, relheight=self.relheight)
            self.after(5, self.animate_backwards)  # Re-run the function until the animation is completed
        else:
            self.in_start_pos = True


# --------------------------------- Functions -------------------------------- #
# Function that moves and chages the color of button
def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx=button_x, rely=0.5, anchor="center")
    
    if button_x < 0.9:
        window.after(10, move_btn)

    # Configure
    #colors_list = ["red", "yellow", "green", "pink", "blue", "orange"]
    #button.configure(fg_color=choice(colors_list))

# Function to demonstarte .after
def infinite_print():
    global button_x
    button_x += 0.5

    if button_x < 10:
        print("INFINITE"); print(button_x)
        window.after(100, infinite_print)  # After runs a function after a given time in milisec

# Function to change theme
def change_theme():
    global theme_state
    if theme_state:
        ctk.set_appearance_mode("light")
        button_theme.configure(text="🌞")
        theme_state = False
    else:
        ctk.set_appearance_mode("dark")
        button_theme.configure(text="🌙")
        theme_state = True


# ---------------------------------- Window ---------------------------------- #
window = ctk.CTk()
window.title("Animation")
window.geometry("600x400")
ctk.set_appearance_mode("dark")


# ---------------------------------- Widgets --------------------------------- #
# Animated widget
animated_pannel = SlidePanel(window, 0, -0.3)
ctk.CTkLabel(animated_pannel, text="Panel").pack(expand=True, fill="both", padx=2, pady=10)
ctk.CTkButton(animated_pannel, text="Button", corner_radius=0).pack(expand=True, fill="both", pady=10)
ctk.CTkTextbox(animated_pannel, fg_color=("#dbdbdb","#2b2b2b")).pack(expand=True, fill="both", pady=10)

# Panel button
button_x = 0.5
button = ctk.CTkButton(window, text="Toggle sidebar", command=animated_pannel.animate)
button.place(relx=button_x, rely=0.5, anchor="center")

# Theme button
theme_state = True
button_theme = ctk.CTkButton(window, text="🌙", width=1, command=change_theme)
button_theme.place(relx=0.99, rely=0.99, anchor="se")


# ------------------------------------ Run ----------------------------------- #
window.mainloop()