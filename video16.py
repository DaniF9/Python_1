def NumerosImpares():
     for i in range(1,100):
         if i % 2 != 0:
             print(i, end=",")

NumerosImpares()

#////////ejerciicio////////

# contra = input("Ingrese su contrasena:  ")
# contador = 0
# for i in range(len(contra)):
#     if contra[i]==" ":
#         contador =1
# if len(contra)<8 or contador>0:
#     print("Password invalid")
# else:
#     print("Password Ok")


#///////ejercicio //////

# password= input("Introduced you password : ")
# def evalua_password(password):
#      valido = True

#      if len(password)<8 or " " in password:
#          valido=False
#      return valido

# if evalua_password(password):
#      print("You password is correct !! ")
# else:
#     print("You password is incorrect !!")

#//////ejercicio/////////
email = input("Ingrese su email : ")
contadorarroba = 0
contadorpunto = 0
for i in range(len(email)):
    if email[i] == "@":
        contadorarroba = contadorarroba+1
    if email[i]== ".":
        contadorpunto = contadorpunto+1
if contadorpunto==0 or contadorarroba !=1:
    print("Este no es un correo !!!")
else:
    print(" Email correcto  !!! ")

#/////ejercicio///// 

a =['1','123','1234','123445']
def maslarga(a):
    maslarga = ""

    for i in a:
        if len(i) > len(maslarga):
            maslarga = i 
    return maslarga

print(maslarga(a))

#////////////ejercicio//////////

lista = ['hola','Daniel','Quehaces']
#print(lista[0])
longitud = 0 
palabra = ""
for i in lista:
    if len(i) > longitud:
        longitud = len(i)
        palabra = i
print(palabra)


    


