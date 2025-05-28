from Validaciones.Todas_validaciones import*

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    """la funcion genera una matriz segun la cantidad de filas, columnas y valor que se le indique.
    Args:
        Recibe la cantidad de filas, columnas y el valor que se le dará a todos los numeros de la matriz.
    Returns:
        La matriz generada
    """
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz


def cargar_datos(nombres:list, generos:list, legajos:list, calificaciones:list)-> None:
    """Es una funcion que me permite ingresar los datos de cada estudiante y almanenarlos en listas.
    Args:
        Recibe los nombres, generos, legajos y calificaciones ingresados.
    Return:
        None.
    """
    for i in range(len(nombres)):
        print(f"Estudiante_{i+1}:")

        while True:
            nombre = input("Ingrese nombre: ")
            if validar_nombre(nombre):
                nombres[i] = nombre
                break
            print("Error. El nombre debe contener letras")

        while True:
            genero=input("Ingrese genero F/M/X (en mayuscula): ")
            if validar_genero(genero):
                generos[i]= genero
                break
            print("Error. Ingrese nuevamente el genero que corresponda")
        
        while True:
            legajo = input("Ingrese un legajo de 5 digitos: ")
            if validar_legajo(legajo):
                legajos[i] = int(legajo)
                break
            print("Error. Legajo debe ser un numero de 5 digitos")
        
        for j in range(len(calificaciones[i])):
            while True:
                calificacion = input(f"Calificacion materia {j+1} (entre 1 y 10): ")
                if validar_calificaciones(calificacion):
                    calificaciones[i][j]= int(calificacion)
                    break
                print("Error. La calificacion debe ser un numero entero entre 1 y 10.")


