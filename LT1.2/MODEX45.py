def calcular_serie_alternada_n_div_n2(limite):
    serie = 0.0
    for n in range(1, limite + 1):
       
        termo_abs = n / (n * n) 
        
        termo = termo_abs
      
        if n % 2 == 0:
            termo = -termo
            
        sinal_str = '-' if termo < 0 else ('+' if n > 1 else '')
        print(f"{sinal_str}{abs(n)}/{n*n} = {termo}")
        
        serie += termo
    return serie

def main():
    limite = 15
    serie = calcular_serie_alternada_n_div_n2(limite)
    print(f"\nSoma da série: {serie}")

if __name__ == "__main__":
    main()