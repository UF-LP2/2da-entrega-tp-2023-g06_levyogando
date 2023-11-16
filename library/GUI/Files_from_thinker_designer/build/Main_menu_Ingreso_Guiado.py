import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from library.Classes.cSalaEspera import *

# --------------------------Variables Globales---------------------------------

# -- Path's--
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r".\assets\frame0")

global Father_off_windows


# -- Imagenes de Bottones --
button_image_1 = None
button_image_2 = None
button_image_3 = None
button_image_4 = None

# ----- Ventanas -----
Ventana_aux = None
grafico_categorias_creado = False
canvas_grafico_pacientes_categorias_aux=None

grafico_sala_espera_creado = False
canvas_grafico_pacientes_sala_espera_aux=None
Tablas_pacientes_atendidos=None
# --- cSalaEspera ---
Sala_de_espera = cSalaEspera()

# --- entry's -----

# ------------------------------Metodosaccesorios----------------------------
def relative_to_assets_menu_ingreso_guiado(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def relative_to_assets_rojo(path: str) -> Path:
    ASSETS_PATH = Path(r".\assets\frame4") / path
    return ASSETS_PATH


def relative_to_assets_amarillo(path: str) -> Path:
    ASSETS_PATH = Path(r".\assets\frame6") / path
    return ASSETS_PATH


def relative_to_assets_naranja(path: str) -> Path:
    ASSETS_PATH = Path(r".\assets\frame5") / path
    return ASSETS_PATH


def relative_to_assets_Verde(path: str) -> Path:
    ASSETS_PATH = Path(r".\assets\frame7") / path
    return ASSETS_PATH


def relative_to_assets_Ingreso_ya_clasificado(path: str) -> Path:
    ASSETS_PATH = Path(r".\assets\frame9")/ path
    return ASSETS_PATH
# ------------------------------ Ventanas ----------------------------

def Ingresar_paciente_con_guia():
    """
    En esta funcion se ejecuta el GUI general
    para poder categorzar a un paciente que llego a
    la sala de espera
    :return:
    """

    # -- Ventana de Ejecucion --
    window = tk.Tk()
    window.geometry("1440x900")
    window.configure(bg="#F0F0F0")

    button_image_ventana_rojo_1 = PhotoImage(file=relative_to_assets_rojo("button_1.png"))
    button_image_ventana_rojo_2 = PhotoImage(file=relative_to_assets_rojo("button_2.png"))

    canvas = Canvas(window, bg="#F0F0F0",
                    height=900,
                    width=1440,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge"
                    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        64.0,
        815.0,
        167.0,
        835.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        450.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_2.png"))
    image_2 = canvas.create_image(
        148.0,
        162.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=56.0,
        y=272.0,
        width=135.0,
        height=20.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_3.png"))
    image_3 = canvas.create_image(
        73.0,
        341.0,
        image=image_image_3
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=64.0,
        y=328.0,
        width=158.0,
        height=31.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=64.0,
        y=212.0,
        width=142.0,
        height=20.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_4.png"))
    image_4 = canvas.create_image(
        115.0,
        825.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_5.png"))
    image_5 = canvas.create_image(
        466.0,
        76.0,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        940.0,
        73.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#DBDBDB",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=715.0,
        y=48.0,
        width=450.0,
        height=48.0
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_6.png"))
    image_6 = canvas.create_image(
        736.2000122070312,
        72.199951171875,
        image=image_image_6
    )

    canvas.create_text(
        773.0,
        65.0,
        anchor="nw",
        text="Search Something",
        fill="#9A9A9A",
        font=("Montserrat Medium", 14 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_7.png"))
    image_7 = canvas.create_image(
        1253.0,
        73.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_8.png"))
    image_8 = canvas.create_image(
        456.0,
        172.0,
        image=image_image_8
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Rojo(window, button_image_ventana_rojo_1, button_image_ventana_rojo_2),
        relief="flat"
    )
    button_4.place(
        x=320.0,
        y=151.0,
        width=275.3648681640625,
        height=43.0
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_9.png"))
    image_9 = canvas.create_image(
        117.0,
        69.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets_menu_ingreso_guiado("image_10.png"))
    image_10 = canvas.create_image(
        72.81015014648438,
        397.76214599609375,
        image=image_image_10
    )

    canvas.create_text(
        108.00003051757812,
        393.0,
        anchor="nw",
        text="Settings",
        fill="#FFFFFF",
        font=("Montserrat Medium", 16 * -1)
    )

    window.resizable(True, True)
    window.mainloop()


def Rojo(_window, button_image_1, button_image_2):
    global Father_off_windows
    """
    Para empezar a categorizar empiezo realizando preguntas,
    Empiezo por las pregutnas que tendría un paciente que requiere de una atencion urgente
    :param _window:
    :return:
    """
    print("button_4 clicked")
    # Creo una nueva ventana

    ventana_roja = tk.Toplevel(_window)
    Father_off_windows = _window
    ventana_roja.title("Es rojo?")
    ventana_roja.geometry("680x282")
    ventana_roja.configure(bg="#FFFFFF")

    canvas = Canvas(
        ventana_roja,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_rojo("image_1.png"))
    image_1 = canvas.create_image(
        485.0,
        141.0,
        image=image_image_1
    )
    button_1 = Button(
        master=ventana_roja,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_datos_cargados(_window, "rojo"),
        relief="flat"
    )
    button_1.place(
        x=447.576904296875,
        y=120.0,
        width=76.784423828125,
        height=43.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_rojo("image_2.png"))
    image_2 = canvas.create_image(
        245.0,
        141.0,
        image=image_image_2
    )

    button_2 = Button(
        master=ventana_roja,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Naranja(ventana_roja, button_image_1, button_image_2),
        relief="flat"
    )
    button_2.place(
        x=207.576904296875,
        y=120.0,
        width=75.784423828125,
        height=43.0
    )
    canvas.create_text(
        186.0,
        16.0,
        anchor="nw",
        text="¿Tiene Politraumatismo?",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )


def Naranja(_window, button_image_1, button_image_2):
    print("button_4 clicked")
    global Father_off_windows
    _window.destroy()  # destruyo la ventana anterior
    Father_off_windows.wm_state('zoomed')
    Ventana_naranja = tk.Toplevel(Father_off_windows)  # Crea una nueva ventana con el padre de menu
    Ventana_naranja.title("Es Naranja?")
    Ventana_naranja.geometry("680x282")
    Ventana_naranja.configure(bg="#FFFFFF")

    canvas = Canvas(
        Ventana_naranja,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_naranja("image_1.png"))
    image_1 = canvas.create_image(
        474.0,
        92.0,
        image=image_image_1
    )

    button_1 = Button(
        master=Ventana_naranja,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_datos_cargados(_window, "Naranja"),
        relief="flat"
    )
    button_1.place(
        x=436.0,
        y=69.0,
        width=76.784423828125,
        height=43.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_naranja("image_2.png"))
    image_2 = canvas.create_image(
        474.0,
        204.0,
        image=image_image_2
    )

    button_2 = Button(

        master=Ventana_naranja,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Amarillo(Ventana_naranja, button_image_1, button_image_2),
        relief="flat"
    )
    button_2.place(
        x=436.576904296875,
        y=183.0,
        width=76.107177734375,
        height=43.0
    )

    canvas.create_text(
        64.0,
        7.0,
        anchor="nw",
        text="Actualmente tiene algun sintoma de :  \nComa \n\nConvulsion \n\nHemorragia Digestiva\n Isquemia",
        fill="#000000",
        font=("MontserratRoman Medium", 24 * -1)
    )


def Amarillo(_window, button_image_1, button_image_2):
    print("Boton No Naranja Apretado")
    global Father_off_windows
    _window.destroy()  # destruyo la ventana anterior
    Father_off_windows.wm_state('zoomed')
    Ventana_amarillo = tk.Toplevel(Father_off_windows)  # Crea una nueva ventana con el padre de menu
    Ventana_amarillo.title("Es Amarillo? ")
    Ventana_amarillo.geometry("680x282")
    Ventana_amarillo.configure(bg="#FFFFFF")

    canvas = Canvas(
        Ventana_amarillo,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_amarillo("image_1.png"))
    image_1 = canvas.create_image(
        599.0,
        69.0,
        image=image_image_1
    )

    button_1 = Button(
        master=Ventana_amarillo,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_datos_cargados(_window, "Amarillo"),
        relief="flat"
    )
    button_1.place(
        x=561.0,
        y=46.0,
        width=76.784423828125,
        height=43.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_amarillo("image_2.png"))
    image_2 = canvas.create_image(
        595.0,
        204.0,
        image=image_image_2
    )

    button_2 = Button(
        master=Ventana_amarillo,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Verde(Ventana_amarillo, button_image_1, button_image_2),
        relief="flat"
    )
    button_2.place(
        x=557.576904296875,
        y=183.0,
        width=76.107177734375,
        height=43.0
    )

    canvas.create_text(
        64.0,
        7.0,
        anchor="nw",
        text="Cefalea brusca,  paresia, \nhipertensión arterial,  \nvértigo con afectación vegetativa \nsíncope \nurgencias psiquiátricas",
        fill="#000000",
        font=("MontserratRoman Medium", 24 * -1)
    )


def Verde(_window, button_image_1, button_image_2):
    print("Botton No Naranja Apretado")
    global Father_off_windows
    _window.destroy()  # destruyo la ventana anterior
    Father_off_windows.wm_state('zoomed')
    Ventana_verde = tk.Toplevel(Father_off_windows)  # Crea una nueva ventana con el padre de menu
    Ventana_verde.title("Es verde? ")
    Ventana_verde.geometry("680x282")
    Ventana_verde.configure(bg="#FFFFFF")

    canvas = Canvas(
        Ventana_verde,
        bg="#FFFFFF",
        height=282,
        width=680,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets_Verde("image_1.png"))
    image_1 = canvas.create_image(
        474.0,
        92.0,
        image=image_image_1
    )

    button_1 = Button(
        master=Ventana_verde,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_datos_cargados(_window, "Verde"),
        relief="flat"
    )
    button_1.place(
        x=436.0,
        y=69.0,
        width=76.784423828125,
        height=43.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_Verde("image_2.png"))
    image_2 = canvas.create_image(
        474.0,
        204.0,
        image=image_image_2
    )

    button_2 = Button(
        master=Ventana_verde,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_datos_cargados(_window, "azul"),
        relief="flat"
    )

    button_2.place(
        x=436.576904296875,
        y=183.0,
        width=76.107177734375,
        height=43.0
    )

    canvas.create_text(
        60.0,
        65.0,
        anchor="nw",
        text="categoría normal.\n Otalgias,\n odontalgias, \ndolores inespecíficos leves, \ntraumatismos \n esguinces",
        fill="#000000",
        font=("MontserratRoman Medium", 24 * -1)
    )


def Abrir_menu_ingreso_datos_cargados(_window, color):
    # print("Boton No de Naranja Apretado")
    global Father_off_windows
    if (_window == Father_off_windows):
        _window.destroy()  # destruyo la ventana anterior
    else:
        _window.destroy()
        Father_off_windows.destroy()
    Ingreso_ya_clasificado(color)


def Abrir_menu_ingreso_guiado(_window):
    print("Boton Ingreso Guiado Apretado")
    global Father_off_windows
    if _window == Father_off_windows:
        _window.destroy()  # destruyo la ventana anterior
    else:
        _window.destroy()
        Father_off_windows.destroy()
    Ingresar_paciente_con_guia()


def Ingreso_ya_clasificado(color):
    global Father_off_windows
    window = Tk()

    Father_off_windows = window
    window.geometry("1280x720")
    window.configure(bg="#F0F0F0")

    canvas = Canvas(
        window,
        bg="#F0F0F0",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        64.0,
        815.0,
        167.0,
        835.0,
        fill="#000000",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_1.png"))
    image_1 = canvas.create_image(
        444.0,
        60.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_2.png"))
    image_2 = canvas.create_image(
        125.0,
        360.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=64.0,
        y=328.0,
        width=158.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=64.0,
        y=272.0,
        width=142.0,
        height=20.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=64.0,
        y=212.0,
        width=142.0,
        height=20.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Abrir_menu_ingreso_guiado(window),
        relief="flat"
    )
    button_4.place(
        x=64.0,
        y=152.0,
        width=168.0,
        height=20.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_3.png"))
    image_3 = canvas.create_image(
        115.0,
        685.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_4.png"))
    image_4 = canvas.create_image(
        117.0,
        69.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_5.png"))
    image_5 = canvas.create_image(
        72.81005859375,
        397.76214599609375,
        image=image_image_5
    )

    canvas.create_text(
        108.0,
        393.0,
        anchor="nw",
        text="Settings",
        fill="#FFFFFF",
        font=("Montserrat Medium", 16 * -1)
    )

    canvas.create_text(
        427.0,
        436.0,
        anchor="nw",
        text="Distribucion pacientes por gravedad",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )

    canvas.create_text(
        281.0,
        407.0,
        anchor="nw",
        text="Sala de \nespera",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_6.png"))
    image_6 = canvas.create_image(
        1031.0,
        289.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_7.png"))
    image_7 = canvas.create_image(
        1031.0,
        289.0,
        image=image_image_7
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: atender_manual_por_turno(window),
        relief="flat"
    )
    button_5.place(
        x=938.173828125,
        y=254.6649169921875,
        width=184.4345703125,
        height=68.4775390625
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_8.png"))
    image_8 = canvas.create_image(
        1031.0,
        123.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_9.png"))
    image_9 = canvas.create_image(
        1031.0,
        123.0,
        image=image_image_9
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=938.173828125,
        y=88.6649169921875,
        width=184.4345703125,
        height=68.4775390625
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_10.png"))
    image_10 = canvas.create_image(
        395.0,
        238.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_11.png"))
    image_11 = canvas.create_image(
        395.0,
        238.0,
        image=image_image_11
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Clasificar_paciente_sin_clasificar(window),
        relief="flat"
    )
    button_7.place(
        x=302.173828125,
        y=203.6649169921875,
        width=184.4345703125,
        height=68.4775390625
    )
    # Las posiciones de este rectangulo se tiene que utilizar para poner el grafico
    # por gravedades
    Agregar_grafico_pacientes_categorias(window)
    canvas.create_rectangle(
        395.0,
        476.0,
        881.0,
        720.0,
        fill="#F0F0F0",
        outline="")

    # La posicion de este rectangulo se va a utilizar para poner el grafico total de la sala
    # De espera
    # Yellow
    Agregar_Grafico_Pacientes_en_sala(window)
    canvas.create_rectangle(
        267.0,
        473.0,
        378.0,
        720.0,
        fill="#F0F0F0",
        outline="")

    canvas.create_text(
        906.0,
        438.0,
        anchor="nw",
        text="Ultimos pacientes derivados  ",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )
    # La posicion de este grafico se tienen que poner los pacientes que ya fueron guardados
    mostrar_datos(window)
    canvas.create_rectangle(
        894.0,
        476.0,
        1266.0,
        640.0,
        fill="red",
        outline="")

    image_image_12 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("image_12.png"))
    image_12 = canvas.create_image(
        725.0,
        256.0,
        image=image_image_12
    )

    canvas.create_text(
        608.0,
        134.0,
        anchor="nw",
        text="Clasificacion Personalizada",
        fill="#000000",
        font=("MontserratRoman SemiBold", 16 * -1)
    )
    #Aca se van a guardar los datos del entry antes de pasarselo para crear el objeto



    entry_image_1 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        664.0,
        193.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F3F3F3",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=603.5,
        y=183.0,
        width=121.0,
        height=19.0
    )

    canvas.create_text(
        600.0,
        161.0,
        anchor="nw",
        text="Nombre y Apellido",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        664.0,
        248.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F3F3F3",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=603.5,
        y=238.0,
        width=121.0,
        height=19.0
    )

    canvas.create_text(
        600.0,
        217.0,
        anchor="nw",
        text="Edad",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        664.0,
        304.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#F3F3F3",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=603.5,
        y=294.0,
        width=121.0,
        height=19.0
    )

    canvas.create_text(
        600.0,
        273.0,
        anchor="nw",
        text="Sector",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        664.0,
        365.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#F3F3F3",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=605.0,
        y=353.0,
        width=118.0,
        height=22.0
    )

    canvas.create_text(
        597.0,
        332.0,
        anchor="nw",
        text="Gravedad",
        fill="#000000",
        font=("Montserrat Medium", 16 * -1)
    )

    canvas.create_text(
        606.0,
        852.0,
        anchor="nw",
        text="en  sala de espera",
        fill="#000000",
        font=("Montserrat SemiBold", 24 * -1)
    )

    entry_4.insert(0, color)

    button_image_8 = PhotoImage(
        file=relative_to_assets_Ingreso_ya_clasificado("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: clasificar(entry_1,entry_2,entry_3,entry_4,window),
        relief="flat"
    )
    button_8.place(
        x=776.0,
        y=257.0,
        width=94.0,
        height=24.0
    )
    window.resizable(True, True)
    window.mainloop()


def Agregar_paciente_clasificado(nombre, color):
    Sala_de_espera.Pacientes_Clasificados(color, nombre, "18", "Unkown")


def Atender_paciente_clasificado(window):
    Sala_de_espera.DerivarProximo()
    Agregar_Grafico_Pacientes_en_sala(window)
    Agregar_grafico_pacientes_categorias(window)
    mostrar_datos(window)

def Clasificar_paciente_sin_clasificar(window):
    """
    Este metodo simula la llegada de un paciente random a la sala de espera
    este no fue categorizado
    :return:
    """

    # el Texto Hisotrial se tendría que buscar en la base de datos del hospital para poder mostrarle al
    # enfero del triage elementos relevantes
    paciente = Sala_de_espera.generar_Paciente_sin_gravedad("20", "", )
    Sala_de_espera.Pacientes_sin_Clasificar(paciente)
    Agregar_Grafico_Pacientes_en_sala(window)
    Agregar_grafico_pacientes_categorias(window)


def Agregar_Grafico_Pacientes_en_sala(window):
    global grafico_sala_espera_creado
    global canvas_grafico_pacientes_sala_espera_aux
    # Verificar si el gráfico ya ha sido creado
    if grafico_sala_espera_creado:
        # Si el gráfico ya existe, eliminarlo
        canvas_grafico_pacientes_sala_espera_aux.get_tk_widget().destroy()
    # Datos para el gráfico de barras
    pacientes = ['']

    pacientes_categorizados = len(Sala_de_espera.Lista_pacientes.Lista_de_pacientes)
    pacientes_sin_categorizar = len(Sala_de_espera.Sala_Espera)
    total = pacientes_categorizados +pacientes_sin_categorizar


    valores1 = [pacientes_sin_categorizar]
    valores2 = [pacientes_categorizados]

    # Crear una figura de Matplotlib
    fig = plt.Figure(figsize=(2, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Personalizar los colores de las barras
    color1 = '#F3F3F3'
    color2 = '#37B3E2'
    bar_width = 0.20

    ax.bar(pacientes, valores1, width=bar_width, color=color1)
    ax.bar(pacientes, valores2, width=bar_width, color=color2, bottom=valores1)

    # Agregar una leyenda
    ax.legend(frameon=False)

    # Ocultar ejes y líneas de cuadrícula
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Establecer el límite del eje x para centrar la barra
    ax.set_xlim(-0.25, 0.15)
    # Desplazar el eje vertical hacia la derecha
    ax.spines['left'].set_position(('data', -0.1))
    # Definir las coordenadas del rectángulo
    x1, y1, x2, y2 = 277.0, 473.0, 378.0, 690.0

    # Obtener las dimensiones del rectángulo
    rect_width = x2 - x1
    rect_height = y2 - y1

    # Obtener el tamaño de la figura en función de las dimensiones del rectángulo
    fig_width = rect_width
    fig_height = rect_height

    canvas = FigureCanvasTkAgg(fig, master=window)
    # Posicionar el lienzo dentro del rectángulo
    canvas.get_tk_widget().place(x=x1, y=y1, width=fig_width, height=fig_height)

    canvas_grafico_pacientes_sala_espera_aux = canvas
    return canvas


def Agregar_grafico_pacientes_categorias(window):
    #Sala_de_espera.Lista_pacientes.Reorganizar_greedy()
    #La sigueinte porcion de cosigo es fea y bruta

    Cant_rojo= Sala_de_espera.Lista_pacientes.contar_pacientes_gravedad_roja()
    Cant_naranja = Sala_de_espera.Lista_pacientes.contar_pacientes_gravedad_naranja()
    Cant_amarillo = Sala_de_espera.Lista_pacientes.contar_pacientes_gravedad_amarillo()
    Cant_verde = Sala_de_espera.Lista_pacientes.contar_pacientes_gravedad_verde()
    Cant_azul = Sala_de_espera.Lista_pacientes.contar_pacientes_gravedad_azul()

    global grafico_categorias_creado
    global canvas_grafico_pacientes_categorias_aux
    # Verificar si el gráfico ya ha sido creado
    if grafico_categorias_creado:
        # Si el gráfico ya existe, eliminarlo
        canvas_grafico_pacientes_categorias_aux.get_tk_widget().destroy()

    # Datos para el gráfico de barras
    categorias = ['Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul']
    valores1 = [Cant_rojo, Cant_naranja, Cant_amarillo, Cant_verde, Cant_azul]

    # Crear una figura de Matplotlib
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Personalizar los colores de las barras
    colors = ["red", "orange", "yellow", "green", "blue"]
    bar_width = 0.35

    ax.bar(categorias, valores1, width=bar_width, color=colors, label='')

    # Agregar una leyenda
    ax.legend(frameon=False)
    # Ocultar ejes y líneas de cuadrícula
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Crear un lienzo para mostrar la figura en la ventana
    canvas = FigureCanvasTkAgg(fig, master=window)

    # ax.spines['left'].set_position(('data', -0.1))
    # Definir las coordenadas del rectángulo
    x1, y1, x2, y2 = 395.0, 476.0, 881.0, 690.0,

    # Obtener las dimensiones del rectángulo
    rect_width = x2 - x1
    rect_height = y2 - y1

    # Obtener el tamaño de la figura en función de las dimensiones del rectángulo
    fig_width = rect_width
    fig_height = rect_height

    canvas = FigureCanvasTkAgg(fig, master=window)
    # Posicionar el lienzo dentro del rectángulo
    canvas.get_tk_widget().place(x=x1, y=y1, width=fig_width, height=fig_height)
    canvas_grafico_pacientes_categorias_aux = canvas
    # Marcar que el gráfico ha sido creado
    grafico_creado = True


def mostrar_datos(window):
    global Tablas_pacientes_atendidos
    """
    Esta funcion se encagar de desplegar en una tabla los ultimos pacientes derivados por los medicos
    :param window:
    :return:
    """
    if(Tablas_pacientes_atendidos is not None):
        Tablas_pacientes_atendidos.destroy()
        Sala_de_espera.HandlerArchivos = cManejoArchivo()
    ultimos_datos = Sala_de_espera.HandlerArchivos.obtener_ultimos_datos()
    primeros_tres_pacientes = Sala_de_espera.HandlerArchivos.pacientes_buscando_cama().head(3)
    window.title("Últimos Datos")

    tree = ttk.Treeview(window, columns=(
        "Nombre", "Edad", "Gravedad", "Historial", "Enfermero", "Fecha", "CasoClinico", "Matricula"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Edad", text="Edad")
    tree.heading("Gravedad", text="Gravedad")
    tree.heading("Historial", text="Historial")
    tree.heading("Enfermero", text="Enfermero")
    tree.heading("Fecha", text="Fecha")
    tree.heading("CasoClinico", text="Caso Clinico")
    tree.heading("Matricula", text="Matricula")

    # Aplicar el estilo de línea azul a las filas de pacientes buscando cama
    tree.tag_configure("line_color", background="#37B3E2")
    tree.tag_configure("no_line", background="white")

    # Insertar los primeros tres pacientes que buscan cama en el Treeview
    for _, fila in primeros_tres_pacientes.iterrows():
        valores = fila.values
        tree.insert("", "end", values=tuple(valores))

    # Insertar una fila con estilo "line_color" como separador
    tree.insert("", "end", values=("", "", "", "", "", "", "", ""), tags=("line_color",))

    # Insertar los últimos datos en el Treeview
    for _, fila in ultimos_datos.iterrows():
        valores = fila.values
        tree.insert("", "end", values=tuple(valores))

    tree.grid(row=0, column=0, padx=10, pady=10)
    tree.place(x=894, y=476, width=372, height=(len(primeros_tres_pacientes) + len(ultimos_datos)) * 30)
    Tablas_pacientes_atendidos = tree

def clasificar(entry1,entry2,entry3,entry4,window):
    print("Button_8 clicked")
    if len(Sala_de_espera.Sala_Espera)>0:
        Sala_de_espera.Sala_Espera.pop(0)
    enty1=entry1.get()
    enty2 = entry2.get()
    enty3 = entry3.get()
    enty4 = entry4.get()
    print("entry1: " +entry1.get())
    print("entry2: " +entry2.get())
    print("entry3: " +entry3.get())
    print("entry4: " +entry4.get())
    entry1.insert(0, "")
    entry2.insert(0, "")
    entry3.insert(0, "")
    entry4.insert(0, "")

    caso_clinico=Sala_de_espera.Lista_pacientes.Handler.BusquedaUltimo()
    paciente = Sala_de_espera.generarPaciente(enty4,enty1,enty2,caso_clinico,Sala_de_espera.Lista_enfermeros_triage[0],enty3)
    Sala_de_espera.Lista_pacientes.insert(paciente)

    #chequeo si no tengo que mover a algun paciente de gravedad
    Sala_de_espera.Lista_pacientes.Reorganizar_greedy()

    Agregar_Grafico_Pacientes_en_sala(window)
    Agregar_grafico_pacientes_categorias(window)



def atender_manual_por_turno(window):
    print("Button_5 clicked")

    # Obtener la hora actual
    ahora = datetime.now().time()

    #la cantidad de enfemeros dependiente del turno
    enfermeros_dedicados=0

    # Determinar cuántos enfermeros están dedicados en este momento
    if (ahora >= datetime.strptime("23:00", "%H:%M").time() or ahora < datetime.strptime("6:00", "%H:%M").time()):
        enfermeros_dedicados = 1
    elif ahora < datetime.strptime("10:00", "%H:%M").time():
        enfermeros_dedicados = 2
    elif ahora < datetime.strptime("16:00", "%H:%M").time():
        enfermeros_dedicados = 5
    else:
        enfermeros_dedicados = 3

    # Llamar a la función atender la cantidad de veces correspondiente
    for i in range(enfermeros_dedicados):
        Atender_paciente_clasificado(window)

#para atender: usar def Atender_paciente_clasificado()

if __name__ == '__main__':
    # Handler()
    Ingresar_paciente_con_guia()
