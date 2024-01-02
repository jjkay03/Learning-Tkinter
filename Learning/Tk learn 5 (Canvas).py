# ---------------------------------------------------------------------------- #
#                                    Canvas                                    #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="flatly")
window.title("Canvas")
window.geometry("600x400")


# ---------------------------------- Canvas ---------------------------------- #
canvas = ttk.Canvas(
    master = window,
    bg = "white"
    )
canvas.pack()

#canvas.create_rectangle((0, 0, 100, 200), fill="red", width=10, dash=(4,2,1,1), outline="green")
#canvas.create_oval((200, 0, 300, 100), fill="green")
#canvas.create_line((0, 0, 100, 150), fill="blue")

#canvas.create_text((100, 250), text="THIS IS TEXT!")

#canvas.create_window((50, 100), window= ttk.Label(window, text="THIS IS TEXT IN A LABEL"))


# --------------------------------- Functions -------------------------------- #
brush_size = 2

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x-brush_size/2, y-brush_size/2, x+brush_size/2, y+brush_size/2), fill="black")

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 1
    else:
        brush_size -= 1
    brush_size = max(0, min(brush_size, 50))  # Set max and min size


# ---------------------------------- Events ---------------------------------- #
# Draw on canvas when movin cursor
canvas.bind(
    sequence = "<Motion>",
    func = draw_on_canvas
)

# Change brush size when scrolling mouse wheel
canvas.bind(
    sequence = "<MouseWheel>",
    func = brush_size_adjust
)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()