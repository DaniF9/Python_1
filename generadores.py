def generaPares(limite):
    num=1

    lista = []

    while num<limite:
        lista.append(num*2)
        num +=1
    
    return lista

print(generaPares(10))

devuelvePares = generaPares(10) #lOS DEVUELVE EN FORMA DE LISTA

for i in devuelvePares: # LOS DEVUELVE UNO POR UNO
    print(i)

def generaPares2(limite):
    num =1
    while num < limite:
        yield num*2
        num +=1
devuelvePares2 = generaPares2(10)

print(next(devuelvePares2))
print("Aqui puede ir codigo")
print(next(devuelvePares2))
print("Aqui puede ir codigo ")    

# ****************************AQUI VAMOS A VER EL YIELDFROM ***************************
def ciudades(*ciudad):  # *ciudad : el asterisco significa que va a recibir mas datos

    for elemento in ciudad:
        yield elemento

ciudades_devuelta = ciudades("Mexico","Madrid","Barcelona")
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))

#/////////////////////////////////
def ciudades(*ciudad):  # *ciudad : el asterisco significa que va a recibir mas datos

    for elemento in ciudad:
        yield from elemento   # Yield from accede como a los subelementos

ciudades_devuelta = ciudades("Mexico","Madrid","Barcelona")
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))




