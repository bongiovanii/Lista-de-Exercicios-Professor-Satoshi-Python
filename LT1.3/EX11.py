# EX11.py
"""
[cite_start]Lote 1.3 - Exercício 11 [cite: 181, 182, 183]
Criar uma matriz [8] [8] inteiro e o programa irá carregar segundo:
[cite_start](O padrão mostrado na imagem [cite: 184-243] é o de "distância da borda")
1 1 1 1 1 1 1 1
1 2 2 2 2 2 2 1
1 2 3 3 3 3 2 1
1 2 3 4 4 3 2 1
1 2 3 4 4 3 2 1
1 2 3 3 3 3 2 1
1 2 2 2 2 2 2 1
1 1 1 1 1 1 1 1
"""
matriz = [[0 for _ in range(8)] for _ in range(8)]

n = 8
for i in range(n):
    for j in range(n):
        # Calcula a distância mínima de todas as 4 bordas
        dist_i = i
        dist_j = j
        dist_n_i = (n - 1) - i
        dist_n_j = (n - 1) - j
        
        # O valor é o mínimo das distâncias + 1 (pois começa em 1)
        matriz[i][j] = min(dist_i, dist_j, dist_n_i, dist_n_j) + 1
        
print("Matriz [8][8] Padrão (Distância da Borda):")
for linha in matriz:
    print(f"[{', '.join(map(str, linha))}]")