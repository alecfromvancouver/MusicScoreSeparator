from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Music Score Separator")

content = ttk.Frame(root, padding=(0, 0))

score_frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=340, height=440)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
score_frame.grid(column=0, row=1, columnspan=6, rowspan=3, sticky=(N, S, E, W))
namelbl.grid(column=0, row=0)
name.grid(column=1, row=0, columnspan=6, sticky=W)
cancel.grid(column=3, row=0, columnspan=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()