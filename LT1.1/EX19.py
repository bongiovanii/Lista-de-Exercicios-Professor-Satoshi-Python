# . Receba 2 valores reais. Calcule e mostre o maior deles.
valores = []

valores.append(int(input("Digite um primeiro valor: ")))
valores.append(int(input("Digite um segundo valor: ")))

for i in range(len(valores)):
   for j in range(len(valores)-i-1):
      if(valores[j] > valores[j+1]):
         aux = valores[j]
         valores[j] = valores[j+1]
         valores[j+1] = aux




print(f"Maior: {valores[1]} , Menor: {valores[0]}")