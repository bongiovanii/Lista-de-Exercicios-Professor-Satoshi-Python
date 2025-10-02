def obter_dados():
    horas = int(input("Digite a quantidade de horas trabalhadas: "))
    valor_hora = int(input("Insira o valor por hora trabalhada: "))
    desconto = int(input("Digite o percentual de desconto (sem '%' apenas o número): ")) / 100
    descendentes = int(input("Insira o número de descendentes em sua família: "))
    return horas, valor_hora, desconto, descendentes

def calcular_salario(horas, valor_hora):
    return horas * valor_hora * 31

def calcular_desconto(salario, percentual):
    return salario * percentual

def calcular_acrescimo(descendentes):
    return 100 * descendentes

def calcular_salario_final(salario, desconto, acrescimo):
    return salario - desconto + acrescimo

def main():
    horas, valor_hora, percentual, descendentes = obter_dados()
    salario = calcular_salario(horas, valor_hora)
    desconto = calcular_desconto(salario, percentual)
    acrescimo = calcular_acrescimo(descendentes)
    salario_final = calcular_salario_final(salario, desconto, acrescimo)
    print("O salário final após o reajuste será de:", salario_final)

if __name__ == "__main__":
    main()