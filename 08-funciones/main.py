"""
conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse
invocando a la funcion tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    bloque de codigo o conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)

# ************ejemplo 1**********
print("**********ejemplo 1***********")


def muestraNombre():
    print("Victor")
    print("Carlos")
    print("Esteban")


muestraNombre()


# ************ejemplo 2**********
print("**********ejemplo 2***********")



def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")


nombre = input("Introduce tu nombre ")
edad = int(input("introduce tu edad: "))
mostrarTuNombre(nombre, edad)

"""

# ************ejemplo 3**********
print("**********ejemplo 3***********")


def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")
    tabla(3)

    for numero_tabla in range(1, 11):
        tabla(numero_tabla)
