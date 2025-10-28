# # Criar e coletar valores inteiros nos vetores VT1[3] e VT2[3]. 
# Concatenar esses valores em um 3o vetor (VT3[6]) e mostrar os seus dados. 

import random

def concat(vet3, vet1, vet2):
    for j in range(3):
        vet3.append(vet1[j])
        vet3.append(vet2[j])
    return vet3


vet1 =[]
vet2 = []
vet3 = []

for i in range(3):
    num = random.randint(0,100)
    num2 = random.randint(0,100)
    vet1.append(num)
    vet2.append(num2)

vet3 = concat(vet3, vet1, vet2)
vet3.sort()
print(f"Vetor 1: {vet1} \nVetor 2: {vet2} \nVetor 3: {vet3}")