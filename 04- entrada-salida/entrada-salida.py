# entrada

nombre = input("¿Cual es tu nombre?")
edad = input("¿Cual es tu edad?")

# salida

print(f"Me alegro de conocerte {nombre} , veo que tienes {edad} años")
# en este caso me funciona bien ya que esta concatenando 2 string

# print(f"Me alegro de conocerte {nombre} , veo que tienes {edad + 2} años")
# en este caso no me funciona y arroja error  ya que esta concatenando 1 string con 1 entero
# para solucionar esto debemos convertir el entero en string

print(f"Me alegro de conocerte {nombre} , veo que tienes {int(edad) + 2} años")
# en este caso me funciona bien ya que esta concatenando 2 string
