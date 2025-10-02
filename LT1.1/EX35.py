# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre
# o resultado da somatória dos números ímpares entre esses valores.

def soma_imp(numeros):
   min = numeros[0]
   max = numeros[1]
   soma = 0
   for j in range(min,max+1):
      if(j % 2 != 0):
         soma += j
   return soma

numeros = []

for i in range(2):
   numeros.append(int(input("Digite um número: ")))

numeros.sort()
print(f"Maior número: {numeros[1]}")

soma_impares =  soma_imp(numeros)
print(f"Soma dos números impares entre {numeros[0]} e {numeros[1]}: {soma_impares}")