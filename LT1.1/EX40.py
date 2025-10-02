# Receba 2 números inteiros. Verifique e mostre todos os números primos
# existentes entre eles.
def valida_primo(n):
   if n <=1:
      return False
   for i in range(2, n):
      if n % i == 0:
         return False
   return True


nums = []
primos = []
soma = 0
for _ in range(2):
   nums.append(int(input("Digite um número: ")))

for i in range(nums[0], nums[1]):
   valida_num = valida_primo(i)
   if valida_num == True:
      soma += i
      primos.append(i)
      
print(f"Soma dos número primos entre {nums[0]} e {nums[1]}: {soma}")      
print(f"Números primos: {primos}")