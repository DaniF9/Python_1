class coche():
    #Propiedas
    def __init__(self):
        
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 
        self.__enmarcha = False

#Hacemos nuestros metodos
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo ==  False):

            return "Algo a ido mal en el chequeo "
        else:
            return "El coche esta parado "
        

    def estado(self):
        
        print("El coche tiene ", self.__ruedas,"ruedas" ". Un ancho de ", self.__anchoChasis , "Un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Estoy realizando un chequeo interno ")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):

            return True
        else:
            return False


micoche = coche() 
print(micoche.arrancar(True)) 
micoche.estado()

print("*********** A continuacion creamos el segundo objeto ***********")

Coche2 = coche()
Coche2.estado() 
print(Coche2.arrancar(False)) 
