#  Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3. 

value = int(input("Digite um valor: "))

if value % 2  == 0 and value  % 3 == 0:
   print(f"O valor {value} é divisivel por 2 e por 3")
else:
   print(f"O valor {value} não é divisivel por 2 e por 3")
   