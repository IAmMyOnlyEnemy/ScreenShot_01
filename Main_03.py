from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pathlib
import pyautogui

class main_frame(Tk):
	def __init__(self):
		#----------- root -----------------
		super(main_frame,self).__init__()
		self.title("Main 03, upgrade!")
		self.minsize(width=400, height=200)
		self.wm_iconbitmap("Images\\zoom_01.ico")
		#----------- path entry -----------
		self.path_var=StringVar()
		self.path_var.set(pathlib.Path().absolute())
		self.path_entry(self.path_var)
		#----------- path button ----------
		self.browse_butt()
		#----------- resolution label -----
		self.dim_var=StringVar()
		self.dim_var.set("1800x4000 [1900x1080]")
		self.dim_label(self.dim_var)
		#----------- radiobutton option ---
		self.tso_option=StringVar()
		self.tso_option.set("CICS")
		self.tso_radbut(self.tso_option,"CICS",130)
		self.tso_radbut(self.tso_option,"TSO",190)
		#----------- spinboxes ------------
		self.s1_var = StringVar()
		self.s1_var.set("01")
		self.spinBox(self.s1_var, self.get_spin_vals(0), 10)
		self.s2_var = StringVar()
		self.s2_var.set("A")
		self.spinBox(self.s2_var, self.get_spin_vals(1), 50)
		self.s3_var = StringVar()
		self.s3_var.set("01")
		self.spinBox(self.s3_var, self.get_spin_vals(0), 167)
		#----------- resolution label -----
		self.list_var = StringVar()
		self.list_var.set("CONT")
		self.listBox()
		#----------- picture name label ---
		self.img_value = StringVar()
		self.img_label_change()
		self.img_label()
		#----------- picture button -------
		self.pic_butt()
		#----------- end ------------------

	def pic_cmd(self):
		if self.tso_option.get() == "CICS":
			self.tso_option.set("TSO")
		else:
			self.tso_option.set("CICS")

		myScreenshot = pyautogui.screenshot()
		myScreenshot.save(self.path_var.get() +
							'\\' + 
							self.img_value.get() +
							'.jpg')
		#self.s3_w.invoke('buttonup')
		#self.s1_var.set("01")
		#self.s2_var.set("A")
		#self.s3_var.set("01")

	def pic_butt(self):
		self.image_bpic = PhotoImage(file="Images\\icons8-screenshot-64.png")
		self.pic_button = ttk.Button(self,
										command=self.pic_cmd,
										image=self.image_bpic,
										#text="Picture",
										#compound="left",
										width=10)
		self.pic_button.place(x=317,y=63)

	def img_label_change(self):
		self.img_value.set(self.s1_var.get() + 
							self.s2_var.get() + "_" + 
							self.screen_list.get(ANCHOR) + "_" +
							self.s3_var.get())

	def img_label(self):
		self.img_label_w = ttk.Label(self,
									width=15,
									font=("Monospace",10),
									justify="left",
									textvariable=self.img_value)
		self.img_label_w.place(x=10,y=35)

	def listBox(self):
		self.screen_list = Listbox(self,
								listvariable=self.list_var,
								exportselection=0,
								selectmode=SINGLE,
								font=("Monospace",10),
								height=4,
								width=10)
		self.screen_list.insert(0, "CONT")
		self.screen_list.insert(1, "SAVE")
		self.screen_list.insert(2, "TREC")
		self.screen_list.insert(3, "TBLT")
		self.screen_list.place(x=90,y=65)

	def spinBox(self, var, vals, pos_x):
		self.spin_w = ttk.Spinbox(self,
								values=vals,
								width=3,
								textvariable=var,
								command=self.img_label_change,
								justify="center")
		self.spin_w.place(x=pos_x,y=65)

	def get_spin_vals(self,vals_type):
		vals = []
		if vals_type == 1:
			for i in range(65, 91):
				vals.append(chr(i))
		else:
			for i in range(1, 26):
				if i<10:
					vals.append("0" + str(i))
				else:
					vals.append(str(i))
		return vals

	def tso_radbut(self, op_val, text_val, pos_x):
		self.tso_radbut_w = ttk.Radiobutton(self,
											text=text_val,
											variable=op_val,
											value=text_val)
		self.tso_radbut_w.place(x=pos_x,y=35)

	def dim_label(self,dim_value):
		self.dim_label_w = ttk.Label(self,
									width=21,
									font=("Monospace",10),
									justify="right",
									textvariable=dim_value)
		self.dim_label_w.place(x=255,y=35)

	def browse_butt(self):
		self.image_bbr = PhotoImage(file="Images\\folder_icon2.png")
		self.br_button = ttk.Button(self,
										command=self.browse_cmd,
										image=self.image_bbr,
										#text="Browse", 
										#compound="left",
										width=5)
		self.br_button.place(x=360,y=5)

	def browse_cmd(self):
		folder_path = filedialog.askdirectory()
		if folder_path != "":
			self.path_var.set(folder_path)

	def path_entry(self, str_path):
		self.path_entry_w = ttk.Entry(self,
							justify="left",
							textvariable=str_path,
							width=55)
		self.path_entry_w.place(x=10,y=8)

if __name__ == "__main__":
	root = main_frame()
	root.mainloop()