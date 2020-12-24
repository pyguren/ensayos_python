from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formulario con Tkinter")

encabezado = Label(
    ventana, text="Formularios con Tkinter | Esteban Sologuren")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Arial", 20),
    padx=10,
    pady=10
)

encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

Label(ventana).grid(row=1, column=0)

# Campo para introducir el nombre
label = Label(ventana, text="Nombre:")
label.grid(row=2, column=0, sticky=NW, padx=5, pady=0)

campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5)
campo_texto.config(
    justify="right",
    state="normal",
    width=40
)
#################

# Campo para introducir el apellido
label = Label(ventana, text="Apellido:")
label.grid(row=3, column=0, sticky=NW, padx=5, pady=0)

campo_texto = Entry(ventana)
campo_texto.grid(row=3, column=1, padx=5, pady=5)
campo_texto.config(
    justify="right",
    state="normal",
    width=40
)
#################

# Campo para introducir el texto de la descripcion
label = Label(ventana, text="Descripcion:")
label.grid(row=4, column=0, sticky=NW, padx=5, pady=5)
campo_grande = Text(ventana)
campo_grande.grid(row=4, column=1)
campo_grande.config(
    width=30,
    height=5,
    padx=5,
    pady=5

)

#################

# Crear boton para enviar

Label(ventana).grid(row=5, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=6, column=1, sticky=W)
boton.config(
    padx=5,
    pady=5,
    bg="green",
    fg="white",
    bd=3,
    relief="sunken",
)


ventana.mainloop()
