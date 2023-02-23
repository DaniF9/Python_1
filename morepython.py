#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

lista = ['123','holaquehaces','quepedal']
def filtrarpalabras(lista,n):
    for i in lista:
        if len(i)>n:
            print(i)
filtrarpalabras(lista,5)

#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 

cadena = input("Ingrese alguna frase : ")

def Mayus(cadena):
    cont = 0
    for  i in cadena:
        if i != i.lower():
            cont +=1
    print("Las mayusculas que tiene es ", cont)

Mayus(cadena)
# Hacer un programa que inprima 5 hola mundo con un while y con for 
num = int(input("Ingrese un numero : "))
cont=1
while cont<=num:
    print("HOla mundo")
    cont +=1

num = int(input("Ingrese un numero : "))
cont=1
for i in range(num):
    print("HOla mundo")
    cont +=1

#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

# def main():
#     a_curso = input ("Ingresa el anio en curso: ")
#     for i  in range (3):
#         nombre = input ("Nombre de la persona: ")
#         nacimiento = input ("Anio de nacimiento: ")
#         print  (nombre, "cumple", a_curso - nacimiento, "anios en el", a_curso)

# main()

# def main():
#     year = int(input(" Enter the current year : "))

#     for i in range(3):
#         nombre = input(" Ingrese el nombre : ")
#         nacimiento = int(input("Ingrese el year de nacimiento : "))
#         actual = year - nacimiento
#         print("HOla", nombre , "usted cumple" , actual , "your year of birth is : ", nacimiento)

# main()



def main ():
    cont = 0
    numeros = int(input("Cuantos nombres quiere ingresar : "))
    year = int(input("Enter the current year : "))
    
    while numeros <=3:
        print("Usted debe ingresar ", numeros, "nombres !!! ")

        nombre = input("ingrese el nombre : ")
        nacimiento = int(input(" Enter your year of birth : "))
        actual = year - nacimiento
        cont +=1
        print("Su nombre es ",nombre,"Usted cumple",actual,"your year of birth is ", nacimiento)

        if numeros == cont:
            break

main()




