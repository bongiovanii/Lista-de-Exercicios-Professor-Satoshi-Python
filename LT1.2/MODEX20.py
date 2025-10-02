import math

def calcular_raizes_bhaskara(A, B, C):
    if A == 0:
        print("Não é uma equação do 2º grau, pois A = 0.")
        return False
    
    delta = B**2 - 4*A*C
    print(f"Delta = {delta:.2f}")

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -B / (2*A)
        print(f"A equação possui uma raiz real: x = {raiz:.2f}")
    else:
        raiz1 = (-B + math.sqrt(delta)) / (2*A)
        raiz2 = (-B - math.sqrt(delta)) / (2*A)
        print("A equação possui duas raízes reais:")
        print(f"x1 = {raiz1:.2f}")
        print(f"x2 = {raiz2:.2f}")
        
    return True

def main():
    try:
        A = float(input("Digite o coeficiente A: "))
        B = float(input("Digite o coeficiente B: "))
        C = float(input("Digite o coeficiente C: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    calcular_raizes_bhaskara(A, B, C)
    
if __name__ == "__main__":
    main()