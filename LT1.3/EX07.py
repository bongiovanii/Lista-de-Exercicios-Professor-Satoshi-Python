# EX07.py
"""
Lote 1.3 - Exercício 7
A partir do exercício 6 (vetor classificado) solicitar um valor qualquer e
verificar a sua existência no vetor (utilizar pesquisa binária).
"""
import random

def pesquisa_binaria(vet, valor):
    inicio = 0
    fim = len(vet) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if vet[meio] == valor:
            return meio
        elif vet[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return -1

# Criando e classificando o vetor (baseado no ex 6)
vetor = []
for _ in range(20):
    vetor.append(random.randint(1, 100))
    
vetor.sort()

print(f"Vetor classificado: {vetor}")

# Solicitação e pesquisa binária
try:
    valor_busca = int(input("Digite o valor a ser buscado: "))
    
    posicao = pesquisa_binaria(vetor, valor_busca)
    
    if posicao != -1:
        print(f"O valor {valor_busca} foi encontrado na posição (índice) {posicao}.")
    else:
        print(f"O valor {valor_busca} não foi encontrado no vetor.")

except ValueError:
    print("Entrada inválida. Digite um número inteiro.")