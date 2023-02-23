# nombre =  input("Ingrese su nombre : ")
# dire = input("Ingrese su direccion : ")
# telefono =  input("Ingrese su numero de telefono : ")

# lista = [nombre, dire,telefono]

# print("Los datos personales son : ", lista, end = ",")

# print()
# print()

#Realice un programa que ingreses 3 numeros por teclado y te devuelva la media aritmetica
# print("Programa para calcular la media aritmetica !!!!!!")

# num1 = int(input("Ingrese el primer  numero : "))
# num2 =  int(input("Ingrese el segundo numero : "))
# num3 = int(input("INgrese el tercer numero : "))

# resultado = (num1+num2+num3)/3

# print("La media aritmetica es : ", resultado )


#//////// ejercicio /////// 
#mylista = []
# i = 1 
# for i in range(5):
#     print("Ejecucion # ", i)
#     dato =int(input("Ingrese el numero "))
#     mylista.append(dato) # Aqui siempre se debe poner la variable con la que estas pidiendo el dato 
#     i = i+1   
# print(mylista)

# desicion =input("Desea agregar otra lista ? ")
# while desicion == "s":
#     mylista2 = []
#     i = 1 
#     for i in range(5):
#         print("Ejecucion # ", i)
#         dato =int(input("Ingrese el numero "))
#         mylista2.append(dato) # Aqui siempre se debe poner la variable con la que estas pidiendo el dato 
#         i = i+1   
#     print(mylista2)

#     desicion=input("Desea agregar otra lista ? ")

#     if desicion == 'n':
#         print("Tus listas son ", mylista, ",",mylista2)

#     else:
#         print("Dame tu lista de 5 elementos : ")

#////////ejercicio 2 /////////////////
#Definir una función superposicion() que tome dos listas y 
#devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

lista1 = [1,2,3,4,5]
lista2 = [5,6,7,8,9]

def superposicion(lista1,lista2):
    for i in lista1:
        for x in lista2:
            if i ==x:
                return True
    return False

print(superposicion(lista1,lista2))

#////////// ejercicio 3 //////////////
#Definir una función generar_n_caracteres() que tome un entero n y 
#devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
num = int(input("ingrese el numero : "))
letra = input("INgrese el caracter a multiplicar :")

def generador(num,letra):
    valor = num*letra
    print(valor)

generador(num,letra)

#////////ejercicio /////////// 
#Definir un histograma procedimiento() que tome una lista de números 
#enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
lista3 = [1,2,3,4]
def procedimiento(lista3):
    for i in lista3:
        print( i*"x")

procedimiento(lista3)
