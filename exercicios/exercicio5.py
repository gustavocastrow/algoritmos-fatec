# Exercício 05 - PG 62

# Dada uma determinada data de aniversário (dia, mês e ano separadamente), elabore um algoritmo que solicite a
# data atual (dia, mês e ano separadamente) e calcule a idade em anos, em meses e em dias.

data_nascimento = int(input("Informe o dia de nascimento: "))
mes_nascimento = int(input("Informe o mes de nascimento: "))
ano_nascimento = int(input("Informe o ano de nascimento: "))

data_atual = int(input("Informe a data de hoje: "))
mes_atual = int(input("Informe o mes atual: "))
ano_atual = int(input("Informe o ano atual: "))

idade_anos = ano_atual - ano_nascimento
print(f'Sua idade em anos é: {idade_anos}')

idade_meses = idade_anos * 12
print(f'Sua idade em meses é: {idade_meses}')

idade_dias = idade_anos * 365
print(f'Sua idade em dias é: {idade_dias}')

