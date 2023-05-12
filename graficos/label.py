from tkinter import *

root = Tk()

miframe = Frame(root , width = 500 , height = 400)
miframe.pack()
imagen = PhotoImage(file = "images.png") # Usamos imagenes en el frame 
#milabel = Label(miframe, text = "Hola alumnos ", fg = 'red')
milabel = Label(miframe, image =imagen )
#milabel.pack()
milabel.place(x = 100, y = 100)



root.mainloop()