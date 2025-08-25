   #  Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos. 

x = int(input("Insira x: "))
y = int(input("Insira y: "))

aux = x
x = y
y = aux

print("Valores trocados: \n x= ", x, " \n y= ", y )