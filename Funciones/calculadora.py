operacion = input("Ingrese que operacion desea realizar(1 suma, 2 resta, 3 multiplicacion y 4 division): ")
a = int(input("Ingrese un numero: "))
b= int(input("Ingrese otro numero: "))

def sumar(a,b):
    resultado = a+b
    return resultado

def restar(a,b):
    resultado = a-b
    return resultado

def multiplicar(a,b):
    resultado = a*b
    return resultado

def dividir(a,b):
    resultado = a/b
    return resultado

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
