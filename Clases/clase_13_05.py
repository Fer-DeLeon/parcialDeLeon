#suma de matrices
matriz_1 = [[1,3,5],
             [5,7,5]]
matriz_2 = [[2,4,6],
             [6,8,9]]
def suma_de_matrices(matriz_1:list, matriz_2:list)->list:
    resultado = [[0,0,0],
                  [0,0,0]]
    for filas in range (len(matriz_1)):
        for columnas in range(len(matriz_2[filas])):
            resultado[filas][columnas] = matriz_1[filas][columnas] + matriz_2[filas][columnas]

        return resultado
    
llamada = suma_de_matrices (matriz_1, matriz_2)
print(llamada)


#producto por un escalar
def escalar_matriz(matriz_1:list, escalar:int) -> list:
    matriz_resultado = inicializar_matriz(len(matriz_1), len(matriz_1[0]), 0)
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            matriz_resultado[i][j]= matriz_1 [i][j] * escalar
        return matriz_resultado
    

#multiplicacion de matrices


def multiplicacion_de_matrices(matriz_1: list, matriz_2: list) -> list:

    matriz_nueva = inicializar_matriz(2, 2, 0)
    suma_valores = 0

    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            valor_multiplicado = matriz_1[i][j] * matriz_2[j][i]
            suma_valores += valor_multiplicado
        matriz_nueva[i][j] = suma_valores
    return matriz_nueva


#Palindromo

#De todo hay GDB EN FAVORITOS- Multiplicacion de matrices no lo termino.
