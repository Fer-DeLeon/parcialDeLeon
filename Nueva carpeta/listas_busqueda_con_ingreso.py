#Busqueda por DNI.
def buscar_datos(DNIs:list, dni:int) -> int: #devuelve el indice de la pesona
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
    indice = buscar_datos(DNIs, dni) #encontrado = indice
    if indice == None:
        print("DNI INEXISTENTE")
    else:
        print("NOMBRE\t\tEDAD\tGENERO\tESTATURA\tDNI")
        if len(nombres[indice]) > 7:
            print(f"{nombres[indice]}\t{edades[indice]}\t{generos[indice]}\t{estaturas[indice]}\t\t{DNIs[indice]}")
        else:
            print(f"{nombres[indice]}\t\t{edades[indice]}\t{generos[indice]}\t{estaturas[indice]}\t\t{DNIs[indice]}")

    continuar = input("Desea continuar? si - no: ").lower()
    if continuar == "no":
        break

#Busqueda con carga secuencial
def buscar_datos(DNIs:list, dni:int) -> int: #devuelve el indice de la pesona
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
    edades[i] = input("Edad: ")
    generos[i] = input("Genero: ")
    estaturas[i] = input("Estatura: ")
    DNIs[i] = input("DNI: ")

for i in range (len(nombres)):
    print(f"{nombres[i]}\t\t {edades[i]} \t {generos[i]} \t {estaturas[i]} \t\t {DNIs[i]}")

while True:
    dni = int(input("Ingrese el DNI: "))
    indice = buscar_datos(DNIs, dni) #encontrado = indice
    if indice == None:
        print("DNI INEXISTENTE")
    else:
        print("NOMBRE\t\tEDAD\tGENERO\tESTATURA\tDNI")
        if len(nombres[indice]) > 7:
            print(f"{nombres[indice]}\t{edades[indice]}\t{generos[indice]}\t{estaturas[indice]}\t\t{DNIs[indice]}")
        else:
            print(f"{nombres[indice]}\t\t{edades[indice]}\t{generos[indice]}\t{estaturas[indice]}\t\t{DNIs[indice]}")

    continuar = input("Desea continuar? si - no: ").lower()
    if continuar == "no":
        break

def cargar_datos_secuencial(nombres: list, edades: list, generos: list, estructuras: list, DNIs: list, tamano:int) -> None:
    for i in range (tamano):
        nombres[i] = input("Nombre: ")
        while nombres[i] == "x":
            nombres[i] = input("Nombre: ")
    
    edades[i] = int(input("Edad: "))
    while edades[i]<0 or edades[i]>100:
        edades[i] = int(input("Edad: "))
    generos[i] = input("Genero: ")
    estaturas[i] = input("Estatura: ")
    DNIs[i] = input("DNI: ")

def imprimir_dato(nombres: list, edades: list, generos: list, estructuras: list, DNIs: list, indice:int) -> None:
    print(f"{nombres[indice]}\t\t{edades[indice]}\t{generos[indice]}\t{estaturas[indice]}\t\t{DNIs[indice]}")

def imprimir_datos(nombres: list, edades: list, generos: list, estructuras: list, DNIs: list, tamano:int) -> None:
    for i in range(tamano): 
        imprimir_dato(nombres,edades,generos,estaturas,DNIs, i)
     

nombres = ["x", "x", "x"]
edades = [0, 0, 0]
generos = ["x", "x", "x"]
estaturas = [0, 0, 0]
DNIs = [0, 0, 0]
tam = len(nombres)

cargar_datos_secuencial(nombres, edades, generos, estaturas, DNIs, tam)
imprimir_datos(nombres, edades, generos, estaturas, DNIs, tam)
