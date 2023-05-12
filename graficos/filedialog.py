from tkinter import *
from tkinter import filedialog


root = Tk()

root.geometry("300x300")

def abreFichero():

    fichero = filedialog.askopenfilename(title="Abrir", initialdir="/home" , filetypes =(("Fichero de texto","*txt" ), 
    ("Fichero de python", "*.*")))

    print(fichero)

Button(root ,  text =  " Abrir fichero " , command=abreFichero).pack()

root.mainloop()
