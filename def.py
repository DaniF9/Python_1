#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def edades():
    
    
    tuplas = []
    cad = int(input("Ingrese las edades que quiere en la tupla : "))
    for i in range(cad):
        tupla=  int(input("Ingrese las edades : "))
        tuplas.append(tupla)
        i +=1
    print(tuplas)


    cont = 0  
    for i in tuplas:
        if i >= 20:
            cont +=1            

    print("Hay",cont,"Personas mayores ")

edades() 

#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

#mylista = ['Carlos' ,'Gaby','Daniel']

#contador = 0
def nombres():
    
    nombre = int(input("Cuantos nombres quiere ingresar : "))
    mylista = []
    for i in range(nombre):
        nombres = input("Igresa el nombre : ")
        mylista.append(nombres)

    print("")

    inicio = input("Con que letra quieres que se haga el conteo : ")
    contador = 0 

    for i in  mylista:
        if i[0] == inicio.lower() or i[0]== inicio.upper():
            contador +=1
    return contador

resultado = nombres()
print(resultado)
