#comprador mayoritario
#declaracion
nombre=""
ruc=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)
if(total>10000):
    print("comprador mayoritario")
#fin_if
