
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
import ast
from tkinter.constants import *
 

polzv_columns = {"id_polz": 0, "F_P" : 1, "I_P" : 2, "O_P" : 3, "email" : 4, "login" : 5, "password" : 6, "dostup" : 7}

my_login = "admin"

class VerticalScrolledFrame(ttk.Frame):
    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)
 
        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, 
                                width = 200, height = 300,
                                yscrollcommand=vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command = self.canvas.yview)
 
        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
 
        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = ttk.Frame(self.canvas)
        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=NW)
 
 
    def _configure_interior(self, event):
        # Update the scrollbars to match the size of the inner frame.
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion=(0, 0, size[0], size[1]))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width = self.interior.winfo_reqwidth())
         
    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())
         
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
  
        self.show_frame(Login_page)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont, pred = None):
        if pred:
            self.frames[pred].forget()
        frame = self.frames[cont]
        frame.pack()
  
# first window frame startpage
  
class StartPage(tk.Frame):

    def update_polzv (self):
        frame = self.frame_polz_scrolled.interior
        for widget in frame.winfo_children():
            widget.destroy()
        polz = self.bd_get.get_polz_view()
        for p in polz:
            rb = ttk.Radiobutton(
                frame,
                text=p,
                value=str(p),
                variable=self.selected_polz,
                command = self.set_polz_attr)
            rb.grid()

    def update_zayavka (self):
        frame = self.frame_zayavka_scrolled.interior
        for widget in frame.winfo_children():
            widget.destroy()
        polz = self.bd_get.get_polz_view()
        for p in polz:
            rb = ttk.Radiobutton(
                frame,
                text=p,
                value=str(p),
                variable=self.selected_polz,
                command = self.set_polz_attr)
            rb.grid()

    def update_po (self):
        frame = self.frame_polz_scrolled.interior
        for widget in frame.winfo_children():
            widget.destroy()
        polz = self.bd_get.get_polz_view()
        for p in polz:
            rb = ttk.Radiobutton(
                frame,
                text=p,
                value=str(p),
                variable=self.selected_polz,
                command = self.set_polz_attr)
            rb.grid()


    def set_polz_attr(self):
        self.var_F_U.set(str(ast.literal_eval(self.selected_polz.get())[polzv_columns["F_P"]]))
        self.var_I_U.set(str(ast.literal_eval(self.selected_polz.get())[polzv_columns["I_P"]]))
        self.var_O_U.set(str(ast.literal_eval(self.selected_polz.get())[polzv_columns["O_P"]]))
        self.var_Login_U.set(str(ast.literal_eval(self.selected_polz.get())[polzv_columns["login"]]))
        self.var_Pass_U.set(str(ast.literal_eval(self.selected_polz.get())[polzv_columns["password"]]))
        self.var_Email_U.set(str(ast.literal_eval(self.selected_polz.get())[polzv_columns["email"]]))

    def add_polz(self):
        global my_login
        
        auth = Autorization()
        if auth.check_login(self.var_Login_U.get()):
            mb.showerror("Ошибка", "Такой логин уже существует!")
            return

        dolj_id = self.bd_get.get_iddolj(my_login)

        if dolj_id == 1:
            dolj_user = "Преподаватель"
        else:
            dolj_user = "Студент"

        
        registr = Registration()
        registr.registration(self.var_F_U.get(),  self.var_I_U.get(), self.var_O_U.get(), self.var_Email_U.get(), self.var_Login_U.get(), self.var_Pass_U.get(), dolj_user)

        mb.showinfo("Информация", "Пользователь добавлен")

        # error = self.bd_add.add_polz(self.var_F_U.get()
        #                                 , self.var_I_U.get()
        #                                 , self.var_O_U.get()
        #                                 , self.var_Email_U.get()
        #                                 , self.var_Login_U.get()
        #                                 , self.var_Pass_U.get())
        # if error:
        #     mb.showerror("Ошибка БД", error)

        self.update_polzv()

    # def validate_none (self, event):
    #     widget = event.widget
    #     value =widget.get()
    #     if value is None or not str(value):
    #         widget.config (bg = "red")
    #     else:
    #         widget.config (bg = "white")



    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bd_get = Bd_get_data()
        self.bd_add = Bd_add()

        # create a notebook
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True)

        # create frames
        frame_zayavka = ttk.Frame(notebook, width=400, height=280)
        frame_polz = ttk.Frame(notebook, width=400, height=280)
        frame_lickluch = ttk.Frame(notebook, width=400, height=280)
        frame_errors = ttk.Frame(notebook, width=400, height=280)


        frame_zayavka.pack(fill='both', expand=True)
        frame_polz.pack(fill='both', expand=True)
        frame_lickluch.pack(fill='both', expand=True)
        frame_errors.pack(fill='both', expand=True)

        # add frames to notebook

        notebook.add(frame_zayavka, text='Заявки')
        notebook.add(frame_lickluch, text='Лицензионные ключи')
        notebook.add(frame_polz, text='Пользаватели')
        notebook.add(frame_errors, text='Ошибки')

        # Вкладка пользователи
        label_F_U = ttk.Label(frame_polz, text ="Фамилия")
        label_F_U.grid(row = 0, column = 0)
        self.var_F_U = tk.StringVar()
        entry_F_U = tk.Entry(frame_polz, textvariable = self.var_F_U)
        entry_F_U.grid(row = 1, column = 0)

        label_I_U = ttk.Label(frame_polz, text ="Имя")
        label_I_U.grid(row = 0, column = 1)
        self.var_I_U = tk.StringVar()
        entry_I_U = tk.Entry(frame_polz, textvariable = self.var_I_U)
        entry_I_U.grid(row = 1, column = 1)

        label_O_U = ttk.Label(frame_polz, text ="Отчество")
        label_O_U.grid(row = 0, column = 2)
        self.var_O_U = tk.StringVar()
        entry_O_U = tk.Entry(frame_polz, textvariable = self.var_O_U)
        entry_O_U.grid(row = 1, column = 2)

        label_Email_U = ttk.Label(frame_polz, text ="Email")
        label_Email_U.grid(row = 2, column = 0)
        self.var_Email_U = tk.StringVar()
        entry_Email_U = tk.Entry(frame_polz, textvariable = self.var_Email_U)
        entry_Email_U.grid(row = 3, column = 0)

        label_Login_U = ttk.Label(frame_polz, text ="Логин")
        label_Login_U.grid(row = 2, column = 1)
        self.var_Login_U = tk.StringVar()
        entry_Login_U = tk.Entry(frame_polz, textvariable = self.var_Login_U)
        entry_Login_U.grid(row = 3, column = 1)

        label_Pass_U = ttk.Label(frame_polz, text ="Пароль")
        label_Pass_U.grid(row = 2, column = 2)
        self.var_Pass_U = tk.StringVar()
        entry_Pass_U = tk.Entry(frame_polz, textvariable = self.var_Pass_U)
        entry_Pass_U.grid(row = 3, column = 2)

        button1 = ttk.Button(frame_polz, text ="Удалить")
        button1.grid(row = 4, column = 0)
        
        button2 = ttk.Button(frame_polz, text ="Изменить")
        button2.grid(row = 4, column = 1)

        button3 = ttk.Button(frame_polz, text ="Добавить", command = self.add_polz)
        button3.grid(row = 4, column = 2)

        frame_polz_scrolled = VerticalScrolledFrame(frame_polz)
        frame_polz_scrolled.grid(columnspan=3)
        self.frame_polz_scrolled = frame_polz_scrolled

        self.selected_polz = tk.StringVar()

        self.update_polzv()




        # Вкладка Заявки

        label_num_zayavka = ttk.Label(frame_zayavka, text ="Номер заявки")
        label_num_zayavka.grid(row = 0, column = 0)
        self.var_num_zayavka = tk.StringVar()
        entry_num_zayavka = tk.Entry(frame_zayavka, textvariable = self.var_num_zayavka)
        entry_num_zayavka.grid(row = 1, column = 0)

        label_name__zayavka = ttk.Label(frame_zayavka, text ="Название ПО")
        label_name__zayavka.grid(row = 0, column = 1)
        self.var_name__zayavka = tk.StringVar()
        entry_name__zayavka = tk.Entry(frame_zayavka, textvariable = self.var_name__zayavka)
        entry_name__zayavka.grid(row = 1, column = 1)

        label_version_zayavka = ttk.Label(frame_zayavka, text ="Версия ПО")
        label_version_zayavka.grid(row = 0, column = 2)
        self.version_zayavka = tk.StringVar()
        entry_version_zayavka = tk.Entry(frame_zayavka, textvariable = self.version_zayavka)
        entry_version_zayavka.grid(row = 1, column = 2)

        label_status_zayavka = ttk.Label(frame_zayavka, text ="Статус")
        label_status_zayavka.grid(row = 2, column = 0)
        self.var_status_zayavka = tk.StringVar()
        entry_status_zayavka = tk.Entry(frame_zayavka, textvariable = self.var_status_zayavka)
        entry_status_zayavka.grid(row = 3, column = 0)

        label_Login_zayavka = ttk.Label(frame_zayavka, text ="Логин")
        label_Login_zayavka.grid(row = 2, column = 1)
        self.var_Login_zayavka = tk.StringVar()
        entry_Login_zayavka = tk.Entry(frame_zayavka, textvariable = self.var_Login_zayavka)
        entry_Login_zayavka.grid(row = 3, column = 1)

        button1 = ttk.Button(frame_zayavka, text ="Удалить")
        button1.grid(row = 4, column = 0)
        
        button2 = ttk.Button(frame_zayavka, text ="Изменить")
        button2.grid(row = 4, column = 1)

        button3 = ttk.Button(frame_zayavka, text ="Добавить")
        button3.grid(row = 4, column = 2)

        frame_zayavka_scrolled = VerticalScrolledFrame(frame_zayavka)
        frame_zayavka_scrolled.grid(columnspan=3)
        self.frame_zayavka_scrolled = frame_zayavka_scrolled

        
        self.selected_zayavka = tk.StringVar()
        
        self.update_zayavka()



        # Вкладка лицензионные ключи

        label_name_po = ttk.Label(frame_lickluch, text ="Название ПО")
        label_name_po.grid(row = 0, column = 0)
        entry_name_po = tk.Entry(frame_lickluch)
        entry_name_po.grid(row = 1, column = 0)

        label_version_po = ttk.Label(frame_lickluch, text ="Версия")
        label_version_po.grid(row = 0, column = 1)
        entry_version_po = tk.Entry(frame_lickluch)
        entry_version_po.grid(row = 1, column = 1)

        label_count_kluch = ttk.Label(frame_lickluch, text ="Количество")
        label_count_kluch.grid(row = 0, column = 2)
        entry_count_kluch = tk.Entry(frame_lickluch)
        entry_count_kluch.grid(row = 1, column = 2)

        label_kluch_po = ttk.Label(frame_lickluch, text ="Лицензионный ключ")
        label_kluch_po.grid(row = 2, column = 0)
        entry_kluch_po = tk.Entry(frame_lickluch)
        entry_kluch_po.grid(row = 3, column = 0)


        button1 = ttk.Button(frame_lickluch, text ="Удалить")
        button1.grid(row = 4, column = 0)
        
        button2 = ttk.Button(frame_lickluch, text ="Изменить")
        button2.grid(row = 4, column = 1)

        button3 = ttk.Button(frame_lickluch, text ="Добавить")
        button3.grid(row = 4, column = 2)


        frame_lickluch_scrolled = VerticalScrolledFrame(frame_lickluch)
        frame_lickluch_scrolled.grid(columnspan=3)
        
        # bd_get = Bd_get_data()

        # polz = bd_get.get_polz_view()
        # self.selected_lickluch = tk.StringVar()
        # for p in range(10):
        #     rb = ttk.Radiobutton(
        #         frame_lickluch_scrolled.interior,
        #         text=polz[0],
        #         value=p,
        #         variable=self.selected_polz)
        #     rb.grid()

        # Вкладка ошибки

        label_name_error = ttk.Label(frame_errors, text ="Название ошибки")
        label_name_error.grid(row = 0, column = 0)
        entry_name_error = ttk.Entry(frame_errors)
        entry_name_error.grid(row = 1, column = 0)

        label_opisanie_error = ttk.Label(frame_errors, text ="Описание ошибки")
        label_opisanie_error.grid(row = 2, column = 0)
        entry_opisanie_error = ttk.Entry(frame_errors)
        entry_opisanie_error.grid(row = 3, column = 0)

        button3 = ttk.Button(frame_errors, text ="Отправить")
        button3.grid(row = 4, column = 0)







  
          
  
  
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
        button1 = ttk.Button(self, text ="Забыл пароль", command = self.forgot_password)
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
