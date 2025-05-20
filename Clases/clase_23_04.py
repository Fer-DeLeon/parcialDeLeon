

''' 13) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.'''
#opcion 1
def numero_entero() -> int:

    num = int(input("Ingrese un numero entero: "))
    while type(num) != int:
        num = int(input("Error. Ingrese un numero entero valido: "))

    return num

print (numero_entero())

#opcion 2
dato = "1"
print(ord(dato)) #sale 49

print(chr(49)) #sale uno 


#tabla de codigo Asky- ver- opcion 3.
#un digito
numero = input("Ingresa un numero de un digito: ")

while ord(numero) < 48 or  ord(numero) > 57:
    numero = input(["Error. Ingrese un numero de un digito"])

#mas de un digito- Validar que el ingreso sea un numero entero (que no haya letras)

def verifica_dato_numerico(cadena : str) -> bool:
    flag = True
    for elemento in cadena: 
        if ord(elemento) < 48 or  ord(elemento) > 57:
            flag = False
            break

    return flag 

dato2 = input("Ingresar un dato numerico: ")

es_numero = verifica_dato_numerico(dato2)

while es_numero == False:
    dato2= input("Error. Ingresar un dato numerico: ")
    es_numero = verifica_dato_numerico(dato2)

print(verifica_dato_numerico(dato2))

dato2 = int(dato2)

print(dato2)



