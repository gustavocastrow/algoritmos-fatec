#1. Leia um vetor de 10 elementos e calcule o maior e o menor valor.
import random as r
vetor10 = 10 * [ r.randint(1, 1500) for index in range(0,10)] #vai chamar 10x randint e gerar um vetor aleatorio entre 1 e 1500

maxValue = -9999
minValue = 9999

for value in vetor10:
    if value < minValue:
        minValue = value
    if value > maxValue:
        maxValue = value

print(f'Menor valor gerado : {minValue}')
print(f'Maior valor gerdo: {maxValue}')
# ======================================================================================================
vetor20 = 20 * [ r.randint(1, 1500) for index in range(0,20)]

print(f'Menor valor gerado: {min(vetor20)}')
print(f'Maior valor gerado: {max(vetor20)}')