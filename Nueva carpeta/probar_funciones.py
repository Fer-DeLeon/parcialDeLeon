'''
#FUNCION SACAR PROMEDIO
def sacar_promedio(notas:list)->int:
    for i in range(len(notas)):
       suma = 0
       suma = suma + notas[i]
    promedio = suma / len(notas)
    return promedio
   
materia_1 = [10, 9, 7, 2, 5, 1, 3, 8, 4, 3, 7, 7, 8, 8, 9, 3, 4, 6, 6, 7, 7, 7, 7, 6, 9, 10, 9, 9, 3, 6]

sacar_promedio(materia_1)
print()


materia_1 = [10, 9, 7, 2, 5, 1, 3, 8, 4, 3, 7, 7, 8, 8, 9, 3, 4, 6, 6, 7, 7, 7, 7, 6, 9, 10, 9, 9, 3, 6]
suma = 0
for i in range(len(materia_1)):
    suma = suma + materia_1[i]

promedio = suma/ len(materia_1)

print(suma)
print(promedio)
'''

'''
#BIEN FUNCION ORDENAR :)
def ordenar(lista_a:list, primer_modo = 1, segundo_modo = 1) -> None: 
    for i in range(0, len(lista_a)-1, 1):
        for j in range(i+1,len(lista_a), 1):
    
            if (lista_a[i]> lista_a[j] and primer_modo == 1) or (lista_a[i]< lista_a[j] and primer_modo == 2): 
                #SWAP (intercambio)
                edad_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= nombre_auxiliar

                genero_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= genero_auxiliar
'''

#FUNCION MOSTRAR MAYOR


#funcion de busqueda por legajo
def buscar_datos(legajo:int) -> str: #devuelve el indice de la pesona
    indice = None
    for i in range (len(legajos)):
        if legajos[i] == legajo:
            print(f"{nombres[i]}\t\t{generos[i]}\t\t{legajos[i]}")
        else:
            print("DNI inexistente")


nombres = ["Ana", "Jose", "Pepe", "Fer", "Nico", "Rodri", "Maria", "Luz", "Sofia", "Beni", "Marta", "Eri", "Lore", "Iara", "Ariel", "Gise", "Lucho", "Pablo", "Paula", "Vivi", "Vale", "Yani", "Ivan", "Agus", "Yesi", "Leo", "Abril", "Mauro", "Fede", "Rafa"]
generos = ["F", "M", "M", "M", "M", "M", "F", "F","F","M","F", "F", "F", "F", "M", "F", "M", "M", "F", "F", "F", "F", "M", "F", "F", "M", "X", "M", "M", "M"]
legajos = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029]

buscar_datos(10013)

