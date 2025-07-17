def saludar():
    print("¡Hola!")

saludar()

def saludar_persona(nombre):
    print(f"¡Hola {nombre}!")

saludar_persona("Agus")

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(f"Resultado de la suma: {resultado}")

def obtener_pi():
    return 3.1416

pi = obtener_pi()
print(f"Valor de pi: {pi}")

def datos_persona(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, vive en {ciudad}.")

datos_persona("Agus", 20, "Madrid")

def operacion(a, b):
    def multiplicar(x, y):
        return x * y
    return multiplicar(a, b)

print(f"Multiplicación: {operacion(4, 6)}")

lista = [1, 2, 3, 4, 5]
print(f"Tamaño de la lista: {len(lista)}")

mensaje = "Soy global"

def cambiar_mensaje():
    mensaje = "Soy local"
    print("Dentro de la función:", mensaje)

cambiar_mensaje()
print("Fuera de la función:", mensaje)

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(f"Contador global: {contador}")
