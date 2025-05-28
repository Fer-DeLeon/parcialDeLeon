nombres = ["Ana", "Jose", "Sofia", "Andy"]
generos = ["F", "M", "F", "X"]
legajos = [10001, 10002, 10003, 10004]
calificaciones = [[6, 9, 9, 10, 10],
                  [6, 9, 9, 10, 10],
                  [7, 7, 8, 8, 10],
                  [3, 5, 5, 6, 7]]


#numero_valido = False

def validar_numero_materia(numero_materia:int)-> bool:
    numero_valido = False
    if numero_materia >= 1 and numero_materia <= 5:
        numero_valido = True
    return numero_valido
#ver = validar_numero_materia(numero_materia)
#print(ver)



def mostrar_repeticion_notas(calificaciones: list)-> list:
    """Muestra la cantidad de veces que se repite cada una de las notas del 1 al 10 en una materia en particular.
    Args:
        Calificaciones de los estudiantes.
    Return:
        Lista de 10 elementos donde muestra cuanto se repite cada uno de las notas.
    """
    repeticion = [0] * 10
    numero_materia = int(input("Ingrese un numero de materia: "))
    numero_valido = validar_numero_materia(numero_materia)
    while numero_valido == False:
        if numero_valido == True:
            numero_materia = int(numero_materia)
        else:
            numero_materia = int(input("Error. Ingrese un numero de materia que sea correcto.")) 

    indice_materia = numero_materia - 1
    print("Repitencia de notas: ")
    
    for estudiante in calificaciones:
        nota = estudiante [indice_materia]
        if nota >= 1 and nota <= 10:
            indice_nota = nota - 1
            repeticion[indice_nota] += 1
    print("NOTA 1\tNOTA 2\tNOTA 3\tNOTA 4\tNOTA 5\tNOTA 6\tNOTA 7\tNOTA 8\tNOTA 9\tNOTA 10")
    print(f"{repeticion[0]}\t{repeticion[1]}\t{repeticion[2]}\t{repeticion[3]}\t{repeticion[4]}\t{repeticion[5]}\t{repeticion[6]}\t{repeticion[7]}\t{repeticion[8]}\t{repeticion[9]}")
        #return repeticion

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
        #return repeticion
    else:
        print("Error. Ingrese un numero de materia que sea correcto.")
    """ 
ver_2 = mostrar_repeticion_notas(calificaciones)
#print(ver_2)