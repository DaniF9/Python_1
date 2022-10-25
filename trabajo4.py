dato = int(input("Ingrese la fecha : "))

def bisiesto(dato):
    if (dato % 4 == 0 and dato % 100 != 0 ) or dato % 400 == 0:
        print("El ", dato , "bisiesto")
    else:
        print("El" , dato , "No es bisiesto")
bisiesto(dato)
