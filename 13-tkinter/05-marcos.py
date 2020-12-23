from tkinter import *

ventana = Tk()
ventana.title("Frames en Tkinter")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=N)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT)
marco.pack_propagate(FALSE)
texto = Label(marco, text="Mi segundo marco")
texto.config(
    bg="green",
    fg="white",
    font=("Arial, 20"),
    height=10,
    width=15,
    bd=3,
    # relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)

############################

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT)
marco.pack_propagate(FALSE)
texto = Label(marco, text="Mi primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial, 20"),
    height=10,
    width=15,
    bd=3,
    # relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)

#########################

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT)
marco.pack_propagate(FALSE)
texto = Label(marco, text="Mi cuarto marco")
texto.config(
    bg="orange",
    fg="white",
    font=("Arial, 20"),
    height=10,
    width=15,
    bd=3,
    # relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)

############################

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT)
marco.pack_propagate(FALSE)
texto = Label(marco, text="Mi tercer marco")
texto.config(
    bg="yellow",
    fg="black",
    font=("Arial, 20"),
    height=10,
    width=15,
    bd=3,
    # relief=SOLID,
    anchor=CENTER
)
texto.pack(fill=Y, expand=YES)


ventana.mainloop()
