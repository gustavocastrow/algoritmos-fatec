# Exercicio 2.8 PG 46-47

# O IMC - lndice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição
# de peso de uma pessoa adulta. A fórmula é IMC = peso/ (altura)2• Elabore um algoritmo que leia o peso e a altura de
# um adulto e mostre sua condição.

peso = float(input("Informe seu peso em KG: "))
altura = float(input("Informe sua altura em M: "))
imc = float(peso/(altura*altura))

if imc <= 18.5:
    print(f'O seu IMC é de: {imc:.2f}, poranto você esta ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print(f'O seu IMC é de: {imc:.2f}, poranto você esta com o PESO NORMAL')
elif imc > 25 and imc <= 30:
    print(f'O seu IMC é de: {imc:.2f}, poranto você esta ACIMA DO PESO')
elif imc > 30:
    print(f'O seu IMC é de: {imc:.2f}, portanto você esta OBESO')