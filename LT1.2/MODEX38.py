import random

def encontrar_maior_e_menor(quantidade=100):
    nums = []
    
    # Gerando 100 números aleatórios para praticidade (como no código original)
    for _ in range(quantidade):
       nums.append(random.randint(1, 1000))
    
    # <---- CÓDIGO ALTERNATIVO PARA INPUT MANUAL (Comentado) ---->
    # while len(nums) < quantidade:
    #     try:
    #         num = int(input(f"Digite um número positivo ({len(nums) + 1}/{quantidade}): "))
    #         if num < 0:
    #             print("Número inválido (número negativo), insira outro número.")
    #         else:
    #             nums.append(num)
    #     except ValueError:
    #         print("Entrada inválida. Insira um número inteiro positivo.")
    
    if not nums:
        return None, None, []
        
    nums.sort()
    
    maior = nums[-1]
    menor = nums[0]
    
    return maior, menor, nums

def main():
    maior, menor, nums = encontrar_maior_e_menor(100)
    
    if maior is not None:
        print(f"Maior número: {maior} \nMenor número: {menor}")
        print(nums)
    else:
        print("Nenhum número foi processado.")

if __name__ == "__main__":
    main()