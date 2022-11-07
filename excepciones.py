import math
def calcularaiz(num):
    if num < 0:
        raise ValueError("El numero no puede ser negativo !!! ")
    else:
        return math.sqrt(num)
opc = int(input("INGRESE EL NUMERO  : "))

try:
    print(calcularaiz(opc))
except ValueError as ErrordeNumeroNegativo:
    print(ErrordeNumeroNegativo)
print("Programa terminado !! ")