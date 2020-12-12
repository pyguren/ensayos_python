from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",  # color de la letra
    bg="black",  # color background
    padx=120,  # padding x
    pady=40,  # padding Y
    font=("Arial", 30)
)
texto.pack()

texto = Label(ventana, text="Mi nombre es Esteban")
texto.config(
    width=400,
    height=400,
    fg="white",
    bg="orange",
    padx=50,
    pady=40,
    font=("Arial", 30)
)
texto.pack(anchor=CENTER)

ventana.mainloop()
