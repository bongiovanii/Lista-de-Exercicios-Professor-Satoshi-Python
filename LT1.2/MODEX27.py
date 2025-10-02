def calcular_velocidade_media(num_voltas, ext_circuito_m, tempo_min):
    distancia_total_m = num_voltas * ext_circuito_m
    distancia_total_km = distancia_total_m / 1000
    tempo_horas = tempo_min / 60
    
    if tempo_horas == 0:
        return 0.0

    vel_med_kmh = distancia_total_km / tempo_horas
    
    return vel_med_kmh

def main():
    try:
        nmr_voltas = int(input("Digite o número de voltas: "))
        ext_circuito = float(input("Digite a extensão do circuito (em metros): "))
        tempo = float(input("Digite o tempo de duração do circuito (em minutos): "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    vel_med = calcular_velocidade_media(nmr_voltas, ext_circuito, tempo)

    print(f"Velocidade média: {vel_med:.2f} km/h")

if __name__ == "__main__":
    main()