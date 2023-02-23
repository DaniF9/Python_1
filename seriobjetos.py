import pickle
class Vehiculo():

    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelos = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelarar (self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):
        print("Marca : " , self.marca , "\nModelo : ", self.modelos, "\n En marcha : " , self.enmarcha , "\nAcelerando : ",self.acelera , 
        "\nFRenado : " , self.frena)



Coche1 = Vehiculo("Mazda","BMW")
Coche2 = Vehiculo("Honda","jetta")
Coche3 = Vehiculo("seat","Ferrari")

coche = [Coche1, Coche2,Coche3]

fichero = open("Loscoches","wb")
pickle.dump(coche,fichero)
fichero.close()
del(fichero)


ficheroApertura = open("Loscoches", "rb")
miscoches = pickle.load(ficheroApertura)
ficheroApertura.close()
for c in miscoches:

    print(c.estado()) #cuando llamemos una funcion siiempre debemos hacerlo con parentesis en este caso puse estado y me daba un error 
