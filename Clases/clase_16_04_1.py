#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def integresar_numero () -> int:
    """
    """
    numero = int(input("Ingresar un numero: "))
    return numero
print(ingresar_numero())


#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def integresar_numero () -> float:
    """
    """
    numero = float(input("Ingresar un numero: "))
    return numero
print(ingresar_numero())


#Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def integresar_cadena () -> str:
    """
    """
    cadena = input("Ingresar una cadena: ")
    return cadena
print(ingresar_cadena())


#Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
def Calcular_area_rectangulo (b,h)
    area = b*h
    return area
print (Calcular_area_rectangulo(10,5))


#Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def calcular_area_circulo (radio)
    area = 3.14 * (radio**2)
    return area 


#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def verificacion_numero_par_impar (n)
    if n == 0:
        print("Cero no es par ni impar")
    elif n%2 == 0:
        print ("Es par")
    else:
        print ("Es impar")
verificacion_numero_par_impar(5)

#Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
def verificar_numero_true_false(numero):
    verificacion = False
    if numero % 2 == 0:
        verificacion = True
    return verificacion

#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo (a,b,c)

    if a!= b and b!=c:
        if a > b and a > c:
            numero_mas_grande = a
        elif b>c:
            numero_mas_grande = b
        else:
            numero_mas_grande = c
    else:
        numero_mas_grande = a #cualquiera de los tres

    return numero_mas_grande

print(encontrar_maximo(3,2,3)) #problema cuando los numeros son iguales

#Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def calcular_potencia (a,b)
    potencia = a ** b
    return potencia

resultado = calcular_potencia(2,3)
print(resultado)

print(calcular_potencia(2,3)) #otra opcion de hacer las lineas 81 y 82.
