# Tkinter
# Modulo para crear interfaces de usuarios

import os.path
from tkinter import *

# crear la ventana raiz
ventana = Tk()

# Titulo de la ventana
ventana.title("Interfas front-end con codigo python")

# comprobar si existe un archivo desde la ruta absoluta
ruta_icono = os.path.abspath("./imagenes/seoguren.ico")

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath("./01-tkinter/imagenes/seoguren.ico")

# Icono de la ventana
ventana.iconbitmap("./imagenes/seoguren.ico")

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana y que no se pueda redimensionar
ventana.resizable(0, 0)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
