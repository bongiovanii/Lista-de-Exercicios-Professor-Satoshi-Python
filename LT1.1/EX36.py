# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
import math

num = int(input("Digite um número: "))

soma = 0
for i in range(num):
   soma += 1 + (1/math.factorial(i))

print(f"Resultado da soma de '1+1/n': {soma: .3f}")