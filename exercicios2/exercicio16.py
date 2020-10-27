# Exercicio 22 PG-64
# Escreva um algoritmo que imprima todas as possibilidades de que no lançamento de dois dados tenhamos o valor
# 7 como resultado da soma dos valores de cada dado.

num1 =  int (input('Digite o numero 1 '))
num2 =  int (input('Digite o numero 2 '))
count = 0
print(f'Numero 1  digitado {num1} \n número 2 digitado {num2}')
for i in range (0,num1+1):
    for c in range (0,num2+1):
        if i + c == 7:
           print (f' Variação com numero 1 + numero 2  \n --{i}-- + --{c}-- = {i+c}')
           print(f' Variação com numero 2 + numero 1  \n --{c}-- + --{i}-- = {i + c}')


