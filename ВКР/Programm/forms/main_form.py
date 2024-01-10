



from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/main_form")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1151x642")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 642,
    width = 1151,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    575.0,
    321.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=895.0,
    y=552.0,
    width=197.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=500.0,
    y=552.0,
    width=213.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=105.0,
    y=552.0,
    width=213.0,
    height=45.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    994.0,
    519.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_1.place(
    x=862.0,
    y=497.0,
    width=264.0,
    height=42.0
)

canvas.create_text(
    854.0,
    470.0,
    anchor="nw",
    text="Пароль",
    fill="#312C4D",
    font=("Inter", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    992.0,
    438.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_2.place(
    x=860.0,
    y=418.0,
    width=264.0,
    height=39.0
)

canvas.create_text(
    854.0,
    385.0,
    anchor="nw",
    text="Логин",
    fill="#312C4D",
    font=("Inter", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    607.0,
    517.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_3.place(
    x=475.0,
    y=497.0,
    width=264.0,
    height=38.0
)

canvas.create_text(
    467.0,
    470.0,
    anchor="nw",
    text="Email",
    fill="#312C4D",
    font=("Inter", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    607.0,
    437.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_4.place(
    x=475.0,
    y=416.0,
    width=264.0,
    height=41.0
)

canvas.create_text(
    467.0,
    393.0,
    anchor="nw",
    text="Отчество",
    fill="#312C4D",
    font=("Inter", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    211.0,
    519.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_5.place(
    x=79.0,
    y=497.0,
    width=264.0,
    height=42.0
)

canvas.create_text(
    71.0,
    470.0,
    anchor="nw",
    text="Имя",
    fill="#312C4D",
    font=("Inter", 20 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    211.0,
    437.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_6.place(
    x=79.0,
    y=415.0,
    width=264.0,
    height=42.0
)

canvas.create_text(
    71.0,
    390.0,
    anchor="nw",
    text="Фамилия",
    fill="#312C4D",
    font=("Inter", 20 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    566.5,
    227.0,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#B5CEF5",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_7.place(
    x=19.0,
    y=89.0,
    width=1095.0,
    height=274.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=960.0,
    y=21.0,
    width=162.0,
    height=47.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=513.0,
    y=23.0,
    width=304.0,
    height=47.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=258.0,
    y=21.0,
    width=209.0,
    height=48.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=90.0,
    y=21.0,
    width=133.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
