# Mostre todas as possibilidades de 2 dados de forma que a soma tenha como
# resultado 7.

for dado1 in range(1, 7):
	for dado2 in range(1, 7):
		if dado1 + dado2 == 7:
			print(f"({dado1}, {dado2})")

