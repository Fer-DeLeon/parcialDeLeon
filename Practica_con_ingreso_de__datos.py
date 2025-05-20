from MIs_funciones_2 import*

nombres = [0] * 30
materia_1 = [0] * 30
materia_2 = [0] * 30
materia_3 = [0] * 30
materia_4 = [0] * 30
materia_5 = [0] * 30
generos = [0] * 30
legajos = [0] * 30

for i in range(len(nombres)):
    nombres = input(f"Ingrese nombre del alumno: ")
    verificacion_nombre = Verificar_nombre(nombres)
    materia_1 = int(input("Ingrese notas de la materia_1: "))
    materia_2 = int(input("Ingrese notas de la materia_2: "))
    materia_3 = int(input("Ingrese notas de la materia_3: "))
    materia_4 = int(input("Ingrese notas de la materia_4_ "))
    materia_5 = int(input("Ingrese notas de la materia_5: "))
    generos = input("Ingrese el genero: ")
    legajos = int(input("Ingrese numero de legajo: "))

print("Materia_1\tMateria_2\tMateria_3\tMateria_4\tMateria_5")

mi_matriz = inicializar_matriz(30,5,0)

for i in range(len(nombres)):
    print(f"{materia_1[i]}\t\t{materia_2[i]}\t\t{materia_3[i]}\t\t{materia_4[i]}\t\t{materia_5[i]}")

verificacion_nombre = Verificar_nombre(nombres)
print(verificacion_nombre)