# Exercicio 2.9 PG 46-47

# Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada; calcule, então,
# a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual a operação aritmética escolhida.

numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))
operacao = int(input("Informe a operacaod desejada:   \n"
      '[1] (+) SOMA  \n'
      '[2] (-) SUBTRAÇÃO   \n'
      '[3] (*) MULTIPLICACAO  \n'
      '[4] (/) DIVISAO  \n'))

if operacao == 1:
    calculo = numero1 + numero2
    print(f'A soma entre {numero1} e {numero2} é igual a: {calculo}')
elif operacao == 2:
    calculo = numero1 - numero2
    print(f'A subtracao entre {numero1} e {numero2} é igual: {calculo}')
elif operacao == 3:
    calculo = numero1 * numero2
    print(f'A multiplicacao entre {numero1} e {numero2} é igual: {calculo}')
elif operacao == 4:
    calculo = numero1 / numero2
    print(f'A divisão entre {numero1} e {numero2} é igual: {calculo}')