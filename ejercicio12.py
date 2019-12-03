#ejercicio12
#declarar
produto1,producto2,producto3,montototal=0,0,0,0
produto1=int(input("ingrse precio de  producto 1:"))
producto2=int(input("ingrese precio de producto 2:"))
producto3=int(input("ingrese precio de producto 3:"))

montototal=produto1+producto2+producto3

#procesing
if(montototal>900):
    print("se lleva de regalo una canasta")
else:
    print("se lleva un juguete")
#fin-if
