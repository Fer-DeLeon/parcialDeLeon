'''
from Funciones.Mis_funciones_parcial import*
from Validaciones.Todas_validaciones import*

calificaciones = inicializar_matriz(4,5,0)
nombres = [""] * 4
generos = [""] * 4
legajos = [0] * 4

nombres = ["Ana", "Jose", "Sofia", "Andy"]
generos = ["F", "M", "F", "X"]
legajos = [10001, 10002, 10003, 10004, 10005]
calificaciones = [[5, 7, 7, 8, 9],
                  [6, 9, 9, 10, 10],
                  [7, 7, 8, 8, 10],
                  [3, 5, 5, 6, 7],
                  [9, 10, 10, 9, 9]]

datos_cargados= False
#datos_cargados = True
promedios = None
error = "Debe ingresar los datos del estudiante en primer lugar."

while True:
    print("MENU")
    print("1. Insertar nombre, genero, legajo y calificaciones: ")
    print("2. Mostrar datos")
    print("3. Ver promedios")
    print("4. Ordenar promedios")
    print("5. Materia con mayor promedio")
    print("6. Mostrar informacion mediante el legajo")
    print("7. Salir")
    elegir = input("Inserte una opcion: ")

    match elegir: 
        case "1":
            cargar_datos(nombres, generos, legajos, calificaciones)
            datos_cargados = True
        case"2":
            if datos_cargados == True:
                imprimir_datos(nombres, generos, legajos, calificaciones)
            else:
                print(error)
        case "3":
            if datos_cargados:
                promedios = ver_promedios_estudiantes(calificaciones)
            else: 
                print(error)
        case "4":
            if datos_cargados and promedios != None:
                mostrar_datos_ordenados(nombres, generos, legajos, promedios, calificaciones, orden)
            else: 
                print(error)
        case "5":
            if datos_cargados:
                mostrar_materias_mayor_promedio(calificaciones)
            else: 
                print(error)
        case "6":
            if datos_cargados and promedios != None:
                encontrar_legajos(nombres, generos, legajos, promedios, calificaciones)
            else:
                print(error)
        case "7":
            print("Muchas gracias")
        case _:
            print("Error. Ingrese un numero perteneciente al menu")
            '''

def validar_nombre(cadena:str)-> bool:
    es_nombre = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 97) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <=122):
            contador_caracteres = contador_caracteres -1
        contador_caracteres += 1
    if contador_caracteres == len(cadena):
        es_nombre = True
    return es_nombre

