def calcular_anos_crescimento(altura_ana_ini, altura_maria_ini, cresc_ana, cresc_maria):
    altura_ana = altura_ana_ini
    altura_maria = altura_maria_ini
    anos = 0
    
    while altura_ana <= altura_maria:
        altura_ana += cresc_ana
        altura_maria += cresc_maria
        anos += 1
        
    return anos

def main():
    altura_ana_ini = 1.10
    altura_maria_ini = 1.50
    cresc_ana = 0.03 
    cresc_maria = 0.02
    
    anos = calcular_anos_crescimento(
        altura_ana_ini, 
        altura_maria_ini, 
        cresc_ana, 
        cresc_maria
    )
    
    print(f"Serão necessários {anos} anos para que Ana seja mais alta que Maria.")

if __name__ == "__main__":
    main()