# EX05.py
"""
Lote 1.3 - Exercício 5
Criar e coletar em um vetor [20] inteiro. Calcule e exiba, segundo:
Fórmula: Soma(i=1 até 10) (A[i] - A[21-i]) 
(Adaptado para índice 0: Soma(i=0 até 9) (A[i] - A[19-i]))
"""
import random

vetor = []
soma_exp = 0

for _ in range(20):
    vetor.append(random.randint(1, 100))
    
# A fórmula original parece usar base 1 (A[1] e A[21-1]).
# Adaptando para base 0 (A[0] e A[19-0]), A[i] e A[19-i]
for i in range(10):
    soma_exp += (vetor[i] - vetor[19 - i])
    
print(f"Vetor: {vetor}")
print(f"Resultado da somatória: {soma_exp}")