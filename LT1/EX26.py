#  Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do 
# menor. 

numeros = {
   'primeiro': int(input("Digite o primeiro numero: ")),
   'segundo': int(input("Digite o segundo numero: "))
}
print("-"*60)
if(numeros['primeiro'] > numeros['segundo']):
   print(f"O numero {numeros['primeiro']} é o maior")
   if (numeros['primeiro'] % numeros['segundo'] == 0):
      print(f"O numero {numeros['primeiro']} é divisível pelo {numeros['segundo']}")
   else:
      print(f"O numero {numeros['primeiro']} não é divisível pelo {numeros['segundo']}")

print("-"*60)

if(numeros['segundo'] > numeros['primeiro']):
   print(f"O numero {numeros['segundo']} é o maior")
   if (numeros['segundo'] % numeros['primeiro'] == 0):
      print(f"O numero {numeros['segundo']} é divisível pelo {numeros['primeiro']}")
   else:
      print(f"O numero {numeros['segundo']} não é divisível pelo {numeros['primeiro']}")


