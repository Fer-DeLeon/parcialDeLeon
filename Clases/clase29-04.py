numero = 4
for n in range (numero, 0, -1):
    if n>1:
        if n==numero:
            resultado = n * (n-1)
        else:
            resultado = resultado * (n-1)
print(resultado)

#otra opción
numero = 4
resultado = 1
for n in range (numero,0,-1):
    resultado = resultado * n
print(resultado)

#Otro ejercicio

mi_lista = [43, 21, 53, 53, 12]
suma = 0

for i in range (len(mi_lista)):
    suma = suma + mi_lista[i]

promedio = suma / len(mi_lista)
print(mi_lista)
print(suma)
print(promedio)

#Otro ejercicio

mi_lista = [43, 21, 54, 23, 12]
print("Los numeros pares son: ")
for i in range (len(mi_lista)):
    if(mi_lista[i] % 2 == 0):
        print(f"el valor de i: {i} el valor de mi_lista {mi_lista}")

print("Los numeros impares son: ")
for i in range (len(mi_lista)):
    if(mi_lista[i] % 2 != 0):
        print(f"el valor de i: {i} el valor de mi_lista {mi_lista}")

#Otro ejercicio

mi_lista = [0] * 5

for i in range(len(mi_lista)):
    mi_lista[i] = i

print(mi_lista)
