tupla = ("juan", 2,5,2000)
lista = list(tupla) # el metodo list convier una tupla en list
print(tupla[3])
print(lista)
lista1 = [1,2,3,4,5,3]
tupla1 = tuple(lista1) # el metodo tuple convierte una lista en tupla
print(tupla1)
print(1 in tupla1)

print(tupla1.count(3))
print(len(tupla1))

# //////desempaquetado DE TUPLA//////

mitupla2 = ("Daniel" , 19, 9, 2000)
nombre, day, mount, year=mitupla2
print(nombre)
print(day)
print(mount)
print(year)
