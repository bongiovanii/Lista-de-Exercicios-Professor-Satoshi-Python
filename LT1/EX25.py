#  Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo
# em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e
# pode começar num dia e terminar noutro.


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


print(tempo_incial, tempo_final)
