def valida_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def soma_primos_intervalo(inicio, fim):
    primos = []
    soma = 0
    # O loop deve incluir o início, mas o código original não incluía o 'fim'
    for i in range(inicio, fim):
        if valida_primo(i):
            soma += i
            primos.append(i)
    return soma, primos

def main():
    nums = []
    try:
        nums.append(int(input("Digite o número de início do intervalo: ")))
        nums.append(int(input("Digite o número de fim do intervalo (exclusivo): ")))
    except ValueError:
        print("Entrada inválida. Insira números inteiros.")
        return

    # Garante que a ordem seja do menor para o maior para o range
    nums.sort() 
    
    soma, primos = soma_primos_intervalo(nums[0], nums[1])
        
    print(f"Soma dos número primos entre {nums[0]} e {nums[1]}: {soma}")      
    print(f"Números primos: {primos}")

if __name__ == "__main__":
    main()