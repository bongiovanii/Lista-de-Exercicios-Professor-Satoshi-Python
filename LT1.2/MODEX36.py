import math

def calcular_serie_soma_fatorial(num_termos):
    soma = 0.0
    for i in range(num_termos):
        # A série original parece ter um erro de fórmula, 
        # interpretando como S = Sum(1 + 1/i!) para i de 0 a n-1, que seria 
        # S = n + Sum(1/i!). 
        # Se for E = 1 + 1/1! + 1/2! + ..., o loop deve começar de 0 ou 1.
        # Mantendo a lógica do original: soma += 1 + (1/i!)
        # O fatorial de 0 é 1 (math.factorial(0) = 1)
        try:
             soma += 1 + (1 / math.factorial(i))
        except ValueError:
             # Isso não deve ocorrer com i >= 0
             pass 
    return soma

def main():
    try:
        num = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
        return

    soma = calcular_serie_soma_fatorial(num)

    print(f"Resultado da soma de '1+1/n!': {soma: .3f}")

if __name__ == "__main__":
    main()