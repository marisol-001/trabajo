#ejercicio 2
#declarar
compra1,compra2,compra3,totaldecompra=0,0,0,0
compra1=int(input("compra1"))
compra2=int(input("compra2"))
compra3=int(input("compra3"))

totaldecompra=compra1+compra2+compra3

#procesing
if(totaldecompra>200):
    print("saldo insuficiente")
else:
    print("saldo suficiente")
#fin-if
