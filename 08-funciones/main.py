"""
conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse
invocando a la funcion tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    bloque de codigo o conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)

"""
# ************ejemplo 1**********
print("**********ejemplo 1***********")


def muestraNombre():
    print("Victor")
    print("Carlos")
    print("Esteban")


muestraNombre()


# ************ejemplo 2**********
print("**********ejemplo 2***********")


def mostrarTuNombre(nombre):
    print(f"Tu nombre es {nombre}")


nombre = input("Introduce tu nombre ")
mostrarTuNombre(nombre)
