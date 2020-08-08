from tkinter import *
from tkinter import ttk
from class_tab import *
from import_settings import *

class main_frame(Tk):

	#img_tab = tab()
	#setting_tab = tab()

	global settings
	settings = {}

	class my_notebook:
		print("aaaaa")

	class settings_parameters:
		print("vvvvv")

	def __init__(self):
		#----------- root -----------------
		super(main_frame,self).__init__()
		self.title("Main 04, upgrade!")
		self.minsize(width=400, height=200)
		self.iconbitmap("Images\\zoom_01.ico")
		my_not = ttk.Notebook(self)
		my_not.pack()
		self.tab1 = tab(my_not)
		self.tab2 = tab(my_not)
		my_not.add(self.tab1, text="Print screen")
		my_not.add(self.tab2, text="Settings")

