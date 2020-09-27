# Exercício 06 - PG 62

# Um dado comerciante maluco cobra 10% de acréscimo para cada prestação em atraso e depois dá um desconto de 10% sobre
# esse valor. Faça um algoritmo que solicite o valor da prestação em atraso e apresente o valor final a pagar, assim como
# o prejuízo do comerciante na operação.

valor_prestacao = int(input("Informe o valor da prestacao em atraso: R$ "))
juros = (valor_prestacao * 0.10 )
parcela_juros = valor_prestacao + juros
desconto = (parcela_juros * 0.10)
parcela_desconto = parcela_juros - desconto
prejuizo = valor_prestacao - parcela_desconto



print(f'O valor da parcela com juros é de: {parcela_juros}')
print(f'O valor do desconto sera de: {desconto}')
print(f'O valor da parcela apos o desconto de 10% sera de: {parcela_desconto}')
print(f'O comerciante tera um prejuizo de: {prejuizo}')