# Criar e coletar um vetor [100] inteiro e exibir:
# a. O maior e o menor valor;
# b. A média dos valores.

import random

array = []
som = 0
for i in range(100):
    num = random.randint(0,9999)
    array.append(num)
    som += num
array.sort()
print(f"O menor valor é: {array[0]} \nO maior valor é: {array[99]}")
print(f"A media dos valores é: {som/100}")
print(array)
