#Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

numeros = 1
while numeros <= 10:
    print (numeros)
    numeros += 1

#Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

numeros = 10
while numeros > 0:
    print(numeros)
    numeros-=1

#Mostrar la suma de los números pares desde el 1 hasta el 10.

suma = 0
numero = 0
while numero <= 10:
    suma = suma + numero
    numero += 2
    print(suma)

#Solicitar el ingreso de 5 números, calcular la suma de los 
# números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

contador = 0
acumulador = 0
while contador < 5:
    numero= int(input("Ingrese un numero: "))
    contador += 1
    acumulador = acumulador + numero 

print("La suma de los numeros es: ", acumulador)
promedio = acumulador / contador
print("El promedio de los numeros es: ", promedio)


#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

#No se como continuarlo

#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

#No se como continuarlo
