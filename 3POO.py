class Persona():

    def __init__(self,nombre,edad,residencia):

        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    
    def descripcion(self):

        print("Nombre", self.nombre , "Edad" ,self.edad, "Residencia", self.residencia)


class Empleado(Persona): #Aqui estamos heredando de nuestra clase padre llamada persona 

    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado) # esto se hace referenciar a nuestra clase padre 
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
         super().descripcion()
         print("SALARIO: ", self.salario,"ANTIGUEDAD:",self.antiguedad)
    

Manuel = Empleado(1500,15,"Manuel",55,"Colombia")
Manuel.descripcion()

print(isinstance(Manuel,Empleado))
