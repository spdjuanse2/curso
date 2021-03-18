class coche():

    pueras=4
    asientos=5
    potencia_del_motor=3.65

    def __init__(self):#se usa el __init__ para definir un punto inicial de caracteristicas es decir para definir que datos tendrean los onjetos nada mas ingresar a la clase
        self.__largo=200#los __ luego del punto son para encapsular la variable y que sus valores solo puedan ser cambiados en la clase atra vez de las metodos def (self):
        self.__altura=100
        self.__ruedas=4
        self.enmarcha=False


    def arrancar(self):
        self.enmarcha=True

        if (self.enmarcha):
            chequeo=self.__chequeo_inicial()

        if (self.enmarcha and chequeo):
            return "el estado del viculo se encuentra arrancado"

        elif (self.enmarcha and chequeo==False):
            return "durante el chequeo del carro ocurrio un problema revise el estado del carro"

        else:
            return "el estado del veiculo es que se encuentra detenido"


    def estado(self):
        print("el auto tiene un motor de ", self.potencia_del_motor, "el auto tiene un numero de ", self.__ruedas," ruedas"," el veiculo riene una altura de ", self.__altura, " y un largo de", self.__largo)


    def __chequeo_inicial(self):
        self.nivel_gasolina="ok"
        self.nivel_aceite="ok"
        self.puertas="cerradas"

        if (self.nivel_gasolina=="ok" and self.nivel_aceite and self.puertas=="cerradas"):
            return True

        else:
            return False


micoche=coche()
#se usa para darle una clase a una variable

print("BIENVENIDO A LA APLICACION DE INFORMACION DEL NUEVO SPT98")
print("responda (si) o (no) segun corresponda")
inf=str(input("desea conoser la informacion y estado actual del viculo? "))
info=inf.lower()

while True:
    if (info=="si"):
        micoche.estado()
        if(micoche.enmarcha==False):
            print("el viculo se encuentra detenido")
            decicion=str(input("Desea poner en marcha el viculo? "))
            while True:

                if (decicion=="si"):
                    micoche.arrancar()
                    break

                elif (decicion=="no"):
                    micoche.enmarcha=False
                    print("el veiculo sigue detenido",micoche.enmarcha)
                    break

                else:
                    print("porfavor limite su respuesta a los parametros dados")
                    decicion=str(input("Desea poner en marcha el viculo? "))
            break
        else:
            print("el veiculo se encuentra en en movimiento")
            decicion=str(input("Desea detener el viculo? "))
            while True:

                if (decicion=="si"):
                    micoche.enmarcha=False
                    print("el veiculo fue detenido con exito",micoche.enmarcha)
                    break

                elif (decicion=="no"):
                    micoche.enmarcha=True
                    print("el veiculo sigue en marcha ",micoche.enmarcha)
                    break

                else:
                    print("porfavor limite su respuesta a los parametros dados")
                    decicion=str(input("Desea poner en marcha el viculo? "))
            break

    elif (info=="no"):
        print("Gracias por su coperacion vuelva pronto")
        break

    else:
        print("Porfavor ingrese si o no unicamente")
        print("BIENVENIDO A LA APLICACION DE INFORMACION DEL NUEVO SPT98")
        print("responda (si) o (no) segun corresponda")
        inf=str(input("desea conoser la informacion y estado actual del viculo? "))
        info=inf.lower()
