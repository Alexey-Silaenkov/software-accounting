import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter.messagebox as mb
from BD import *
from modules import *
import os
import secrets
import string



lst = []
window = None

def show():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\autorization")

    first_login = First_login()
    module_autorization = Autorization()


    if first_login.is_first_login():
        first_login.first_login("Администратор", "Администратор", "Администратор","ychet.po@gmail.com","admin","admin")
        mb.showinfo("Информация", "Пользователь добавлен, вы можете зайти под данными: Логин - admin Пароль - admin")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    def open_registration():
        
        login = entry_2.get("1.0", "end-1c")
        passwd = entry_1.get("1.0", "end-1c")

        # mb.showerror("Ошибка", login)
        if not module_autorization.check_login(login):
            mb.showerror("Ошибка", "Такого логина нет")
            return
        if not (module_autorization.get_password() == passwd):
            mb.showerror("Ошибка", "Неправильный пароль")
            return
        
        pass
        # window.withdraw()
        # os.system('python forms/main_form.py')
        # return 10

    def forgot_password():
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        
        login = entry_2.get("1.0", "end-1c")

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
        
        












    window = Tk()

    window.geometry("480x416")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=416,
        width=480,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        240.0,
        208.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        240.0,
        253.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30),
        wrap='none'
    )
    entry_1.place(
        x=108.0,
        y=224.0,
        width=264.0,
        height=56.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        240.0,
        122.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 )
    )
    entry_2.place(
        x=108.0,
        y=93.0,
        width=264.0,
        height=56.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_registration,
        relief="flat"
    )
    button_1.place(
        x=247.0,
        y=316.0,
        width=133.0,
        height=58.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=forgot_password,
        relief="flat"
    )
    button_2.place(
        x=100.0,
        y=316.0,
        width=133.0,
        height=58.0
    )

    canvas.create_text(
        182.0,
        42.0,
        anchor="nw",
        text="Логин",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        182.0,
        173.0,
        anchor="nw",
        text="Пароль",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

