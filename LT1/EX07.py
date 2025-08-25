   #  Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume. 

def calculaArea(comp,larg,alt):
   volume = comp * larg * alt

   return volume



comp = int(input("Digite o comprimento: "))
larg = int(input("Digite o comprimento: "))
alt = int(input("Digite o comprimento: "))

volume = calculaArea(comp,larg,alt)
print("O volume é igual a: ", volume,"m cúbicos")