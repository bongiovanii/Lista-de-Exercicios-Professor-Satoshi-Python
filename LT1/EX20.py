#  Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula 
# AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, 
# calcule e mostre.

import math


A = float(input("Digite o coeficiente A: "))
B = float(input("Digite o coeficiente B: "))
C = float(input("Digite o coeficiente C: "))


if A == 0:
    print("Não é uma equação do 2º grau, pois A = 0.")
else:
    
    delta = B**2 - 4*A*C

    print(f"Delta = {delta}")

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -B / (2*A)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-B + math.sqrt(delta)) / (2*A)
        raiz2 = (-B - math.sqrt(delta)) / (2*A)
        print(f"A equação possui duas raízes reais:")
        print(f"x1 = {raiz1}")
        print(f"x2 = {raiz2}")


