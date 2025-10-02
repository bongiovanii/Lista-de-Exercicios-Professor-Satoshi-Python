def verificar_divisibilidade(valor):
    return valor % 2 == 0 and valor % 3 == 0

def main():
    try:
        value = int(input("Digite um valor: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return

    if verificar_divisibilidade(value):
       print(f"O valor {value} é divisível por 2 e por 3")
    else:
       print(f"O valor {value} não é divisível por 2 e por 3")

if __name__ == "__main__":
    main()