# 2 Faça um programa que receba a idade de N pessoas, ate que idade informada seja igual a 0,
# calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos

contador_is18 = 0
while True:
    idade = int(input("Informe sua idade: "))

    if idade != 0:
        if idade >= 18:
            contador_is18 += 1
    else:
        break
print(f"Total de pessoas com idade igual ou superior a 18 - {contador_is18}")