import math
i=1

while i <= 10:
    print("Ejecuciion #" , i)
    i = i+1
print("Termino la ejecucion !!!")

edad = int(input("Ingrese la edad : "))
while edad <0:
    print("Haz introducido una edad negativa. Vuelve a intentarlo")
    edad = int(input("Introduce tu edad : "))

print("Gracias , puedes pasar ")
print("Su edad introducida es ",edad)
#/////////////////////////////////////////////////////////
print("Programa de calculo de raiz cuadrada")
numero = int(input("introduce un numero : "))

intentos = 0 
while numero<0:
    print("No se puede hallar la raiz de un numero negativo")
    
    if intentos ==2:
        print("Haz hecho demasiados intentos !!!")
        break

    numero = int(input("INtroduce un numero por favor : "))
    if numero < 0:
        intentos=intentos+1
if intentos < 2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de ", numero, "es :", solucion)