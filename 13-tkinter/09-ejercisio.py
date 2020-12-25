"""
CALCULADORA:
- Dos campo de textos
- $ botones para las operaciones
- Mostrar resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercisio completo con tkinter")
ventana.config(bd=25)
ventana.geometry("450x450")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=300)
marco.config(
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir").pack(side="left", fill=X, expand=YES)


ventana.mainloop()
