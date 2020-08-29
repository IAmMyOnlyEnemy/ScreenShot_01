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

        self.pathentry=MyEntry(parent=self, entry_setts=[51, 10, 8])

        self.imglabel=MyLabel(parent=self, label_setts=[None, 15, "w", 10, 30])
        self.imglabel.config(justify=tk.LEFT)
        self.tso_option=tk.StringVar()
        self.tso_option.set(global_settings['TSO_option'][0])
        self.reslabel=MyLabel(parent=self, label_setts=[None, 18, "e", 245, 30])
        cics_radbutt = MyRadiobutt(parent=self,op_val=self.tso_option,val="CICS",pos_x=135)
        tso_radbutt = MyRadiobutt(parent=self,op_val=self.tso_option,val="TSO",pos_x=190)
        cics_radbutt.config(command=self.update_frame_res())
        tso_radbutt.config(command=self.update_frame_res())
        
        self.update_frame_res()
        '''
        self.reslabel.set_label(
                "{0} x {1} [{2}x{3}]".format(
                                    global_settings['CICS_dimmension'][0],
                                    global_settings['CICS_dimmension'][1],
                                    self.winfo_screenwidth(),
                                    self.winfo_screenheight())
                                )
        '''
        self.image_bbr = tk.PhotoImage(file="Images\\Browse_button.png")
        browse_button = tk.Button(self,
                            command=self.browse_command,
                            image=self.image_bbr,
                            text="Browse",
                            compound=tk.LEFT
                            ).place(x=322,y=3)
        self.image_bpic = tk.PhotoImage(file="Images\\Pic_button.png")
        print_button = tk.Button(self,
                            command=self.pic_cmd,
                            image=self.image_bpic,
                            text="PrintScreen",
                            compound=tk.TOP
                            ).place(x=297,y=90)
        up_button = tk.Button(self,
                            text="Up",
                            compound="center",
                            command=lambda: self.screenlist.move_up(),
                            width=3
                            ).place(x=10,y=170)
        down_button = tk.Button(self,
                            text="Dn",
                            compound="center",
                            command=lambda: self.screenlist.move_down(),
                            width=3
                            ).place(x=50,y=170)
        del_button = tk.Button(self,
                            text="Del",
                            compound="center",
                            command=lambda: self.screenlist.delete_item(),
                            width=4
                            ).place(x=170,y=170)

        self.screenlist = MyList(parent=self)
        self.screenlist.bind('<<ListboxSelect>>', self.onselect_listbox)
        self.screenlist.event_generate("<<ListboxSelect>>")

        num_vals = self.get_spin_vals(0)
        lett_vals = self.get_spin_vals(1)
        self.spin1 = MySpinbox(parent=self,spinvals=num_vals,pos_x=10)
        self.spin1.config(command=self.set_img_name)
        self.spin2 = MySpinbox(parent=self,spinvals=lett_vals,pos_x=50)
        self.spin2.config(command=self.set_img_name)
        self.spin3 = MySpinbox(parent=self,spinvals=num_vals,pos_x=170)
        self.spin3.config(command=self.set_img_name)

        self.checkbox1 = MyCheckbox(parent=self,pos_x=12)
        self.checkbox1.set_checkbox(global_settings['Checkbox_options'][0])
        self.checkbox2 = MyCheckbox(parent=self,pos_x=52)
        self.checkbox2.set_checkbox(global_settings['Checkbox_options'][1])
        self.checkbox3 = MyCheckbox(parent=self,pos_x=92)
        self.checkbox3.set_checkbox(global_settings['Checkbox_options'][2])
        self.checkbox4 = MyCheckbox(parent=self,pos_x=172)
        self.checkbox4.set_checkbox(global_settings['Checkbox_options'][3])

        self.listentry=MyEntry(parent=self, entry_setts=[12, 90, 175])
        self.listentry.set_entry(self.screenlist.get_selected())
        self.set_img_name()
        print(len(self.screenlist.cget('listvariable')))

    def browse_command(self):
        folder_path = filedialog.askdirectory(
            title="Select where to save the images",
            initialdir=self.pathentry.get_entry()
            )
        if folder_path != "":
            self.pathentry.set_entry(folder_path)

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
        img.save(self.pathentry.get_entry() + '\\' + 
                self.imglabel.get_label() + ".jpg", "jpeg")

        if self.checkbox1.get_checkbox():
            self.spin1.spinNext()
        if self.checkbox2.get_checkbox():
            self.spin2.spinNext()
        if self.checkbox4.get_checkbox():
            self.spin3.spinNext()

        self.set_img_name()

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

    def get_img_name(self):
        return (self.spin1.get_spin() + 
                self.spin2.get_spin() + "_" +
                self.screenlist.get_selected() + "_" +
                self.spin3.get_spin()
                )

    def set_img_name(self):
        self.imglabel.set_label(self.get_img_name())

    def onselect_listbox(self, evt):
        self.set_img_name()
        self.listentry.set_entry(self.screenlist.get_selected())

    def update_frame_res(self):
        print(global_settings[self.tso_option.get() + '_dimmension'][0])
        print(global_settings[self.tso_option.get() + '_dimmension'][1])
        self.reslabel.set_label(
                "{0} x {1} [{2}x{3}]".format(
                                    global_settings[self.tso_option.get() + '_dimmension'][0],
                                    global_settings[self.tso_option.get() + '_dimmension'][1],
                                    self.winfo_screenwidth(),
                                    self.winfo_screenheight())
                                )

