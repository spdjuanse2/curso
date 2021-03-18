#en las tuplas no se pueden alterar los datos es decir no se eliminan ni agregan estos datos
nombre=("juan","pedro",1,20,1,1,1)
print(nombre[:])
#las tuplas tambien pueden ser listas con list
lista=list(nombre)
print(lista[2])
#para buscar en una tupla tambien se usa in
print(20 in (nombre))
#para saber cuantos hay repetidos se usa count
print(nombre.count(1))
#PARA SABER CUANTOS ELEMENTOS HAY SE USA LEN
print(len(nombre))


#para hacer una tula de un solo elemento se unas una , luego del elemento
tupla=("unica",)
print(len(tupla))


#el desempaquetado de tupla sirve para darle a una serie de variales el valor de la tupla pero se heredan por orden de iz a dere
desem=("juan",9,4,2002)
name,mes,dia,year=desem
print(name)
print(year)
print(mes)
print(dia)
#busqueda con index
print(desem.index(9))