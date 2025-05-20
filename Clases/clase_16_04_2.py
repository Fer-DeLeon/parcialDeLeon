def encontrar_maximo (a,b,c):

    if a!= b and a!=c and b!=c:
        if a > b and a > c:
            numero_mas_grande = a
        elif b>c:
            numero_mas_grande = b
        else:
            numero_mas_grande = c
    else:
        numero_mas_grande = a #cualquiera de los tres

    return numero_mas_grande

print(encontrar_maximo(3,2,3)) #problema cuando los numeros son iguales




def encontrar_maximo (a,b,c):
    
    if a== b and a == c:
        numero_mas_grande = a
    elif a!= b and a!=c and b!=c:
        if a > b and a > c:
            numero_mas_grande = a
        elif b>c:
            numero_mas_grande = b
        else:
            numero_mas_grande = c
    elif a==b and a>c or a==c and a>b:
        numero_mas_grande = a
    elif b == c and b > a or b == a and b >c:
        numero_mas_grande = b
    elif c == a and c>b or c == b and c>a:
        numero_mas_grande = c
    elif a== b and c > a:
        numero_mas_grande = c
    elif a == c and b > c:
        numero_mas_grande = b
    else:
        numero_mas_grande = a        

    return numero_mas_grande

print(encontrar_maximo(3,2,3))

#Otra opcion

def encontrar_maximo (a,b,c):
    #determino si los tres numeros son iguales
    if a== b and a == c:
        numero_mas_grande = a
        #determino si los tres numeros no son iguales
    else:
        #determino si uno de los tres es mayor
        if a > b and a > c:
            numero_mas_grande = a
        elif b>c:
            numero_mas_grande = b
        elif c>a and c>b:
            numero_mas_grande = c
        #dos iguales y el mayor es uno de los iguales
        elif a==b and a>c or a==c and a>b:
            numero_mas_grande = a
        elif b == c and b > a or b == a and b >c:
            numero_mas_grande = b
        elif c == a and c>b or c == b and c>a:
            numero_mas_grande = c
        #dos iguales y el mayor es el que no es igual
        elif a== b and c > a:
            numero_mas_grande = c
        elif a == c and b > c:
            numero_mas_grande = b
        else:
            numero_mas_grande = a        

    return numero_mas_grande

print(encontrar_maximo(3,2,3))