# Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. 
# Mostre a mensagem de acordo com a média: a. Se a média for >= 6,0 exibir 
# “APROVADO”; b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”; c. Se a média for 
# < 3,0 exibir “RETIDO”. 

notas = []

notas.append(float(input("Insira a nota do primeiro bimestre: ")))
notas.append(float(input("Insira a nota do segundo bimestre: ")))
notas.append(float(input("Insira a nota do terceiro bimestre: ")))
notas.append(float(input("Insira a nota do quarto bimestre: ")))

media = 0
i = 0
while i < len(notas):
   media += notas[i]
   i += 1

media /= 4
print(f"A media é de {media}")
