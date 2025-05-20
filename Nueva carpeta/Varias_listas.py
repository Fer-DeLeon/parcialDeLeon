#Dos listas entre nombres y edades.
nombres = ["Karen", "Jose", "Marcos"]
edades = [25, 50, 32]
for index in range(len(nombres)):
    print(f"{nombres[index]} tiene {edades[index]} años")


#Armado de listado en formato cuadro
nombres = ["Karen", "Jose", "Marcos"]
edades = [25, 50, 32]
generos = ["M", "F", "X"]

print("NOMBRE\t\tEDAD\tGENERO")

for index in range(len(nombres)):
    print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}")

#Armado de listado en formato cuadro
nombres = ["Karen", "Jose", "Marcos"]
edades = [25, 50, 32]
generos = ["F", "M", "X"]
estaturas = [1.65, 1.83, 1.54]

print("NOMBRE\t\tEDAD\tGENERO\tESTATURA")

for index in range(len(nombres)):
    print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")

#Problema si el nombre tiene mas de 7 caracteres
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

