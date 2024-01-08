# ---------------------------------------------------------------------------- #
#                             ttkboutstrap Widgets                             #
# ---------------------------------------------------------------------------- #

import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter


# ---------------------------------- Window ---------------------------------- #
window = ttk.Window(themename="darkly")
window.title("ttkb Widgets")


# ---------------------------------- Widgets --------------------------------- #
# Scrolled frame
scroll_frame = ScrolledFrame(window).pack()
'''
for i in range(100):
	frame = ttk.Frame(scroll_frame)
	ttk.Label(frame, text=f'Label: {i}').pack(fill ='x', side='left')
	ttk.Button(frame, text=f'Button: {i}').pack(fill='x', side='left')
	frame.pack(fill='x', expand=True)
'''

# Toast
toast = ToastNotification(
	title = 'This the title', 
	message = 'This is the message',
	duration = 2000,
	bootstyle = 'danger',
	alert=True,
	position = (50, 50, 'ne')
	)
ttk.Button(window, text='Show Toast', command=toast.show_toast, bootstyle="danger").pack(pady = 10)

# Tooltip
button = ttk.Button(window, text='Tooltip button', bootstyle='warning')
button.pack(pady=10)
ToolTip(button, text='⚠ This does something', bootstyle='warning-inverse')

# Calendar 
calendar = DateEntry(window).pack(pady=10)
ttk.Button(window, text='Get calendar date', command=(lambda: print(calendar.entry.get()))).pack()

# Progress -> Floodgauge
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(
	window, 
	text = 'Progress', 
	variable = progress_int,
	bootstyle = 'success',
	mask = 'Mask {}%'
	)
progress.pack(pady=10, fill='x')
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()

# Meter 
meter = ttk.Meter(
	window,
	amounttotal = 100,
	amountused = 10,
	interactive = True,
	metertype = 'semi',
	subtext = 'Text',
	bootstyle = 'info'
	)
meter.pack(pady=10)

# ------------------------------------ Run ----------------------------------- #
window.mainloop()