# 1 Faça um programa que verifique e mostre os numeros entre 1000 e 2000
# (inclusive) que quando divididos por 11 produzam resto igual a 5

init = 1000
finish = 2000
contador = 0

while init <= finish:
    if init % 11 == 5:
        print(f'{init} possui resto igual a 5!')
        contador += 1
    init += 1
print(f'Quantidade total de numeros com resto igual a 5 é {contador}')