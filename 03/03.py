# Listas
nombres = ["Agus", "Luffy", "Pepe"]
print(nombres)
nombres.append("Zoro") # Añadir contenido a una lista
print(nombres)
nombres.remove("Pepe") # Eliminar contenido de una lista
print(nombres)

print(nombres[0]) # Acceder a la posición 0 para cambiarla mas adelante
nombres[0] = "Sanji" # Actualizar el indice 0
print(nombres)

# Ordenar una lista
nombres.sort() # Ordenar alfabeticamente 

# Tuplas. Contenido inmutable
mi_tupla = ("Monkey", "D. Luffy", "Hito Hito No Mi")

# Acceder a los elementos de la tupla
for i in range(len(mi_tupla)):
    print(mi_tupla[i])


print("----------")

# Diccionarios
datos = {
    "nombre":"Agus",
    "apellido":"Fernandez",
    "edad":20,
    "en_vida":True
}

# Añadir nuevo par clave:valor
datos["ocupacion"] = "vividor"

# Ver los elementos de un diccionario
for clave, valor in datos.items():
    print(clave, "->", valor)

# Editar par clave:valor
datos["ocupacion"] = ""

# Eliminar una clave
del datos["ocupacion"]

# Ver los elementos de un diccionario
for clave, valor in datos.items():
    print(clave, "->", valor)