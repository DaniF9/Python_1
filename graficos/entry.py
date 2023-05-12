from tkinter import *
raiz = Tk()
raiz.title("Aplicacion de entry")
#texto = Entry(raiz)
#texto.pack()
miframe = Frame(raiz , width = 1200 , height = 600)
miframe.pack()

minombre =StringVar() # Cadena de caracteres

nombretexto =Entry(miframe, textvariable=minombre) # text variable para asignar el nombre de la funcion  codigobotton
#texto.place(x = 100 , y = 100)
nombretexto.grid(row = 0, column =1)
#nombretexto.config(fg = "red",justify = "right")
nombrelabel = Label(miframe , text = "Nombre : ")
nombrelabel.grid(row = 0 , column = 0 , sticky = "e",padx =10 ,pady = 10)
#nombrelabel.place(x =100 ,  y = 100)

cupassword = Entry(miframe)
cupassword.grid(row = 1, column = 1 , padx = 10 , pady = 10)
cupassword.config(show = "*")
passlabel = Label(miframe , text = "Password : " )
passlabel.grid(row = 1 , column = 0 , sticky = "e" , padx = 10 , pady = 10)



apellido = Entry(miframe)
apellido.grid(row = 2 , column = 1 , padx=10 , pady=10)
apellidoLabel =  Label(miframe , text = " Apellido : ")
apellidoLabel.grid(row = 2 , column = 0,sticky = "e",padx =10 ,pady = 10)

dirreccion = Entry(miframe)
dirreccion.grid(row = 3, column = 1 ,padx=10 ,pady=10)
dirreccionLabel = Label(miframe , text = "Direccion : ")
dirreccionLabel.grid(row = 3 , column = 0,sticky = "e",padx =10 ,pady = 10)

comentariolabel = Label (miframe, text = "Comentarios")
comentariolabel.grid(row =4 , column =0 , sticky = "e", padx = 10, pady = 10)

textocomentario = Text(miframe, width=15 , height=7)
textocomentario.grid(row =4 , column =1 , padx =10 , pady =10)


scrol = Scrollbar(miframe, command = textocomentario.yview)
scrol.grid(row =4 , column = 2, sticky ="nsew")
textocomentario.config(yscrollcommand = scrol.set)

def codigoBoton():
    minombre.set(" DANIEL ")

botonenvio = Button(raiz, text = "Enviar" , command = codigoBoton)
botonenvio.pack()

raiz.mainloop()