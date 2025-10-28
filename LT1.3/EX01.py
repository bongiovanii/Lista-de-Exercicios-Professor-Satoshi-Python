# -*- coding: utf-8 -*-
# Criar e coletar um vetor [50] inteiro. Calcular e exibir:
# a. A média dos valores entre 10 e 200;
# b. A soma dos números ímpare.s

import random

# Gerar vetor com 50 números inteiros aleatórios entre 1 e 300
numeros = [random.randint(1, 300) for _ in range(50)]

print("Vetor gerado:")
print(numeros)

# a) Calcular a média dos valores entre 10 e 200
valores_entre_10_e_200 = [n for n in numeros if 10 <= n <= 200]

if valores_entre_10_e_200:
    media = sum(valores_entre_10_e_200) / len(valores_entre_10_e_200)
else:
    media = 0  # evita divisão por zero

# b) Calcular a soma dos números ímpares
soma_impares = sum(n for n in numeros if n % 2 != 0)

# Exibir os resultados
print(f"\nMédia dos valores entre 10 e 200: {media}")
print(f"Soma dos números ímpares: {soma_impares}")

