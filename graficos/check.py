from tkinter import *
from PIL import ImageTk , Image
root = Tk()
root.title("Turismo")
# foto = Image.open("avion.png")
# foto = Image.resize((200,200), Image.ANTIALIAS) #metodo de rederizacion
playa = IntVar()
bosque = IntVar()
turismo = IntVar()

def opcionViaje():

    opciones = ""
    if (playa.get() == 1):
        opciones+= "playa"
    if(bosque.get() == 1):
        opciones+= "bosque" 
    if(turismo.get() == 1):
        opciones += "turismo"
    textofinal.config(text = opciones)
foto  = PhotoImage(file = "images.png" )
Label(root ,  image = foto).pack()

frame = Frame(root)
frame.pack()

Label(frame,  text = "Elige tu destino" , width = 50).pack()
Checkbutton(frame , text = "Playa ", variable = playa ,  onvalue =1 , offvalue = 0 , command=opcionViaje).pack() # cuando esta selecionado el valor es 1 
Checkbutton(frame, text = "Bosque ", variable = bosque  ,  onvalue =1 , offvalue = 0 , command=opcionViaje).pack()
Checkbutton(frame ,  text = "Turismo rural ",variable = turismo ,  onvalue =1 , offvalue = 0 , command=opcionViaje).pack()

textofinal = Label(frame)
textofinal.pack()



root.mainloop()