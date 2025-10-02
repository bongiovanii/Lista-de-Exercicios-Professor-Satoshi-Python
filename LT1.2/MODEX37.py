def fibo(num):
    seq = []
    a, b = 0, 1
    for _ in range(num):
        seq.append(a)
        a, b = b, a + b
    return seq

def main():
    try:
        num = int(input("Digite um numero qualquer: "))
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
        return

    seq = fibo(num)
    print(f"Sequência de fibonacci até o {num} termo: {seq}" )

if __name__ == "__main__":
    main()