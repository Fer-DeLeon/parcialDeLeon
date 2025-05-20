"""Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
"""
suma1 = 0
suma2 = 0

while True:
    numero = int(input("Ingrese un numero: "))
    if int(numero) < 0:
        suma1 = int(numero) + suma1
    if numero > 0:
        suma2 = int(numero) + suma2
    continuacion = input("¿Desea continuar? S | N: " )
    while continuacion != "S" and continuacion != "s" and continuacion != "N" and continuacion !="n":
        continuacion = input("ERROR. ¿Desea continuar? S | N: ")

    if continuacion == "N" or continuacion == "n":
        break

#cantidad de numeros negativos
promedio_positivos = suma2 / #cantidad de numeros positivos
#calcular el positivo mas grande.
porcentaje_negativos = #cantidadnegativos * 100 / total de numeros
print(f"La suma de los numeros negativos es: {suma1}")
print(f"La suma de los numeros positivos es: {suma2}")
 
