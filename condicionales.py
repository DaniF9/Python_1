print("programa de evaluacion de notas ")

nota = int(input("Ingrese la nota del alumno : "))

def evaluacion(nota):
     valoracion = "aprobado"
     if nota < 5:
         valoracion= "reprobado"
     return valoracion 

print(evaluacion(nota))


salario1 = int(input("Ingrese el salario del presidente : "))
print("El salario del presidente es : ", salario1)

salario2 = int(input("Ingrese el salario del director : "))
print("El salario del director es : ", salario2)

salario3 = int(input("Ingrese el salario del jefe de area  : "))
print("El salario del jefe de area es : ", salario3)

salario4 = int(input("Ingrese el salario del administrativo : "))
print("El salario del administrativo es : ", salario4)

if salario4<salario3<salario2<salario1:
     print("Todo funciona bien")
else:
     print("Algo falla en la empresa")

print(" !!! Programa becas of the year !!!")

distancia = int(input("Ingrese los Km de su casa a la escuela : "))
print(distancia)

hermanos = int(input("Ingrese los hermanos que tiene : "))
print(hermanos)

salario_familiar = int(input("Ingrese el salario familiar mensual : "))

if distancia <= 50 and hermanos<=3 and salario_familiar <= 15000:
    print("Felicidades beca otorgada !!!! ")

else:
    print("Beca rechazada :( ")


print("Asignaturas !! ")

print("Asignaturas optativas : desarrollo web - software  ")

opcion = input("ingrese su asignatura : ")

if opcion in ("desarrolo web ", "software "):
    print("Asignatura elegida " , opcion)
else:
    print("Ingrese una opcion valida !!! ")