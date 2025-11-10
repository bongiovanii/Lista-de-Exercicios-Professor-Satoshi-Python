# EX13.py
"""
CAIXA ELETRÔNICO
1. Criar um menu de opções:
Menu Principal
1- Carregar Notas
2-Retirar Notas
3- Estatística
9-Fim

1.1. Carregar a quantidade de notas em uma área da memória com 6 ocorrências.
1.2. Solicitar que o cliente faça a retirada de valores obedecendo ao critério do maior
pelo menor.
1.3. Dar a opção para o cliente escolher o valor e a quantidade de notas.
1.4. Caso não tenha o valor da maior cédula, disponibilizar a próxima. (Implementado no 1.2)
1.5. Se o valor a ser solicitado for maior que o saldo total do caixa, enviar a mensagem
"EXCEDEU O LIMITE DO CAIXA".
1.6. Solicitar até 100 retiradas ou até não haver mais notas.
1.7. No momento da solicitação do valor, coletar também o código do banco que o
cliente tem conta, segundo:
(1=BB, 2=Santander, 3=Itaú, 4=Caixa)
1.8. No final, exibir a estatística, separada por bancos, com:
1.8.1. O maior e o menor valor sacado;
1.8.2. A média dos saques;
1.8.3. Valor total dos saques;
1.8.4. Valor das sobras dos caixas.
(Obs: Assumindo notas de 200, 100, 50, 20, 10, 5)
"""
import math



def carregar_notas(notas_caixa):
    print("--- 1. Carregar Notas ---")
    try:
        # 6 ocorrências
        notas_caixa[0] = int(input("Qtd Notas R$ 200: "))
        notas_caixa[1] = int(input("Qtd Notas R$ 100: "))
        notas_caixa[2] = int(input("Qtd Notas R$ 50: "))
        notas_caixa[3] = int(input("Qtd Notas R$ 20: "))
        notas_caixa[4] = int(input("Qtd Notas R$ 10: "))
        notas_caixa[5] = int(input("Qtd Notas R$ 5: "))
        print("Notas carregadas com sucesso.")
    except ValueError:
        print("Erro: Digite apenas números inteiros.")
    return notas_caixa

def calcular_saldo_total(notas_caixa, valores_notas):
    saldo = 0
    for i in range(len(notas_caixa)):
        saldo += notas_caixa[i] * valores_notas[i]
    return saldo

def atualizar_estatisticas(estatisticas, banco, valor_saque):
    estatisticas[banco]["total_sacado"] += valor_saque
    estatisticas[banco]["num_saques"] += 1
    
    if valor_saque > estatisticas[banco]["maior_saque"]:
        estatisticas[banco]["maior_saque"] = valor_saque
    
    # Inicia o menor saque com o primeiro saque válido
    if estatisticas[banco]["menor_saque"] == float('inf'):
        estatisticas[banco]["menor_saque"] = valor_saque
    elif valor_saque < estatisticas[banco]["menor_saque"]:
        estatisticas[banco]["menor_saque"] = valor_saque
        
    return estatisticas

