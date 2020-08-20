# **********ejercisio 1***********

"""
crear variables una pais y otra continente
mostrar su valor por pantalla
poner un comentario diciendo el tipo de dato
"""

pais = "venezuela"
continente = "america"
year = 2020

print(f"pais - america - {str(year)}")

# **********ejercisio 2***********

"""
escribir un script que nos muestre por pantalla todos los numeros pares
del 1 al 120
"""


for contador in range(1, 121):
    if contador % 2 == 0:
        print(contador)

# **********ejercisio 3***********
# con while
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1
# con for
numero = 0
for numero in range(0, 61):
    cuadrado = numero * numero
    print(f"el cuadrado de {numero} es {cuadrado}")

# **********ejercisio 4***********
"""
pedir dos numeros al usuario y hacer todas las operaciones basicas
de una calculadora y mostrarlo por pantalla
"""

numero1 = int(input("Favor introducir el primer numero: "))
numero2 = int(input("Ahora introduce el segundo numero: "))

print("**********calculadora*********")
print("suma:" + str(numero1 + numero2))
print("resta:" + str(numero1 - numero2))
print("multiplicacion:" + str(numero1 * numero2))
print("division:" + str(numero1 / numero2))
