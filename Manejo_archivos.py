from io import open
                    #nombre del archivo , write = w 
#archivo_texto = open ("archivo.txt", "w")

#frase = "Estudiando python \n el martes"

#archivo_texto.write(frase) 
#archivo_texto.close()


#\\\\\\\\\\\\\\\ MODO LECTURA \\\\\\\\\\\\\\

#archivo_texto = open ("archivo.txt", "r")
#texto = archivo_texto.read()
#archivo_texto.close()
#print(texto)

#\\\\\\\\\AGREGAR LINEA A UN TEXTO \\\\\\\\\\\

archivo_texto = open("archivo.txt","a")
archivo_texto.write("\n python good")
archivo_texto.close()

