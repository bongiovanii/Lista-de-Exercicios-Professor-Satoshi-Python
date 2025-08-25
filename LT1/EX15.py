# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a
# hipotenusa.

import math

cat1 = int(input("Insira o valor do primeiro cateto: "))
cat2 = int(input("Insira o valor do segundo cateto: "))

hip = float(math.sqrt(cat1**2) + (cat2**2))

print("A  hipotenusa será igual a ", hip)