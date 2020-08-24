from tkinter import *
from tkinter import ttk
import pathlib

def path_entry(my_base):
	path_var=StringVar()
	path_var.set(pathlib.Path().absolute())
	path_entry_w = ttk.Entry(my_base,
							justify="left",
							textvariable=path_var,
							width=55
							)
	path_var.set("asdfsaf")
	path_entry_w.place(x=10,y=8)
	return path_entry_w