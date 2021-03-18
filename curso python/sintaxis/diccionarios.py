#en los diccionarios se una la clave segida del valor es decir
diccionario={"colombia":"bogota","francia":"paris","españa":"madrid","Estados unidos":"washinto"}
print(diccionario["colombia"])
print(diccionario)
#para agregar datos es de la siguiente manera pero py los sobre escribe es decir si escribo el de agregar dos veces con una clave igual
#y un valor distinto se sobre escribe y el ultimo cambiado sera el valor desicivo
diccionario["Japon"]="medellin"
print(diccionario)
diccionario["Japon"]="Tokio"
print(diccionario)
#para eliminar un dato se usa del
del diccionario["españa"]
print(diccionario)


#los diccionarios funcionan las caves como id y los valores como su resultado
idd={12:"juan","juan":56}
print(idd)



#para unir tulas y listas con el diccionario se hace asi
numeros=[1,2,3,4]*5
desem=("juan",9,4,2002)
dicc={numeros[0]:"juan",numeros[2]:"pablito",desem[0]:"maria",desem[2]:"corazon"}
print(dicc)
#para imprimir un valor espesifico podemos o usar el nombre original es decir 1 o numeros[0]
print(dicc[numeros[0]])
print(dicc[1])
#si queremos que en vez de tomar datos de las tulas y las listas tauga ya en su interior las tulas se hace asi
dicci={12:"jordam",1:"pablo","vip":{"NAME":["kica","pablo","ector","mami-chan"]}}#ESTA ES UN DICCIONARIO QUE TIENE OTRO DICCIONARIO QUE LLEVA UNA TULA
print(dicci)
#PARA IMPRIMIR SOLO LAS CALVES O LOS VALORES SE USAN LAS VARIABLES VALUES KEYS Y PARA CONOSER EL TAMAÑO DEL DICCIONARIO LEN
print(dicci.keys())
print(dicci.values())
print(len(dicci))