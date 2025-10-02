# . Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias
# durará esse alimento sabendo que a pessoa consome 50g ao dia

alimento_quilos =  float(input("Insira a quantidade de quilos de alimento: "))
alimento_gramas = alimento_quilos * 1000
duracao_do_alimento = alimento_gramas / 50

print("O alimento durará para uma pessoa ", duracao_do_alimento, " dias.")