class MyEntry(tk.Entry):
    def __init__(self,parent,entry_setts):
        tk.Entry.__init__(self,parent)
        self.entry_var = tk.StringVar()
        self.entry_var.set(global_settings['save_path'][0])
        self.config(justify=tk.LEFT)
        self.config(textvariable=self.entry_var)
        self.config(width=entry_setts[0])
        self.place(x=entry_setts[1],y=entry_setts[2])

    def set_entry(self, new_text):
        self.entry_var.set(new_text)

    def get_entry(self):
        return self.entry_var.get()

class MyLabel(tk.Label):
    def __init__(self,parent,label_setts):
        tk.Label.__init__(self,parent)
        self.label_var = tk.StringVar()
        self.config(justify=tk.LEFT)
        self.config(font=("Monospace",10))
        self.config(background=label_setts[0])
        self.config(width=label_setts[1])
        self.config(anchor=label_setts[2])
        self.config(textvariable=self.label_var)
        self.config(bg="Red")
        self.place(x=label_setts[3],y=label_setts[4])

    def set_label(self, new_text):
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
        self.config(width=6)
        self.config(indicator = 0)
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
        self.check_scrollbar()
        self.place(x=90,y=80)

    def get_selected(self):
        return self.get(self.curselection())

    def insert_new(self,newitem):
        print("Insert new value in list")
        self.insert(tk.END, newitem)
        self.check_scrollbar()

    def move_up(self):
        print("Move selected value up")

    def move_down(self):
        print("Move selected value down")

    def delete_item(self):
        print("Delete this item")
        self.check_scrollbar()

    def check_scrollbar(self):
        print("Check if a scrollbar is needed or not")

class MySpinbox(tk.Spinbox):
    def __init__(self,parent=None,spinvals=None,pos_x=0):
        tk.Spinbox.__init__(self,parent)
        self.spin_var = tk.StringVar()
        self.config(textvariable=self.spin_var)
        self.config(values=spinvals)
        self.config(width=3)
        self.config(justify="center")
        self.config(bg="Green")
        self.place(x=pos_x,y=80)

    def spinNext(self):
        next_idx = self.spin_var.get()
        try:
            if self.spin_var.get() == "25":
                pass
            else:
                next_idx = str(int(self.spin_var.get()) + 1)
                if len(next_idx) == 1:
                    next_idx = "0" + next_idx
        except ValueError:
            try:
                if self.spin_var.get() == "Z":
                    pass
                else:
                    next_idx=chr(ord(self.spin_var.get()) + 1)
            except:
                pass
        self.spin_var.set(next_idx)

    def spinPrev(self):
        prev_idx = self.spin_var.get()
        try:
            if self.spin_var.get() == "01":
                pass
            else:
                prev_idx = str(int(self.spin_var.get()) - 1)
                if len(prev_idx) == 1:
                    prev_idx = "0" + prev_idx
        except ValueError:
            try:
                if self.spin_var.get() == "A":
                    pass
                else:
                    prev_idx=chr(ord(self.spin_var.get()) - 1)
            except:
                pass
        self.spin_var.set(prev_idx)

    def get_spin(self):
        return self.spin_var.get()

class MyCheckbox(tk.Checkbutton):
    def __init__(self,parent=None,pos_x=0):
        tk.Checkbutton.__init__(self,parent)
        self.checkbox_var = tk.IntVar()
        self.config(variable=self.checkbox_var)
        self.config(onvalue=1)
        self.config(offvalue=0)
        self.config(bg="Blue")
        self.place(x=pos_x,y=53)

    def get_checkbox(self):
        if self.checkbox_var.get() == 1:
            return True
        else:
            return False

    def set_checkbox(self,myvar):
        self.checkbox_var.set(myvar)

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