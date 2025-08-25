#  Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de
# desconto e o número de descendentes. Calcule o salário que serão as horas
# trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto –
# desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o
# salário a receber.


horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora_trabalhada = int(input("Insira o valor por hora trabalhada: "))
percentual_desconto = int(
    input("Digite o percentual de desconto (sem '%' penas o numero): "))
percentual_desconto = percentual_desconto / 100
numero_descendentes = int(
    input("Insira o numero de descendetes em sua família: "))

salario = (horas_trabalhadas * valor_hora_trabalhada) * 31
salario_liquido = salario - percentual_desconto
acrescimo = 100 * numero_descendentes

salario_liquido += acrescimo

print("O salario final após o reajuste será de: ", salario_liquido)
