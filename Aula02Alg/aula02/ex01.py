#  Seu salário atual é de R$ 6500 reais. Faça um programa que calcule o novo salário com um aumento de 5%
salario_atual = 6.500
salario_novo = salario_atual * 1.05
print(salario_novo)

calculo = 3 * 0.1
print("Resultado do calculo = %.2f, repetindo %.2f" %(calculo, calculo))
print("Resultado do calculo = {}, repetndo {}".format(calculo, calculo))

# Escreva um programa que exiba seu nome na tela
nome = input("Informe seu nome: ")
print(f'Bem vindo {nome}')

# Calcule a soma de tres variaves
var1 = int(input('Digite o primeiro numero: '))
var2 = int(input('Digite o segundo numero: '))
var3 = int(input('Digite o terceiro numero: '))
soma = var1 + var2 + var3
print(f'A soma de {var1} + {var2} + {var3} é igual a: {soma}')

# O que acontece se eu colocar textos nas tres variaveis anteriores
# R: Ele ira concatenar os valores.

a = 4
b = '4'
print(a == b)
print(a == int(b))
print(str(a) == b)

verfificar_nome = 'jose' == input('Informe seu nome: ')
print(verfificar_nome)

# ! - not
# && - and
# || - or

# or - ou inclusivo
# xor - ou exclusivo

# ordem: not > and > or


