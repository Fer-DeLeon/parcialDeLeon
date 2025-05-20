def mostrar_datos(lista_a:list, lista_b:list, lista_c:list) -> None:
    for i in range(len(lista_a)):
        if len(lista_a[i]) < 8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}")
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")

def copiar_lista(lista_a:list, lista_b:list, lista_c:list) -> list:
    nombres_originales = [-1]*len(lista_a)
    edades_originales = [-1]*len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i]=lista_a[i]
        edades_originales[i]=lista_b[i]

    return nombres_originales, edades_originales

def funcion_orden_ascendente(lista_a:list, lista_b:list, lista_c:list) -> list:

    for i in range(0, len(lista_a)-1, 1):

        for j in range(i+1,len(lista_a), 1):
    
            if lista_c[i]> lista_c[j]: #para cambiar a descendente cambio el signo > por <
                edad_auxiliar = lista_b[i]
                lista_b[i]= lista_b[j]
                lista_b[j]= edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= nombre_auxiliar

                genero_auxiliar = lista_a[i]
                lista_a[i]= lista_a[j]
                lista_a[j]= genero_auxiliar

#2 criterio de ordenamiento: en el caso de que los generos son iguales, veo el tema del nombre:
#Saco el tema del genero porque ya estoy diciendo que son iguales, por lo cual no voy a intercambiarlos entre si.

            elif lista_c[i] == lista_c[j]:
                if lista_a[i]> lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i]= lista_b[j]
                    lista_b[j]= edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i]= lista_a[j]
                    lista_a[j]= nombre_auxiliar

def ordenar(lista_a:list, lista_b:list, lista_c:list, modo = 1) -> None:

    for i in range(0, len(lista_a)-1, 1):

        for j in range(i+1,len(lista_a), 1):
    
            if lista_c[i]> lista_c[j] and modo == 1 or lista_c[i]< lista_c[j] and modo == 2: 
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
                if lista_a[i]> lista_a[j] and modo == 1 or lista_a[i]< lista_a[j] and modo == 2:
                    edad_auxiliar = lista_b[i]
                    lista_b[i]= lista_b[j]
                    lista_b[j]= edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i]= lista_a[j]
                    lista_a[j]= nombre_auxiliar