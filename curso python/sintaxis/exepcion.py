
def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2


def divi(num1,num2):
    try:
        return num1/num2


    except ZeroDivisionError:
        print("no se puede dividir entre 0 ")

while True:
    try:
        op1=int(input("ingrese el primer numero: "))
        op2=int(input("ingrese el segundo numero: "))

        break
    except ValueError:
        print("porfavor ingrese un valor numerico")


operacion=str(input("ingrese respectivamente las palabras divicion,resta,multiplicacion,suma: "))
dato=operacion.lower()

if dato=="suma":
    print(suma(op1,op2))

elif dato=="resta":
    print(resta(op1,op2))

elif dato=="multiplicacion":
    print(multi(op1,op2))

elif dato=="divicion":
    print(divi(op1,op2))

else:
    print("no ingreso el parametro esperado error de sisteme")
