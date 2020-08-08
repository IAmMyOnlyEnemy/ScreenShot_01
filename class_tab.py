from tkinter import *
from tkinter import ttk

def tab(my_note):
	#my_note = ttk.Notebook()
	my_frame = Frame(my_note, width=500,height=500)
	my_frame.pack(fill="both",expand=1)
	return my_frame