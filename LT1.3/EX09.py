# EX09.py
"""
[cite_start]Lote 1.3 - Exercício 9 [cite: 168, 169]
Criar e carregar uma matriz [4] [4] com valores aleatórios, sendo que a
[cite_start]diagonal principal terá seus dados carregados no programa segundo: [cite: 169]
[cite_start]1 [cite: 170]
[cite_start]4 [cite: 171]
[cite_start]16 [cite: 172]
[cite_start]64 [cite: 173]
(Padrão: 4^i, onde i é o índice da linha/coluna 0, 1, 2, 3)
"""
import random

matriz = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        if i == j:
            # 4^0=1, 4^1=4, 4^2=16, 4^3=64
            matriz[i][j] = 4 ** i
        else:
            matriz[i][j] = random.randint(1, 100)
            
print("Matriz [4][4] com diagonal principal (4^i):")
for linha in matriz:
    print(linha)