# > Mayor
# >= Mayor igual
# == igual
# <= Menor igual 
# < Menor

a = 5
b = 7
c = 7
resultado = (a > 5 and c < 7)
print(resultado)

#if hace la condicion si es verdadera 
var1 = int(input("ingrese el valor numero 1 : "))
var2 = int(input("ingrese el valor numero 2 : "))

if var1 < var2:
    print("hola perro")
else:
    print("que pedo")

nombre = "Carlos"
edad = 22
print("HOLA {} TIENES LA EDAD DE {}".format(nombre,edad)) #Es otra forma de salida que puedes tener 

#***********************DECLARAR UN WHILE**********************
#contador = int(input("Ingrese el numero : "))
contador = 0
while contador <=10:
    if contador % 2 == 0:
        print(contador , "El numero es par ")
    contador += 1



contador = 1
while contador <= 10:
    print("Contador vale : ", contador )

    if contador == 5:
        print("Aqui se rompio el bucle")
        break
    contador += 1
print("Estamos fuera del while")


# contador = 1
# while contador <= 10:
#     if contador % 2 == 0:
#         print(contador , "Es un numero par")
#         continue
#     print("Ahora incremento el contador ")
#     contador += 1
contador = 0
while contador <= 10:
    contador += 1
    if contador % 2 == 0:
        print(contador , "Es un numero par")
        continue
    print("Estoy aqui por que vale ", contador ,"y no se dispara el continue")





