#ejercicio 1
#declarar
nota1,nota2,nota3,nota4,nota5,promedio=0,0,0,0,0,0
nota1=int(input("nota1"))
nota2=int(input("nota2"))
nota3=int(input("nota3"))
nota4=int(input("nota4"))
nota5=int(input("nota5"))
promedio=(nota1+nota2+nota3+nota4+nota5)/5
desaprobados=promedio<11
#procesing
if(promedio<11):
    print("desaprobado")
#fin-if
