texto = "hola soy un texto"
numero = 776
numero = str("776")
# de la siguiente forma convierto un entero en string
print(texto + " " + numero)
print(type(numero))
# de la siguiente forma convierto un string en entero
numero = int(numero)
print(type(numero))
# de la siguiente forma convierto un entero en decimal
numero = float(776)
print(type(numero))


# /////////////////////////////////

mi_texto = "master"
mi_texto2 = "en \'Python\'"

# aca imprime dejando un espacio entre las dos palabras
texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

# aca imprime dejando la frase en dos lineas separadas
texto_unido = mi_texto + " \n " + mi_texto2
print(texto_unido)

# aca imprime dejando un espacio tabulador  entre las dos palabras
texto_unido = mi_texto + " \t " + mi_texto2
print(texto_unido)

# aca imprime borrando la primera palabra y solo dejando la segunda
texto_unido = mi_texto + " \r " + mi_texto2
print(texto_unido)
