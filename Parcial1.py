'''Una matriz de 30 filas por 5 columnas
Fila:estudiantes. 
Columnas:Materias. 
Interseccion notas entre 1 y 10

Hay que hacer:
Lista de nombre de estudiantes
Lista de generos de los estudiantes (F,M,X)
Una lista de legajos de los estudiantes: numero entero de cinco digitos

1. Realizar la carga de los datos en la matriz y en cada una de las listas.
Validar cada dato.

2. Mostrar la matriz completa de calificaciones + las 3 listas. Realizar
una funcion que muestre uno y otra que muestre todos.

3. Calcular el promedio (con una funcion) de cada estudiante y guardarlo en una nueva lista.

4. Ordenar y mostrar los datos de los estudiantes por promedio de manera Desc. (Con funcion la cual pueda ordenar ASC O DESC de acuerdo a un parametro)

5. Mostrar la/s materia/s con mayor promedio. (Funcion para mostrar todas y otra para mostrar una)

6. Mostrar todos los datos de un estudiante por legajo: Realizar funcion de busqueda.
Realizar una funcion que muestre uno y otra que muestre todos.

7. SALIR del programa
'''

from MIs_funciones_2 import*

#Ejemplo de lista 
'''mi_lista = [4,9,3,7,1]

for i in range(len(mi_lista)):
    print(mi_lista[i])
'''
#Ejemplo de matriz
'''
matriz = [[2,4,5,8],
          [6,3,1,9]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print("")
'''

nombre = [Ana, Jose, Pepe, Fer, Nico, Rodri, Maria, Luz, Sofia, Beni, Marta, Eri, Lore, Nico, Ariel, Gise, Lucho, Pablo, Paula, Vivi, Vale, ]
materia_1 = [] * 30
materia_2 = [] * 30
materia_3 = [] * 30
materia_4 = [] * 30
materia_5 = [] * 30

print(len(nombre))

print("NOMBRE\t\tmateria_1\tmateria_2\tmateria_3\tmateria_4\tmateria_5")

mi_matriz = inicializar_matriz(30,5,0)
for i in range(len(mi_matriz)):
        for j in range(len(mi_matriz[i])):
            print(mi_matriz[i][j], end=" ")
        print("")

for i in range(len(nombre)):
    print(f"{nombre[i]}\t\t{materia_1[i]}\t{materia_2[i]}\t{materia_3[i]}\t{materia_4[i]}\t{materia_5[i]}")


'''for index in range(len(nombres)):
    if len(nombres[index]) > 7:
        print(f"{nombres[index]}\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")
    else:
        print(f"{nombres[index]}\t\t{edades[index]}\t{generos[index]}\t{estaturas[index]}")
'''