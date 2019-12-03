#ejercicio13
#declarar
horasdetrabajo,horasdetardanza,diferenciadehoras=0.0,0.0,0.0
horasdetrabajo=float(input("ingrese las horas que trabaja:"))
horasdetardanza=float(input("ingrese las horas que llego tarde:"))

diferenciadehoras=horasdetrabajo-horasdetardanza

#procesing
if(diferenciadehoras>8):
    print("se descontara 80 soles")
else:
    print("no sera descontado")
