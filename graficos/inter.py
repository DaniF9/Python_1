#import tkinter as tk
from tkinter  import *
import tkinter
from PIL import Image,ImageTk
raiz = tkinter.Tk()
raiz.title("Ventana de pruebas ")

im = Image.open('images.png')
photo = ImageTk.PhotoImage(im)
raiz.wm_iconphoto(True,photo)

raiz.geometry("650x350")
raiz.config(bg = "blue") #bg =  backround cambia el fondo de la pantalla 

miframe = Frame()
miframe.pack() # empaquetamos la raiz 

miframe.config(bg ="red")
miframe.config(width = "650" , height="350")
miframe.config(bd= 35)
miframe.config(relief = "groove")

raiz.mainloop() # siempre debe estar al final  