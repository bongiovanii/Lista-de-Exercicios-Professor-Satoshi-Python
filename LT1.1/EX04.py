   #  Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5. 

print("------------------- Conversor de Temperatura ------------------- \n")
tempCelsius = int(input("Insira a temperatura desejada em graus Celsius: "))
tempFah = (9*tempCelsius+160) /5
print("Temperatura em fahrenheit: ", tempFah)