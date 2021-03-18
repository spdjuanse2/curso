#bucle determinado
for i in ["pablo","edgar",7]:
    print("Juan",end=", ") #el end sirve para que tras una imprecion se le de un caracter esto se usa normalmente cuando queremos que se muesteren en una misma linea

#ejercisio 1
contador_email=0
correo_electronico=str(input("Ingrese su correo electronico porfavor: "))

for i in correo_electronico:
    if (i=="@" or i=="."):
            contador_email=contador_email+1

if(contador_email==2):
    print("El email es correcto")
else:
    print("El email es incorrecto")

#range se usa pera repetir una sierta cantidad de veces pero los valores tomas puestos desde el 0
for i in range(5):
    print(i)
#en el tipo range se pueden poner 3 valores numericons donde el primero marca desde donde comienza a contar el segundo hasyadonde -1 y el tercero de cuanto en cuanto los piensa contar dentro de ese limite
for i in range(5,50,2):
    print(f"valor de la variable {i}")#el f"" es para unir una variable con un enunciado y las {nos permiten ingresar la variable}
