print("Bienvenido a la seleccion de materias extra")
respuesta=str(input("desea ver la lista de materias? responda con un si o un no: "))
if respuesta=="si":
    print("Calculo")
    print("Ciencias")
    print("Algebra")
    opcion=str(input("Cual materia decea? "))
    #existen dos funciones una para pasar los datos a todos minuscula o todos mayuscula los cuales son lower para minusculas y upper para mayusculas
    materia=opcion.lower()
    #materia=opcion.upper()
    if materia in ("calculo","ciencias","algebra"):
        print("la materia seleccionada a sido almacenada la proxima semana recuerde asistir.")
    else:
        print("la materia seleccionada no existe porfavor intente de nuevo.")

else:
    print("Gracias por su respuesta vulva pronto")