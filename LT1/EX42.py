# Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
serie = 0
for numerador in range(1, 51):
	denominador = 2 * numerador - 1
	termo = numerador / denominador
	print(f"{numerador}/{denominador} = {termo}")
	serie += termo
print(f"\nSoma da série: {serie}")