def exibir_tabuada(num):
    print(f"Tabuada de {num}: ")
    for i in range(11):
       result = num * i 
       print(f"{num} X {i} = {result}")

def main():
    try:
        num = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
        return

    exibir_tabuada(num)

if __name__ == "__main__":
    main()