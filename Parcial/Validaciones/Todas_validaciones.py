def validar_nombre(cadena:str)-> bool:
    """La funcion debe validar lo ingresado como nombre, siendo letras de la a a la z en miniscula y mayuscula. 
    Args:
    Recibe lo ingresado como nombre.
    Return:
    Si lo ingresado es un nombre valido o no (verdadero o falso)
    """
    es_nombre = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if (ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90) or (ord(cadena[i]) >= 97 and ord(cadena[i]) <= 122):
            contador_caracteres += 1
    if contador_caracteres == len(cadena):
        es_nombre = True
    return es_nombre


def validar_legajo(cadena:int)-> bool:
    """La funcion debe validar lo ingresado como legajo, siendo un numero de 5 digitos. 
    Args:
    Recibe lo ingresado como legajo.
    Return:
    Si lo ingresado es un legajo valido o no (verdadero o falso)
    """
    es_legajo = False
    contador_caracteres = 0

    for i in range(len(cadena)):
        if ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57:
            contador_caracteres += 1
    if contador_caracteres == len(cadena) == 5:
        es_legajo = True
    return es_legajo


def validar_genero(cadena:str)-> bool:
    """La funcion debe validar lo ingresado como genero, siendo una letra F, M O X en mayuscula. 
    Args:
    Recibe lo ingresado como genero.
    Return:
    Si lo ingresado es un genero valido o no (verdadero o falso)
    """    
    es_genero = False

    if len(cadena) == 1 and (ord(cadena) == 70 or ord(cadena) == 77 or ord(cadena) == 88):
        es_genero = True
    return es_genero


def validar_calificaciones(cadena:int)-> bool:
    """La funcion debe validar lo ingresado como calificaciones, siendo un numero entre 1 y 10. 
    Args:
    Recibe lo ingresado como calificacion.
    Return:
    Si lo ingresado es una calificacion valido o no (verdadero o falso)
    """    
    es_calificacion = False
    
    if len(cadena) == 1 and ord(cadena) >= 49 and ord(cadena) <= 57:
        es_calificacion = True
    elif len(cadena) == 2:
        for i in range(len(cadena)):
            if ord(cadena[0]) == 49 and ord(cadena[1]) == 48:
                es_calificacion = True
    return es_calificacion

def validar_numero_materia(numero_materia:int)-> bool:
    """La funcion debe validar lo ingresado como materia, siendo un numero entre 1 y 5. 
    Args:
    Recibe lo ingresado como numero de materia.
    Return:
    Si lo ingresado es un numero de materia valido o no (verdadero o falso)
    """    
    numero_valido = False
    if numero_materia >= 1 and numero_materia <= 5:
        numero_valido = True
    return numero_valido

