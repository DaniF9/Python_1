for letra in "Python":
    if letra == "h":
        continue
print("Letra encontrada !!") #Dependiendo donde coloque el print es como se va a repetir el mensaje "Letra encontrada "


nombre = "Hola que hace"
contador = 0

for i in nombre:
    if i == " ":  # NO CUENTA LOS ESPACIOS
        continue
    contador +=1
print(contador)


def funcion(): # USO DEL PASS , PASA A LO SIGUIENTE SIN MARCAR ERROR 
    pass

email = input("Ingrese su correo : ")

for i in email:
    if i == "@":
        arroba=True
        break
else:
    arroba = False
print(arroba)

