# Tkinter
# Modulo para crear interfaces de usuarios

import os.path
from tkinter import *


class Programa:

    def __init__(self):
        self.title = "Master en Python con Victor Robles"
        self.icon = "./imagenes/seoguren.ico"
        self.icon_alt = "./01-tkinter/imagenes/seoguren.ico"
        self.size = "750x450"
        self.resizable = False

    def cargar(self):

        # crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title("Interfaz front-end con codigo python")

        # comprobar si existe un archivo desde la ruta absoluta
        ruta_icono = os.path.abspath("./imagenes/seoguren.ico")

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath("./01-tkinter/imagenes/seoguren.ico")

        # mostrar texto en la ventana
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        ventana.iconbitmap("./imagenes/seoguren.ico")

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana y que no se pueda redimensionar
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.register(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()


# instanciar el programa mediante la clse
programa = Programa()
programa.cargar()
programa.addTexto("Hola bienvenidos a tkinter")
programa.addTexto("Probando la ventana")
programa.addTexto("Mi nombre es Esteban")
programa.mostrar()
