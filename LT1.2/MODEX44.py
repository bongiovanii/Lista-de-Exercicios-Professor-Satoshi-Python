def calcular_potencia(base, expoente):
    return base ** expoente

def main():
    try:
        base = float(input("Digite o número da base: "))
        expoente = float(input("Digite o expoente: "))
    except ValueError:
        print("Entrada inválida. Insira números válidos.")
        return
        
    potencia = calcular_potencia(base, expoente)
    
    print(f"{base} elevado a {expoente} é igual a {potencia}")

if __name__ == "__main__":
    main()