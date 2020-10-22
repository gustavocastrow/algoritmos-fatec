# Exercicio 18 PG-64

# Construa um algoritmo que, dado o conjunto de valores inteiros positivos, determine qual o menor e maior valor
# do conjunto. O final do conjunto de valores é conhecido pelo valor -1, que não deve ser considero.

#Utilizando função max e min:
numbers = [10, 20, 50, 99, 12, 2]

print(max(int(number) for number in numbers))
print(min(int(number) for number in numbers))

#Utilizando for:
lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Informe um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')