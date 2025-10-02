#  Calcule a quantidade de litros gastos em uma viagem, sabendo que o 
# automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. 

tempo = int(input("Insira o tempo do percurso (horas): "))
velocidade_media= int(input("Insira a velocidade média (vm): "))

distancia = tempo * velocidade_media
litros = distancia / 12
print(f"Litros gastos na viagem {litros}L")


