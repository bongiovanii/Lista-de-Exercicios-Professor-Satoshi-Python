# EX04.py
"""
Lote 1.3 - Exercício 4
Criar e coletar em um vetor [30] real e calcular e exibir:
a. A média do grupo;
b. A quantidade de notas acima do grupo;
c. As posições dos valores abaixo da média do grupo.
"""
import random

vetor = []
soma = 0
acima_media = 0
posicoes_abaixo = []

for _ in range(30):
    vetor.append(random.uniform(0.0, 100.0))

if len(vetor) > 0:
    for val in vetor:
        soma += val
        
    media = soma / len(vetor)
    
    for i in range(len(vetor)):
        if vetor[i] > media:
            acima_media += 1
        elif vetor[i] < media:
            posicoes_abaixo.append(i)
            
    print(f"Vetor (primeiros 10): {vetor[:10]}...")
    print(f"Média do grupo: {media:.2f}")
    print(f"Quantidade de notas acima da média: {acima_media}")
    print(f"Posições dos valores abaixo da média: {posicoes_abaixo}")
else:
    print("Vetor está vazio.")