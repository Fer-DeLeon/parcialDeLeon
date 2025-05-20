numeros = [4,3,1,5,2]
nombres = ["agustina", "brenda", "hernan", "marcela", "franco"]
edades = [9, 40, 30, 20, 10]

print(nombres)
print(edades)

def copiar_lista(lista_a:list, lista_b:list) -> list:
    nombres_originales = [-1]*len(lista_a)
    edades_originales = [-1]*len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i]=lista_a[i]
        edades_originales[i]=lista_b[i]

    return nombres_originales, edades_originales

def funcion_orden_ascendente(lista_a:list, lista_b:list) -> list:

    for i in range(0, len(lista_a)-1, 1):
        for j in range(i+1,len(lista_a), 1):
    
            if lista_b[i]> lista_b[j]:
                edad_auxiliar = lista_b[i]
                lista_b[i]= lista_b[j]
                lista_b[j]= edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= nombre_auxiliar

#copia = copiar_lista(numeros)
funcion_orden_ascendente(nombres, edades)
print(nombres)
print(edades)


#Agregamos un dato que puede estar repetido= generos

from Mis_funciones_07_05 import *

nombres = ["agustina", "brenda", "hernan", "marcela", "franco"]
edades = [9, 40, 30, 20, 10]
generos = ["F", "F", "M", "X", "M"]


print("Datos desordenados")
mostrar_datos(nombres, edades, generos)
funcion_orden_ascendente(nombres, edades, generos)
print("\n\n Datos ordenados")
mostrar_datos(nombres, edades, generos)