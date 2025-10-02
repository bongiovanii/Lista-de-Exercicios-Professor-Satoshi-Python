# Receba preço atual e média mensal de um produto calcule e mostre o novo preço sabendo que:

preco_atual = float(input("Insira o preço atual do produto: "))
media_mensal = int(input("Agora insira a média mensal de vendas desse produto: "))

if media_mensal < 500 and preco_atual < 30:
    ajuste = preco_atual * 0.1  # 10% de aumento
    preco = preco_atual + ajuste
    print(f"Preço ajustado R${preco:.2f}")
elif (media_mensal >= 500 and media_mensal < 1000) and (preco_atual >= 30 and preco_atual < 80):
    ajuste = preco_atual * 0.15  # 15% de aumento
    preco = preco_atual + ajuste
    print(f"Preço ajustado R${preco:.2f}")
elif media_mensal >= 1000 and preco_atual >= 80:
    ajuste = preco_atual * 0.05  # 5% de desconto
    preco = preco_atual - ajuste
    print(f"Preço ajustado R${preco:.2f}")
else:
    print("ERRO: Nenhum dos parâmetros de validação foi atendido! Verifique os dados inseridos e tente novamente.")
