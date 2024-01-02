import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_str.set(f"{km_output} Km")

# Window
#window = tk.Tk() # Create normal tk window
window = ttk.Window(themename="journal") # Create window with ttkbootstrap
window.title("Test")
window.geometry('300x150')

# title
title_label = ttk.Label(master=window, text="Miles To Kilometers", font="Calibri 24 bold")
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=5)
button.pack(side="left")
input_frame.pack(pady=10)

# Output
output_str = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font="Calibri 20", textvariable=output_str)
output_label.pack(pady=5)

# Run
window.mainloop()