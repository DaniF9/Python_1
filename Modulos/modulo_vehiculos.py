class Vehiculos(): #clase padre
    
    def __init__(self,marca,modelo):  #metodos

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False


    def arrancar(self):
        
        self.enmarcha = True
    
    def acelerar(self):
        
        self.acelera = True

    def frenar(self):

        self.frena = True
    
    def estado(self):

        print("Marca", self.marca , "\nModelo" ,  self.modelo , "\nEnmarcha" , self.enmarcha , "\nAcelerando" , self.acelera , "\nFrenando" , self.frena )

class Furgoneta(Vehiculos):
    
    def Carga(self,cargar):
        self.cargado = cargar

        if (self.cargado):
            return "La furgoneta esta cargada "
        else:
            return "La furgoneta no esta cargada "

#Heredamos de clase vehiculos una que se llame Moto
class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito "

    def estado(self): #Escribi este estado para visualizar el estado de moto ya que el metodo caballito esta fuera de la clase padre 

        print("Marca", self.marca , "\nModelo" ,  self.modelo , "\nEnmarcha" , self.enmarcha , "\nAcelerando" , self.acelera , "\nFrenando" , self.frena , 
        "\n", self.hcaballito)

class Electricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargarenergia(self):
        self.cargando = True


