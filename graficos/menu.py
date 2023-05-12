from tkinter import * 
from tkinter import messagebox
root = Tk()

def infoadicional():
    messagebox.showinfo("Procesador de Daniel " , "Procesador de texto version 2023 ") # el show info muestra solo info

def avisolicencia():
    messagebox.showwarning("Licencia " ,  "Producto bajo licencia ") # showwarning muestra advertencias

def  salirAplicaion():
    valor = messagebox.askokcancel("Salir" ,  "Desea salir de la aplicacion ") # devuelve valores 'si' o 'no' 
    #valor = messagebox.askquestion("Salir ", "Desea salir de la aplicacion ") # devuelve valores True o False

    if valor == True:
        root.destroy()
    else:
        pass
def cerrardoc():
    valor = messagebox.askretrycancel("Reintertar ", "Noes posible cerrar el documento bloqueado")
    if valor == False:
        root.destroy()
    else:
        pass

root.title(" ****** MENU *******")
barraMenu = Menu(root)
root.config(menu = barraMenu , width = 300 , height = 300)

archivomenu = Menu(barraMenu , tearoff = 0)
archivomenu.add_command(label = " Nuevo archivo ")
archivomenu.add_command(label= " Editar archivo ")
archivomenu.add_command (label = " Guardar ")
archivomenu.add_command(label = " Guardar Como ")
archivomenu.add_separator()
archivomenu.add_command(label = " Salir " , command=salirAplicaion)
archivomenu.add_command(label = " Cerrar " ,  command = cerrardoc)

archivoEdicion = Menu(barraMenu , tearoff= 0 )
archivoEdicion.add_command(label = " Copiar")
archivoEdicion.add_command(label = " Cortar ")
archivoEdicion.add_command(label = " Pegar ")

archivoHerramientas = Menu(barraMenu , tearoff= 0)
archivoHerramientas.add_command(label = " IDE ")

archivoAyuda = Menu(barraMenu , tearoff= 0)
archivoAyuda.add_command(label = " Licencia " , command=avisolicencia)
archivoAyuda.add_command(label = " Acerca de " , command = infoadicional)

barraMenu.add_cascade(label = "Archivo" , menu = archivomenu)
barraMenu.add_cascade(label = "Edicion" , menu = archivoEdicion)
barraMenu.add_cascade(label = "Herramientas " , menu = archivoHerramientas)
barraMenu.add_cascade(label = "Ayuda" ,  menu = archivoAyuda)


root.mainloop()