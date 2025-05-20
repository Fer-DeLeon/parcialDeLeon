texto = 'PYTHON ES "DIVERTIDO"'
texto2 = texto [0:6]*3
texto3 = texto2 + texto
texto4 = len(texto2)
print(texto4)
for i in range(len(texto2)):
    print('indice', i )
    print(texto2[i])

texto = 'PYTHON ES "DIVERTIDO"'
texto2 = texto [0:6]*3

for i in range(len(texto)):
    texto2 += texto[i]
    print(texto2) #piramide


texto = 'PYTHON ES DIVERTIDO"'
texto2 = []

for i in range(len(texto)):
    texto2 += texto[i]
    print(texto)
print(texto2 == texto)

#Crear una función que reciba una cadena de caracteres  y verificar con una función si tienen números. Además crear otra función si la cadena de caracteres 
# ingresada es un correo electrónico.
#Crear una función que reciba una cadena de caracteres  y verificar con una función si tienen números, es decir verificar sea un nombre. 
# Además crear otra función si la cadena de caracteres ingresada es un correo electrónico.

def verificar_nombre(nombre:list) -> bool:
    nombre = input("Ingrese su nombre: ")

    for i in range(len(nombre)):
        letra = 