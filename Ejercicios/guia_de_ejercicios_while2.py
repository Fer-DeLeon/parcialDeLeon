#While validaciones

'''1) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.'''
contraseña = int(input("Ingrese su contraseña: "))
validacion=123
while contraseña != validacion:
    contraseña = int(input("Error. Ingrese contraseña nuevamente: "))
print("La clave ingresada es correcta")
    

'''2) Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.'''
contraseña = int(input("Ingrese su contraseña: "))
validacion=123
contador = 0
while contraseña != validacion and contador <2:
    contraseña = int(input("Error. Ingrese contraseña nuevamente: "))
    contador = contador + 1
if contraseña == validacion:
    print("La clave ingresada es correcta")
else:
    print("La clave ingresada es incorrecta")


'''3) Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.'''
nota = int(input("Ingresar una nota: "))
while nota < 1 or nota >10:
    nota = int(input("La nota es incorrecta. Vuelve a ingresar una nota: "))
print(f"La nota es {nota}")


'''4)Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.'''
color = input("Ingrese un color: ")
while color != "Rojo" and color != "Verde" and color != "Azul":
    color = input("Error. Ingrese nuevamente un color: ")
print(f"El color elegido es: {color}")


'''Integrador:
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
'''

apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil: ")
numero_de_legajo = int(input("Ingrese su numero de legajo: "))

while edad < 18 or edad > 90:
    edad = int(input("El valor es incorrecto. Vuelva a ingresar su edad: "))

while estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Casado" and estado_civil != "Casada" and estado_civil != "Divorciado" and estado_civil != "Divorciada" and estado_civil != "Viudo" and estado_civil != "Viuda":
    estado_civil = input("Error. Ingrese nuevamente su estado civil: ")

while numero_de_legajo < 1000 or numero_de_legajo > 9999:
    numero_de_legajo = int(input("Error. Ingrese nuevamente su numero de legajo: "))

print(f"Su apellido es {apellido}")
print (f"Su edad es {edad}")
print(f"Su estado civil es {estado_civil}")
print(f"Su numero de legajo es: {numero_de_legajo}")
