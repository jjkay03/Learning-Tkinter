# ---------------------------------------------------------------------------- #
#                                Custom CTk App                                #
# ---------------------------------------------------------------------------- #

# Converted TK learn 21 to use CTk instead of Tk

#import tkinter as tk
#from tkinter import ttk
import customtkinter as ctk


# --------------------------------- App Class -------------------------------- #
class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()

        # Main setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0],size[1])

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # Run the app
        self.mainloop()


# ------------------------------- Other Classes ------------------------------ #
class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.create_widgets()
    
    def create_widgets(self):
        # Creating widgets
        menu_button1 = ctk.CTkButton(self, text="Button 1")
        menu_button2 = ctk.CTkButton(self, text="Button 2")
        menu_button3 = ctk.CTkButton(self, text="Button 3")

        menu_slider1 = ctk.CTkSlider(self, orientation="vertical", width=20)
        menu_slider2 = ctk.CTkSlider(self, orientation="vertical", width=20)

        toggle_frame = ctk.CTkFrame(self)
        menu_toggle1 = ctk.CTkCheckBox(toggle_frame, text="Check 1")
        menu_toggle2 = ctk.CTkCheckBox(toggle_frame, text="Check 2")

        entry = ctk.CTkEntry(self)

        # Creating grid for layout
        self.columnconfigure((0,1,2), weight=1, uniform="a")
        self.rowconfigure((0,1,2,3,4), weight=1, uniform="a")

        # Placing widgets on grid
        menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2, padx=4, pady=4)
        menu_button2.grid(row=0, column=2, sticky="nsew", padx=4, pady=4)
        menu_button3.grid(row=1, column=0, sticky="nsew", columnspan=3, padx=4, pady=4)

        menu_slider1.grid(row=2, column=0, sticky="ns", rowspan=2, pady=20)
        menu_slider2.grid(row=2, column=2, sticky="ns", rowspan=2, pady=20)

        toggle_frame.grid(row=4, column=0, sticky="nsew", columnspan=3)
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")
        
class Main(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entry(self, "Label 1", "Button 1", "red")
        Entry(self, "Label 2", "Button 2", "blue")

class Entry(ctk.CTkFrame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text=label_text)
        button = ctk.CTkButton(self, text=button_text)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)
        self.pack(side="left", expand="True", fill="both", padx=20, pady=20)


# ------------------------------------ Run ----------------------------------- #
# Calling the App class
App("CTk App", (600,600))