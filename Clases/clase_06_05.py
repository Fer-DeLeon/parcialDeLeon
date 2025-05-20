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
    respuesta = input("S para seguir cargando")
    if respuesta != "s":
        break

for nombre in nombres:
    if nombre != "a":
        print(nombre)

#Carga mas real, mixta.
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

#Ordenamiento

numeros = [4,3,1,5,2]

print(numeros)

def funcion_orden(lista:list) -> list: #funcion que me ordena una lista

    for i in range(0, len(lista)-1, 1):
        #print(lista[i])
        for j in range(i+1,len(lista),1):
            if lista[i>lista[j]]:
                numero_auxiliar = lista[i]
                lista[i]=lista[j]
                lista[j]=numero_auxiliar

funcion_orden(numeros)
print(numeros)

#para manterner ambas listas en linea 52 agrego:

numeros = [4,3,1,5,2]
numeros_original = [-1] * len(numeros)

for i in range(len(numeros)):
    numeros_original[i] = numeros[i]

#funcion

numeros = [4,3,1,5,2]

def copiar_lista(lista:list) -> list:
    numeros_original = [-1]*len(lista)
    for i in range(len(lista)):
        numeros_original[i]=lista[i]
    return numeros_original

print(numeros)

def funcion_orden(lista:list) -> list: #funcion que me ordena una lista

    for i in range(0, len(lista)-1, 1):
        #print(lista[i])
        for j in range(i+1,len(lista),1):
            if lista[i>lista[j]]:
                numero_auxiliar = lista[i]
                lista[i]=lista[j]
                lista[j]=numero_auxiliar

copia = copiar_lista(numeros)
funcion_orden(numeros)
print(numeros)
print(copia)

    
