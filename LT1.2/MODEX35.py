
def soma_impares_intervalo(num1, num2):
    numeros = sorted([num1, num2])
    min_val = numeros[0]
    max_val = numeros[1]
    
    soma = 0
    # Começa do menor+1 para não incluir o próprio limite se for ímpar
    for j in range(min_val + 1, max_val):
       if(j % 2 != 0):
         soma += j
    return soma

def main():
    numeros = []
    try:
        numeros.append(int(input("Digite o primeiro número: ")))
        numeros.append(int(input("Digite o segundo número: ")))
    except ValueError:
        print("Entrada inválida. Insira números inteiros.")
        return

    numeros.sort()
    
    print(f"Maior número: {numeros[1]}")

    soma_impares = soma_impares_intervalo(numeros[0], numeros[1])
    print(f"Soma dos números ímpares entre {numeros[0]} e {numeros[1]}: {soma_impares}")

if __name__ == "__main__":
    main()