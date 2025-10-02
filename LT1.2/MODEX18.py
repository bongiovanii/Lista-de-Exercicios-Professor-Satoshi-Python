def ordenar_e_calcular_diferenca(num1, num2):
    numeros = [num1, num2]
    
    if numeros[0] > numeros[1]:
        numeros[0], numeros[1] = numeros[1], numeros[0]
        
    diferenca = numeros[1] - numeros[0]
    return diferenca, numeros

def main():
    try:
        primeiro_numero = int(input("Insira o primeiro número: "))
        segundo_numero = int(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        return

    diferenca, numeros_ordenados = ordenar_e_calcular_diferenca(primeiro_numero, segundo_numero)
    
    print(f"Diferença: {diferenca} e vetor ordenado: {numeros_ordenados}")

if __name__ == "__main__":
    main()