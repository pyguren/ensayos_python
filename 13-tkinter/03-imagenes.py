from tkinter import *
# aca utilizo la libreria pillow para incrustar la imagen en la ventana
#from pillow import Image, ImageTk

try:
    from PIL import Image, ImageTk
except ImportError:
    # Que hacer si el módulo no se puede importar
    print("Módulo no instalado")

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Esteban").pack(anchor=W)

imagen = Image.open('./13-tkinter/imagenes/logo.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()
