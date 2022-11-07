lista = [1,2,3,4,5]

def suma(lista):
    contador = 0
    for i in lista:
        contador += i
    return contador

def multi(lista):
    contador = 1
    for i in lista:
        contador *= i
    return contador

print(suma(lista))
print(multi(lista))


