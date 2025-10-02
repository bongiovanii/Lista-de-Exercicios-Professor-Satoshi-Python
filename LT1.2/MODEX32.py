def calcular_fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

def main():
    try:
        n = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
        return

    try:
        fatorial = calcular_fatorial(n)
        print(f"O fatorial de {n} é {fatorial}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()