def bubble_sort(lista_numeros):
    n = len(lista_numeros)
    for i in range(n):
        for j in range(n - i - 1):
            if lista_numeros[j] > lista_numeros[j+1]:
                lista_numeros[j], lista_numeros[j+1] = lista_numeros[j+1], lista_numeros[j]
    return lista_numeros

def main():
    num = []
    try:
        num.append(int(input("Insira o primeiro numero: ")))
        num.append(int(input("Insira o segundo numero: ")))
        num.append(int(input("Insira o terceiro numero: ")))
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        return

    num_ordenado = bubble_sort(num)

    print(f"Valores em ordem crescente {num_ordenado[0]}, {num_ordenado[1]} e {num_ordenado[2]} ")

if __name__ == "__main__":
    main()