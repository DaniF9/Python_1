def max(a,b):
    if a>b:
        print("El numero mayor es : ", a)
    elif b>a:
        print("El numero mayor es : ", b)
    else:
        print("Los numeros son iguales ")

max(2,1)

def max(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        print("Los numeros son iguales")

print(max(23,1))


def max_tres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        print("los numeros son iguales ")

resultado = max_tres(16,5,6)
print(resultado)

def len(lista):
    count = 0
    for i in lista:
        count +=1
    return count
print(len("Querollo"))



letra = input("Ingrese la letra : ")
def vocales(letra):
    if letra in 'aeiou':
        return True
    else:
        return False

print(vocales(letra))

letras = input("INgrese la letra : ")
def vocal(letras):
    if letras in 'aeiou':
        print("Es una vocal")
    else:
        print("NO es una vocal")
vocal(letras)

