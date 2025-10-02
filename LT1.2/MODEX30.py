def count_bissexto_entre_anos(ano_ini, ano_fim):
    if ano_ini > ano_fim:
        ano_ini, ano_fim = ano_fim, ano_ini
        
    cont = 0
    for ano in range(ano_ini, ano_fim):
        if ano % 4 == 0: 
            cont += 1
    return cont      

def calcular_idade(data_nascimento_str, data_atual_str):
    try:
        nascimento = list(map(int, data_nascimento_str.split("/")))
        atual = list(map(int, data_atual_str.split("/")))
        
        dia_nasc, mes_nasc, ano_nasc = nascimento
        dia_atual, mes_atual, ano_atual = atual
        
        idade_anos = ano_atual - ano_nasc
        idade_mes = mes_atual - mes_nasc
        idade_dia = dia_atual - dia_nasc
        
        if idade_mes < 0 or (idade_mes == 0 and idade_dia < 0):
            idade_anos -= 1
            idade_mes += 12
            
        idade_mes = atual[1] - nascimento[1]
        idade_dia = abs(atual[0] - nascimento[0])
            
        anos_bissextos = count_bissexto_entre_anos(ano_nasc, ano_atual)
        
        idade_dia += anos_bissextos

        return idade_anos, idade_mes, idade_dia
        
    except Exception as e:
        print(f"Erro ao processar as datas: {e}")
        return None, None, None


def main():
    data_nascimento = input("Insira a sua data de nascimento (dia/mes/ano): ")
    data_atual = input("Insira a data atual (dia/mes/ano): ")
    
    idade_anos, idade_mes, idade_dia = calcular_idade(data_nascimento, data_atual)

    if idade_anos is not None:
        print(f"{idade_anos} Anos, {idade_mes} Mêses e {idade_dia} Dias")

if  __name__ == "__main__":
    main()