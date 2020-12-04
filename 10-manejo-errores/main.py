# capturar excepciones y manejar excepciones en codigo suceptible a fallos / errores

"""
try:
    nombre = input("¿Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = "tu nombre es " + nombre
    print(nombre_usuario)

except:
    print("ha ocurrido un error, introduzca bien su nombre")

else:
    print("Todo ha salido ok")
finally:
    print("Fin de la iteracion!!!")
"""

##########################################################

# Multiples excepsiones
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado :"))
    print("El cuadrado es" + str(numero*numero))

except TypeError:
    print("Debes convertir tu cadena a entero en el codigo")

except ValueError:
    print("Introduce un numero correcto")

except Exception as e:
    print(type(e))
    print("ha ocurrido un error: ", type(e).__name__)
"""
##########################################################

# Excepsiones personalizadas

try:
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("la edad ingresada no es correcta!!!")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master {nombre} !!!")

except ValueError:
    print("Ingresa los datos correctamente")
except Exception as e:
    print("existe un error: ", e)
