# Ex 02 - Aula06
# Faca um programa que leia o valor de n, inteiro e positivo, calculo e mostre o resultado
# da seguinte sequencia S = 1 + 1 / 2 + 1 / 3 + ... + 1 / n


n = int(input("Informe o valor de N: "))

denominador = 1
resultado = 0

while denominador <= n:
    resultado += 1 / denominador
    denominador += 1

print(f'Resultado: {resultado}')