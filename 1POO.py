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
            return "El coche esta en marcha"
        else:
            return "El coche esta parado "
        #El self hace referencia al objeto pertenenciente a la clase 
        #self.enmarcha = True

    def estado(self):
        # if(self.enmarcha):
        #     return "El coche esta en marcha "
        
        # else:
        #     return "El coche esta parado "

        print("El coche tiene ", self.__ruedas,"ruedas" ". Un ancho de ", self.__anchoChasis , "Un largo de ", self.__largoChasis)

#crear una instancia o ejemplar 
# nombre del ejemplar = nombre de la clase()
micoche = coche() # Instanciar a una clase

#Acediendo al comportamiento de un objeto
#print("El largo de mi coche es : ", micoche.largoChasis)
#print("El coche tiene : " , micoche.ruedas)

print(micoche.arrancar(True)) # micoche se almacena en el self de arrancar y pone en marcha el objeto 
micoche.estado()# Aqui tuve un error ya que mande a llamar sin los () los puse y jalo sin problema 


print("*********** A continuacion creamos el segundo objeto ***********")

Coche2 = coche() # Esta es mi segunda instancia 
#print ("El largo de mi coche es : ", Coche2.__largoChasis)
#print("El coche tiene ", Coche2.__ruedas, "ruedas")
Coche2.estado() # LOs quite del print dado que en el metodo estado ya las imprimi
print(Coche2.arrancar(False)) # Las puse en un print dado a que utilizamos un parametro y necesitamos imprimirlo 


