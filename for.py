lista = [1,2,3,4,5]

for  valor in lista:
    print(valor)


for numero in range(10):
    print(numero)
    

for numero1 in range(1,5):
    print( numero1 ,  end = " ") # hacer el salto 

longitud = len(lista)
for numero in range(longitud):
     print(lista[numero])


lista_2 = ["hola","mensaje",'que']

for palabra in lista_2:
    print("La palabra es : ", palabra)
    if palabra == "mensaje":
        print("He encontrado la palabra")
        break
#Para ordenar una lista se hace lo siguiente : 
lista_1 = [1,5,8,9,3,4,5,6]
print(lista_1)

lista_ordenada = sorted(lista_1)
print(lista_ordenada)

lista_ordenada = sorted(lista_1, reverse=True)
print(lista_ordenada)

