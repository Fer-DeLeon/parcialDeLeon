'''1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.'''
def ingresar_numero () -> int:
    """
    """
    numero = int(input("Ingresar un numero: "))
    return numero
print(ingresar_numero())


'''2) Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.'''
def integresar_numero () -> float:
    """
    """
    numero = float(input("Ingresar un numero: "))
    return numero
print(ingresar_numero())


'''3) Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.'''
def ingresar_cadena () -> str:
    """
    """
    cadena = input("Ingresar una cadena: ")
    return cadena
print(ingresar_cadena())


'''4) Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.''' 
def Calcular_area_rectangulo (b,h):
    area = b*h
    return area
print (Calcular_area_rectangulo(10,5))


'''5) Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.'''
def calcular_area_circulo (radio):
    area = 3.14 * (radio**2)
    return area 
print (calcular_area_circulo (5))


''' 6) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.'''
def verificacion_numero_par_impar (n):
    if n == 0:
        print("Cero no es par ni impar")
    elif n%2 == 0:
        print ("Es par")
    else:
        print ("Es impar")
verificacion_numero_par_impar(8)


''' 7) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.'''
def verificar_numero_true_false(numero):
    verificacion = False
    if numero % 2 == 0:
        verificacion = True
    return verificacion

print(verificar_numero_true_false(8))


''' 8) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.'''
def encontrar_maximo (a,b,c):
    #determino si los tres numeros son iguales
    if a== b and a == c:
        numero_mas_grande = a
        #determino si los tres numeros no son iguales
    else:
        #determino si uno de los tres es mayor
        if a > b and a > c:
            numero_mas_grande = a
        elif b>c:
            numero_mas_grande = b
        elif c>a and c>b:
            numero_mas_grande = c
        #dos iguales y el mayor es uno de los iguales
        elif a==b and a>c or a==c and a>b:
            numero_mas_grande = a
        elif b == c and b > a or b == a and b >c:
            numero_mas_grande = b
        elif c == a and c>b or c == b and c>a:
            numero_mas_grande = c
        #dos iguales y el mayor es el que no es igual
        elif a== b and c > a:
            numero_mas_grande = c
        elif a == c and b > c:
            numero_mas_grande = b
        else:
            numero_mas_grande = a        

    return numero_mas_grande
print(encontrar_maximo(3,2,3))


''' 9) Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.'''
def calcular_potencia (a,b):
    potencia = a ** b
    return potencia
resultado = calcular_potencia(3,3)
print(resultado)


''' 10) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.'''
numero = int(input("Ingrese un numero: "))
if numero % b = 0:
    print (f"{numero} no es numero primo")
else:
    print(f"{numero} es un numero primo")

''' 11) Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y 
un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.'''

''' 12) Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) 
para definir el rango de multiplicación. Por defecto es del 1 al 10.'''
def tabla_de_multiplicar (a,b,c):
    
''' 13) Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.'''

def numero_entero() -> int:

    num = int(input("Ingrese un numero entero: "))
    while type(num) != int:
        num = int(input("Error. Ingrese un numero entero valido: "))

    return num

print (numero_entero())