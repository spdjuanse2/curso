import math
#imprt math es para usar una clase ya pre definida de python

#es un bucle indeterminado es decir no se puede decidir su longitud o las veces que se ejecute
respuesta1=0

while respuesta1==0:
    respuesta=str(input("Quieres ser mi duo w.w? "))
    if respuesta=="si":
        respuesta1=respuesta1+1

print("sabia que dirias si ")
print("la respuesta fue" + str(respuesta1))

#ejercisio while

print("Bienvenido a la aplicacion para conoser la raiz cuadrada")
numero=int(input("inserte un numero:" ))

#el math.sqrt() funciona para sacar la raiz cuadrada
def raizcuadrada(numero):
    raiz=math.sqrt(numero)
    print("la raiaz cuadrada del numero es: " + str(raiz))

while numero<0:
    print("el numero ingresado es negativo por lo que no es posible sacarle raiz inserte un numero nuevamente")
    numero=str(input("inserte un numero: "))

if (numero>0):
    raizcuadrada(numero)