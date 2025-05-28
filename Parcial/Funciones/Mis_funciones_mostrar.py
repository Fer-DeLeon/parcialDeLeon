from Funciones.Mis_funciones_parcial import*

def mostrar_datos(nombres:list, generos:list, legajos:list, calificaciones:list)-> None:
    """Es una funcion que muestra los datos en formato cuadro.
    Args:
        Recibe los datos ingresados: nombres, generos, legajos, calificaciones.
    Returns:
        None / La impresion de los datos en formato cuadro.
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
        None / La impresion de los datos en formato cuadro.
    """    
    print("NOMBRE\t\tGENERO\tLEGAJO\tPROMEDIOS\tCALIFICACIONES")
    for i in range(len(legajos)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")
        else:
            print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}\t{promedios[i]}\t\t{calificaciones[i]}")


            def mostrar_datos_ordenados(nombres:list, generos:list, legajos:list, promedios:list, calificaciones:list)-> None:
    """Muestra los datos de manera ordenada.
    Arg:
        Toma nombres, generos, legajos, promedios, calificaciones.
    Return:
        None / Muestra los datos a partir del orden establecido en la funcion ordenar.
    """
    ordenar(nombres,generos,legajos,promedios,calificaciones)
    print("NOMBRE\t\tGENERO\tLEGAJO\tPROMEDIOS\tCALIFICACIONES")
    mostrar_datos_con_promedios(nombres, generos, legajos, promedios, calificaciones)


def mostrar_promedios_estudiantes(calificaciones:list, nombres:list)-> None:
    """ Muestra el promedio de los estudiantes. 
    Arg:
        Calificaciones y nombres de los estudiantes.
    Return:
        La lista de los promedios.
    """
    lista_promedios=calcular_promedios_estudiante(calificaciones)
    for i in range(len(lista_promedios)):
        promedio = lista_promedios[i]

    print("NOMBRES\t\tPROMEDIO")
    for i in range(len(nombres)):
        if len(nombres[i]) > 7:
            print(f"{nombres[i]}\t{lista_promedios[i]}")
        else:
            print(f"{nombres[i]}\t\t{lista_promedios[i]}")
        
        #print (f"{nombres[i]} tiene promedio {promedio}")
    return lista_promedios


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


def mostrar_repeticion_notas(calificaciones: list)-> list:
    """Muestra la cantidad de veces que se repite cada una de las notas del 1 al 10 en una materia en particular.
    Args:
        Calificaciones de los estudiantes.
    Return:
        Lista de 10 elementos donde muestra cuanto se repite cada uno de las notas.
    """
    numero_materia = int(input("¿Que materia quiere calcular?: "))
    repeticion = [0] * 10
    indice_materia = numero_materia - 1
    print("Notas repetidas: ")
    
    for estudiante in calificaciones:
        nota = estudiante [indice_materia]
        if nota >= 1 and nota <= 10:
            indice_nota = nota - 1
            repeticion[indice_nota] += 1
    print("NOTA 1\tNOTA 2\tNOTA 3\tNOTA 4\tNOTA 5\tNOTA 6\tNOTA 7\tNOTA 8\tNOTA 9\tNOTA 10")
    print(f"{repeticion[0]}\t{repeticion[1]}\t{repeticion[2]}\t{repeticion[3]}\t{repeticion[4]}\t{repeticion[5]}\t{repeticion[6]}\t{repeticion[7]}\t{repeticion[8]}\t{repeticion[9]}")
    return repeticion