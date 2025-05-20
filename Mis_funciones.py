nombres = ["agustina", "brenda", "hernan", "marcela", "franco"]
edades = [9, 40, 30, 20, 10]

def copiar_lista(lista_a:list, lista_b:list) -> list:
    nombres_originales = [-1]*len(lista_a)
    edades_originales = [-1]*len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i]=lista_a[i]
        edades_originales[i]=lista_b[i]

    return nombres_originales, edades_originales

def ordenar_ascendente(lista_a:list, lista_b:list) -> list:

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
ordenar_ascendente(nombres, edades)
print(nombres)
print(edades)


#Agregamos un dato que puede estar repetido= generos
nombres = ["agustina", "brenda", "hernan", "marcela", "franco"]
edades = [9, 40, 30, 20, 10]
generos = ["F", "F", "M", "X", "M"]

def mostrar_datos(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(len(lista_a)):
        if len(lista_a[i]) < 8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}")
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")

print(nombres)
print(edades)
print(generos)

def copiar_lista(lista_a:list, lista_b:list) -> list:
    nombres_originales = [-1]*len(lista_a)
    edades_originales = [-1]*len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i]=lista_a[i]
        edades_originales[i]=lista_b[i]

    return nombres_originales, edades_originales

def ordenar_ascendente(lista_a:list, lista_b:list, lista_c:list) -> list:

    for i in range(0, len(lista_a)-1, 1):
        for j in range(i+1,len(lista_a), 1):
    
            if lista_c[i]> lista_c[j]: #me determina por que valor voy a ordenar
                
                edad_auxiliar = lista_b[i]
                lista_b[i]= lista_b[j]
                lista_b[j]= edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i]= lista_c[j]
                lista_c[j]= genero_auxiliar
#Segundo criterio de ordenamiento
            elif lista_c[i] == lista_c[j]:
                if lista_a[i]> lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i]= lista_b[j]
                    lista_b[j]= edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i]= lista_a[j]
                    lista_a[j]= nombre_auxiliar

print("Datos desordenados")
mostrar_datos(nombres,edades,generos)

ordenar_ascendente(nombres, edades, generos)
print("\n\nDatos Ordenados")
mostrar_datos(nombres,edades,generos)


def ordenar_descendente(lista_a:list, lista_b:list, lista_c:list) -> None:

    for i in range(0, len(lista_a)-1, 1):
        for j in range(i+1,len(lista_a), 1):
    
            if lista_c[i]< lista_c[j]: #me determina por que valor voy a ordenar
                
                edad_auxiliar = lista_b[i]
                lista_b[i]= lista_b[j]
                lista_b[j]= edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i]= lista_c[j]
                lista_c[j]= genero_auxiliar
#Segundo criterio de ordenamiento
            elif lista_c[i] == lista_c[j]:
                if lista_a[i]< lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i]= lista_b[j]
                    lista_b[j]= edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i]= lista_a[j]
                    lista_a[j]= nombre_auxiliar

def ordenar(lista_a:list, lista_b:list, lista_c:list, primer_modo = 1, segundo_modo = 1) -> None:

    for i in range(0, len(lista_a)-1, 1):

        for j in range(i+1,len(lista_a), 1):
    
            if (lista_c[i]> lista_c[j] and primer_modo == 1) or (lista_c[i]< lista_c[j] and primer_modo == 2): 
                #SWAP (intercambio)
                edad_auxiliar = lista_b[i]
                lista_b[i]= lista_b[j]
                lista_b[j]= edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= nombre_auxiliar

                genero_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= genero_auxiliar

            elif lista_c[i] == lista_c[j]:
                if (lista_a[i]> lista_a[j] and segundo_modo == 1) or (lista_a[i]< lista_a[j] and segundo_modo == 1):
                    edad_auxiliar = lista_b[i]
                    lista_b[i]= lista_b[j]
                    lista_b[j]= edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i]= lista_a[j]
                    lista_a[j]= nombre_auxiliar

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial: any) -> list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas

        matriz += [fila]

    return matriz
