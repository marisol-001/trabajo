# copradora compulsiva de maquillaje
#declaracion
nombre=""
producto=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
producto=input("ingrese producto")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)
if(total>250):
    print("compradora_compulsiva_maquillaje")
#fin_if
