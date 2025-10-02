# Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

num = int(input("Digite um numero qualquer: "))
cont = 1
resultado = 0
for i in range(num):
   resultado += 1/cont
   cont += 1
print(f" Resultado da série 1 + ... 1/{num}: {resultado}")