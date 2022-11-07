for i in [1,2,3]:
    print(" Hola mundo ")





#Este pedazo de codigo comprueba si es un correo o no dependiendo si tiene el caracter @ 
# correo = input("Ingrese su correo : ")
# email=False
# for i in correo:
#     if i == "@":
#         email=True
# if email==True:
#     print("el email es correcto")
# else:
#     print("El email es incorrecto ")

email=False 
corre2 =  input("Ingrese el correo : ")

for i in corre2:
    if i == "@" or i == ".":
         email=True

if email==True:
    print("El email es correcto !!! ")
else:
    print("El correo es incorrecto !!!")
