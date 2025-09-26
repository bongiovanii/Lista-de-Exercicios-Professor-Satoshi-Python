# Receba a data de nascimento e atual em ano, mês e dia. Calcule e mostre a
# idade em anos, meses e dias, considerando os anos bissextos

def count_bissexto(anos):
   cont = 0
   for i in range(anos[0], anos[1]):
      if i // 4 == 0:
         cont += 1
   return cont      

data_nascimento = input("Insira a sua data de nascimento (dia/mes/ano): ")
data_atual = input("Insira a data atual(dia/mes/ano): ")

partes_nasc = data_nascimento.split("/")
partes_atual = data_atual.split("/")

nascimento = list(map(int,partes_nasc))
atual = list(map(int,partes_atual))
print(partes_nasc)
print(partes_atual)


idade_anos = atual[2] - nascimento[2]
anos = []
anos.append(atual[2])
anos.append(nascimento[2])
idade_mes = atual[1] -  nascimento[1]

anos_bissextos = count_bissexto(anos)
print(anos_bissextos)
dias = []
dias.append(atual[0])
dias.append(nascimento[0])
dias.sort()

idade_dia = dias[1] - dias[0]
idade_dia += anos_bissextos


print(f"{idade_anos} Anos {idade_mes} Mêses e {idade_dia} Dias")
