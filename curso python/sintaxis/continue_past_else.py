#continue se usa para saltaar lineas de codigo una vez se cumpla la condicion
nombr=str(input("ingrese su nombre completo: "))
num_leters=0

for i in nombr:

    if i==" ":
        continue
    num_leters+=1


print(num_leters)

#past se usa para darle un valor nulo es decir como si no existiera se usa para dejar el trabajo en continuara
def adicion():
    pass #se implementara mas adelante


#else

correo=str(input("ingrese su correo electreonico: "))
existe=False


for i in correo:
    if i=="@":
        existe=True
        break
else:
    existe=False

if existe==True:
    print("el correo es correcto.")
else:
    print("el correo es incorrecto.")