from tkinter import * 

root = Tk()

root.title("RdioButtons")
varOpcion = IntVar()

def imprimir():
    #print(varOpcion.get())
    if varOpcion.get()== 1:
        etiqueta.config(text = "Haz elegido Masculino")
    elif varOpcion.get() == 2:
        etiqueta.config(text = "Haz elegido Femenino" )

    else:
        etiqueta.config(text = "Hz elegido otros")
Radiobutton(root, text = "Masculino", variable = varOpcion , value =1 ,  command =  imprimir).pack()
Radiobutton(root, text = "Femenino",variable = varOpcion , value =2, command = imprimir).pack()
Radiobutton(root, text = "Otras Opciones" , variable = varOpcion ,  value = 3 ,  command = imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()