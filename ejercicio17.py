#EJERCICIO 02
# ganacias
#declaracion
nombre=""
ruc=""
producto=""
cantidad=0
pecio_compra=0.0
pecio_venta=0.0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad"))
precio_compra=float(input("ingrese precio de compra:"))
pecio_venta=float(input("ingrese precio de venta:"))

#procesing
ganancia=( pecio_venta - precio_compra)
if(ganancia>precio_compra):
    print("ganancia")
#fin_if
