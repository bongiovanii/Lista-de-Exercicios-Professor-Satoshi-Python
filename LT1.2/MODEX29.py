
def calcula_investimento_rend(valor):
   porcent = valor * 0.05
   rendimento = porcent * 30
   valor += rendimento
   return valor


def calcula_investimento_poup(valor):
   porcent = valor * 0.03
   rendimento = porcent * 30
   valor += rendimento
   return valor

tipo_investimento  = int(input("Digite o tipo de investimento: \n 1-Poupança \n 2-Renda Fixa \n"))
if tipo_investimento < 1 or tipo_investimento > 2:
   raise ValueError("Opção de conta inexistente")
else:
   valor = float(input("Digite o valor do investimento: "))

   match tipo_investimento:
      case 1:
         valor = calcula_investimento_poup(valor)
         print(f"Valor corrigido com o rendimento de 30 dias na poupança: R${valor}")
      case 2:
         valor = calcula_investimento_rend(valor)
         print(f"Valor corrigido com o rendimento de 30 dias na renda fixa: R${valor}")