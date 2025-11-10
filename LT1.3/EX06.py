# EX06.py
"""
Lote 1.3 - Exercício 6
Criar e coletar em um vetor [20] com números aleatórios. 
Classificar este vetor em ordem crescente e mostre os dados.
"""
import random

vetor = []
for _ in range(20):
    vetor.append(random.randint(1, 1000))
    
print(f"Vetor original: {vetor}")

vetor.sort()

print(f"Vetor classificado: {vetor}")