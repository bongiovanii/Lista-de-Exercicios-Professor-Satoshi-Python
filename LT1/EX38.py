# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor
# valor. Obs.: somente valores positivos.

import random

nums = []
for _ in range(100):
   # Para fins de teste eu resolvi utilizar a lib random e importar o método randint para praticidade, o programa funcionará
   # com o usuário dando input também

   # <----Desconmentar o código abaixo caso seja necessário pedir ao usuário dar input----->

   # num = int(input("Digite um número (necessariamente positivo)"))
   # if num < 0:
   #    raise Error("Número inválido (número negativo), insira outro número")
   #    num = int(input("Digite um número (necessariamente positivos)"))
   # else:
   #    nums.append(num)

   nums.append(random.randint(1,1000))

nums.sort()
print(f"Maior número: {nums[99]} \nMenor número: {nums[0]}")
print(nums)