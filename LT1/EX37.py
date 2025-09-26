# Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu
# N’nésimo termo.

def fibo(num):
   seq = []
   a, b = 0, 1
   for _ in range(num):
      seq.append(a)
      a, b = b, a + b
   return seq

num = int(input("Digite um numero qualquer: "))

seq = fibo(num)
print(f"Sequência de fibonacci  até o {num} termo: {seq}" )

