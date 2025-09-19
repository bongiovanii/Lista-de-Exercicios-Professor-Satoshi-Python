# Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

nmr_voltas = int(input("Digite o número de voltas: "))
ext_circuito = int(input("Digite a extensão do circuito (em metros): "))
tempo = int(input("Digite o tempo de duração do circuito (em minutos): "))
vel_med = (nmr_voltas * ext_circuito)/tempo

print(f"Velocidade média: {vel_med:.2f}km/h")
