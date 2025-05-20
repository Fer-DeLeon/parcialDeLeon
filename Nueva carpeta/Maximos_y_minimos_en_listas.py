#Buscar maximos y minimos en listas:
def maximos_lista(lista):
    maximo=lista[0]
    for i in range(len(lista)):
        numero = lista[i]
        if numero > maximo: 
            maximo = numero
    posiciones = [-1]*len(lista)
    contador = 0
    for i in range(len(lista)):
        if lista[i] == maximo:
            posiciones[contador] = i
            contador += 1
    return posiciones

lista = [2,140,6,8,140,7,80,140]

posiciones = maximos_lista(lista)
contador = 0

for dato in posiciones:
    if dato > -1:
        contador += 1

maximos = [-1] * contador

j = 0
for i in range (len(posiciones)):
    if posiciones[i] > -1:
        maximos[j] = posiciones[i]
        j += 1

print(maximos)