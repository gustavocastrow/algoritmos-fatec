# Exercicio 24 PG-64
# Construa um algoritmo que leia um conjunto de dados contendo altura e sexo ('M' para Masculino e 'F' para feminino)
# de 50 pessoas, e depois calcule e escreva
# -> A maior e a menor altura do grupo
# -> A media de altura das mulheres
# -> O numero de homens e a diferença percentual entre eles e mulheres

mais_alta = 0
mais_baixa = 0
media = 0
mulheres = 0
for dados in range(0, 2):
    altura = float(input('Informe sua altura: '))
    sexo = str(input('Informe seu sexo: [M/F] ')).strip()

    if sexo in 'Mm':
        mulheres += 1
        media = altura / mulheres
print(f'A média de altura das mulheres é: {media}')