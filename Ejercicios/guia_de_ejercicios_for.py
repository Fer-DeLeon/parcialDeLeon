'''1) Mostrar los números ascendentes desde el 1 al 10:'''
lista = list(range(1,11,1))
print(lista)

'''2) Mostrar los números descendentes desde el 10 al 1'''
lista = list(range(10,0,-1))
print(lista)


'''3) Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.'''
numero= int(input("Ingresar un numero: "))
lista = list(range(0,numero+1,1))
print(lista)


'''4) Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
	5 x 0 = 0
	5 x 1  = 5
	5 x 2 = 10
	5 x 3  = 15 …'''
numero= int(input("Ingresar un numero: "))
lista = list(range(0,1000,numero))
print(lista)


'''5) Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.'''
contador = 0
suma = 0
for contador in range (10):
    numero= int(input("Ingrese un numero: "))
    contador = contador + 1
    suma = suma + numero
    if numero == 0:
        break
promedio = suma / contador
print(f"La suma de los numeros es {suma} y el promedio es {promedio}")


'''6) Imprimir los números múltiplos de 3 entre el 1 y el 10.'''
lista = list(range(0,10,3))
print(lista)

'''7) Mostrar los números pares que hay desde la unidad hasta el número 50.'''
lista = list(range(0,51,2))
print(lista)

'''8) Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:'''



'''9) Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.'''

numero = int(input("Ingresa un numero: "))
lista = list(range(0,numero,1))
if numero % lista == 0:
    print(lista)

'''10) Ingresar un número. Determinar si el número es primo o no.'''



'''11) Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron. '''

