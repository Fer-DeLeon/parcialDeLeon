from Paquete_ejemplo.Funciones import * #Deberia hacerlo con el Main de afuera del paquete.

operacion = input("Ingrese que operacion desea realizar(1 suma, 2 resta, 3 multiplicacion y 4 division): ")
a = int(input("Ingrese un numero: "))
b= int(input("Ingrese otro numero: "))

match operacion:
    case "1":
        resultado1 = sumar (a,b)
    case "2":
        resultado1 = restar (a,b)
    case "3":
        resultado1 = multiplicar (a,b)
    case "4":
        if b==0:
            print("Error. El divisor no puede ser cero")
        else:
            resultado1 = dividir (a,b)
    case _:
        print("Error. Ingrese nuevamente el numero correspondiente: ")

print (f"El resultado de la cuenta es: {resultado1}")