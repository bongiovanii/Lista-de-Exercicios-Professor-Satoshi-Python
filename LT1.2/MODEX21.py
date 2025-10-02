def calcular_media(notas):
    soma_notas = sum(notas)
    if not notas:
        return 0
    media = soma_notas / len(notas)
    return media

def main():
    
    notas = []
    try:
        notas.append(float(input("Insira a nota do primeiro bimestre: ")))
        notas.append(float(input("Insira a nota do segundo bimestre: ")))
        notas.append(float(input("Insira a nota do terceiro bimestre: ")))
        notas.append(float(input("Insira a nota do quarto bimestre: ")))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos para as notas.")
        return

    media = calcular_media(notas)
    print(f"A média é de {media:.2f}")

if __name__ == "__main__":
    main()