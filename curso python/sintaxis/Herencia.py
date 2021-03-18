class veiculos():

    def __init__(self,Modelo,marca):
        self.marca=marca
        self.Modelo=Modelo
        self.arrancar=False
        self.frenar=False
        self.acelerar=False

    def enciende(self):
        self.arrancar=True

    def acelera(self):
        self.arrancar=True

    def freno(self):
        self.frenar=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.Modelo, "\nAcelerar: ", self.acelerar, "\nFrenar: ", self.frenar, "\nArrancar", self.arrancar)


class Moto(veiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Estoy haciendo el caballito"
        #si traemos una accion de la calse padre a la clase hijo y la sbre escribivimos invalida la clase padre y muestra la propia claro siempre y cuando se llama a la accion de la clase hijo y no padre
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.Modelo, "\nAcelerar: ", self.acelerar, "\nFrenar: ", self.frenar, "\nArrancar", self.arrancar, "\n", self.hcaballito)


miMOTO=Moto("Honda","CTR34")

caba=str(input("deseas hacer el caballito? "))
caba=caba.lower()

if caba=="si":
        miMOTO.caballito()

else:
        print("")

miMOTO.estado()