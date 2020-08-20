# ejemplo 1
print("***************ejemplo 1*************")
"""
color = input("Adivina cual es mi color favorito")

if color == "rojo":
    print("felicidades acertaste mi color favorito")

else:
    print("Te equivocaste de color")



Operadores de comparacion

== igual
!= diferente
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que


Operadores logicos

and Y
! NEGACION
not NO
or O


"""
# ejemplo 2
"""
print("***************ejemplo 2*************")

nombre = "Esteban"
ciudad = "Santiago"
continente = "america"
edad = 41
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} eres mayor de edad!!")
    if continente != "america":
        print(f"No eres americano")
    else:
        print(f"Enhorabuena...eres americano")
else:
    print(f"{nombre} lo siento pero eres menor de edad")

# ejemplo 3
print("***************ejemplo 3*************")

dia = int(input("introduce el número del dia de la semana"))

if dia == 1:
    print("Hoy es lunes")
else:
    if dia == 2:
        print("Hoy es martes")
    else:
        if dia == 3:
            print("Hoy es miercoles")
        else:
            if dia == 4:
                print("Hoy es jueves")
            else:
                if dia == 5:
                    print("Hoy es viernes")
                else:
                    print("Entonces es fin de semana")
"""
# ejemplo 4
print("***************ejemplo 4*************")

# dia = int(input("introduce el número del dia de la semana"))
"""
if dia == 1:
    print("Hoy es lunes")
elif dia == 2:
    print("Hoy es martes")
elif dia == 3:
    print("Hoy es miercoles")
elif dia == 4:
    print("Hoy es jueves")
elif dia == 5:
    print("Hoy es viernes")
else:
    print("Estamos en fin de semana")
"""

# ejemplo 5
print("***************ejemplo 5*************")

edad_minima = 18
edad_maxima = 65
edad_real = int(input("Cual es tu edad? "))

if edad_real >= 18 and edad_real <= 65:
    print("Estas en edad de trabajar")
else:
    print("NO puedes trabajar")
