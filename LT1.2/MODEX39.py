def calcular_graos_xadrez(num_casas=64):
    tabuleiro = []
    quantidade = []

    for i in range(1, num_casas + 1):
        tabuleiro.append(i)
        quantidade.append(2 ** (i - 1))
        
    return tabuleiro, quantidade

def main():
    tabuleiro, quantidade = calcular_graos_xadrez()
    
    for j in range(len(tabuleiro)):
        print(f"Casa: {tabuleiro[j]} Quantidade: {quantidade[j]:.0f}")

if __name__ == "__main__":
    main()