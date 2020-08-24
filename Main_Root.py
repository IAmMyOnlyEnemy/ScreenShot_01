from tkinter import *
from tkinter import ttk
from class_tab import *

class main_frame(Tk):
	
	def create_notebook(Tk):
		notebook1 = ttk.Notebook(Tk)
		notebook1.pack()

		tab1 = image_tab(notebook1)
		notebook1.add(tab1, text="Print screen")

		tab1 = setting_tab(notebook1)
		notebook1.add(tab1, text="Settings")
		
		return notebook1

	def __init__(self):
		#----------- root ---------------------------
		super(main_frame,self).__init__()
		self.title("Main 04, upgrade!")
		self.minsize(width=400, height=200)
		self.iconbitmap("Images\\zoom_01.ico")
		# - Create the notebook for tabs: - #
		#my_not = self.create_notebook()