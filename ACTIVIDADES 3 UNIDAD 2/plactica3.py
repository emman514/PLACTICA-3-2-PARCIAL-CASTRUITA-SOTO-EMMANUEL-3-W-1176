# Imprime una línea en blanco
print(" ")

# Imprime el nombre del autor y un identificador
print("CASTRUITA SOTO EMMANUEL 3-W 1176")

# Imprime otra línea en blanco
print(" ")

# Creación de un diccionario que almacena los precios de diferentes frutas
diccionario = {
    'melon': 19.60,    # Precio por kilo de melón
    'sandia': 44.40,   # Precio por kilo de sandía
    'platano': 30.20,  # Precio por kilo de plátano
    'pera': 15.4,     # Precio por kilo de pera
    'mango': 12.5   # Precio por kilo de mango
}

# Pide al usuario que ingrese el nombre de la fruta que desea comprar
frutas = input("Ingrese la fruta de su seleccion: ")
print("")

# Pide al usuario que ingrese la cantidad de kilos que desea comprar
kilos = float(input("Ingrese la cantidad de kilos que quiere comprar: "))
print("")

# Verifica si la fruta ingresada está en el diccionario de precios
if frutas in diccionario:
    # Calcula el precio final multiplicando el precio por kilo por la cantidad de kilos
    precio_final = diccionario[frutas] * kilos

    # Imprime el costo total de la fruta comprada
    print(f"{kilos} kilos de {frutas} serán: {precio_final:f}  pesos")
    print("")
    # Imprime el precio por kilo de la fruta seleccionada
    print(diccionario[frutas])
else:
    # Si la fruta no está en el diccionario, muestra un mensaje de error
    print("No tenemos esa fruta")
    print("")
