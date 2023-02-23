import pickle

# nombres = ["carlos", "daniel","janette"]
# fichero_binario = open("nombre","wb")

# pickle.dump(nombres,fichero_binario)

# fichero_binario.close()

# del(fichero_binario)

fichero =  open("nombre", "rb")
lista = pickle.load(fichero)
print(lista)