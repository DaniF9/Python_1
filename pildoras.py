Mystr = "que rollon"
def palabras():
    print("ESTA FUNCION SOLO SIRVE PARA TEXTO ")
    print("Estamos aprendiendo funciones  ")
palabras()
print(Mystr.upper())

#/////////Listas //////

milista =["pepe","maria","marta","antonio"]
print(milista)
print(milista[:])
print(milista[2])

milista.append("Daniel")
print(milista)

milista.insert(2,"Carlos")
print(milista)

milista.extend(["Gabriela","Janette"])
print(milista)
milista.remove("maria")
print(milista)

lista4 = ["Carlos","Gaby","Janette"]
lista2 = [1,2,3,4,5]

lista3 = lista4+lista2
print(lista3)
lista3.pop()
print(lista3)

