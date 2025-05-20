#Factorial de un numero
numero = 4
for n in range (numero, 0, -1):
    if n>1:
        if n==numero:
            resultado = n * (n-1)
        else:
            resultado = resultado * (n-1)
print(resultado)

#Segunda opcion
numero = 4
resultado = 1
for n in range (numero,0,-1):
    resultado = resultado * n
print(resultado)

#Usando funcion recursiva
def calcular_factorial (numero):
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    return resultado

numero = int(input("Ingrese un numero"))
factorial = calcular_factorial(numero)
print(factorial)