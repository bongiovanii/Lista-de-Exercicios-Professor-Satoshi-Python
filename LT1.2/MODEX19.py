def encontrar_maior_e_menor(valor1, valor2):
    valores = [valor1, valor2]
    
    if valores[0] > valores[1]:
        valores[0], valores[1] = valores[1], valores[0]
        
    menor = valores[0]
    maior = valores[1]
    return maior, menor

def main():
    try:
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        return

    maior, menor = encontrar_maior_e_menor(valor1, valor2)
    
    print(f"Maior: {maior} , Menor: {menor}")

if __name__ == "__main__":
    main()