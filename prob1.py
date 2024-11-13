import random

def puntosFueraParM(lad, num):
    punCua=num
    punInt=0

    for z in range(num):
        x=random.uniform(-lad/2, lad/2)
        y=random.uniform(-lad/2, lad/2)
        #print(f"{x},{y}")
        if (y*y - 4*x) <= 0:
            punInt+=1

    return punCua, punInt

#######
lad = float(input("Ingrese lado del cuadrado: "))
num = int(input("Ingrese cantidad de puntos: "))

pc, pi = puntosFueraParM(lad, num)
pf = pc-pi
areaC = lad * lad
areaF = areaC / pc * pf

print(f"Puntos en cuadrado {pc}, en interseccion {pi}")
print(f"El area fuera de la parábola mide {areaF}")