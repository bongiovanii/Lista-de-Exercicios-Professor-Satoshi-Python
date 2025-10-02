#  Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo
# em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e
# pode começar num dia e terminar noutro.

               
def calcula_tempo(temp_ini, temp_fin):
    # Função para converter os
    minutos_iniciais = temp_ini[0] * 60 + temp_ini[1]
    minutos_finais = temp_fin[0] * 60 + temp_fin[1]

    if minutos_finais <= minutos_iniciais:
        duracao_total_minutos = (1440 - minutos_iniciais) + minutos_finais
    else:
        duracao_total_minutos = minutos_finais - minutos_iniciais

    horas_de_jogo = duracao_total_minutos // 60
    minutos_de_jogo = duracao_total_minutos % 60

    return (horas_de_jogo, minutos_de_jogo)


_inicio = input("Digite  a hora inicial do jogo (HH:MM): ")
_inicial = _inicio.split(":")
hora_incial = int(_inicial[0])
min_inicial = int(_inicial[1])

_fim = input("Digite  a hora inicial do jogo (HH:MM): ")
_final = _fim.split(":")
hora_final = int(_final[0])
min_final = int(_final[1])

tempo_incial = []
tempo_final = []
tempo_incial.append(hora_incial)
tempo_incial.append(min_inicial)

tempo_final.append(hora_final)
tempo_final.append(min_final)


if tempo_incial[0] > 23 or tempo_final[0] > 23 or tempo_incial[1] < 0 or tempo_final[1] < 0:
    raise ValueError("ERRO: Horas ou Minutos inválidos")
else:
    tempo_da_partida = calcula_tempo(tempo_incial, tempo_final)
    print("-" * 40)
    print(f"Início do jogo: {_inicio}")
    print(f"Fim do jogo:    {_fim}")
    print(f"Tempo de jogo:  {tempo_da_partida[0]} hora(s) e {tempo_da_partida[1]} minuto(s).")
    print("-" * 40)

