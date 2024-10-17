# Imprime una línea en blanco
print(" ")

# Imprime el nombre del autor y un identificador
print("CASTRUITA SOTO EMMANUEL 3-W 1176")

# Imprime otra línea en blanco
print(" ")

# Pide al usuario que ingrese su nombre
Nombre = input("Ingresa tu nombre:")

# Pide al usuario que ingrese su edad
Edad = input("Ingresa tu edad:")

# Pide al usuario que ingrese su dirección (país)
Direccion = input("Ingresa tu direccion(País):")

# Pide al usuario que ingrese su número de teléfono
numero = input("Ingresa tu numero de telefono:")

# Creación de un diccionario que almacena la información del usuario
diccionario = {
    "nombre": Nombre,  # Almacena el nombre ingresado
    "edad": Edad,  # Almacena la edad ingresada
    "direccion": Direccion,  # Almacena la dirección ingresada
    "telefono": numero  # Almacena el número de teléfono ingresado
}

# Imprime una línea en blanco
print(" ")

# Imprime el nombre del usuario a partir del diccionario
print("se llama:")
print(diccionario["nombre"])

# Imprime la edad del usuario a partir del diccionario
print("Su edad es:")
print(diccionario["edad"])

# Imprime la dirección del usuario a partir del diccionario
print("Su dirección o localización actual es:")
print(diccionario["direccion"])

# Imprime el número de teléfono del usuario a partir del diccionario
print("Su número de teléfono es:")
print(diccionario["telefono"])