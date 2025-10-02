def comparar_e_verificar_divisibilidade(num1, num2):
    resultados = []
    
    if num1 > num2:
        maior = num1
        menor = num2
        resultados.append(f"O número {maior} é o maior")
        if (maior % menor == 0):
            resultados.append(f"O número {maior} é divisível pelo {menor}")
        else:
            resultados.append(f"O número {maior} não é divisível pelo {menor}")
            
    elif num2 > num1:
        maior = num2
        menor = num1
        resultados.append(f"O número {maior} é o maior")
        if (maior % menor == 0):
            resultados.append(f"O número {maior} é divisível pelo {menor}")
        else:
            resultados.append(f"O número {maior} não é divisível pelo {menor}")
    else:
        resultados.append(f"Os números são iguais: {num1}")
        
    return resultados

def main():
    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        return
        
    resultados = comparar_e_verificar_divisibilidade(num1, num2)
    
    print("-" * 60)
    for resultado in resultados:
        print(resultado)
    print("-" * 60)

if __name__ == "__main__":
    main()