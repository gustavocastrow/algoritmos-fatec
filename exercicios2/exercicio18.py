# Exercicio 24 PG-64
# Construa um algoritmo que leia um conjunto de dados contendo altura e sexo ('M' para Masculino e 'F' para feminino)
# de 50 pessoas, e depois calcule e escreva
# -> A maior e a menor altura do grupo [X]
# -> A media de altura das mulheres [X]
# -> O numero de homens e a diferença percentual entre eles e mulheres

mais_alta = 0
mais_baixa = 0
media = 0
altura_mulheres = 0
contador_mulheres = 0
contador_homens = 0

for dados in range(1, 6):
    print(f'<----- PESSOA {dados}° ----->')
    altura = float(input('Informe sua altura: '))
    sexo = str(input('Informe seu sexo: [M/F] ')).strip()

    #Maior e Menor altura do grupo.

    if dados == 1:
        mais_alta = altura
        mais_baixa = altura
    else:
        if altura > mais_alta:
            mais_alta = altura
        if altura < mais_baixa:
            mais_baixa = altura

    #Média de altura das mulheres

    if sexo == 'F':
        altura_mulheres = altura_mulheres + altura
        contador_mulheres = contador_mulheres + 1

    #O numero de homens e a diferença percentual entre eles e mulheres

    if sexo == 'M':
        contador_homens = contador_homens + 1


media_altura_mulheres = altura_mulheres / contador_mulheres

print(f'Número de mulheres: {contador_mulheres}')
print(f'Numero de homens: {contador_homens}')
print(f'Diferença percentual entre homens e mulheres:')
print(f'A média de altura das mulheres é: {media_altura_mulheres:.2f}')
print(f'A maior altura do grupo é de: {mais_alta:.2f}')
print(f'A menor altura do grupo é de: {mais_baixa:.2f}')