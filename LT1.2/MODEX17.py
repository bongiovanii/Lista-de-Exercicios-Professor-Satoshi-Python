def receber_dados():
	tempo = int(input("Insira o tempo do percurso (horas): "))
	velocidade_media = int(input("Insira a velocidade média (vm): "))
	return tempo, velocidade_media

def calcular_distancia(tempo, velocidade_media):
	return tempo * velocidade_media

def calcular_litros(distancia):
	return distancia / 12

def main():
	tempo, velocidade_media = receber_dados()
	distancia = calcular_distancia(tempo, velocidade_media)
	litros = calcular_litros(distancia)
	print(f"Litros gastos na viagem {litros: .2f}L")

if __name__ == "__main__":
	main()
