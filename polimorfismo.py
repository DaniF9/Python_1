class Coche():


    def desplazamiento(self):
        print("Me desplazo en 4 ruedas ")



class Moto():


    def desplazamiento(self):

        print("Me desplazo en 2 ruedad")


class Camion():


    def desplazamiento(self):

        print("Me desplazo en 6 ruedas ")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)

Vehiculo2 = Coche()
desplazamientoVehiculo(Vehiculo2)
# miVehiculo = Moto()
# miVehiculo.desplazamiento()

# Vehiculo2 = Coche()
# Vehiculo2.desplazamiento()

# Vehiculo3 = Camion()
# Vehiculo3.desplazamiento()

