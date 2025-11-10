# EX10.py
"""
[cite_start]Lote 1.3 - Exercício 10 [cite: 174, 175, 178]
Criar uma matriz [8] [8] onde o programa irá carregar segundo:
[cite_start]casa 1 2 3 4 ... [cite: 177]
[cite_start]valor 1 2 4 8 ... [cite: 179]
[cite_start]Exibir a soma dos valores [cite: 180]
(Refere-se ao problema do trigo no tabuleiro de xadrez)
"""
matriz = [[0 for _ in range(8)] for _ in range(8)]
soma_total = 0

valor = 1

for i in range(8):
    for j in range(8):
        matriz[i][j] = valor
        soma_total += valor
        valor *= 2
        
print("Matriz [8][8] (Grãos de Xadrez):")
for i in range(8):
    # Mostrando apenas 8 colunas por linha (embora o cálculo continue)
    print(f"Linha {i+1}: {[matriz[i][j] for j in range(8)]}")
    
print(f"\nSoma total dos valores: {soma_total}")