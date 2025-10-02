#  Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem 
# crescente. 
def boubleSort(num):
   for i in range(len(num)):
      for j in range(len(num)-i-1):
         if(num[j] > num[j+1]):
            aux =  num[j]
            num[j] =  num[j+1]
            num[j+1] = aux
   return num


num = []
num.append(int(input("Insira o primeiro numero: ")))
num.append(int(input("Insira o segundo numero: ")))

num =  boubleSort(num)

print(f"Valores e ordem crescente {num[0]} e {num[1]} ")

