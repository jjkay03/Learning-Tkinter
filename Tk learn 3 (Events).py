import tkinter as tk
import ttkbootstrap as ttk

'''
LIST OF EVENTS:
https://www.pythontutorial.net/tkinter/tkinter-event-binding/
'''

# --------------------------------- Functions -------------------------------- #
def get_pos(event):
    print(f"EVENT 3: X:{event.x} / Y:{event.y}")


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="superhero")
window.title("Events")
window.geometry("600x500")


# ---------------------------------- Widgets --------------------------------- #
text = ttk.Text(window); text.pack()
entry = ttk.Entry(window); entry.pack()
button = ttk.Button(master=window, text="Button"); button.pack()


# ---------------------------------- Events ---------------------------------- #
# Event trigers when Alt+A is pressed while on the window
window.bind(
    sequence = "<Alt-KeyPress-a>",
    func = (lambda event: print(f"EVENT 1:\n{event}"))
)

# Event trigers when any key is pressed while on the window
window.bind(
    sequence = "<KeyPress>",
    func = (lambda event: print(f"EVENT 2: Key pressed ({event.char})"))
)

# Events trigers when moving cursor on the text widget
text.bind(sequence="<Motion>", func=get_pos)

# Events trigers when entry widget is selected
entry.bind(
    sequence = "<FocusIn>",
    func = (lambda event: print("EVENT 4: Entry field selected!"))
)

# Events trigers when entry widget is unselected
entry.bind(
    sequence = "<FocusOut>",
    func = (lambda event: print("EVENT 5: Entry field unselected!"))
)

# Event trigers when user holds down shift and uses the mousewheel while text widget is selected
text.bind(
    sequence = "<Shift-MouseWheel>",
    func = (lambda event: print("EVENT 5: Mouswheel!"))
)

# ------------------------------------ Run ----------------------------------- #
window.mainloop()