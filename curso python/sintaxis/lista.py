#las listas pueden ser mixtas es decir pueden variar
nombres=["MARIA","SIMON",3.1,2,"MARIA","MARIA","MARIA"]

print(nombres[0])
#si es ne gativo va de derecha a izquierda
print(nombres[-2])
#sacar una porcion de la lista es decir de cierta cantidad a otra
print(nombres[0:3]);print(nombres[:2]);print(nombres[1:3]);print(nombres[1:])#el 0 es inecesario
#para agregar un dato se usa
nombres.append("malcom")
print(nombres[:])
#append se usa para ponerlo al final de la lista pero insert permite disponer un espacio
nombres.insert(2,"paula")
print(nombres[:])
#para agregar muchos datos a la ves se usa extend
nombres.extend(["minino","niky","nany"])
print(nombres[:])
#si quiero saber en que lugar o posicion esta nany debo usar index pero si se repite el nombre en la lista solo tomara el mas sercano a 0
print(nombres.index("nany"))
#para saber si un elemento existe o no se usa in
print("nany" in nombres)
#para eliminar elementos se usa remove
nombres.remove("nany")
print(nombres[:])
#para eliminar el ultimo elemento de la lista se usa pop
nombres.pop()
print(nombres[:])


#para unir listas se suma como si fueran variables
apellidos=["porras","rodrigez"]
nombres_completos=nombres+apellidos
print(nombres_completos[:])


#el asterisco * replica la totalidad de las tablas dependiendo el numero que le indiques
numeros=[1,2,3,4]*5
print(numeros[:])
#para convertit una lista en tupla se usa tuple
tupla=tuple(numeros)
print(tupla[2])
#para saber cuantos hay repetidos se usa count
print(nombres.count("MARIA"))
#para saber que tan larga es una lista se usa len
print(len(numeros))
#para hacer una lista de un elemento se pone una coma luego de el unico dato
lista=("unico",)
print(len(lista))


#el desempaquetado de lista sirve para darle a una serie de variales el valor de la tupla pero se heredan por orden de iz a dere
desem=["juan",9,4,2002]
name,mes,dia,year=desem
print(name)
print(year)
print(mes)
print(dia)