#manera 1
def resultado():

    numero1=4
    numero2=5
    print("la suma de los dos numeros es: ")
    print(numero1+numero2)

resultado()
print("codigo x")
resultado()
print("codigo y")
resultado()

#manera 2
numero1=5
numero2=5


def suma(numero1,numero2):

    print("la suma de los dos numeros es: ")
    print(numero1+numero2)

numero3=4
numero4=4

def adicio(numero3,numero4):

    print("la suma de los dos numeros es: ")
    print(numero3+numero4)

suma(numero1,numero2)

adicio(numero3,numero4)


#manera 3

def suma2(num1,num2):

    print("la suma de los dos numeros es: ")
    print(num1+num2)

suma2(4,3)

suma2(30,4)

#manera 6 con return

def multi(num1,num2):

    resultado=num1*num2
    return resultado

print(multi(2,2))

print(multi(5,5))

resultado=multi(6,6)

if resultado<5:
    print("el resultado es menor a 5")
elif resultado>5:
    print("el resultado es mayor a 5")
else:
    print("el resultado es igual a 5")
