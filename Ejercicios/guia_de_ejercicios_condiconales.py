# IF ELSE ELIF

'''1) A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, 
considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot'''

altura = float (input("Escribe la altura del jugador en centimetros: "))
if altura < 0: 
    print("Error. Ingrese una altura correcta.")
elif altura < 160:
    print("Jugador es base")
elif altura <= 179:
    print("Jugador es Escolta")
elif altura <= 199:
    print("Jugador es Alero")
else:
    print("Jugador es Ala-Pivot o Pivot")

'''2) Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...'''

nota = int (input("Ingrese la nota: "))
if 6 <= nota <=10:
    print(f"Promocion directa, la nota es {nota}")
elif 4 <= nota < 6:
    print(f"Aprobado, la nota es {nota}")
elif 1 <= nota < 4:
    print(f"Desaprobado, la nota es {nota}")
else:
    print("Error. La nota ingresada no es correcta")

#MATCH

'''1) Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.'''

estacion = input("Ingrese la estacion del año(verano, invierno, primavera u otoño): ")
lugar = input("Ingrese el lugar donde desea viajar: ")
match estacion:
    case "verano":
        if lugar == "Mar del Plata" or lugar == "Cataratas":
            print("Se viaja")
        else: 
            print("No se viaja")
    case "invierno":
        if lugar == "Bariloche":
            print ("Se viaja")
        else:
            print ("No se viaja")
    case "primavera":
        if lugar == "Bariloche":
            print("No se viaja")
        else:
            print("Se viaja")
    case "otoño":
        print("Se viaja")
    case _:
        print("Ingrese una estacion del año correcta")
