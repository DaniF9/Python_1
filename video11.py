num1 =  int(input("Ingrese el primer numero : "))
num2 = int(input("Ingrese el segundo numero : "))

def DevuelveMax(num1,num2):
    if num1<num2:
        return num2
    else:
        return num1

print(DevuelveMax(num1,num2))


num3 = int(input("Ingrese el primer numero : "))
num4 = int(input("Ingrese el segundo numero : "))

def Nuevo(num3,num4):
    if num3<num4:
        return num4
    elif num4 < num3:
        return num3
    else:
        print("Los numeros son iguales !!! ")
print(Nuevo(num3,num4))


num5 = int(input("Ingrese el numero : "))
num6 = int(input("Ingrese un segundo numero : "))

def NumeroMaximo(num5,num6):

    if num5 < num6:
        return num6
    elif num6 < num5:
        return num5
    else:
        print("Los numeros iguales ingrese otros numero !!! ")
resultado = NumeroMaximo(num5,num6)
print("El numero mas grande es : ", resultado)
