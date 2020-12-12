from tkinter import *
# aca utilizo la libreria pillow para incrustar la imagen en la ventana
from PIL import Image, ImageTk


ventana = Tk()
ventana.geometry("700x500")

imagen = Image.open('./13-tkinter/imagenes/logo.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()
