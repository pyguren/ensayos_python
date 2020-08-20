"""
for variable in elemento iterable (listas, tuplas, diccionarios, rango)
    bloque de instrucciones
"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el numero" + str(contador))

    resultado = resultado + contador
print(f"El resultado es:{resultado}")


# ejemplo 2
print("*********Ejercisio 2*********")

numero_usuario = int(input("¿De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n #########tabla de mukltiplicar del numero{numero_usuario}")

for numero_tabla in range(1, 10):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos!!!")
        break
else:
    print("La tabla esta terminada")
