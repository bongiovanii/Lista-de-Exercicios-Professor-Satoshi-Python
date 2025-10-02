def calcular_quadrados_ate_150():
    i = 10
    while i % 150 != 0:
        quadrado = i ** 2
        print(f" Numero {i} = {quadrado}")
        i += 1 

def main():
    calcular_quadrados_ate_150()

if __name__ == "__main__":
    main()