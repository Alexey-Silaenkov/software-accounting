
from pathlib import Path
import os
from BD import *
import tkinter.messagebox as mb

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
def show():

    my_login = "qwerty"
    auth = Autorization()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets/registration")





    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def open_main():
        # registration.withdraw()
        # os.system('python main.py')
       
        print("go main")

    def register_user():

        f_user = entry_6.get("1.0", "end-1c")
        i_user = entry_5.get("1.0", "end-1c")
        o_user = entry_4.get("1.0", "end-1c")
        email_user = entry_2.get("1.0", "end-1c")
        login_user = entry_3.get("1.0", "end-1c")
        password_user = entry_1.get("1.0", "end-1c")

        if not f_user or not i_user or not email_user or not login_user or not password_user:
            mb.showerror("Ошибка", "Не все данные заполнены!")
            return
        if auth.check_login(login_user):
            mb.showerror("Ошибка", "Такой логин уже существует!")
            return

        get_data = Bd_get_data()
        dolj_id = get_data.get_iddolj(my_login)

        if dolj_id == 1:
            dolj_user = "Преподаватель"
        else:
            dolj_user = "Студент"

        
        registr = Registration()
        registr.registration(f_user, i_user, o_user, email_user, login_user, password_user, dolj_user)

        mb.showinfo("Информация", "Пользователь добавлен")
        




    registration = Tk()

    registration.geometry("909x581")
    registration.configure(bg='#FFFFFF')

    canvas = Canvas(
        registration,
        bg="#FFFFFF",
        height=581,
        width=909,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        454.0,
        290.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        670.0,
        378.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_1.place(
        x=538.0,
        y=349.0,
        width=264.0,
        height=56.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        670.0,
        150.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_2.place(
        x=538.0,
        y=121.0,
        width=264.0,
        height=56.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        670.0,
        264.0,
        image=entry_image_3
    )
    entry_3 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_3.place(
        x=538.0,
        y=235.0,
        width=264.0,
        height=56.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        244.0,
        378.0,
        image=entry_image_4
    )
    entry_4 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_4.place(
        x=112.0,
        y=349.0,
        width=264.0,
        height=56.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        241.0,
        264.0,
        image=entry_image_5
    )
    entry_5 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_5.place(
        x=109.0,
        y=235.0,
        width=264.0,
        height=56.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        244.0,
        150.0,
        image=entry_image_6
    )
    entry_6 = Text(
        bd=0,
        bg="#B5CEF5",
        fg="#000716",
        highlightthickness=0,
        font=("Inter", 30 * -1)
    )
    entry_6.place(
        x=112.0,
        y=121.0,
        width=264.0,
        height=56.0
    )

    canvas.create_text(
        104.0,
        76.0,
        anchor="nw",
        text="Фамилия",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        101.0,
        195.0,
        anchor="nw",
        text="Имя",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        101.0,
        309.0,
        anchor="nw",
        text="Отчество",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=open_main,
        relief="flat"
    )
    button_1.place(
        x=101.0,
        y=463.0,
        width=280.0,
        height=74.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=register_user,
        relief="flat"
    )
    button_2.place(
        x=513.0,
        y=463.0,
        width=314.0,
        height=74.0
    )

    canvas.create_text(
        530.0,
        195.0,
        anchor="nw",
        text="Логин",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        530.0,
        76.0,
        anchor="nw",
        text="Email",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        530.0,
        309.0,
        anchor="nw",
        text="Пароль",
        fill="#312C4D",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        19.0,
        10.0,
        anchor="nw",
        text="Регистрация",
        fill="#312C4D",
        font=("Inter", 36 * -1)
    )
    registration.resizable(False, False)
    registration.mainloop()
