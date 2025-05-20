from Mis_funciones import*

nombres = ["agustina", "brenda", "hernan", "marcela", "franco"]
edades = [9, 40, 30, 20, 10]
generos = ["F", "F", "M", "X", "M"]


print("Datos desordenados")
mostrar_datos(nombres,edades,generos)

ordenar_ascendente(nombres, edades, generos)
print("\n\nDatos Ordenados ASC")
mostrar_datos(nombres,edades,generos)

ordenar_descendente(nombres, edades, generos)
print("\n\nDatos Ordenados DESC")
mostrar_datos(nombres,edades,generos)

ordenar(nombres, edades, generos, 2, 2)
print("\n\nDatos Ordenados")
mostrar_datos(nombres,edades,generos)

ordenar(nombres, edades, generos, 1, 2)
print("\n\nDatos Ordenados")
mostrar_datos(nombres,edades,generos)