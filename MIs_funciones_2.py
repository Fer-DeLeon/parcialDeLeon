def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas

        matriz += [fila]

    return matriz

def ver_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
    print("")

def cargar_matriz_secuencialmente(matriz:list)-> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            dato = input("Ingrese un dato: ")
            if Verificar_numero(dato) == True:
                matriz [i][j] = int(dato)
    return matriz

#cargar_matriz_secuencialmente(mi_matriz)

def Verificar_nombre(cadena:str)-> bool:
    es_nombre = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 97) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <=122):
            contador_caracteres = contador_caracteres -1
        contador_caracteres += 1
    if contador_caracteres == len(cadena):
        es_nombre = True
    return es_nombre

def Verificar_legajo(cadena:int)-> bool:
    es_legajo = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
            contador_caracteres = contador_caracteres -1
        contador_caracteres += 1
    if contador_caracteres == len(cadena):
        es_legajo = True
    return es_legajo

def Verificar_genero(cadena:int)-> bool:
    es_genero = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if ord(cadena[i]) == 70 and ord(cadena[i]) == 77:
            contador_caracteres = contador_caracteres -1
        contador_caracteres += 1
    if contador_caracteres == len(cadena):
        es_genero = True
    return es_genero

def Verificar_numero(cadena:int)-> bool:
    es_numero = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
            contador_caracteres = contador_caracteres -1
        contador_caracteres += 1
    if contador_caracteres == len(cadena):
        es_numero = True
    return es_numero

def sacar_promedio(notas:int)->int:
    for i in range(len(notas)):
        suma = suma + notas
        promedio = suma / len(notas)
    return promedio


