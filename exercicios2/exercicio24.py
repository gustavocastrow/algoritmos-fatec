# Exercicio 30 PG-64
# Calcule o imposto de renda de um grupo de dez contribuientes....

#Salario minimo 2020 -> R$ 1.045
salario_minimo = float(input('Informe o salário minimo atual: '))
desconto_salario_minimo = salario_minimo * 5 / 100

for contribuinte in range(1, 10):
    print(f'<------- Contribuinte {contribuinte} ------->')
    cpf = int(input('Informe o número do seu CPF: '))
    dependentes = int(input('Informe o número de dependentes: '))
    renda_mensal = float(input('Informe sua renda mensal: R$ '))
    renda_salario_minimo = renda_mensal / salario_minimo

    if renda_salario_minimo < 2:
        print('Você está isento do IR!')
        desconto = desconto_salario_minimo * dependentes
    elif renda_salario_minimo > 2 and renda_salario_minimo < 3:
        desconto = desconto_salario_minimo * dependentes
        ir = renda_mensal * 5 / 100 - desconto
        print(f'Aliquota 5%: {ir:.2f}')
    elif renda_salario_minimo > 3 and renda_salario_minimo < 5:
        desconto = desconto_salario_minimo * dependentes
        ir = renda_mensal * 10 / 100 - desconto
        print(f'Aliquota 10%: {ir:.2f}')
    elif renda_salario_minimo > 5 and renda_salario_minimo < 3:
        desconto = desconto_salario_minimo * dependentes
        ir = renda_mensal * 15 / 100 - desconto
        print(f'Aliquota 15%: {ir:.2f}')
    elif renda_salario_minimo > 7:
        desconto = desconto_salario_minimo * dependentes
        ir = renda_mensal * 20 / 100 - desconto
        print(f'Aliquota 20%: {ir:.2f}')


