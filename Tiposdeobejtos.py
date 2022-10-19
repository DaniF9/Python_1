lista = [1,2,3,4]
print(lista)
lista.append('X')
print(lista)
lista_2 = [5,6,7]
lista.append(lista_2) #AGREGUE UNA LISTA DENTRO DE OTRA LISTA CON EL METODO .append
print(lista)

vacio = []  #CREE UNA LISTA VACIA PARA DESPUES AGREGAR EL TEXTO O CUAL QUIER OTRO ELEMENTO 
print(vacio)
vacio.append('hola que hace perron')
print(vacio)

#DEFINIR UN DICCCIONARIO 
diccionario = {
    "clave_1" : "20",
    "clave_2" : "40"
}
print(diccionario)

print(diccionario["clave_1"]) #IMPRIMIMOS EL CONTENIDO DE CLAVE_1 QUE TIENE EL DICCIONARIO 
print(diccionario["clave_2"]) #IMPRIMIMOS EL CONTENIDO DE CLAVE_2 QUE TIENE EL DICCIONARIO

valor1 = diccionario["clave_1"] #IMPRIMIMOS EL CONTENIDO DE CLAVE_1 Y LO ASIGNAMOS EN UNA VARIABLE
print(valor1)
valor2 = diccionario["clave_2"] #IMPRIMIMOS EL CONTENIDO DE CLAVE_2 Y LOS ASIGNAMOS EN UNA VARIABLE
print(valor2)

#CAMBIAMOS EL CONTENIDO DE CLAVE_1 
diccionario["clave_1"] = 10
print(diccionario)

diccionario_2 = {
    'clave3': 5,
    'clave4': 6,
    'clave5': 7,
    'clave6': 8
}
print(diccionario_2)

diccionario_2.pop('clave3') #ELIMINAMOS CLAVE3 DEL DICCIONARIO_2 CON EL METODO POP
print(diccionario_2)
elementoeliminado = diccionario_2.pop('clave4') #ELIMINAMOS CLAVE_4 Y LO GUARDAMOS EN UNA VARIABLE 
print(elementoeliminado)

#DEFINIR UN SET

conjunto = {1,2,3,1,2,3,1,2,3,4,4,5,5}
print(conjunto)

a = {1,2,3,4,4,5}
b = {6,7,2,3}
print(a|b)

#Convertir una lista en una cadena 

Listatexto = ['hola','que','haces']
print(Listatexto)
print(''.join(Listatexto)) #Esto convierte la lista en una cadena
