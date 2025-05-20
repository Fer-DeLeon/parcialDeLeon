nombres = ["Karen", "Jose", "Marcos"]
edades = [25, 50, 32]
generos = ["M", "F", "X"]

print("NOMBRE\t\tEDAD\tGENERO")

for index in range(len(nombres)):
    print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}")

#Agregamos estatura

nombres = ["Karen", "Jose", "Marcos"]
edades = [25, 50, 32]
generos = ["F", "M", "X"]
estaturas = [1.65, 1.83, 1.54]

print("NOMBRE\t\tEDAD\tGENERO\tESTATURA")

for index in range(len(nombres)):
    print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")

#problema de tabulacion con longitud de nombre

nombres = ["Mathias", "Antonela", "Umma", "Sol"]
edades = [25, 50, 32, 13]
generos = ["F", "M", "X", "F"]
estaturas = [1.65, 1.83, 1.54, 1.79]

print("NOMBRE\t\tEDAD\tGENERO\tESTATURA")

for index in range(len(nombres)):
    if len(nombres[index]) > 7:
        print(f"{nombres[index]}\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")
    else:
        print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")

#para imprimir solo los masculinos
nombres = ["Mathias", "Antonela", "Umma", "Sol"]
edades = [25, 50, 32, 13]
generos = ["F", "M", "X", "F"]
estaturas = [1.65, 1.83, 1.54, 1.79]

print("NOMBRE\t\tEDAD\tGENERO\tESTATURA")

for index in range(len(nombres)):
    if generos[index] == "F": #puedo poner != F
        if len(nombres[index]) > 7:
            print(f"{nombres[index]}\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")
        else:
            print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")

#Hacemos busqueda

nombres = ["Mathias", "Antonela", "Umma", "Sol"]
edades = [25, 50, 32, 13]
generos = ["F", "M", "X", "F"]
estaturas = [1.65, 1.83, 1.54, 1.79]
DNIs = [11111110, 11111111, 11111112, 11111113, 11111114]

while True:
    encontrado = False
    dni = int(input("Ingrese el DNI: "))

    for index in range(len(nombres)):
        if DNIs[index] == dni:
            encontrado = True
            print("NOMBRE\t\tEDAD\tGENERO\tESTATURA\tDNI")
            if len(nombres[index]) > 7:
                print(f"{nombres[index]}\t{edades[index]}\t{generos[index]}\t{estaturas[index]}\t\t{DNIs[index]}")
            else:
                print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}\t{estaturas[index]}\t\t{DNIs[index]}")

    if encontrado == False:
        print("DNI INEXISTENTE")
    continuar = input("Desea continuar? si - no: ")
    if continuar == "no":
        break

#Otro ejercicio

def buscar_datos(DNIs:list, dni:int) -> int:

    indice = None
    for index in range (len(DNIs)):
        if DNIs[index] == dni:
            indice = index
            break
    return indice

nombres = ["Mathias", "Antonela", "Umma", "Sol"]
edades = [25, 50, 32, 13]
generos = ["F", "M", "X", "F"]
estaturas = [1.65, 1.83, 1.54, 1.79]
DNIs = [11111110, 11111111, 11111112, 11111113, 11111114]

while True:
    dni = int(input("Ingrese el DNI: "))
    encontrado = buscar_datos(DNIs, dni) #encontrado = indice
    if encontrado == None:
        print("DNI INEXISTENTE")
    else:
        print("NOMBRE\t\tEDAD\tGENERO\tESTATURA\tDNI")
        if len(nombres[encontrado]) > 7:
            print(f"{nombres[encontrado]}\t{edades[encontrado]}\t{generos[encontrado]}\t{estaturas[encontrado]}\t\t{DNIs[encontrado]}")
        else:
            print(f"{nombres[encontrado]}\t\t{edades[encontrado]}\t{generos[encontrado]}\t{estaturas[encontrado]}\t\t{DNIs[encontrado]}")

#Se sigue con el ejercico para hacer la carga nosotros

def buscar_datos(DNIs:list, dni:int) -> int:

    indice = None
    for index in range (len(DNIs)):
        if DNIs[index] == dni:
            indice = index
            break
    return indice

nombres = ["x", "x", "x"]
edades = [0, 0, 0]
generos = ["x", "x", "x"]
estaturas = [0, 0, 0]
DNIs = [0, 0, 0]

for i in range (len(nombres)):
    nombres[i] = input("Nombre: ")
    edad[i] = input("Edad: ")
    generos[i] = input("Genero: ")
    estaturas[i] = input("Estatura: ")
    DNIs[i] = input("DNI: ")

for i in range (len(nombres)):
    
#while True:
    dni = int(input("Ingrese el DNI: "))
    encontrado = buscar_datos(DNIs, dni) #encontrado = indice
    if encontrado == None:
        print("DNI INEXISTENTE")
    else:
        print("NOMBRE\t\tEDAD\tGENERO\tESTATURA\tDNI")
        if len(nombres[encontrado]) > 7:
            print(f"{nombres[encontrado]}\t{edades[encontrado]}\t{generos[encontrado]}\t{estaturas[encontrado]}\t\t{DNIs[encontrado]}")
        else:
            print(f"{nombres[encontrado]}\t\t{edades[encontrado]}\t{generos[encontrado]}\t{estaturas[encontrado]}\t\t{DNIs[encontrado]}")