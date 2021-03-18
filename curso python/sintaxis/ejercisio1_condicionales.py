#mas lejos que 40 km mas de 2 hermanos y un salario de 20000 dolares
print("Programa de vecas colombia")
distancia=int(input("Porfavor ingrese la distancia en km ala que se encuentra su casa de la escuela: "))
ingresos=int(input("Porfavor ingrese el dinero que entra a su familia cada mes: "))
hermanos=int(input("Porfavor denos el numero de hermanos con el que vive: "))
print(distancia)
print(ingresos)
print(hermanos)

if distancia>40 and ingresos<=20000 and  hermanos>2:
    print("tu eres apto para adquirir la beca.")
else:
    print("tu no puedes adquirir una beca.")
