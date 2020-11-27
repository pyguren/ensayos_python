nombre = "Esteban Sologuren"

# funciones generales

print(type(nombre))

# detectar el tipado

comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variables es un string")
else:
    print("No es un string")

if not isinstance(nombre, float):
    print("la variable no es un numero con decimal")

# limpiar espacios
frase = "            mi contenido       "
print(frase)
print(frase.strip())


# eliminar variables

year = 2020
print(year)
del year


# comprobar si variable esta vacia o cuantos caracteres tiene

texto = "  ff  "
if len(texto) <= 0:
    print(" la variable esta vacia")
else:
    print("la variable tiene contenido: ", len(texto))

# encontrar caracteres

frase = "la vida es bella"
print(frase.find("vida"))


# reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# mayusculas y minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())
