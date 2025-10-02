def calcular_serie_n_div_2n_menos_1(limite):
    serie = 0.0
    for numerador in range(1, limite + 1):
        denominador = 2 * numerador - 1
        termo = numerador / denominador
        print(f"{numerador}/{denominador} = {termo}")
        serie += termo
    return serie

def main():
    # O código original ia até n=50, então usamos 50 como limite
    limite = 50 
    serie = calcular_serie_n_div_2n_menos_1(limite)
    print(f"\nSoma da série: {serie}")

if __name__ == "__main__":
    main()