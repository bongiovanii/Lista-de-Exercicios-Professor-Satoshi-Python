# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior 
# pelo menos valor. 


numeros = []
primeiro_numero =  int(input("Insira um numero: "))
numeros.append(primeiro_numero)
segundo_numero = int(input("Digite um segundo numero: "))
numeros.append(segundo_numero)

for i in range(len(numeros)):
   for j in range(len(numeros)-i-1):
      if(numeros[j] > numeros[j+1]):
         aux = numeros[j]
         numeros[j] = numeros[j+1]
         numeros[j+1] = aux

diferenca = numeros[1] - numeros[0]
print(f"Diferença: {diferenca}  e vetor ordenado:",numeros)

