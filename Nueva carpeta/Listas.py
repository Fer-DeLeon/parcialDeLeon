#Suma, promedio, len
mi_lista = [43, 21, 53, 53, 12]
suma = 0

for i in range(len(mi_lista)):
    suma = suma + mi_lista[i]

promedio = suma/ len(mi_lista)
print(mi_lista)
print(suma)
print(promedio)


#Listar los pares y los impares
mi_lista = [43, 21, 54, 12, 23]

print("Los numeros pares son:")
for i in range(len(mi_lista)):
    if(mi_lista[i] % 2 == 0):
        print(f"el valor de i: {i} el valor de mi_lista : {mi_lista[i]}")

print("Los numeros impares son:")
for i in range(len(mi_lista)):
      if(mi_lista[i] % 2 != 0):
           print(f"el valor de i: {i} el valor de mi_lista : {mi_lista[i]}")
