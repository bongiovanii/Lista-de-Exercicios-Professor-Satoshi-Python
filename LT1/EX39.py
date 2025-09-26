# Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

tabuleiro = []
quantidade = []

for i in range(1,65):
   tabuleiro.append(i)
   quantidade.append(2 ** (i-1))

for j in range(len(tabuleiro)):
   print(f"Casa: {tabuleiro[j]} Quantidade: {quantidade[j]}")


