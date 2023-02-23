nombre = input ("Introduce un nombre de usuario : ")
print("El nombre es : ", nombre.upper())

edad = input("Introduce la edad : ")
# print(edad.isdigit())

while (edad.isdigit() == False):
    print("INgrese un valor numerico : ")

    edad = input("Ingrese la edad : ")


if (int(edad)<18):

    print("NO puedes pasar ")
else:
    print("Puedes pasar ")


email = input("Ingrese su correo de email : ")
arro = email.count('@')

if (arro != 1 or email.find('@') == 0 ):
    print("EL email es incorrecto ")

else:
    print(" correo verdadero ")