def mostrar_datos(nombres:list, generos:list, legajos:list, calificaciones:list)-> None:
    """Es una funcion que muestra los datos en formato cuadro.
    Args:
        Recibe los datos ingresados: nombres, generos, legajos, calificaciones.
    Returns:
        None
    """
    print("NOMBRE\t\tGENERO\tLEGAJO\tCALIFICACIONES")

    for i in range(len(nombres)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{calificaciones[i]}")
        else:
            print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{calificaciones[i]}")


def mostrar_datos_con_promedios(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list)-> None:
    """Es una funcion que muestra los datos en formato cuadro.
    Args:
        Recibe los datos ingresados: nombres, generos, legajos, promedios, calificaciones.
    Returns:
        None
    """    
    print("NOMBRE\t\tGENERO\tLEGAJO\tPROMEDIOS\tCALIFICACIONES")
    for i in range(len(legajos)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")
        else:
            print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")


def ordenar(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list) -> None:
    """Es una funcion que ordena los parametros a partir de los promedios, de forma descendente(1) o ascendente(2).
    Args:
        Recibe los nombres, legajos, promedios y calificaciones ingresados / el parametro de ordenamiento.
    Return:
        None
    """
    modo_1 = int(input("Inserte el primer parametro de ordenamiento (1.DES / 2. ASC): "))
    modo_2 = int(input("Inserte el segundo parametro de ordenamiento (1.DES / 2. ASC): "))

    for i in range(0, len(nombres)-1, 1):
        for j in range(i+1,len(nombres), 1):
    
            if (promedios[i]> promedios[j] and modo_1 == 2) or (promedios[i]< promedios[j] and modo_1 == 1): 
                
                genero_auxiliar = generos[i]
                generos[i]= generos[j]
                generos[j]= genero_auxiliar

                nombre_auxiliar = nombres[i]
                nombres[i]= nombres[j]
                nombres[j]= nombre_auxiliar

                legajo_auxiliar = legajos[i]
                legajos[i]= legajos[j]
                legajos[j]= legajo_auxiliar

                promedio_auxiliar = promedios[i]
                promedios[i]= promedios[j]
                promedios[j]= promedio_auxiliar

                calificacion_auxiliar = calificaciones[i]
                calificaciones[i]= calificaciones[j]
                calificaciones[j]= calificacion_auxiliar

            elif promedios[i] == promedios[j]:
                if (nombres[i]> nombres[j] and modo_2 == 1) or (nombres[i]< nombres[j] and modo_2 == 2):
                    edad_auxiliar = generos[i]
                    generos[i]= generos[j]
                    generos[j]= edad_auxiliar

                    nombre_auxiliar = nombres[i]
                    nombres[i]= nombres[j]
                    nombres[j]= nombre_auxiliar

def mostrar_datos_ordenados(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list)-> None:
    """Muestra los datos de manera ordenada.
    Arg:
        Toma nombres, generos, legajos, promedios, calificaciones.
    Return:
        None
    """
    ordenar(nombres,generos,legajos,promedios,calificaciones)
    mostrar_datos_con_promedios(nombres, generos, legajos, promedios, calificaciones)


def mostrar_promedios_estudiantes(calificaciones:list, nombres:list)-> list:
    """ Muestra el promedio de los estudiantes. 
    Arg:
        Calificaciones y nombres de los estudiantes.
    Return:
        La lista de los promedios.
    """
    lista_promedios=calcular_promedios_estudiante(calificaciones)

    print("NOMBRES\t\tPROMEDIO")
    for i in range(len(nombres)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{lista_promedios[i]}")
        else:
            print(f"{nombres[i]}\t\t{lista_promedios[i]}")
    
    return lista_promedios
    #for i in range(len(lista_promedios)):
        #promedio = lista_promedios[i]
    #print (f"{nombres[i]} tiene promedio {promedio}")        
    


def calcular_promedios_estudiante(calificaciones:list)-> list:
    """Calcula el promedio de cada uno de los estudiantes.
    Arg:
        La lista de calificaciones.
    Return:
        La lista de los promedios de cada estudiante.
    """
    lista_promedios = [0] * len(calificaciones)
    for i in range(len(calificaciones)):
        suma = 0
        for j in range(len(calificaciones[i])):
            suma += calificaciones[i][j]
        promedio_un_estudiante = suma / len(calificaciones[i])
        lista_promedios[i]= promedio_un_estudiante
    return lista_promedios


def calcular_promedio_cada_materia(calificaciones:list)->list:
    """Calcula el promedio de cada materia.
    Args:
        Toma las calificaciones de cada estudiante/materia.
    Retunr:
        Promedio de cada materia.
    """
    cantidad_materias = len(calificaciones[0])
    promedio_final = [0] * cantidad_materias

    for i in range(cantidad_materias):
        suma = 0
        for j in range(len(calificaciones)):
            suma += calificaciones[j][i]
        promedio_cada_una = suma / len(calificaciones)
        promedio_final[i]= promedio_cada_una
    return promedio_final

def mostrar_materias_mayor_promedio(calificaciones:list)-> None:
    """Muestra la/s materia/s con mayor promedio.
    Args:
        La lista de calificaciones.
    Return:
        None / Print donde indica cual es la materia con mayor promedio.
    """
    promedios = calcular_promedio_cada_materia (calificaciones)
    mayor_promedio = promedios[0]
    for i in range(1, len(promedios)):
        if promedios[i]>mayor_promedio:
            mayor_promedio=promedios[i]
    
    for i in range(len(promedios)):
        if promedios[i] == mayor_promedio: 
            print(f"La materia con mayor promedio es: Materia_{i+1} con promedio {promedios[i]}%")

def mostrar_desde_legajo(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list)-> None:
    """Muestra los datos de un estudiantes a partir de la busqueda de su legajo.
    Args:
        El nombre, genero, legajo, promedio y calificaciones de un estudiante.
    Return:
        Los datos del estudiante con el legajo buscado o la leyenda que no existe ese legajo
    """
    legajo_ingresado = int(input("Ingrese el numero de legajo a buscar: "))
    encontrados = None

    for i in range(len(legajos)):
        if legajos[i] == legajo_ingresado:
            encontrados = True
            if len(nombres[i]) > 7:
                print("NOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
                print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")
            else:
                print("NOMBRE\t\tGENERO\tLEGAJO\tPROMEDIO\tCALIFICACIONES")
                print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")

    if encontrados == None:
        print("Legajo inexistente")


def mostrar_repeticion_notas(calificaciones: list)-> None:
    """Muestra la cantidad de veces que se repite cada una de las notas del 1 al 10 en una materia en particular.
    Args:
        Calificaciones de los estudiantes.
    Return:
        Lista de 10 elementos donde muestra cuanto se repite cada uno de las notas del 1 al 10.
    """
    numero_valido = False
    numero_materia = int(input("Ingrese un numero de materia: "))
    numero_valido = validar_numero_materia(numero_materia)
    if numero_valido == True:
        repeticion = [0] * 10
        indice_materia = numero_materia - 1
        print("Repitencia de notas: ")
    
        for estudiante in calificaciones:
            nota = estudiante [indice_materia]
            if nota >= 1 and nota <= 10:
                indice_nota = nota - 1
                repeticion[indice_nota] += 1
        print("NOTA 1\tNOTA 2\tNOTA 3\tNOTA 4\tNOTA 5\tNOTA 6\tNOTA 7\tNOTA 8\tNOTA 9\tNOTA 10")
        print(f"{repeticion[0]}\t{repeticion[1]}\t{repeticion[2]}\t{repeticion[3]}\t{repeticion[4]}\t{repeticion[5]}\t{repeticion[6]}\t{repeticion[7]}\t{repeticion[8]}\t{repeticion[9]}")
    else:
        print("Error. El numero ingresado de materia no es correcto.")

def menu(opciones:str)-> int:
    """Es una funcion que me muestra las opciones posibles, para poder elegir una de ellas.
    Args:
        La lista de las opciones posibles.
    Return:
        La opcion elegida.
    """
    print(opciones)
    opcion = int(input("Elija una opcion: "))

    return opcion

'''
def impimir_un_dato(nombre:str, genero:str, legajo:str, calificaciones: list):
    print(f"{nombre}\t{genero}\t{legajo}\t{calificaciones}")


def buscar_legajo(legajo_buscado: int, legajos:list)-> int:
    legajo_encontrado = -1
    for i in range (len(legajos)):
        if legajos[i] == legajo_buscado:
            legajo_encontrado = i 
    return legajo_encontrado
'''