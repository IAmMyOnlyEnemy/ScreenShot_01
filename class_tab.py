from tkinter import *
from tkinter import ttk
from import_settings import *
from entries import *
from tkinter import filedialog

global global_settings
global_settings = get_settings()

def create_tab(my_note):
	frame1 = Frame(my_note, width=400,height=200)
	frame1.pack(fill="both",expand=1)
	return frame1

def image_tab(ntbk):
	my_tab = create_tab(ntbk)
	path_entry = entry1(my_tab)
	browse_button = button1(my_tab)
	return my_tab

def button1(tab):
	image_bbr = PhotoImage(file="Images\\folder_icon2.png")
	my_button = ttk.Button(tab,
							command=browse_cmd(),
							image=image_bbr,
							width=5)
	my_button.place(x=360,y=5)
	return my_button

def browse_cmd(path_var):
	folder_path = filedialog.askdirectory(
		title="Select where to save the images",
		initialdir=path_var.get()
		)
	if folder_path != "":
		path_var.set(folder_path)

def entry1(tab):
	path_var=StringVar()
	path_var.set(global_settings['save_path'][0])
	print(global_settings['save_path'])
	print(path_var.get())
	my_entry = ttk.Entry(tab,
						justify="left",
						textvariable=path_var,
						width=55
						)
	my_entry.place(x=10,y=8)

	return my_entry

def setting_tab(ntbk):
	tab1 = create_tab(ntbk)
	return tab1
