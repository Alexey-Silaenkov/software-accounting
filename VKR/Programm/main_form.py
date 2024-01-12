
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.messagebox as mb
from BD import *
from modules import *
import os
import secrets
import string
  

LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     

    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack() 

  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Login_page, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.forget()
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont, pred = None):
        if pred:
            self.frames[pred].forget()
        frame = self.frames[cont]
        frame.pack()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create a notebook
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True)

        # create frames
        frame_zayavka = ttk.Frame(notebook, width=400, height=280)
        frame_polz = ttk.Frame(notebook, width=400, height=280)


        frame_zayavka.pack(fill='both', expand=True)
        frame_polz.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame_zayavka, text='Заявки')
        notebook.add(frame_polz, text='Пользаватели')

  
          
  
  
# second window frame page1 
class Login_page(tk.Frame):
     
    def __init__(self, parent, controller):
        
         
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_login = ttk.Label(self, text ="Логин")
        label_login.grid(row = 1, column = 0)
        self.login_var = tk.StringVar()
        entry_login = ttk.Entry(self, textvariable = self.login_var)
        entry_login.grid(row = 1, column = 1)
        label_password = ttk.Label(self, text ="Пароль")
        label_password.grid(row = 2, column = 0)
        self.password_var = tk.StringVar()
        entry_password = ttk.Entry(self, textvariable = self.password_var, show='*')
        entry_password.grid(row = 2, column = 1)
        button1 = ttk.Button(self, text ="Забыл", command = self.forgot_password)
        button1.grid(row = 3, column = 0)
        button2 = ttk.Button(self, text ="Войти", command = self.open_registration)
        button2.grid(row = 3, column = 1)


    def open_registration(self):
        
        login = self.login_var.get()
        # print(login)
        passwd = self.password_var.get()

    

        # mb.showerror("Ошибка", login)
        if not module_autorization.check_login(login):
            mb.showerror("Ошибка", "Такого логина нет")
            return
        if not (module_autorization.get_password() == passwd):
            mb.showerror("Ошибка", "Неправильный пароль")
            return
        
        self.controller.show_frame(StartPage, Login_page)


    def forgot_password(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        
        login = self.login_var.get()

        mail_pass = Send_email()
        get_data = Bd_get_data()

        edit_pass = Bd_edit()
        auth = Autorization()

        id_user = auth.get_id(login)


        crypt = Crypt()

        edit_pass.edit_polz_password(id_user, crypt.encrypt(password))

        # email = get_data.get_email(login)
        email = "silaenckov2014@yandex.ru"
        mail_pass.send("ychet.po", "swfi ciqc lani rhvm" , email, mail_pass.codPasseordHtml(password))

        mb.showinfo("Информация", "Вам на почту был выслан новый пароль")
  
  
  
  
# third window frame page2
class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1, Page2))
     
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage, Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code

first_login = First_login()
module_autorization = Autorization()


if first_login.is_first_login():
    first_login.first_login("Администратор", "Администратор", "Администратор","ychet.po@gmail.com","admin","admin")
    mb.showinfo("Информация", "Пользователь добавлен, вы можете зайти под данными: Логин - admin Пароль - admin")


app = tkinterApp()
app.mainloop()
