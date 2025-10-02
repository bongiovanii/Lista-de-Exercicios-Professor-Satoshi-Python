# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e
# quantos anos terá daqui a 17 anos.

anoNascimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idade = (anoAtual - anoNascimento) + 17

print("Daqui a 17 anos você  terá ", idade, " anos")