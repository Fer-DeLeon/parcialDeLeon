from MIs_funciones_2 import*

nombres = ["Ana", "Jose", "Pepe", "Fer", "Nico", "Rodri", "Maria", "Luz", "Sofia", "Beni", "Marta", "Eri", "Lore", "Iara", "Ariel", "Gise", "Lucho", "Pablo", "Paula", "Vivi", "Vale", "Yani", "Ivan", "Agus", "Yesi", "Leo", "Abril", "Mauro", "Fede", "Rafa"]
materia_1 = [10, 9, 7, 2, 5, 1, 3, 8, 4, 3, 7, 7, 8, 8, 9, 3, 4, 6, 6, 7, 7, 7, 7, 6, 9, 10, 9, 9, 3, 6]
materia_2 = [7, 4, 5, 6, 2, 9, 7, 7, 7, 7, 8, 7, 6, 6, 6, 9, 9, 1, 9, 10, 2, 3, 4, 5, 6, 4, 7, 7, 7, 10]
materia_3 = [9, 9, 9, 4, 5, 6, 5, 5, 7, 1, 7, 6, 6, 8, 8, 8, 9, 9, 10, 3, 4, 5, 6, 7, 7, 7, 7, 6, 9, 10]
materia_4 = [6, 6, 7, 7, 6, 6, 5, 4, 3, 7, 8, 9, 9, 9, 1, 9, 7, 10, 4, 2, 3, 4, 5, 1, 7, 8, 8, 8, 9, 8]
materia_5 = [7, 7, 7, 8, 6, 5, 4, 6, 6, 7, 7, 8, 8, 9, 10, 3, 4, 5, 6, 10, 9, 8, 4, 5, 2, 9, 7, 10, 1, 7]
generos = ["F", "M", "M", "M", "M", "M", "F", "F","F","M","F", "F", "F", "F", "M", "F", "M", "M", "F", "F", "F", "F", "M", "F", "F", "M", "X", "M", "M", "M"]
legajos = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029]

print("Materia_1\tMateria_2\tMateria_3\tMateria_4\tMateria_5")

mi_matriz = inicializar_matriz(30,5,0)

for i in range(len(nombres)):
    print(f"{materia_1[i]}\t\t{materia_2[i]}\t\t{materia_3[i]}\t\t{materia_4[i]}\t\t{materia_5[i]}")

cargar_matriz_secuencialmente(mi_matriz)