# ---------------------------------------------------------------------------- #
#                               Multiple Windows                               #
# ---------------------------------------------------------------------------- #

# Info about messagebox: https://docs.python.org/3/library/tkinter.messagebox.html

import tkinter as tk
from tkinter import ttk, messagebox


# --------------------------------- Functions -------------------------------- #
def ask_yes_no():
    answer = messagebox.askquestion("Title", "Budy")
    print(f"MESSAGEBOX ANSWER: {answer}")
    # messagebox.showinfo("Title", "Some info!")
    # messagebox.showerror("Title", "Some info!")

def create_window():
    global extra_window
    extra_window = tk.Toplevel()  # Create an "extra" window
    extra_window.title("Extra window")
    extra_window.geometry("300x400")
    ttk.Label(extra_window, text="THIS IS A NEW WINDOW!").pack(expand=True)

def close_window():
    extra_window.destroy()


# ---------------------------------- Window ---------------------------------- #
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

button1 = ttk.Button(window, text='Open extra window', command=create_window).pack(expand=True)
button2 = ttk.Button(window, text='Close extra window', command=close_window).pack(expand=True)
button3 = ttk.Button(window, text = 'Create yes no window', command=ask_yes_no).pack(expand=True)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()