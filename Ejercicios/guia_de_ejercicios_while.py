#While Estadisticas

'''1) Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.'''
numero = 1
while numero <= 10:
    print (numero)
    numero += 1


'''2) Mostrar 10 repeticiones de números descendentes desde el 10 al 1.'''
numeros = 10
while numeros > 0:
    print(numeros)
    numeros-=1


'''3) Mostrar la suma de los números desde el 1 hasta el 10.'''
suma = 0
numero = 0
while numero <= 10:
    suma = suma + numero
    numero += 1
    print(suma)


'''4) Mostrar la suma de los números pares desde el 1 hasta el 10.'''
suma = 0
numero = 0
while numero <= 10:
    suma = suma + numero
    numero += 2
    print(suma)


'''5) Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.'''
contador = 0
acumulador = 0
while contador < 5:
    numero = int(input("Ingrese un numero: "))
    contador = contador + 1
    acumulador = acumulador + numero
promedio = acumulador / contador
print(f"La suma de los numeros ingresados es: {acumulador}")
print(f"El promedio de los numeros ingresados es {promedio}")


'''6)Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.'''
suma = 0
contador = 0
continuacion = None

while True:
        numero = int(input("Ingrese un numero: "))
        suma = suma + numero
        contador = contador + 1

        continuacion = input("Desea continuar? (Si o No): ")
        while continuacion != "Si" and continuacion != "si" and continuacion != "No" and continuacion != "no":
                continuacion = input ("Error. Desea continuar? (Si o No): ")
        if continuacion == "No" or continuacion == "no":
                break
        
promedio = suma / contador        
print(f"La suma es {suma}")
print(f"El promedio es {promedio}")


'''7)Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.'''
suma = 0
contador = 0
producto = 1

while True:
        numero = int(input("Ingrese un numero: "))
        if numero > 0:
                suma = suma + numero
        elif numero < 0:
                producto = numero * producto

        continuacion = input("Desea continuar? (Si o No): ")
        while continuacion != "Si" and continuacion != "si" and continuacion != "No" and continuacion != "no":
                continuacion = input ("Error. Desea continuar? (Si o No): ")

        if continuacion == "No" or continuacion == "no":
                break
                
print(f"La suma es de los numeros positivos es: {suma}")
print(f"El producto de los numeros negativos es: {producto}")


'''8)Ingresar 10 números enteros. Determinar el máximo y el mínimo.'''
contador = 0
flag = False
while contador < 10:
    numero = int(input("Ingrese un numero: "))
    contador = contador + 1
    if flag == False:
        maximo = numero
        minimo = numero
        flag = True
    if numero > maximo:
          maximo = numero
    if numero < minimo:
          minimo = numero
print (f"El numero maximo es {maximo} y el numero minimo es {minimo}")


'''Integrador:
Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
'''

suma = 0
suma2 = 0
contador = 0
contador_1 = 0
producto = 1
flag = False

while True:
        numero = int(input("Ingrese un numero: "))
        if numero > 0:
            suma = suma + numero
            contador_1= contador_1 + 1
            if flag == False:
                maximo = numero
                flag = True
            if numero > maximo:
                maximo = numero
        elif numero < 0:
                contador = contador + 1
                suma2 = suma2 + numero

        continuacion = input("Desea continuar? (Si o No): ")
        while continuacion != "Si" and continuacion != "si" and continuacion != "No" and continuacion != "no":
                continuacion = input ("Error. Desea continuar? (Si o No): ")

        if continuacion == "No" or continuacion == "no":
                break
        
promedio = suma / contador_1
porcentaje_numeros_negativos = contador * 100 / (contador + contador_1) 
                
print(f"La suma es de los numeros positivos es: {suma}")
print(f"La suma es de los numeros negativos es: {suma2}")
print(f"La cantidad de numeros negativos es {contador}")
print(f"El promedio de los numeros positivos es {promedio}")
print(f"El numero positivo mas grande es {maximo}")
print(f"El porcentaje de numeros negativos con respecto al total es: {porcentaje_numeros_negativos}")
