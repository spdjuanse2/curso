import math

def raiz_cuadrada():

    if n1<0:
        raise ValueError("el numero ingresado es negativo ")
    else:
        return math.sqrt(n1)


n1=float(input("ingrese el numero del que quiere conocer la raiz cuadrada: "))

try:
    print(raiz_cuadrada())

except ValueError as NumeroNegativoErros:
    print("NumeroNegativoError")

print("el programa se completo con exico. ")
