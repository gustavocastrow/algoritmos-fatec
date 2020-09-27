# Exercicio 2.8 PG 46-47

# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a
# escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento
# escolhida e efetuar o cálculo adequado.

valor_produto = int(input("Informe o valor do produto: "))
pagamento = int(input('Informe a condicao de pagamento  \n' 
      '[1] A vista em dinheiro ou cheque, recebe 10% de desconto \n'
      '[2] A vista no cartão de crédito, recebe 5% de desconto \n'
      '[3] Em duas vezes, preço normal de etiqueta sem juros \n'
      '[4] Em três vezes, preço normal de etiqueta mais juros de 10% \n'))

if pagamento == 1:
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
    print(f'O valor a ser pago sera de {valor_final}, totalizando 10% de desconto R$ {desconto}')
elif pagamento == 2:
    desconto = valor_produto * 0.05
    valor_final = valor_produto - desconto
    print(f'O valor a ser pago sera de {valor_final}, totalizando 5% de desconto R$ {desconto}')
elif pagamento == 3:
    parcela = valor_produto / 2
    print(f'O valor da primeira parcela sera de: {parcela} e o segunda: {parcela} totalizando {valor_produto}')
elif pagamento == 4:
    juros = valor_produto * 0.10
    valor_final = valor_produto + juros
    parcela = valor_final / 3
    print(f'O valor das parcelas sera de: R$ {parcela:.2f}, o valor final sera de: {valor_final} totalizando R$ {juros} de juros')
elif pagamento == 0 or pagamento >= 5:
    print(f'Codigo {pagamento}, invalido informe um codigo de 1 a 4')