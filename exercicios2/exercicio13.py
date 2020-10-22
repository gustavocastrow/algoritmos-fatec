# Exercicio 19 PG-64
# A conversão de graus para Fahrenheit para centigrados é obtida pela formula C =  5/9(F-32)
# Escreva um algoritmo que calcule e escreva uma tabela de graus centigrados em função de graus Farenheit
# que variem de 50 a 150 de 1 em 1

# F -> C
# C = 5 / 9 ( F - 32)

for tabela in range(50, 151):
    celcius = (tabela - 32) * 5 /9
    print(f'{tabela} F é igual á {celcius:.2f} C')