# Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes)

import math


a = int(input("Insira A: "))
b = int(input("Insira B: "))
c = int(input("Insira C: "))

delta = (b**2) - 4*(a*c)

if delta < 0:
   print("Esta equação não possui raizes")

else:
   x1 = (-b - math.sqrt(delta)) / (2*a)
   x2 = (-b + math.sqrt(delta)) / (2*a)

   result = [x1,x2]
   print("Resultado: \n x' = ", result[0], " \n x'' = ", result[1])