#  Retirada automática (maior pelo menor)
def retirar_notas_auto(notas_caixa, valores_notas, saques, estatisticas, banco):
    try:
        valor_saque = int(input("Digite o valor a sacar: "))
    except ValueError:
        print("Valor inválido.")
        return notas_caixa, saques, estatisticas
    
    saldo_total_caixa = calcular_saldo_total(notas_caixa, valores_notas)
    
    if valor_saque <= 0:
        print("Valor inválido.")
        return notas_caixa, saques, estatisticas

    #  Verifica se excede o limite do caixa
    if valor_saque > saldo_total_caixa:
        print("EXCEDEU O LIMITE DO CAIXA")
        return notas_caixa, saques, estatisticas

    valor_restante = valor_saque
    notas_a_entregar = [0] * 6
    notas_caixa_temp = list(notas_caixa) # Cópia para simulação
    
    #  Critério do maior pelo menor
    #  Disponibiliza a próxima se não houver da maior
    for i in range(len(valores_notas)):
        qtd_necessaria = valor_restante // valores_notas[i]
        
        if qtd_necessaria > notas_caixa_temp[i]:
            qtd_a_dar = notas_caixa_temp[i]
        else:
            qtd_a_dar = qtd_necessaria
            
        notas_a_entregar[i] = qtd_a_dar
        notas_caixa_temp[i] -= qtd_a_dar
        valor_restante -= qtd_a_dar * valores_notas[i]

    # Verifica se foi possível compor o valor
    if valor_restante != 0:
        print("Não é possível sacar o valor exato com as notas disponíveis.")
        return notas_caixa, saques, estatisticas
    
    # Se chegou aqui, o saque é possível
    print("Saque Aprovado. Entregando:")
    for i in range(len(valores_notas)):
        if notas_a_entregar[i] > 0:
            print(f"{notas_a_entregar[i]} nota(s) de R$ {valores_notas[i]}")
    
    notas_caixa = notas_caixa_temp # Efetiva o saque
    saques.append((banco, valor_saque))
    
    estatisticas = atualizar_estatisticas(estatisticas, banco, valor_saque)
        
    return notas_caixa, saques, estatisticas

#  Retirada manual (cliente escolhe as notas)
def retirar_notas_manual(notas_caixa, valores_notas, saques, estatisticas, banco):
    try:
        print("Digite a quantidade de notas desejada:")
        qtd_200 = int(input(f"Qtd R$ 200 (Disponível: {notas_caixa[0]}): ") or 0)
        qtd_100 = int(input(f"Qtd R$ 100 (Disponível: {notas_caixa[1]}): ") or 0)
        qtd_50 = int(input(f"Qtd R$ 50 (Disponível: {notas_caixa[2]}): ") or 0)
        qtd_20 = int(input(f"Qtd R$ 20 (Disponível: {notas_caixa[3]}): ") or 0)
        qtd_10 = int(input(f"Qtd R$ 10 (Disponível: {notas_caixa[4]}): ") or 0)
        qtd_5 = int(input(f"Qtd R$ 5 (Disponível: {notas_caixa[5]}): ") or 0)
    except ValueError:
        print("Entrada inválida.")
        return notas_caixa, saques, estatisticas

    qtd_desejada = [qtd_200, qtd_100, qtd_50, qtd_20, qtd_10, qtd_5]
    valor_saque = 0
    possivel = True
    
    for i in range(6):
        if qtd_desejada[i] > notas_caixa[i]:
            possivel = False
            print(f"Quantidade de notas de R$ {valores_notas[i]} indisponível.")
            break
        valor_saque += qtd_desejada[i] * valores_notas[i]

    #  Verifica se excede o limite do caixa (para esta combinação)
    if not possivel:
        print("Saque não realizado por falta de notas.")
        return notas_caixa, saques, estatisticas
        
    if valor_saque == 0:
        print("Nenhuma nota solicitada.")
        return notas_caixa, saques, estatisticas

    # Efetiva o saque
    for i in range(6):
        notas_caixa[i] -= qtd_desejada[i]
    
    print(f"Saque de R$ {valor_saque} aprovado.")
    saques.append((banco, valor_saque))

    estatisticas = atualizar_estatisticas(estatisticas, banco, valor_saque)
        
    return notas_caixa, saques, estatisticas

