# ---------------------------------------------------------------------------- #
#                                   Treeview                                   #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk
from random import choice
import names

emails_domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'orange.fr', 'live.com', 'web.de', 'yandex.ru']


# ----------------------------------- Setup ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("Treeview")
window.geometry("600x400")


# --------------------------------- Treeview --------------------------------- #
table = ttk.Treeview(
    master = window,
    columns = ("first", "last", "email"),
    show = "headings"
    )
table.heading("first", text="First name")
table.heading("last", text="Surname")
table.heading("email", text="Email")
table.pack(fill="both", expand=True)

# Insert values in table
#table.insert(parent="", index=0, values=("John", "Doe", "JohnDoe@email.com"))
for i in range (100):
    random_first = names.get_first_name()
    random_last = names.get_last_name()
    random_email = f"{random_first}{random_last}@{choice(emails_domains)}"
    random_data = (random_first, random_last, random_email)
    table.insert(parent="", index=0, values=random_data)


# ------------------------------------ Run ----------------------------------- #
window.mainloop()