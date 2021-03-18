#al igual que una fincion se llama con el def pero se usa en vez de return se usa yield

def numenos_pares(limite):

    x=1


    while x<limite:

        yield x*2

        x=x+1


y=int(input("ingrese el numero de pares que quiere: "))
numeros=numenos_pares(100)
veces=0


if y<100 and y>0:
    while veces<y:
        print(next(numeros))
        veces=veces+1
else:
    print("el numero ingresado o es negativo o sobre pasa el limite." )

#yield fROM FINCIONA COMO SIMPLIFICACION A BUCLE FOR ES USADO PARA ENTRAR EN UN ELEMENTO Y MIMAR MAS A FONDO ES DECIR PAIS CAPITALES

def devuelve_paises(*paises):#el * funciona para decirle al programa que es un numero indefinido de datos o elemantos
    for elementos in paises:
        yield from elementos

letras_de_paises=devuelve_paises("colombia","chile","panama")

print(next(letras_de_paises))
print(next(letras_de_paises))