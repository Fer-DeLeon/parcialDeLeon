from Funciones.Mis_funciones_parcial import*
from Validaciones.Todas_validaciones import*
'''
calificaciones = inicializar_matriz(4,5,0)
nombres = ["x"] * 4
generos = ["x"] * 4
legajos = [0] * 4
'''
nombres = ["Ana", "Jose", "Sofia", "Andy", "Fer", "Nico", "Erica", "Lorena", "Andres", "Ariel", "Pablo", "Liliana", "Emilce", "Paula", "Paula", "Claudia", "Benito", "Luca", "Lorenzo", "Sofia", "Martina", "Iara","Julieta", "Nina", "Alina", "Nicolas", "Paloma", "Valentino", "Antonia", "Fermin"]
generos = ["F", "M", "F", "X", "F", "X", "F", "F", "M", "M", "M", "F", "F", "F", "F", "F", "M", "M", "M", "F", "F", "F", "F", "F", "F", "M", "F", "M", "F", "X"]
legajos = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029]
calificaciones = [[5, 7, 7, 9, 9],[6, 7, 8, 7, 8],[7, 8, 9, 9, 10],[4, 6, 9, 9, 9],[5, 6, 7, 8, 9],[1, 2, 3, 4, 4],[4, 4, 7, 7, 9],[5, 5, 6, 7, 7],
                  [4, 5, 10, 10, 10],[2, 4, 4, 5, 6],[9, 10, 10, 10, 10],[8, 9, 9, 10, 9],[9, 9, 8, 10, 10],[7, 9, 9, 10, 10],[8, 8, 8, 9, 8],
                  [7, 7, 8, 7, 7],[7, 7, 10, 8, 1],[9, 9, 8, 7, 8],[2, 1, 4, 3, 2],[4, 4, 6, 5, 5],[9, 9, 8, 7, 9],[8, 8, 8, 8, 9],[7, 7, 7, 8, 6],
                  [6, 5, 7, 7, 7],[7, 6, 6, 5, 4],[5, 4, 8, 7, 7],[9, 9, 10, 9, 10],[6, 9, 9, 10, 10],[7, 7, 8, 10, 10],[3, 5, 5, 7, 7]]

carga_de_datos = True
#carga_de_datos = False
promedios = None
error = "Error. Para realizar esta opcion primero debe cargar los datos."

while True:
    opcion_elegida = menu("1.Cargar datos\n2.Ver datos cargados\n3.Ver promedios de estudiantes\n4.Ver promedios ordenados\n5.Ver materia/s con mayor promedio\n6.Ver informacion mediante legajo\n7.Ver repitencia de calificaciones\n8.Salir")

    match opcion_elegida: 
        case 1:
            cargar_datos(nombres, generos, legajos, calificaciones)
            carga_de_datos = True
        case 2:
            if carga_de_datos == True:
                mostrar_datos(nombres, generos, legajos, calificaciones) 
            else:
                print(error)
        case 3:
            if carga_de_datos == True:
                promedios = mostrar_promedios_estudiantes(calificaciones, nombres)
            else: 
                print(error)
        case 4:
            if carga_de_datos == True and promedios != None:
                mostrar_datos_ordenados(nombres, generos, legajos, promedios, calificaciones)
            else: 
                print(error)
        case 5:
            if carga_de_datos == True:
                mostrar_materias_mayor_promedio(calificaciones)
            else: 
                print(error)
        case 6:
            if carga_de_datos == True and promedios != None:
                mostrar_desde_legajo(nombres, generos, legajos, promedios, calificaciones)
            else:
                print(error)
        case 7:
            if carga_de_datos == True:
                mostrar_repeticion_notas(calificaciones)
        case 8:
            print("Muchas gracias")
            break
        case _:
            print("Error. Ingrese un numero perteneciente al menu")
            