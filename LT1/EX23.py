# Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não 
# necessariamente em ordem. Mostre os 4 números em ordem crescente. 

def boubleSort(num):
   for i in range(len(num)):
      for j in range(len(num)-i-1):
         if(num[j] > num[j+1]):
            aux =  num[j]
            num[j] =  num[j+1]
            num[j+1] = aux
   return num


num = []
num.append(int(input("Insira o primeiro numero em ordem crescente: ")))
num.append(int(input("Insira o segundo numero em ordem crescente: ")))
num.append(int(input("Insira o segundo numero não necessariamente em ordem crescente : ")))

num =  boubleSort(num)

print(f"Valores e ordem crescente {num[0]}, {num[1]} e {num[2]} ")