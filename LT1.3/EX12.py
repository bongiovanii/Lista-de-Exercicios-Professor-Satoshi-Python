# EX12.py
"""
[cite_start]Lote 1.3 - Exercício 12 [cite: 244, 245]
[cite_start]Carregar códigos das peças em um tabuleiro de xadrez, onde: [cite: 245, 248]
[cite_start]Peça: Peão Torre Bispo Cavalo Rainha Rei Vazio [cite: 251, 250]
[cite_start]Código: 1 2 3 4 5 6 7 [cite: 246, 247, 249]
[cite_start]Calcular e mostrar a soma das peças do tabuleiro. [cite: 252]
[cite_start]Não pode utilizar estrutura de decisão e Escolha Caso na contagem das peças [cite: 253]
(Assumindo que a "soma das peças" significa a soma dos valores dos códigos)
"""
tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

# Códigos das Peças
PEAO = 1
TORRE = 2
BISPO = 3
CAVALO = 4
RAINHA = 5
REI = 6
VAZIO = 7

# Montagem do tabuleiro
tabuleiro[0] = [TORRE, CAVALO, BISPO, RAINHA, REI, BISPO, CAVALO, TORRE]
tabuleiro[1] = [PEAO] * 8
for i in range(2, 6):
    tabuleiro[i] = [VAZIO] * 8
tabuleiro[6] = [PEAO] * 8
tabuleiro[7] = [TORRE, CAVALO, BISPO, RAINHA, REI, BISPO, CAVALO, TORRE]

# Vetor para contagem (índice 0 não usado, índices 1-7 correspondem às peças)
contagem_pecas = [0] * 8 # [0, P, T, B, C, R, K, V]
soma_total_valores = 0

for i in range(8):
    for j in range(8):
        codigo_peca = tabuleiro[i][j]
        
        # Contagem sem IF/Switch (usando o código como índice)
        contagem_pecas[codigo_peca] += 1
        
        # Soma total dos códigos
        soma_total_valores += codigo_peca
        
print("Tabuleiro de Xadrez (Códigos):")
for linha in tabuleiro:
    print(linha)
    
print("\nContagem de Peças (sem 'if' ou 'switch'):")
print(f"Peões (1): {contagem_pecas[PEAO]}")
print(f"Torres (2): {contagem_pecas[TORRE]}")
print(f"Bispos (3): {contagem_pecas[BISPO]}")
print(f"Cavalos (4): {contagem_pecas[CAVALO]}")
print(f"Rainhas (5): {contagem_pecas[RAINHA]}")
print(f"Reis (6): {contagem_pecas[REI]}")
print(f"Vazios (7): {contagem_pecas[VAZIO]}")

print(f"\nSoma total dos valores (códigos) das peças: {soma_total_valores}")