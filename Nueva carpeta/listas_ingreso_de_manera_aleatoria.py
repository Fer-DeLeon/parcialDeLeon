estados = [0] * 6
nombres = ["a"] * 6
edad = [-1] * 6

#Carga aleatoria. Diciendole posicion y dar el dato.

while True:
    nombre = input("Ingrese nombre: ")
    posicion = int(input("Ingrese la posicion: "))
    
    while posicion > len(nombres)-1:
        posicion = int(input("Ingrese la posicion: "))

    nombres[posicion] = nombre
    respuesta = input("S para seguir cargando: ")
    if respuesta != "s":
        break

for nombre in nombres:
    if nombre != "a":
        print(nombre)

#Carga mas real, mixta entre aleatoria y secuncial.
estados = [0] * 6
nombres = ["a"] * 6
edades = [-1] * 6
contador = 0
espacio = True 
while True: 
    for i in range (len(estados)):
        if estados[i]==0:
            nombre = input("Ingrese nombre: ")
            edad = int(input("Ingrese la edad: "))
            nombres[i] = nombre
            edades[i]= edad
            estados[i] = 1
            contador += 1
            break
    if contador >= len(estados):
        print("No hay mas espacio")
        break
    respuesta = input("s para seguir cargando")
    if respuesta != "s":
        break

for i in range(len(estados)):
    if estados[i] != 0:
        print(f"{nombres[i]} {edades[i]}")
