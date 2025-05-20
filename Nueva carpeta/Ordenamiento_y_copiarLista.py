#Ordenamiento

numeros = [4,3,1,5,2]

print(numeros)

def funcion_orden(lista:list) -> list: #funcion que me ordena una lista

    for i in range(0, len(lista)-1, 1):
        for j in range(i+1,len(lista),1):
            if lista[i]>lista[j]:
                numero_auxiliar = lista[i]
                lista[i]=lista[j]
                lista[j]=numero_auxiliar

funcion_orden(numeros)
print(numeros)

#copiar lista

def copiar_lista(lista:list) -> list:
    numeros_original = [-1]*len(lista)
    for i in range(len(lista)):
        numeros_original[i]=lista[i]
    return numeros_original