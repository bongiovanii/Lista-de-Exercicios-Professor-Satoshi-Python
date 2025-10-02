def parse_hora_minuto(entrada_str):
    partes = entrada_str.split(":")
    if len(partes) != 2:
        raise ValueError("Formato incorreto. Use HH:MM.")
        
    hora = int(partes[0])
    minuto = int(partes[1])
    
    if not (0 <= hora <= 23 and 0 <= minuto <= 59):
        raise ValueError("Horas (0-23) ou Minutos (0-59) inválidos.")
        
    return hora, minuto

def calcula_tempo(temp_ini_h, temp_ini_m, temp_fin_h, temp_fin_m):
    minutos_iniciais = temp_ini_h * 60 + temp_ini_m
    minutos_finais = temp_fin_h * 60 + temp_fin_m
    total_minutos_dia = 24 * 60

    if minutos_finais <= minutos_iniciais:
        duracao_total_minutos = (total_minutos_dia - minutos_iniciais) + minutos_finais
    else:
        duracao_total_minutos = minutos_finais - minutos_iniciais

    horas_de_jogo = duracao_total_minutos // 60
    minutos_de_jogo = duracao_total_minutos % 60

    return (horas_de_jogo, minutos_de_jogo)

def main():
    try:
        _inicio = input("Digite a hora inicial do jogo (HH:MM): ")
        _fim = input("Digite a hora final do jogo (HH:MM): ")

        hora_incial, min_inicial = parse_hora_minuto(_inicio)
        hora_final, min_final = parse_hora_minuto(_fim)
        
    except ValueError as e:
        print(f"ERRO: Entrada de hora inválida. {e}")
        return

    tempo_da_partida = calcula_tempo(hora_incial, min_inicial, hora_final, min_final)
    
    print("-" * 40)
    print(f"Início do jogo: {_inicio}")
    print(f"Fim do jogo:    {_fim}")
    print(f"Tempo de jogo:  {tempo_da_partida[0]} hora(s) e {tempo_da_partida[1]} minuto(s).")
    print("-" * 40)

if __name__ == "__main__":
    main()