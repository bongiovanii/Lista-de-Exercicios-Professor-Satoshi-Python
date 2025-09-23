# Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a
# idade em anos, meses e dias, considerando os anos bissextos

data_nascimento = input("Insira a sua data de nascimento (dia/mes/ano): ")
data_atual = input("Insira a data atual(dia/mes/ano): ")

partes_nasc = data_nascimento.split("/")
partes_atual = data_atual.split("/")

nascimento = list(map(int,partes_nasc))
atual = list(map(int,partes_atual))
print(partes_nasc)
print(partes_atual)


idade_anos = (len(atual)-1) - (len(nascimento)-1)
print(idade_anos)
