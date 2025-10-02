# Receba 2ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

ang1 = int(input("Digite o primeiro angulo: "))
ang2 = int(input("Digite o segundo angulo: "))

calc = ang1 + ang2
result = 180 - calc
print("O terceiro ângulo  é igual a ", result)