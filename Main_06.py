import tkinter as tk                # python 3
from tkinter import ttk             # python 3
from tkinter import font as tkfont  # python 3
from tkinter import filedialog
from PIL import ImageGrab
from import_settings import *

class SampleApp(tk.Tk):

    global global_settings
    global_settings = get_settings()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Main 06, sper ca e bine...")
        self.minsize(width=global_settings["form_dimensions"][0],
                    height=global_settings["form_dimensions"][1])
        self.wm_iconbitmap("Images\\zoom_01.ico")
        self.title_font = tkfont.Font(family='Helvetica',size=12,weight="bold",slant="italic")
        container = ttk.Notebook(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (PrintScreen, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            container.add(frame, text=page_name)

        self.show_frame("PrintScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        print(page_name)

class PrintScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        pathentry_sets = [51, 10, 8]
        self.pathentry=MyEntry(parent=self, entry_setts=pathentry_sets)
        self.pathentry.entry_var.set(global_settings['save_path'][0])

        imglabel_sets = [None, 15, 10, 30]
        self.imglabel=MyLabel(parent=self, label_setts=imglabel_sets)
        self.imglabel.update_label("img_Label")
        #imglabel.update_label(screen_list.get(ANCHOR))
        self.tso_option=tk.StringVar()
        self.tso_option.set(global_settings['TSO_option'][0])
        cics_radbutt = MyRadiobutt(parent=self,op_val=self.tso_option,val="CICS",pos_x=130)
        tso_radbutt = MyRadiobutt(parent=self,op_val=self.tso_option,val="TSO",pos_x=190)

        reslabel_sets = [None, 19, 245, 30]
        reslabel=MyLabel(parent=self, label_setts=reslabel_sets)
        reslabel.update_label(
                "{0} x {1} [{2}x{3}]".format(
                                    global_settings['CICS_dimmension'][0],
                                    global_settings['CICS_dimmension'][1],
                                    "1900",
                                    "1080")
                                )
        self.image_bbr = tk.PhotoImage(file="Images\\Browse_button.png")
        browse_button = tk.Button(self,
                            command=lambda: self.browse_command(self.pathentry),
                            image=self.image_bbr,
                            text="Browse",
                            compound=tk.LEFT
                            ).place(x=322,y=3)
        self.image_bpic = tk.PhotoImage(file="Images\\Pic_button.png")#.subsample(1,1)
        print_button = tk.Button(self,
                            command=self.pic_cmd,
                            image=self.image_bpic,
                            text="PrintScreen",
                            compound=tk.TOP
                            ).place(x=297,y=90)
        up_button = tk.Button(self,
                            text="Up",
                            compound="center",
                            width=3
                            ).place(x=10,y=170)
        down_button = tk.Button(self,
                            text="Dn",
                            compound="center",
                            width=3
                            ).place(x=50,y=170)
        del_button = tk.Button(self,
                            text="Del",
                            compound="center",
                            width=4
                            ).place(x=170,y=170)

        screenlist = MyList(parent=self)
        print(screenlist.get_selected())

        num_vals = self.get_spin_vals(0)
        lett_vals = self.get_spin_vals(1)
        spin1 = MySpinbox(parent=self,spinvals=num_vals,pos_x=10)
        spin2 = MySpinbox(parent=self,spinvals=lett_vals,pos_x=50)
        spin3 = MySpinbox(parent=self,spinvals=num_vals,pos_x=170)

        checkbox1 = MyCheckbox(parent=self,pos_x=12)
        checkbox2 = MyCheckbox(parent=self,pos_x=52)
        checkbox3 = MyCheckbox(parent=self,pos_x=92)
        checkbox4 = MyCheckbox(parent=self,pos_x=172)

        listentry_sets = [12, 90, 175]
        listentry=MyEntry(parent=self, entry_setts=listentry_sets)
        listentry.entry_var.set(screenlist.get_selected())

    def browse_command(self,entry1):
        folder_path = filedialog.askdirectory(
            title="Select where to save the images",
            initialdir=entry1.get_entry()
            )
        if folder_path != "":
            entry1.update_entry(folder_path)

    def update_label1(self,str1):
        imglabel.update_label(str1)
        print(str1)

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

    def pic_cmd(self):
        img = ImageGrab.grab(bbox=self.img_frame())
        print(self.pathentry.get_entry())
        print(self.imglabel.get_label())
        img.save(self.pathentry.get_entry() + '\\' + 
                self.imglabel.get_label() + ".jpg", "jpeg")
        #next_idx = str(int(self.s3_var.get()) + 1)
        #print(int(self.s3_var.get()))
        #if len(next_idx) == 1:
        #    next_idx = "0" + next_idx
        #self.s3_var.set(next_idx)
        #self.img_label_change()

    def img_frame(self):
        res_x = self.winfo_screenwidth()
        res_y = self.winfo_screenheight()
        if self.tso_option.get() == "CICS":
            x = (res_x - global_settings['CICS_dimmension'][0]) / 2
            y = (res_y - global_settings['CICS_dimmension'][1]) / 2
        else:
            x = (res_x - global_settings['TSO_dimmension'][0]) / 2
            y = (res_y - global_settings['TSO_dimmension'][1]) / 2
        frame = (x, y, res_x - x, res_y - y )
        return frame

class MyEntry(tk.Entry):
    def __init__(self,parent,entry_setts):
        tk.Entry.__init__(self,parent)
        self.entry_var = tk.StringVar()
        self.entry_var.set("")
        self.config(justify="left")
        self.config(textvariable=self.entry_var)
        self.config(width=entry_setts[0])
        self.place(x=entry_setts[1],y=entry_setts[2])

    def update_entry(self, new_text):
        self.entry_var.set(new_text)

    def get_entry(self):
        return self.entry_var.get()

class MyLabel(tk.Label):
    def __init__(self,parent,label_setts):
        tk.Label.__init__(self,parent)
        self.label_var = tk.StringVar()
        self.config(justify="left")
        self.config(font=("Monospace",10))
        self.config(background=label_setts[0])
        self.config(width=label_setts[1])
        self.config(textvariable=self.label_var)
        self.config(bg="Red")
        self.place(x=label_setts[2],y=label_setts[3])

    def update_label(self, new_text):
        self.label_var.set(new_text)

    def get_label(self):
        return self.label_var.get()

class MyRadiobutt(tk.Radiobutton):
    def __init__(self,parent=None,op_val=None,val="",pos_x=0):
        tk.Radiobutton.__init__(self,parent)
        self.config(bg="White")
        self.config(text=val)
        self.config(variable=op_val)
        self.config(value=val)
        self.place(x=pos_x,y=28)

    def set_active(self,activetext):
        self.tso_option.set(activetext)

class MyList(tk.Listbox):
    def __init__(self,parent):
        tk.Listbox.__init__(self,parent)
        self.config(exportselection=0)
        self.config(font=("Monospace",10))
        self.config(selectmode=tk.SINGLE),
        self.config(height=len(global_settings["screen_list"]))
        self.config(width=10)
        for i, item in enumerate(global_settings["screen_list"]):
            self.insert(tk.END, item)
        self.select_set(0)
        self.place(x=90,y=80)

    def get_selected(self):
        return self.get(self.curselection())

class MySpinbox(tk.Spinbox):
    def __init__(self,parent=None,spinvals=None,pos_x=0):
        tk.Spinbox.__init__(self,parent)
        self.config(values=spinvals)
        self.config(width=3)
        self.config(justify="center")
        self.config(bg="Green")
        self.place(x=pos_x,y=80)

    def spinNext(self):
        print("Spin next!")

    def spinPrev(self):
        print("Spin previous!")

    def getspin(self):
        print("This should be the value of spin")

class MyCheckbox(tk.Checkbutton):
    def __init__(self,parent=None,pos_x=0):
        tk.Checkbutton.__init__(self,parent)
        #self.config(text="")
        self.config(onvalue=1)
        self.config(offvalue=0)
        self.config(bg="Blue")
        self.place(x=pos_x,y=53)

class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("PrintScreen"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()