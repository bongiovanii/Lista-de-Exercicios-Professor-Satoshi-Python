def calcular_ajuste_preco(preco_atual, media_mensal):
    novo_preco = None
    
    if media_mensal < 500 and preco_atual < 30:
        ajuste = preco_atual * 0.1
        novo_preco = preco_atual + ajuste
    elif (500 <= media_mensal < 1000) and (30 <= preco_atual < 80):
        ajuste = preco_atual * 0.15
        novo_preco = preco_atual + ajuste
    elif media_mensal >= 1000 and preco_atual >= 80:
        ajuste = preco_atual * 0.05
        novo_preco = preco_atual - ajuste
    
    return novo_preco

def main():
    try:
        preco_atual = float(input("Insira o preço atual do produto: "))
        media_mensal = int(input("Agora insira a média mensal de vendas desse produto: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    preco_ajustado = calcular_ajuste_preco(preco_atual, media_mensal)
    
    if preco_ajustado is not None:
        print(f"Preço ajustado R${preco_ajustado:.2f}")
    else:
        print("ERRO: Nenhum dos parâmetros de validação foi atendido! Verifique os dados inseridos e tente novamente.")

if __name__ == "__main__":
    main()