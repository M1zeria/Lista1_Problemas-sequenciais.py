import math
lado = int(input())
area = (lado**2*math.sqrt(3)/4)*6
perimetro = lado*6
print(f"Lado do hexagono: {lado:.1f} metros,")
print(f"Area: {area} metros quadrados,")
print(f"Perimetro: {perimetro:.1f} metros.")
