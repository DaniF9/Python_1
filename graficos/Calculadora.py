from tkinter import * 
#import tkinter
from PIL import Image,ImageTk

raiz = Tk()
miframe = Frame(raiz)
raiz.title("Calculadora")
im = Image.open('images.png')
photo = ImageTk.PhotoImage(im)
raiz.wm_iconphoto(True,photo)
miframe.pack()
resultado = 0
operacion = ""
reset_pantalla = False
# --------------pantalla ----------------

numeropantalla = StringVar()

pantalla =Entry(miframe , textvariable = numeropantalla)
pantalla.grid(row = 1 , column = 1 , padx = 10 , pady =10 , columnspan = 4)
pantalla.config(background = "black" , fg = "#03f943" , justify = "right")
#-----------------pulsaciones teclado -- ----------

def numeropulsado(num):   # puse el num para que se almacene el numero pulsado
    global operacion
    global reset_pantalla
    if reset_pantalla != False:

        numeropantalla.set(num)
        reset_pantalla = False
    # if operacion !="": # si pulsamos suma no va a concatenar 
    #     numeropantalla.set(num)
    #     operacion = ""
    else:
    
        numeropantalla.set(numeropantalla.get() + num) # aqui concatenamos con el num

#-----------------funcion suma ----------------

def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado +=int(num) 
    operacion = "suma"
    reset_pantalla = True
    numeropantalla.set(resultado)

# ---------------- funcion resta --------------
num1 = 0
contador_resta = 0

def resta(num):
    global operacion
    global reset_pantalla
    global resultado 
    global num1 
    global contador_resta

    if contador_resta == 0:

        num1 = int(num)
        resultado = num1
    else:

        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado =  int(resultado) - int(num)
        
        numeropantalla.set(resultado)
        resultado = numeropantalla.get()
    
    contador_resta = contador_resta+1
    operacion = "resta"

    reset_pantalla = True

# -- - --- --- -- -- -- -  funcion multiplicacion --------------------
contador_multi = 0
def Multiplicacion(num):
    global operacion 
    global resultado 
    global num1 
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1

    else:

        if contador_multi == 1:
            resultado = num1 * int(num)
        else:

            resultado = int(resultado) * int(num)
        
        numeropantalla.set(resultado)

        resultado = numeropantalla.get()
    
    contador_multi = contador_multi+1
    operacion = "multiplicaion"
    reset_pantalla = True

# ----------------- funcion dividir ---------------

contador_divi = 0

def divide(num):

    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1

    else:
        if contador_divi == 1:
            resultado = num1 / float (num)
        else:

            resultado = float(resultado/float(num))
        numeropantalla.set(resultado)
        resultado = numeropantalla.get()
    
    contador_divi = contador_divi + 1
    operacion = "division" 
    reset_pantalla = True

        

# --------------- funcion el_resultado ----------

def el_resultado():
    global resultado
    global operacion 
    global contador_resta
    global contador_multi
    global contador_divi

    if operacion == "suma":
        numeropantalla.set(resultado + int(numeropantalla.get()))
        resultado = 0
    
    elif operacion == "resta":
        numeropantalla.set(int(resultado) - int(numeropantalla.get()))
        resultado  = 0 
        contador_resta = 0

    elif operacion == "multiplicaion":
        numeropantalla.set(int(resultado) * int(numeropantalla.get()))
        resultado = 0
        contador_multi = 0

    elif operacion == "division" : 
        numeropantalla.set(int(resultado) / int(numeropantalla.get()))
        resultado = 0
        contador_divi = 0 

    

    #numeropantalla.set(resultado + int(numeropantalla.get()))
    #resultado = 0
#---------fila 1 ----------------

boton7 = Button(miframe,  text = " 7 " , width=3,command = lambda:numeropulsado("7"))
boton7.grid(row = 2 , column = 1)
boton8 = Button(miframe ,  text = " 8 " , width = 3,command = lambda:numeropulsado("8"))
boton8.grid(row = 2 , column = 2)
boton9 = Button(miframe , text = " 9 " , width = 3, command = lambda:numeropulsado("9"))
boton9.grid(row =2 , column = 3)
botonDiv = Button (miframe , text = " / ", width = 3 , command = lambda:divide(numeropantalla.get()))
botonDiv.grid(row = 2 , column = 4)

#------------- FILA 2 --------------------

boton4 = Button(miframe ,  text = " 4 ", width =3, command = lambda:numeropulsado("4")) # pasamos por parametro el numero 4 
boton4.grid(row = 4 ,  column = 1)
boton5 = Button(miframe , text = " 5 " , width = 3,command = lambda:numeropulsado("5"))
boton5.grid(row =4 , column =2)
boton6 = Button(miframe ,  text = " 6 " , width = 3 ,command = lambda:numeropulsado("6"))
boton6.grid(row = 4 , column = 3)
botonMulti = Button(miframe ,  text = " x ", width =3, command = lambda:Multiplicacion(numeropantalla.get()))
botonMulti.grid(row = 4,  column = 4)
#-------------------- FILA 3 -----------------
boton0 = Button (miframe , text = "1" , width = 3,command = lambda:numeropulsado("1"))
boton0.grid(row = 5 , column =1)
botonPunto = Button(miframe,  text = " 2 " , width = 3,command = lambda:numeropulsado("2"))
botonPunto.grid(row = 5 , column =2)
botonigual = Button(miframe ,  text = " 3 " , width = 3,command = lambda:numeropulsado("3"))
botonigual.grid(row = 5 , column = 3)
botonSuma = Button(miframe , text = " - " ,  width = 3 , command=lambda:resta(numeropantalla.get()) )
botonSuma.grid(row = 5 ,  column = 4)

# ------------------- FILA 4 ----------------- 
boton0 = Button (miframe , text = "0" , width = 3,command = lambda:numeropulsado("0"))
boton0.grid(row = 6 , column =1)
botonPunto = Button(miframe,  text = " . " , width = 3,command = lambda:numeropulsado("."))
botonPunto.grid(row = 6 , column =2)
botonigual = Button(miframe ,  text = " = " , width = 3 , command = lambda:el_resultado())
botonigual.grid(row = 6 , column = 3)
botonSuma = Button(miframe , text = " + " ,  width = 3 , command=lambda:suma(numeropantalla.get()))
botonSuma.grid(row = 6 ,  column = 4)


raiz.mainloop()