#ejercicio11
#declarar
cliente=""
producto=""
cantidad=0
costodeunidad=0.0
cliente=str(input("ingrese nombre del cliente:"))
producto=str(input("ingrese nombre del producto:"))
cantidad=int(input("ingrese cantidad:"))
costodeunidad=float(input("ingrese el costo de uniudad:"))
#procesing
total=cantidad*costodeunidad
if(total>1500):
    print("comprador exigente")
else:
    print("no es comprador exigente ")
#fin-if

