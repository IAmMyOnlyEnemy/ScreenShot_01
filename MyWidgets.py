import tkinter as tk                # python 3
from tkinter import ttk             # python 3
from tkinter import font as tkfont  # python 3
from tkinter import filedialog      # python 3

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
        self.config(justify="left")
        self.config(font=("Monospace",10))
        self.config(background=label_setts[0])
        self.config(width=label_setts[1])
        self.config(textvariable=self.label_var)
        self.config(bg="Red")
        self.place(x=label_setts[2],y=label_setts[3])

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