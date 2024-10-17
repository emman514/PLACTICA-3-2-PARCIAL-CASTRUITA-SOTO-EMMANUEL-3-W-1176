# Imprime una línea en blanco
print(" ")

# Imprime el nombre del autor y un identificador
print("CASTRUITA SOTO EMMANUEL 3-W 1176")

# Imprime otra línea en blanco
print(" ")

# Creación de un diccionario que relaciona nombres de divisas con sus símbolos
diccionario = {
    'euro': '€',  # El símbolo del Euro
    'dollar': '$',  # El símbolo del Dólar
    'yen': '¥'  # El símbolo del Yen
}

# Pide al usuario que ingrese el nombre de una divisa
DIVISA = str(input("Ingrese una divisa: "))

# Verifica si la divisa ingresada está en el diccionario
if DIVISA in diccionario:
    # Si está, imprime el símbolo correspondiente
    print(diccionario[DIVISA])
else:
    # Si no está, informa al usuario que ingrese una divisa válida
    print("NO ESTA EN EL DICCIONARIO")

