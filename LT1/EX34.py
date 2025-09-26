# Receba um número. Calcule e mostre os resultados da tabuada desse número.

num = int(input("Digite um número: "))
print(f"Tabuada de {num}: ")

for i in range(11):
   result = num * i 
   print(f"{num} X {i} = {result}")