# --- Menu de Retirada (Item 2) ---
def menu_retirada(notas_caixa, valores_notas, saques, estatisticas, num_retiradas):
    #  Limite de 100 retiradas
    if num_retiradas >= 100:
        print("Limite de 100 retiradas atingido.")
        return notas_caixa, saques, estatisticas, num_retiradas

    #  Até não haver mais notas
    if calcular_saldo_total(notas_caixa, valores_notas) == 0:
        print("Caixa sem notas. Recarregue.")
        return notas_caixa, saques, estatisticas, num_retiradas
    
    # Coletar código do banco
    try:
        print("Código Banco: (1=BB, 2=Santander, 3=Itaú, 4=Caixa)")
        banco = int(input("Digite o código do seu banco: "))
        if banco not in [1, 2, 3, 4]:
            print("Banco inválido.")
            return notas_caixa, saques, estatisticas, num_retiradas
    except ValueError:
        print("Código inválido.")
        return notas_caixa, saques, estatisticas, num_retiradas

    print("\nModo de Retirada:")
    print("1 - Automático (Maior pela menor)") # 1.2
    print("2 - Manual (Escolher notas)")   # 1.3
    try:
        modo = int(input("Escolha o modo: "))
    except ValueError:
        print("Modo inválido.")
        return notas_caixa, saques, estatisticas, num_retiradas

    if modo == 1:
        notas_caixa, saques, estatisticas = retirar_notas_auto(notas_caixa, valores_notas, saques, estatisticas, banco)
    elif modo == 2:
        notas_caixa, saques, estatisticas = retirar_notas_manual(notas_caixa, valores_notas, saques, estatisticas, banco)
    else:
        print("Modo inválido.")
        return notas_caixa, saques, estatisticas, num_retiradas
    
    num_retiradas += 1
    return notas_caixa, saques, estatisticas, num_retiradas

# --- Função de Estatística (Item 3) ---
def exibir_estatisticas(estatisticas, notas_caixa, valores_notas):
    print("\n--- 3. Estatísticas ---")
    
    nomes_bancos = {1: "Banco do Brasil", 2: "Santander", 3: "Itaú", 4: "Caixa"}
    
    for banco_id, nome in nomes_bancos.items():
        print(f"\n{nome} (Banco {banco_id}):")
        stats = estatisticas[banco_id]
        
        if stats["num_saques"] > 0:
            media = stats["total_sacado"] / stats["num_saques"]
            print(f"  Maior valor sacado: R$ {stats['maior_saque']}") # 1.8.1
            print(f"  Menor valor sacado: R$ {stats['menor_saque']}") # 1.8.1
            print(f"  Média dos saques: R$ {media:.2f}") # 1.8.2
            print(f"  Valor total dos saques: R$ {stats['total_sacado']}") # 1.8.3
        else:
            print("  Nenhum saque realizado.")
            
    #  Valor das sobras
    saldo_sobra = calcular_saldo_total(notas_caixa, valores_notas)
    print(f"\nValor das sobras dos caixas: R$ {saldo_sobra}")
    print("Notas restantes:")
    for i in range(6):
        print(f"  R$ {valores_notas[i]}: {notas_caixa[i]} notas")

# --- Função Principal (Main) ---
def main():
    valores_notas = [200, 100, 50, 20, 10, 5]
    notas_caixa = [0] * 6 # 1.1
    saques = []
    num_retiradas = 0
    
    # Estrutura para estatísticas por banco
    estatisticas = {
        1: {"maior_saque": 0, "menor_saque": float('inf'), "total_sacado": 0, "num_saques": 0}, # BB
        2: {"maior_saque": 0, "menor_saque": float('inf'), "total_sacado": 0, "num_saques": 0}, # Santander
        3: {"maior_saque": 0, "menor_saque": float('inf'), "total_sacado": 0, "num_saques": 0}, # Itaú
        4: {"maior_saque": 0, "menor_saque": float('inf'), "total_sacado": 0, "num_saques": 0}, # Caixa
    }

    while True:
        print("\n--- CAIXA ELETRÔNICO ---")
        print("Menu Principal")
        print("1 - Carregar Notas")
        print("2 - Retirar Notas")
        print("3 - Estatística")
        print("9 - Fim")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue
            
        if opcao == 1:
            notas_caixa = carregar_notas(notas_caixa)
        elif opcao == 2:
            notas_caixa, saques, estatisticas, num_retiradas = menu_retirada(notas_caixa, valores_notas, saques, estatisticas, num_retiradas)
        elif opcao == 3:
            exibir_estatisticas(estatisticas, notas_caixa, valores_notas)
        elif opcao == 9:
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()