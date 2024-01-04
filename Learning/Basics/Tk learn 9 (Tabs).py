# ---------------------------------------------------------------------------- #
#                                     Tabs                                     #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Tabs")
window.geometry("600x400")


# ------------------------------ Notebook Widget ----------------------------- #
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text="TAB 1")
notebook.add(tab2, text="TAB 2")
notebook.add(tab3, text="TAB 3")
notebook.pack()


# ---------------------------------- Widgets --------------------------------- #
# In tab 1
label1 = ttk.Label(tab1, text="Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

# In tab 2
label2 = ttk.Label(tab2, text="Text in tab 2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# In tab 3
button3_1 = ttk.Button(tab3, text="Button in tab 3")
button3_1.pack()
button3_2 = ttk.Button(tab3, text="Button' in tab 3")
button3_2.pack()
label3 = ttk.Label(tab3, text="Text in tab 3")
label3.pack()

# ------------------------------------ Run ----------------------------------- #
window.mainloop()