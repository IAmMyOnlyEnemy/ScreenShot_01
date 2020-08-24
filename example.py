import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import time
import sqlite3
conn = sqlite3.connect('developers.db')
cursor = conn.cursor()
class Frame_Functions(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self)
    def exit(self):
        self.AreYouSure = tk.messagebox.askquestion('Exit the Application?', 'Are you sure you want to exit the application?', icon='warning')
        if self.AreYouSure == 'yes':
            self.master.destroy()
    def tick(self):
        self.time2 = time.strftime('%H:%M:%S')
        self.clock.config(text=self.time2)
        self.clock.after(200, self.tick)
    def back(self):
        self.master.change(Menu_Application)
class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = Login_Screen(self)
        self.frame['bg'] = '#222'
        self.frame.pack(fill=BOTH, expand=1)
    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame['bg'] = '#222'
        self.frame.pack(fill=BOTH, expand=1)
class Login_Screen(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.iconbitmap('icon.ico')
        master.title('Login Screen')
        center_window(450, 250)
        master.resizable(False, False)
        master.configure(background='#222')
        self.title_lbl = tk.Label(self, text='LOGIN', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.user_lbl = tk.Label(self, text='User:', font=('Calibri', 15, 'bold'), bg='#222', fg='#54ff9f').place(x=30, y=85)
        self.user_tb = tk.Entry(self, width=20, border=0, bg='#eee')
        self.user_tb.place(x=90, y=93)
        self.pass_lbl = tk.Label(self, text='Pass:', font=('Calibri', 15, 'bold'), bg='#222', fg='#54ff9f').place(x=30, y=125)
        self.pass_tb = tk.Entry(self, show='*', width=20, border=0, bg='#eee')
        self.pass_tb.place(x=90, y=133)
        self.check_btn = tk.Button(self, text='ENTER', font=('Calibri', 16, 'bold'), border=0, width=10, bg='#54ff9f', activebackground='#28ae7b', command=self.check)
        self.check_btn.place(x=290, y=100)
        self.clock = tk.Label(self, font=('Calibri', 40, 'bold'), bg='#222', fg='#54ff9f')
        self.clock.pack(side=BOTTOM)
        self.exit_btn = tk.Button(self, text='Exit', font=('Calibri', 14, 'bold'), border=0, width=4, bg='#54ff9f', activebackground='#28ae7b', command=self.exit)
        self.exit_btn.place(x=0, y=200)
        self.tick()
    def check(self, event=None):
        user_get = self.user_tb.get()
        pass_get = self.pass_tb.get()
        cursor.execute('SELECT * FROM registered')
        for line in cursor.fetchall():
            if user_get == line[1] and pass_get == line[2]:
                self.master.change(Menu_Application)
                break
        else:
            self.user_tb.delete('0', tk.END)
            self.pass_tb.delete('0', tk.END)
            self.error = tk.messagebox.showerror('Error', 'Invalid username or password')
class Menu_Application(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('Menu')
        center_window(500, 500)
        master.configure(background='#222')
        self.title_lbl = tk.Label(self, text='OPTIONS MENU', font=('Calibri', 25, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.database_btn = tk.Button(self, text='DATABASE', font=('Calibri', 20, 'bold'), pady=5, bg='#54ff9f', width=15, activebackground='#28ae7b', border=0, command=self.open_database)
        self.database_btn.place(x=20, y=90)
        self.games_btn = tk.Button(self, text='GAMES', font=('Calibri', 20, 'bold'), pady=5, bg='#54ff9f', width=15, activebackground='#28ae7b', border=0, command=self.open_game_menu)
        self.games_btn.place(x=20, y=180)
        self.chatbot_btn = tk.Button(self, text='COMMAND BOT', font=('Calibri', 20, 'bold'), pady=5, bg='#54ff9f', width=15, activebackground='#28ae7b', border=0, command=self.open_chatbot)
        self.chatbot_btn.place(x=260, y=90)
        self.notepad_btn = tk.Button(self, text='NOTEPAD', font=('Calibri', 20, 'bold'), pady=5, bg='#54ff9f', width=15, activebackground='#28ae7b', border=0, command=self.open_notepad)
        self.notepad_btn.place(x=260, y=180)
        self.calculator_btn = tk.Button(self, text='CALCULATOR', font=('Calibri', 20, 'bold'), pady=5, bg='#54ff9f', width=15, activebackground='#28ae7b', border=0, command=self.open_calculator)
        self.calculator_btn.place(x=20, y=270)
        self.clock = tk.Label(self, font=('Calibri', 40, 'bold'), bg='#222', fg='#54ff9f')
        self.clock.pack(side=BOTTOM)
        self.exit_btn = tk.Button(self, text='Exit', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.exit)
        self.exit_btn.place(x=445, y=410)
        self.logout_btn = tk.Button(self, text='Logout', font=('Calibri', 14, 'bold'), border=0, width=7, bg='#54ff9f', activebackground='#28ae7b', command=self.logout)
        self.logout_btn.place(x=0, y=410)
        self.tick()
    def logout(self):
        self.AreYouSure = tk.messagebox.askquestion('Logout?', 'Are you sure you want to logout?', icon='warning')
        if self.AreYouSure == 'yes':
            self.master.change(Login_Screen)
    def open_database(self):
        self.master.change(Database)
    def open_game_menu(self):
        self.master.change(Game_Menu)
    def open_chatbot(self):
        self.master.change(Chat_Bot)
    def open_notepad(self):
        self.master.change(Notepad)
    def open_calculator(self):
        self.master.change(Calculator)
class Database(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('DATABASE CONFIG')
        center_window(603, 570)
        self.title_lbl = tk.Label(self, text='DATABASE APPLICATION', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.user_lbl = tk.Label(self, text='User:', font=('Calibri', 15, 'bold'), bg='#222', fg='#54ff9f').place(x=30, y=85)
        self.user_tb = tk.Entry(self, width=20, border=0, bg='#eee')
        self.user_tb.place(x=90, y=93)
        self.pass_lbl = tk.Label(self, text='Pass:', font=('Calibri', 15, 'bold'), bg='#222', fg='#54ff9f').place(x=30, y=125)
        self.pass_tb = tk.Entry(self, show='*', width=20, border=0, bg='#eee')
        self.pass_tb.place(x=90, y=133)
        self.register_edit_btn = tk.Button(self, text='REGISTER & EDIT', font=('Calibri', 16, 'bold'), border=0, width=16, bg='#54ff9f', activebackground='#28ae7b', command=self.register_edit)
        self.register_edit_btn.place(x=330, y=100)
        self.info_btn = tk.Button(self, border=0, bg='#222', activebackground='#222', command=self.info)
        self.img_info = tk.PhotoImage(file='info.png')
        self.info_btn.config(image=self.img_info)
        self.info_btn.place(x=520, y=90)
        self.treeview = ttk.Treeview(self, columns=('#Username', '#Password'))
        self.treeview.heading('#0', text='ID')
        self.treeview.heading('#1', text='Username')
        self.treeview.heading('#2', text='Password')
        self.vsb = ttk.Scrollbar(self, orient='vertical', command=self.treeview.yview)
        self.vsb.place(x=585, y=225, height=200)
        self.treeview.configure(yscrollcommand=self.vsb.set)
        self.treeview.place(x=0, y=200)
        self.update()
        self.delete_btn = tk.Button(self, text='DELETE', font=('Calibri', 16, 'bold'), border=0, width=10, bg='#54ff9f', activebackground='#28ae7b', command=self.delete)
        self.delete_btn.place(x=250, y=440)
        self.unselect_btn = tk.Button(self, text='RESTORE', font=('Calibri', 10, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b', command=self.unselect)
        self.unselect_btn.place(x=541, y=179)
        self.search_lbl = tk.Label(self, text='Search:', font=('Calibri', 18, 'bold'), bg='#222', fg='#54ff9f').place(x=170, y=500)
        self.SEARCH = StringVar()
        self.search_tb = tk.Entry(self, width=20, border=0, bg='#eee', textvariable=self.SEARCH)
        self.search_tb.place(x=260, y=511)
        self.img_lupe = tk.PhotoImage(file='lupe.png')
        self.search_btn = tk.Button(self, border=2, bg='#222', activebackground='#222', command=self.search)
        self.search_btn.config(image=self.img_lupe)
        self.search_btn.place(x=390, y=504)
        self.exit_btn = tk.Button(self, text='Exit', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.exit)
        self.exit_btn.place(x=550, y=510)
        self.back_btn = tk.Button(self, text='Back', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.back)
        self.back_btn.place(x=0, y=510)
    def search(self):
        if self.SEARCH.get() != '''''':
            self.treeview.delete(*self.treeview.get_children())
            cursor.execute('SELECT * FROM `registered` WHERE `user` LIKE ?',
                           (str(self.SEARCH.get()),))
            fetch = cursor.fetchall()
            for data in fetch:
                self.treeview.insert('', 'end', text=data[0], values=(data[1], data[2]))
        self.search_tb.delete('0', tk.END)
    def update(self):
        self.treeview.delete(*self.treeview.get_children())
        for row in cursor.execute('SELECT rowid, * FROM registered').fetchall():
            self.treeview.insert('', 'end', text=row[0], values=(row[2], row[3]))
        self.user_tb.delete('0', tk.END)
        self.pass_tb.delete('0', tk.END)
    def info(self):
        self.info = messagebox.showinfo('Info', '''
        To register a user do not select any id in the database
        and to edit a user select it in the database.''')
    def register_edit(self):
        if not self.treeview.focus():
            user_get = self.user_tb.get()
            pass_get = self.pass_tb.get()
            if user_get == '' or pass_get == '':
                self.error = tk.messagebox.showerror('Error', 'Invalid Username or Password')
            else:
                try:
                    cursor.execute('''
                            INSERT INTO registered(user, pass)
                            VALUES (?, ?)
                            ''', (user_get, pass_get))
                    conn.commit()
                    self.sucess = messagebox.showinfo('Sucess', 'Registration done successfuly')
                except sqlite3.IntegrityError:
                    self.user_tb.delete('0', tk.END)
                    self.pass_tb.delete('0', tk.END)
                    self.error = tk.messagebox.showerror('Error', 'Username already used')
        else:
            user_get = self.user_tb.get()
            pass_get = self.pass_tb.get()
            selected_id = self.treeview.focus()
            rowid = self.treeview.item(selected_id)
            if user_get == '' or pass_get == '':
                self.error = tk.messagebox.showerror('Error', 'Invalid Username or Password')
            else:
                try:
                    cursor.execute('''
                        UPDATE registered
                        SET user = ?, pass = ?
                        WHERE rowid = ?
                        ''', (user_get, pass_get, rowid['text'],))
                    conn.commit()
                    self.sucess = messagebox.showinfo('Sucess', 'User edited successfully')
                except sqlite3.IntegrityError:
                    self.user_tb.delete('0', tk.END)
                    self.pass_tb.delete('0', tk.END)
                    self.error = tk.messagebox.showerror('Error', 'Username already used')
        self.update()
        self.search_tb.delete('0', tk.END)
    def delete(self):
        if not self.treeview.focus():
            messagebox.showerror('Error', 'No user selected')
        else:
            self.AreYouSure = tk.messagebox.askquestion('Delete this user?', 'Are you sure you want to delete this user?', icon='warning')
            if self.AreYouSure == 'yes':
                selected_id = self.treeview.focus()
                rowid = self.treeview.item(selected_id)
                try:
                    cursor.execute('DELETE FROM registered WHERE rowid=?', (rowid['text'],))
                except Exception:
                    self.error = tk.messagebox.showerror('Error', 'An error has occurred')
                    conn.rollback()
                else:
                    conn.commit()
                    self.sucess = messagebox.showinfo('Sucess', 'Deleted user successfully')
        self.update()
        self.search_tb.delete('0', tk.END)
    def unselect(self):
        self.treeview.delete(*self.treeview.get_children())
        for row in cursor.execute('SELECT rowid, * FROM registered').fetchall():
            self.treeview.insert('', 'end', text=row[0], values=(row[2], row[3]))
        self.search_tb.delete('0', tk.END)
        self.user_tb.delete('0', tk.END)
        self.pass_tb.delete('0', tk.END)
class Game_Menu(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('GAMES MENU')
        center_window(300, 470)
        self.title_lbl = tk.Label(self, text='GAMES MENU', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.hangman_game_btn = tk.Button(self, text='HANGMAN GAME', font=('Calibri', 16, 'bold'), border=0, width=20, bg='#54ff9f', activebackground='#28ae7b')
        self.hangman_game_btn.place(x=35, y=70)
        self.memory_game_btn = tk.Button(self, text='MEMORY GAME', font=('Calibri', 16, 'bold'), border=0, width=20, bg='#54ff9f', activebackground='#28ae7b')
        self.memory_game_btn.place(x=35, y=130)
        self.exit_btn = tk.Button(self, text='Exit', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.exit)
        self.exit_btn.place(x=244, y=400)
        self.back_btn = tk.Button(self, text='Back', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.back)
        self.back_btn.place(x=0, y=400)
class Hangman_Game(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('HANGMAN GAME')
        center_window(300, 300)
        self.title_lbl = tk.Label(self, text='HANGMAN GAME', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
class Memory_Game(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('MEMORY GAME')
        center_window(300, 300)
        self.title_lbl = tk.Label(self, text='MEMORY GAME', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
class Chat_Bot(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('COMMAND BOT')
        center_window(350, 600)
        self.title_lbl = tk.Label(self, text='COMMAND BOT', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.box = tk.Text(self, height=20, width=47, font=('Calibri', 11), state=DISABLED)
        self.vscroll = Scrollbar(self, orient=VERTICAL, command=self.box.yview)
        self.box['yscroll'] = self.vscroll.set
        self.vscroll.place(x=332, y=70.4, height=363.5)
        self.box.place(x=0, y=69.5)
        self.box.configure(state='normal', wrap=WORD)
        self.box.insert(INSERT, 'BOT: Wellcome to the command bot, if you need help write "!help".\n'+ '-'*65)
        self.box.configure(state='disabled')
        self.command_lbl = tk.Label(self, text='Command:', font=('Calibri', 13, 'bold'), bg='#222', fg='#54ff9f').place(x=20, y=450)
        self.command_tb = tk.Entry(self, width=20, border=0, bg='#eee')
        self.command_tb.place(x=110, y=457)
        self.command_btn = tk.Button(self, text='COMMIT', font=('Calibri', 12, 'bold'), border=0, width=9, bg='#54ff9f', activebackground='#28ae7b', command=self.commit)
        self.command_btn.place(x=250, y=450)
        self.clear_btn = tk.Button(self, text='CLEAR', font=('Calibri', 10, 'bold'), border=0, width=7, bg='#54ff9f', activebackground='#28ae7b', command=self.clear)
        self.clear_btn.place(x=294, y=49)
        self.exit_btn = tk.Button(self, text='Exit', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.exit)
        self.exit_btn.place(x=294, y=530)
        self.back_btn = tk.Button(self, text='Back', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.back)
        self.back_btn.place(x=0, y=530)
    def commit(self):
        self.commands=['!help', '!github', '!group', '!documentation', '!discord', '!dowload', '!lofi']
        self.efects=['', 'https://github.com/NormanDeveloper/Tkinter-Application', 'https://www.facebook.com/groups/python.brasil/', 'https://docs.python.org/3.7/', 'https://discord.gg/SUFa8y5', 'https://www.python.org/downloads/', '\nhttps://www.youtube.com/watch?v=yrmftUvH0x4&t=32s\nhttps://www.youtube.com/watch?v=K9u8zFVjX1g\nhttps://www.youtube.com/watch?v=EJew8Mvgau0&t=1611s']
        command = self.command_tb.get()
        if command not in self.commands:
            self.error = tk.messagebox.showerror('Error', 'Invalid Command')
        else:
            for i in range(len(self.commands)):
                if command == self.commands[i] and command != '!help':
                    self.box.configure(state='normal')
                    self.box.insert(INSERT, '\nUSER: '+command)
                    self.box.insert(INSERT, '\n\nBOT: ' + self.efects[i] + '\n' + '-' * 65)
                    self.box.see(tk.END)
                    self.box.configure(state='disabled')
            if command == '!help':
                self.box.configure(state='normal')
                self.box.insert(INSERT, '\nUSER: ' + command)
                self.box.insert(INSERT, '\n\nBOT: COMMANDS\n* ' + '\n* '.join(self.commands) + '\n' + '-' * 65)
                self.box.see(tk.END)
                self.box.configure(state='disabled')
        self.command_tb.delete('0', tk.END)
    def clear(self):
        self.box.configure(state='normal')
        self.box.delete('3.0', tk.END)
        self.box.configure(state='disabled')
class Notepad(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('NOTEPAD')
        center_window(400, 600)
        self.title_lbl = tk.Label(self, text='NOTEPAD', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.box = tk.Text(self, height=20, width=57, font=('Calibri', 11))
        self.box.place(x=0, y=70)
        self.archive_name_lbl = tk.Label(self, text='Archive Name', font=('Calibri', 14, 'bold'), pady=10, bg='#222', fg='#54ff9f').place(x=135, y=440)
        self.archive_name_tb = tk.Entry(self, width=15, font=('Calibri', 12))
        self.archive_name_tb.place(x=110, y=480)
        self.txt_lbl = Label(self, text='.txt', font=('Calibri', 14, 'bold'), bg='#222', fg='#54ff9f').place(x=242, y=476)
        self.info_btn = tk.Button(self, border=0, bg='#222', activebackground='#222')
        self.img_info = tk.PhotoImage(file='info.png')
        self.info_btn.config(image=self.img_info)
        self.info_btn.place(x=370, y=42)
        self.create_archive_btn = tk.Button(self, pady=5, text='CREATE ARCHIVE', font=('Calibri', 12, 'bold'), border=0, width=15, bg='#54ff9f', activebackground='#28ae7b', command=self.create)
        self.create_archive_btn.place(x=130, y=540)
        self.exit_btn = tk.Button(self, text='Exit', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.exit)
        self.exit_btn.place(x=350, y=510)
        self.back_btn = tk.Button(self, text='Back', font=('Calibri', 14, 'bold'), border=0, width=5, bg='#54ff9f', activebackground='#28ae7b', command=self.back)
        self.back_btn.place(x=0, y=510)
    def create(self):
        box_get = self.box.get('1.0', END)
        name_get = self.archive_name_tb.get()
        if name_get == '' or box_get == '':
            self.error = tk.messagebox.showerror('Error', 'Empty field!')
        else:
            archive = open(name_get+'.txt', 'w')
            archive.write(box_get)
            archive.close()
class Calculator(Frame_Functions):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        def center_window(w=300, h=200):
            ws = master.winfo_screenwidth()
            hs = master.winfo_screenheight()
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title('CALCULATOR')
        center_window(400, 500)
        self.title_lbl = tk.Label(self, text='CALCULATOR', font=('Calibri', 20, 'bold'), pady=10, bg='#222', fg='#54ff9f').pack(side=TOP)
        self.expression_tb = tk.Entry(self, width=20, border=0, bg='#eee', font=('Calibri', 20))
        self.expression_tb.place(x=60, y=70, height=40)
        self.n1_btn = tk.Button(self, text='1', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n1_btn.place(x=0, y=150)
        self.n2_btn = tk.Button(self, text='2', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n2_btn.place(x=95, y=150)
        self.n3_btn = tk.Button(self, text='3', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n3_btn.place(x=190, y=150)
        self.clear_btn = tk.Button(self, text='C', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.clear_btn.place(x= 285, y=150)
        self.n4_btn = tk.Button(self, text='4', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n4_btn.place(x=0, y=193)
        self.n5_btn = tk.Button(self, text='5', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n5_btn.place(x=95, y=193)
        self.n6_btn = tk.Button(self, text='6', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n6_btn.place(x=190, y=193)
        self.add_btn = tk.Button(self, text='+', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.add_btn.place(x=285, y=193)
        self.n7_btn = tk.Button(self, text='7', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n7_btn.place(x=0, y=236)
        self.n8_btn = tk.Button(self, text='8', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n8_btn.place(x=95, y=236)
        self.n9_btn = tk.Button(self, text='9', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n9_btn.place(x=190, y=236)
        self.n0_btn = tk.Button(self, text='0', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.n0_btn.place(x=95, y=279)
        self.point_btn = tk.Button(self, text='.', font=('Calibri', 16, 'bold'), border=0, width=8, bg='#54ff9f', activebackground='#28ae7b')
        self.point_btn.place(x=0, y=279)
if __name__=='__main__':
    app=Mainframe()
    app.mainloop()
conn.close()