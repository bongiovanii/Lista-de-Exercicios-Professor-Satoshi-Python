def calcular_serie_harmonica(num_termos):
    resultado = 0.0
    for i in range(1, num_termos + 1):
        resultado += 1 / i
    return resultado

def main():
    try:
        num = int(input("Digite um numero qualquer: "))
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
        return

    resultado = calcular_serie_harmonica(num)
    print(f" Resultado da série 1 + ... 1/{num}: {resultado}")

if __name__ == "__main__":
    main()