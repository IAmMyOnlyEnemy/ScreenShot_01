from tkinter import *
from tkinter import ttk
from import_settings import *

class main_frame(Tk):

	#def __doc__(self):
	"This is the class for main frame"

	global global_settings
	global_settings = get_settings()

	def __init__(self):
		super(main_frame,self).__init__()
		self.title("Main 05, AAAAAAAAA!")
		self.minsize(width=400, height=200)
		self.iconbitmap("Images\\zoom_01.ico")
		self.note = ttk.Notebook(self)
		self.note.pack()
		self.tab1 = Frame(self.note, width=400,height=200)
		self.tab1.pack(fill="both",expand=1)
		self.note.add(self.tab1, text="Print screen")
		self.tab1 = Frame(self.note, width=400,height=200)
		self.tab1.pack(fill="both",expand=1)
		self.note.add(self.tab1, text="Settings")

		self.tab2 = tab(self.note)
		#self.tab2.pack(fill="both",expand=1)
		self.note.add(self.tab2, text="KKKKKKKKKKK")
		print(type(self.tab2))

class tab(Frame):

	"This is the class for the frame displayed on a tab"

	def __init__(self,myNote=None):
		#self(width=400,height=200)
		#self.tab1 = Frame(self.note, width=400,height=200)
		self.pack(fill="both",expand=1)

if __name__ == "__main__":
	root = main_frame()
	root.mainloop()