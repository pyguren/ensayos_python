from tkinter import *

ventana = Tk()
# ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",  # color de la letra
    bg="black",  # color background
    padx=120,  # padding x
    pady=40,  # padding Y
    font=("Arial", 30)
)
texto.pack(side=TOP)

########################

texto = Label(ventana, text="Ahora estamos aprendiendo Tkinter")
texto.config(
    fg="white",  # color de la letra
    bg="red",  # color background
    padx=120,  # padding x
    pady=40,  # padding Y
    font=("Arial", 30)
)
texto.pack(side=TOP, fill=X, expand=YES)

########################

texto = Label(ventana, text="Mi nombre es Esteban")
texto.config(
    # width=40,
    height=3,
    fg="white",
    bg="orange",
    padx=10,
    pady=10,
    font=("Arial", 30)
)
texto.pack(side=LEFT, fill=X, expand=YES)

########################

texto = Label(ventana, text="Sologuren")
texto.config(
    # width=40,
    height=3,
    fg="white",
    bg="green",
    padx=10,
    pady=10,
    font=("Arial", 30)
)
texto.pack(side=LEFT, fill=X, expand=YES)

########################

texto = Label(ventana, text="Jamette")
texto.config(
    # width=40,
    height=3,
    fg="black",
    bg="yellow",
    padx=10,
    pady=10,
    font=("Arial", 30)
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()
