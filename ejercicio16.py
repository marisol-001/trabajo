#EJERCICIO 01
#curso aprobado
#declaracion
alumno=""
codigo=""
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0

#Input
alumno=input("ingrese nombre del alumno:")
codigo=input("ingrese codigo del alumno:")
nota1=float(input("ingrese nota1:"))
nota2=float(input("ingrese nota2:"))
nota3=float(input("ingrese nota3:"))
nota4=float(input("ingrese nota4:"))

#procesing
promedio=(nota1+nota2+nota3+nota4)/4
if(promedio>10.5):
    print("curso aprobado")
#fin_if

