# Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
serie = 0
for n in range(1, 16):
	termo = n / (n * n)
	if n % 2 == 0:
		termo = -termo
	print(f"{'-' if termo < 0 else '+' if n > 1 else ''}{abs(n)}/{n*n} = {termo}")
	serie += termo
print(f"\nSoma da série: {serie}")